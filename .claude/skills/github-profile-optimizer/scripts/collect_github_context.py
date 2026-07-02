#!/usr/bin/env python3
"""Collect read-only context about a GitHub profile for the github-profile-optimizer skill.

This collector is deliberately minimal and safe:

- NO authentication token is ever required or read. It only ever calls the
  PUBLIC GitHub REST API, which is subject to unauthenticated rate limits.
- The NETWORK is OPTIONAL. If no username is given (local mode) or if the
  network is unreachable, the script degrades gracefully: it records a note in
  the output and never crashes with a raw traceback.
- It performs NO writes to any GitHub repository and stores nothing beyond the
  optional --out JSON file.

Two modes (they can be combined):

1. Network mode: pass a username. The script queries the public REST API using
   only the Python standard library (urllib) with a short timeout and a
   User-Agent header.
2. Local mode: pass --local-dir. The script scans the directory for README
   files and includes a truncated text preview of each. This mode needs no
   network at all.

Output: a single pretty-printed JSON object (indent=2) with keys
"user", "repos", "local_readmes", and "notes". Missing values become null or
empty lists. Values are never invented.
"""

import argparse
import glob
import json
import os
import socket
import sys
import urllib.error
import urllib.request

# Public GitHub REST API base. No token is ever attached to these requests.
API_BASE = "https://api.github.com"

# A descriptive User-Agent is required by the GitHub API for all requests.
USER_AGENT = "github-profile-optimizer-context-collector/1.0 (stdlib; no-token)"

# Standard Accept header for the current GitHub REST API media type.
ACCEPT_JSON = "application/vnd.github+json"

# The topics field historically required a preview media type. Requesting it
# via Accept is harmless on the current API and lets us read repo topics.
ACCEPT_TOPICS = "application/vnd.github+json, application/vnd.github.mercy-preview+json"

# Network request timeout in seconds. Kept short so offline runs fail fast.
REQUEST_TIMEOUT = 15

# Maximum number of characters kept from each local README preview.
PREVIEW_CHARS = 2000

# How deep to look for nested README.md files in local mode.
LOCAL_README_MAX_DEPTH = 3


def _http_get_json(url, accept):
    """Fetch a URL and parse JSON, never raising to the caller.

    Returns a tuple (data, error). On success, error is None. On failure,
    data is None and error is a short human-readable string describing the
    problem (rate limit, not found, timeout, offline, etc.).
    """
    request = urllib.request.Request(url, method="GET")
    request.add_header("User-Agent", USER_AGENT)
    request.add_header("Accept", accept)
    try:
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT) as response:
            raw = response.read()
        text = raw.decode("utf-8", errors="replace")
        return json.loads(text), None
    except urllib.error.HTTPError as exc:
        # HTTP-level error (403 rate limit, 404 not found, 5xx, etc.).
        if exc.code == 403:
            return None, "GitHub API returned 403 (likely unauthenticated rate limit reached; no token is used by design)"
        if exc.code == 404:
            return None, "GitHub API returned 404 (resource not found: " + url + ")"
        return None, "GitHub API HTTP error " + str(exc.code) + " for " + url
    except urllib.error.URLError as exc:
        # DNS failure, connection refused, or offline. reason may be a socket error.
        return None, "Network error (offline or unreachable) for " + url + ": " + str(exc.reason)
    except socket.timeout:
        return None, "Network timeout after " + str(REQUEST_TIMEOUT) + "s for " + url
    except (ValueError, json.JSONDecodeError) as exc:
        return None, "Could not parse JSON response from " + url + ": " + str(exc)
    except Exception as exc:  # Last-resort guard; never crash the caller.
        return None, "Unexpected error fetching " + url + ": " + str(exc)


def _network_reachable():
    """Best-effort check that the network is reachable.

    Attempts a short TCP connection to the GitHub API host on port 443.
    Returns True on success, False otherwise. Never raises.
    """
    try:
        conn = socket.create_connection(("api.github.com", 443), timeout=REQUEST_TIMEOUT)
        conn.close()
        return True
    except OSError:
        return False
    except Exception:
        return False


