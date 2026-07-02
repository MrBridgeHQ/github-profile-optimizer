# Registry Targets

**Note:** This list was compiled from a brief and general ecosystem knowledge. The URLs, contribution processes, and even the existence of some targets were NOT independently verified at authoring time. Before submitting anything, you must confirm that each URL actually resolves, that the target still exists, and that you have read its current submission rules. Treat every entry below as a lead to check, not a confirmed fact.

Priorities follow the Agent Skills Registry Playbook: curated quality lists are Priority 1, installable or searchable catalogs are Priority 2, and noisy aggregators are Priority 3.

## Verification status (checked 2026-07-02)

The 10 targets were spot-checked on 2026-07-02 via their public pages and GitHub. All 10 resolved and existed at that time. Submission rules can change without notice, so re-check each target's current CONTRIBUTING or submit page at the moment you submit. Star counts are volatile and are deliberately not recorded here.

| Target | Exists (2026-07-02) | Submissions | Mechanism to re-verify |
|---|---|---|---|
| anthropics/skills | Yes | Unclear (curated, no public PR path found) | Treat as not open unless a CONTRIBUTING path is confirmed |
| VoltAgent/awesome-agent-skills | Yes | Open | PR to the awesome-list (CONTRIBUTING present) |
| ComposioHQ/awesome-claude-skills | Yes | Open | PR to the awesome-list |
| travisvn/awesome-claude-skills | Yes | Open | PR to the awesome-list |
| sickn33/antigravity-awesome-skills | Yes | Open | PR (skill template + validation script) |
| heilcheng/awesome-agent-skills | Yes | Open | PR to the awesome-list |
| awesome-skills.com | Yes | Unclear (no visible submit form or own repo) | Site contact only; no public PR path found |
| awesomeclaude.ai/awesome-claude-skills | Yes | Open (front-end) | PR or issue to backing repo webfuse-com/awesome-claude |
| agent-skill.co | Yes | Open (front-end) | PR to backing repo heilcheng/awesome-agent-skills |
| agentskill.sh | Yes | Open (web form) | Submit a GitHub repo or SKILL.md URL at /submit |

Two of the websites are front-ends of GitHub awesome-lists: awesomeclaude.ai is backed by webfuse-com/awesome-claude, and agent-skill.co is backed by heilcheng/awesome-agent-skills. To appear on those sites, submit to the backing repository. This block confirms existence as of the date shown; you must still re-verify submission rules before acting.

## anthropics/skills

- **Name:** anthropics/skills
- **Type:** official / reference
- **Audience:** Claude / Agent Skills users and authors; the canonical reference point for the ecosystem.
- **Priority:** 1 (as a reference to study and align with)
- **Submission conditions to verify:** Whether community pull requests are accepted at all. Do NOT assume they are. Read the repository's current `CONTRIBUTING` and any policy statements before considering a submission. Confirm the exact URL (likely `github.com/anthropics/skills`) resolves.
- **Probable format:** Unknown; possibly a PR, possibly no community submissions at all. Verify.
- **Notes:** Study it as the official reference and as a possible marketplace or distribution surface. Model your skill's structure, frontmatter, and README on what is exemplary here. Do NOT assume community PRs are accepted; verify before acting. This is the single most important target to check rules on before doing anything.

## VoltAgent/awesome-agent-skills

- **Name:** VoltAgent/awesome-agent-skills
- **Type:** curated awesome list
- **Audience:** Developers browsing curated Agent Skills.
- **Priority:** 1
- **Submission conditions to verify:** Confirm the repo exists at the expected path (`github.com/VoltAgent/awesome-agent-skills`), read its `CONTRIBUTING` or README contribution section, check required fields (license, demo, description length), and check whether it enforces a category and ordering.
- **Probable format:** PR adding one categorized line to the README.
- **Notes:** Curated list, so acceptance is a quality signal. Make the repo exemplary before submitting. Match the existing entry format exactly and keep the diff to one line.

## ComposioHQ/awesome-claude-skills

- **Name:** ComposioHQ/awesome-claude-skills
- **Type:** curated awesome list
- **Audience:** Claude Skills users and developers.
- **Priority:** 1
- **Submission conditions to verify:** Confirm the path (`github.com/ComposioHQ/awesome-claude-skills`), read contribution rules, check category structure and any minimum-quality bar (README, license, working example).
- **Probable format:** PR adding one categorized README line.
- **Notes:** Curated; treat acceptance as an endorsement. Follow the list's format precisely and put the entry in the correct category.

## travisvn/awesome-claude-skills

