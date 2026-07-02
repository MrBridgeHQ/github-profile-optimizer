# Example: Profile Audit (AI engineer)

This worked example shows the github-profile-optimizer skill running an end-to-end
Profile Audit on a real-shaped input, then producing the filled Profile Audit Report.
All quantitative figures are marked as user-provided or `[not available]`; the skill
never invents GitHub metrics.

---

## Input (as supplied to the skill)

```yaml
username: dana-okonkwo
display_name: Dana Okonkwo
current_bio: "Software engineer. I like building things. Open to opportunities."
website: (none)
location: Lisbon, Portugal
company: (not listed)
profile_readme_exists: false
repositories:
  - name: mcp-notes-server
    description: "notes mcp thing"
    pinned: false
    primary_use: "Model Context Protocol server exposing a personal notes store to Claude"
    stars: "[not available]"
    last_commit: user-provided (3 weeks ago)
  - name: agent-playground
    description: (empty)
    pinned: false
    primary_use: "experiments wiring a tool-using agent loop over an LLM"
    stars: "[not available]"
    last_commit: user-provided (2 days ago)
  - name: claude-skills-lab
    description: "some skills"
    pinned: false
    primary_use: "collection of Claude Code skills the user authored"
    stars: "[not available]"
    last_commit: user-provided (yesterday)
  - name: resume-site
    description: (empty)
    pinned: false
    primary_use: "static personal site, abandoned"
    stars: "[not available]"
    last_commit: user-provided (14 months ago)
  - name: leetcode-solutions
    description: (empty)
    pinned: false
    primary_use: "practice problems"
    stars: "[not available]"
    last_commit: user-provided (7 months ago)
stated_goal: "I build AI agents, MCP servers, and Claude Code skills. I want to be
  found by teams hiring for applied-AI / agent engineering, and by people who might
  use my skills."
```

---

## Output: Profile Audit Report

### Summary

Dana is an applied-AI builder (agents, MCP servers, Claude Code skills) whose profile
reads like a generic backend engineer. The bio, the empty repository descriptions, and
the absence of a Profile README all hide the one thing that would make this profile
memorable: a focused body of work at the agent/MCP/skills layer. Three repositories
(`mcp-notes-server`, `agent-playground`, `claude-skills-lab`) are active and directly
on-narrative but sit unpinned below two stale repositories. The fastest gains are free:
rewrite the bio, add a Profile README, pin and reorder the on-narrative repos, and fill
in one-line descriptions. No metric in this report is asserted by the skill; star and
traffic figures remain user-provided or `[not available]`.

### Positioning diagnosis

Per-axis score, 0 to 5, where 5 means "a hiring manager or potential user understands
it in under five seconds."

| Axis | Score /5 | Reasoning |
|---|---|---|
| Clarity of focus | 1 | Bio says "building things"; nothing signals agents/MCP/skills. |
| Differentiation | 1 | Reads like any backend engineer; the MCP/skills niche is invisible. |
| Evidence of work | 3 | Strong on-narrative repos exist, but they are unpinned and undescribed. |
| Discoverability | 1 | No README, no website, empty descriptions, no topics on repos. |
| Freshness | 4 | Three repos touched within the last three weeks (user-provided dates). |
| Trust signals | 2 | Location present; no README, links, or licenses to anchor credibility. |
| Call to action | 0 | "Open to opportunities" is passive and gives the reader nowhere to go. |
| Consistency | 2 | Active AI repos coexist with stale practice repos that dilute the story. |

Weakest axes to fix first: Call to action, Clarity of focus, Discoverability,
Differentiation.

### Audience fit

- Primary audience: engineering managers and founders hiring for applied-AI / agent
  engineering roles. They scan for a clear niche and shipped artifacts, not adjectives.
- Secondary audience: developers who might install or fork the Claude Code skills, and
  MCP users looking for a working server to learn from.
- Current fit: poor. Neither audience can tell within five seconds that this profile is
  about agents, MCP, and skills. The evidence exists but is buried and unlabeled.

### Bio rewrite

Current bio:

> Software engineer. I like building things. Open to opportunities.

Proposed bio (specific niche, an outcome, a call to action):

> I build AI agents and MCP servers, and I ship Claude Code skills that turn repeatable
> workflows into one command. Recent work: an MCP notes server and a small library of
> published skills. Hiring for applied-AI? Start with my pinned repos or reach me via
> the link below.