def _extract_user(raw_user):
    """Map a raw GitHub user object to the fixed output shape.

    Missing fields become null. Values are never invented.
    """
    if not isinstance(raw_user, dict):
        return {
            "login": None,
            "name": None,
            "bio": None,
            "blog": None,
            "location": None,
            "followers": None,
        }
    return {
        "login": raw_user.get("login"),
        "name": raw_user.get("name"),
        "bio": raw_user.get("bio"),
        "blog": raw_user.get("blog"),
        "location": raw_user.get("location"),
        "followers": raw_user.get("followers"),
    }


def _extract_repo(raw_repo):
    """Map a raw GitHub repo object to the fixed output shape.

    "topics" is used as-is when present, otherwise an empty list. Missing
    scalar fields become null.
    """
    if not isinstance(raw_repo, dict):
        return None
    topics = raw_repo.get("topics")
    if not isinstance(topics, list):
        topics = []
    return {
        "name": raw_repo.get("name"),
        "description": raw_repo.get("description"),
        "topics": topics,
        "stargazers_count": raw_repo.get("stargazers_count"),
        "forks_count": raw_repo.get("forks_count"),
        "updated_at": raw_repo.get("updated_at"),
        "html_url": raw_repo.get("html_url"),
    }


def collect_network(username, repo, max_repos, notes):
    """Collect user and repo context from the public GitHub REST API.

    Never raises. Appends any errors or limitations to the notes list.
    Returns a tuple (user_dict, repos_list, topics_available).
    """
    user = _extract_user(None)
    repos = []
    topics_available = True

    # Fail fast and clearly if the network is not reachable at all.
    if not _network_reachable():
        notes.append("Network appears offline; skipped GitHub API calls (no token is ever required).")
        return user, repos, topics_available

    # 1) User object.
    user_url = API_BASE + "/users/" + urllib.parse.quote(username)
    raw_user, err = _http_get_json(user_url, ACCEPT_JSON)
    if err is not None:
        notes.append("user: " + err)
    else:
        user = _extract_user(raw_user)

    # 2) Repositories. If --repo is given, fetch just that one; otherwise list.
    if repo:
        repo_url = API_BASE + "/repos/" + urllib.parse.quote(username) + "/" + urllib.parse.quote(repo)
        raw_repo, err = _http_get_json(repo_url, ACCEPT_TOPICS)
        if err is not None:
            notes.append("repo: " + err)
        else:
            extracted = _extract_repo(raw_repo)
            if extracted is not None:
                if not extracted["topics"]:
                    topics_available = False
                repos.append(extracted)
    else:
        repos_url = (
            API_BASE
            + "/users/"
            + urllib.parse.quote(username)
            + "/repos?per_page="
            + str(max_repos)
            + "&sort=updated"
        )
        raw_repos, err = _http_get_json(repos_url, ACCEPT_TOPICS)
        if err is not None:
            notes.append("repos: " + err)
        elif isinstance(raw_repos, list):
            any_topics = False
            for raw_repo in raw_repos[:max_repos]:
                extracted = _extract_repo(raw_repo)
                if extracted is not None:
                    if extracted["topics"]:
                        any_topics = True
                    repos.append(extracted)
            if repos and not any_topics:
                topics_available = False
        else:
            notes.append("repos: unexpected response shape (expected a list)")

    if not topics_available:
        notes.append("Repository topics were not available in the API response; using empty topic lists.")

    return user, repos, topics_available