- **Name:** travisvn/awesome-claude-skills
- **Type:** curated awesome list
- **Audience:** Claude Skills users and developers.
- **Priority:** 1
- **Submission conditions to verify:** Confirm the path (`github.com/travisvn/awesome-claude-skills`), read contribution rules, check formatting and category conventions, check recency of merged PRs to confirm it is actively maintained.
- **Probable format:** PR adding one categorized README line.
- **Notes:** Curated list. Verify it is still active (recent merges) before investing effort, then match its format.

## sickn33/antigravity-awesome-skills

- **Name:** sickn33/antigravity-awesome-skills
- **Type:** curated awesome list
- **Audience:** Agent Skills users (scope to be confirmed).
- **Priority:** 1
- **Submission conditions to verify:** First confirm the repository actually exists at the expected path and is not stale or renamed. Then read its contribution rules and category format.
- **Probable format:** PR adding one categorized README line (assumed; verify).
- **Notes:** Existence and rules are unverified. Confirm the repo is real, maintained, and accepting entries before spending time on a submission.

## heilcheng/awesome-agent-skills

- **Name:** heilcheng/awesome-agent-skills
- **Type:** curated awesome list
- **Audience:** Agent Skills users and developers.
- **Priority:** 1
- **Submission conditions to verify:** First confirm the repository exists at the expected path and is active. Then read its `CONTRIBUTING`, category format, and any quality requirements.
- **Probable format:** PR adding one categorized README line (assumed; verify).
- **Notes:** Existence and rules are unverified. Confirm it is real and maintained before submitting, then match its format and keep the diff minimal.

## awesome-skills.com

- **Name:** awesome-skills.com
- **Type:** searchable website / catalog
- **Audience:** Users searching for skills through a website interface.
- **Priority:** 2
- **Submission conditions to verify:** Confirm the domain resolves. Find whether listing is done via a submission form, an account, or a GitHub-backed process. Check whether it requires a demo or license and how it sources entries. **Verify.**
- **Probable format:** Web submission form or a GitHub-based listing (verify which).
- **Notes:** Searchable catalog, so secondary reach. Confirm the site is legitimate and how listings are created before submitting.

## awesomeclaude.ai/awesome-claude-skills

- **Name:** awesomeclaude.ai/awesome-claude-skills
- **Type:** searchable website
- **Audience:** Claude Skills users browsing a website.
- **Priority:** 2
- **Submission conditions to verify:** Confirm the URL resolves. Determine whether it is a standalone site, a mirror of a GitHub awesome list, or both, and how entries are added (form vs PR to an underlying repo). Check demo/license requirements. **Verify.**
- **Probable format:** Submission form or a PR to a backing GitHub repo (verify which).
- **Notes:** If it mirrors a GitHub list, submit to the underlying repo per that repo's rules. Confirm the mechanism before acting.

## agent-skill.co

- **Name:** agent-skill.co
- **Type:** searchable website / catalog
- **Audience:** Users searching for agent skills via a website.
- **Priority:** 2
- **Submission conditions to verify:** Confirm the domain resolves and is legitimate. Find the submission mechanism (form, account, or GitHub-based) and any requirements (demo, license, description). Check how fresh the catalog is. **Verify.**
- **Probable format:** Web submission form or GitHub-based listing (verify which).
- **Notes:** Searchable catalog; secondary reach. Confirm legitimacy and mechanism before submitting.

## agentskill.sh

- **Name:** agentskill.sh
- **Type:** searchable website / catalog
- **Audience:** Users searching for agent skills via a website.
- **Priority:** 2
- **Submission conditions to verify:** Confirm the domain resolves and is legitimate. Identify the submission mechanism and requirements, and check catalog recency to judge whether it is maintained. **Verify.**
- **Probable format:** Web submission form or GitHub-based listing (verify which).
- **Notes:** Searchable catalog; secondary reach. Confirm it is real and how listings are created before investing effort.

## How to verify a target

For each target, before submitting:

1. **Open the URL.** Confirm it resolves and is the thing you expect (right repo, right site, not renamed, deleted, or squatted).
2. **Find the rules.** Locate the `CONTRIBUTING` file, a submission page, or the README contribution section. If there is no stated process, treat submission as unconfirmed.
3. **Check the category and format.** See exactly how existing entries are structured (link style, description length, section, ordering) so you can match them precisely.
4. **Check requirements.** Confirm whether they require a demo, a license, a minimum README, or other quality gates, and make sure your repo already meets them.
5. **Check recency.** Look at recently merged PRs or recently added listings to confirm the target is actively maintained and still accepting submissions. A dead list is not worth a PR.