Why it works: it names the niche (AI agents + MCP + skills), gives an outcome ("turn
repeatable workflows into one command"), points to evidence (pinned repos), and ends
with a direct call to action. No metrics are claimed.

### Profile README recommendations (outline)

Create `dana-okonkwo/dana-okonkwo` with `README.md` containing:

1. One-line headline: what Dana builds (agents, MCP servers, Claude Code skills).
2. "What I'm building now" - three bullets, one per active repo, each a plain-language
   outcome, each linking to the repo.
3. "Claude Code skills I've published" - short list linking to `claude-skills-lab`,
   with one line on what each skill does.
4. "How I work" - two or three sentences on approach (tool-using agent loops, MCP as
   the integration layer, skills for reproducibility).
5. "Get in touch" - one link (email, site, or a contact form) as the single call to
   action. Leave metrics out unless Dana can source them.

Keep it to one screen. No badges that display counts the user cannot verify.

### Pinned repositories (suggested order, best first)

GitHub allows up to six pins. Order them so the strongest on-narrative repo leads:

1. `mcp-notes-server` - a concrete, working MCP server; the clearest single proof of
   the MCP claim. Rename the description to something like "MCP server exposing a
   personal notes store to Claude Code and other MCP clients."
2. `claude-skills-lab` - directly supports the "I ship Claude Code skills" claim and
   feeds the secondary (user) audience.
3. `agent-playground` - shows the agent-loop work; describe it as "experiments building
   tool-using agent loops over an LLM" so it reads as intentional, not a scratchpad.

Do not pin `resume-site` (14 months stale) or `leetcode-solutions` (off-narrative).
If Dana has fewer than six pin-worthy repos, pin only the on-narrative ones rather than
padding with practice repos.

### Repository hygiene

- Add a one-line description to every repository that is pinned or public. Empty
  descriptions are the biggest quick loss here (`agent-playground`, `claude-skills-lab`,
  `resume-site`, `leetcode-solutions` are all empty).
- Add relevant GitHub topics to the three pinned repos (for example: `mcp`,
  `model-context-protocol`, `ai-agents`, `claude-code`, `agent-skills`). Verify each
  topic actually matches the repo before adding it.
- Add a LICENSE to any repo Dana wants others to use (the skills and the MCP server).
- Archive or make private `resume-site` and `leetcode-solutions` if they are not meant
  to represent current work, so the profile grid reflects the narrative.
- Ensure each pinned repo's README opens with a one-paragraph "what and why" and a copy-
  paste install/run block.

### Trust signals

- Publish the Profile README (single biggest trust gain available for free).
- Add one verifiable external link (personal site, LinkedIn, or a writeup). The current
  profile has no outbound link at all.
- Add LICENSE files so the skills and MCP server look safe to adopt.
- Keep commit activity visible on the on-narrative repos; freshness is already a
  strength (user-provided recent dates) and should stay that way.
- Do not add star/download badges unless the underlying numbers are real and user-
  sourced. Fabricated or stale counts erode trust faster than having none.

### Quick wins

1. Rewrite the bio to the proposed version above (five minutes).
2. Pin and reorder the three on-narrative repos (two minutes).
3. Add a one-line description to each public repo (ten minutes).
4. Add topics to the three pinned repos (five minutes).
5. Add one outbound link to the profile (two minutes).
6. Archive `resume-site` and `leetcode-solutions` (three minutes).

### 7-day action plan

- Day 1: Ship the bio rewrite, pin and reorder the three repos, add one outbound link.
- Day 2: Draft and publish the Profile README using the outline above.
- Day 3: Write one-line descriptions and add verified topics to all public repos.
- Day 4: Add LICENSE files to `mcp-notes-server` and `claude-skills-lab`; polish the
  README of `mcp-notes-server` with a copy-paste run block.
- Day 5: Do the same README pass for `claude-skills-lab` and `agent-playground`.
- Day 6: Archive `resume-site` and `leetcode-solutions`; review the profile grid to
  confirm it now reads as an agents/MCP/skills profile.
- Day 7: Ask one peer to read the profile cold and time how long it takes them to say
  what Dana builds; if it is over five seconds, tighten the bio and README headline.

If Dana later gathers real traffic or install numbers, fold them into the README as
user-provided figures. Until then, this report leaves every metric as `[not available]`.