def _read_preview(path):
    """Read up to PREVIEW_CHARS characters from a file, safely.

    Returns the preview string, or None if the file cannot be read.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            return handle.read(PREVIEW_CHARS)
    except OSError:
        return None
    except Exception:
        return None


def collect_local_readmes(local_dir, notes):
    """Scan a local directory for README files and return previews.

    Looks for README.md, readme.md, README at the root, plus nested
    */README.md files up to a reasonable depth. Needs no network. Never
    raises; appends any problems to notes. Returns a list of
    {path, preview} dicts with paths relative to local_dir.
    """
    results = []
    if not os.path.isdir(local_dir):
        notes.append("local-dir: not a directory: " + local_dir)
        return results

    candidates = []

    # Root-level candidates with common casings.
    for name in ("README.md", "readme.md", "Readme.md", "README", "readme"):
        candidates.append(os.path.join(local_dir, name))

    # Nested README.md files up to LOCAL_README_MAX_DEPTH levels deep.
    for depth in range(1, LOCAL_README_MAX_DEPTH + 1):
        pattern = os.path.join(local_dir, *(["*"] * depth), "README.md")
        try:
            for match in glob.glob(pattern):
                candidates.append(match)
        except Exception:
            # glob should not raise, but guard anyway.
            continue

    # De-duplicate by absolute path while preserving order.
    seen = set()
    for path in candidates:
        try:
            abs_path = os.path.abspath(path)
        except Exception:
            continue
        if abs_path in seen:
            continue
        seen.add(abs_path)
        if not os.path.isfile(abs_path):
            continue
        preview = _read_preview(abs_path)
        if preview is None:
            notes.append("local-readme: could not read " + abs_path)
            continue
        try:
            rel_path = os.path.relpath(abs_path, local_dir)
        except Exception:
            rel_path = abs_path
        results.append({"path": rel_path, "preview": preview})

    if not results:
        notes.append("local-dir: no README files found under " + local_dir)

    return results


def build_context(args):
    """Build the full context object from parsed CLI arguments.

    Never raises for expected error conditions; returns the output dict.
    """
    notes = []
    user = _extract_user(None)
    repos = []
    local_readmes = []

    # Network mode runs only when a username is provided.
    if args.username:
        user, repos, _ = collect_network(args.username, args.repo, args.max_repos, notes)
    else:
        notes.append("No username given; skipped network mode (local-only run).")

    # Local mode runs only when --local-dir is provided.
    if args.local_dir:
        local_readmes = collect_local_readmes(args.local_dir, notes)

    # Always record that no token is used, so downstream consumers understand
    # any rate-limit note in context.
    notes.append("No authentication token was used; public GitHub rate limits apply.")

    return {
        "user": user,
        "repos": repos,
        "local_readmes": local_readmes,
        "notes": notes,
    }


def parse_args(argv):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Collect read-only context about a GitHub profile. No token is ever "
            "required and the network is optional (local README scan works offline)."
        )
    )
    parser.add_argument(
        "username",
        nargs="?",
        default=None,
        help="GitHub username to query via the public API (optional if --local-dir is given).",
    )
    parser.add_argument(
        "--repo",
        default=None,
        help="Fetch a single named repository instead of listing the user's repos.",
    )
    parser.add_argument(
        "--local-dir",
        default=None,
        help="Scan this local directory for README files (no network needed).",
    )
    parser.add_argument(
        "--max-repos",
        type=int,
        default=10,
        help="Maximum number of repositories to fetch in list mode (default: 10).",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Write the JSON output to this file instead of stdout.",
    )
    return parser.parse_args(argv)


def main(argv):
    """Entry point. Returns a process exit code (0 on success)."""
    try:
        args = parse_args(argv)
    except SystemExit:
        # argparse already printed a usage message; propagate its exit code.
        raise

    # At least one input source is required.
    if not args.username and not args.local_dir:
        error = {
            "error": "no_input",
            "message": "Provide a username (network mode) and/or --local-dir (local mode).",
        }
        print(json.dumps(error, indent=2))
        return 2

    if args.max_repos is not None and args.max_repos < 1:
        error = {
            "error": "invalid_max_repos",
            "message": "--max-repos must be a positive integer.",
        }
        print(json.dumps(error, indent=2))
        return 2

    try:
        context = build_context(args)
    except Exception as exc:  # Final safety net: never emit a raw traceback.
        error = {
            "error": "unexpected",
            "message": "Unexpected failure while collecting context: " + str(exc),
        }
        print(json.dumps(error, indent=2))
        return 1

    output = json.dumps(context, indent=2)

    if args.out:
        try:
            with open(args.out, "w", encoding="utf-8") as handle:
                handle.write(output)
                handle.write("\n")
        except OSError as exc:
            error = {
                "error": "write_failed",
                "message": "Could not write output file " + str(args.out) + ": " + str(exc),
            }
            print(json.dumps(error, indent=2))
            return 1
    else:
        print(output)

    return 0


if __name__ == "__main__":
    # urllib.parse is imported lazily here-style at module load via the import
    # below to keep the request-building code readable.
    import urllib.parse  # noqa: E402  (grouped with usage for clarity)

    sys.exit(main(sys.argv[1:]))
