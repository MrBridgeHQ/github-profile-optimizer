# scripts/collect_github_context.py

A small, read-only context collector for the `github-profile-optimizer` skill. It
gathers just enough public information about a GitHub profile (and, optionally,
local README files) to support a profile audit or rewrite, and prints it as a
single JSON object.

## What it does

- Queries the PUBLIC GitHub REST API for a user's profile and repositories.
- Optionally scans a local directory for README files and includes short text
  previews of each.
- Emits one pretty-printed JSON object with a fixed shape, so the skill can
  reason over real data instead of guessing.

## No token, network optional

- It needs NO authentication token. It never reads, requires, or sends a token.
  All API calls hit public, unauthenticated endpoints.
- The network is OPTIONAL. Local mode (README scan) works with no network at
  all. If the machine is offline or the API is unreachable, the script does not
  crash: it records a note in the `notes` array and returns whatever it could
  collect.
- Because there is no token, the stricter public GitHub rate limits apply. When
  a limit is hit the API returns HTTP 403; the script records that as a note and
  keeps going.

## Two modes (can be combined)

1. Network mode: pass a `username`. The script calls, using only the Python
   standard library (`urllib`):
   - `https://api.github.com/users/{username}`
   - `https://api.github.com/users/{username}/repos?per_page={max}&sort=updated`
   - `https://api.github.com/repos/{username}/{repo}` when `--repo` is given.
   Each request sends an `Accept: application/vnd.github+json` header and a
   descriptive `User-Agent`, with a short timeout.
2. Local mode: pass `--local-dir`. The script looks for `README.md`,
   `readme.md`, `README`, and nested `*/README.md` files up to a reasonable
   depth, and includes each file's relative path plus a preview of roughly the
   first 2000 characters.

## Usage examples

```
python3 collect_github_context.py octocat
python3 collect_github_context.py octocat --repo my-skill --max-repos 20
python3 collect_github_context.py --local-dir /path/to/repo
python3 collect_github_context.py octocat --out context.json
```

You can combine a username with `--local-dir` to gather both remote and local
context in a single run.

## Output shape

A single JSON object (pretty-printed with 2-space indent):

```
{
  "user": {
    "login": string or null,
    "name": string or null,
    "bio": string or null,
    "blog": string or null,
    "location": string or null,
    "followers": number or null
  },
  "repos": [
    {
      "name": string or null,
      "description": string or null,
      "topics": [ string, ... ],
      "stargazers_count": number or null,
      "forks_count": number or null,
      "updated_at": string or null,
      "html_url": string or null
    }
  ],
  "local_readmes": [
    { "path": string, "preview": string }
  ],
  "notes": [ string, ... ]
}
```

Notes on the shape:

- Missing values are `null` (scalars) or `[]` (lists). The script never invents
  values.
- `topics` is an empty list when the API does not return topics; a note is added
  to `notes` in that case.
- `notes` collects every error or limitation encountered: rate limit (403),
  not found (404), timeouts, offline runs, unreadable local files, and a
  standing reminder that no token was used.

On invalid input or a write failure, the script prints a small JSON error object
(for example `{"error": "no_input", "message": "..."}`) and exits with a
non-zero status instead of raising a traceback.

## Graceful degradation offline

If the network is unreachable, the script performs a quick reachability check,
skips the API calls, and adds a note such as "Network appears offline". Any
local README scan still runs. This means a fully offline `--local-dir` run
always succeeds.

## Privacy and side effects

- The script performs NO writes to any GitHub repository.
- It stores nothing on disk beyond the optional `--out` file you explicitly
  request. Without `--out`, output goes to stdout only.
- The local IP is only ever exposed to `api.github.com` when you run network
  mode; local mode makes no outbound connection.
