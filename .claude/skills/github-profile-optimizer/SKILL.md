---
name: github-profile-optimizer
description: Use when optimizing a GitHub profile or making repositories and skills more discoverable. Covers auditing or rewriting a GitHub profile README, improving the bio, avatar, headline, pinned repositories and developer branding, doing GitHub SEO and repository discoverability work, and preparing to publish and list Agent Skills / Claude Code SKILL.md skills in awesome lists, registries and directories. Triggers on "optimize my GitHub profile", "GitHub profile README", "profile README", "pinned repositories", "developer branding", "GitHub SEO", "repository discoverability", "agent skills publishing", "submit skill to awesome list", "SKILL.md visibility", "Claude skills registry".
---

# GitHub Profile Optimizer

Audit and improve a GitHub presence, then make the user's repositories and Agent Skills discoverable. This skill produces concrete, structured deliverables (audits, rewrites, SEO kits, submission kits), not vague advice. It works from whatever the user can provide: a username, pasted README text, local files, or screenshots. Network access is optional and never required.

## When to use

Use this skill when the user wants to:
- audit or optimize a GitHub profile (bio, headline, avatar, links, pinned repos, profile README);
- rewrite or create a profile README;
- improve a repository's discoverability (name, description, topics, README, badges, releases);
- publish and list a skill in the Agent Skills / Claude Skills ecosystem (awesome lists, registries, directories);
- position a skill so its description actually triggers usage.

Do not use it to fabricate metrics, invent registry rules, or assert cross-platform compatibility that has not been checked.

## Modes

Pick the mode that matches the request. Each mode has an output template in `templates/` and a worked example in `examples/`.

| Mode | Use when | Output template |
|---|---|---|
| **Profile Audit** | Full profile review | `templates/profile-audit-report.md` |
| **Profile README Rewrite** | Create or rewrite the profile README | `templates/profile-readme-template.md` |
| **Repository SEO Audit** | Make one repo more discoverable | `templates/repository-audit-report.md` |
| **Agent Skill SEO & Registry Submission** | Package and list a skill (central mode) | `templates/skill-repository-seo-kit.md` + `templates/registry-submission-kit.md` |
| **Skill Positioning** | Sharpen who a skill is for and what triggers it | inline, see below |

### Profile Audit
Analyze positioning clarity, the GitHub bio, avatar/name/headline/location/website/socials, coherence between profile + README + pinned repos + activity, readability for the target audience (recruiters, clients, open-source users, investors, partners), credibility signals, call to action, differentiation, and presentation debt.
Output: synthetic diagnosis, per-axis score, priority problems, concrete recommendations, a proposed new bio, a profile-README structure, pinned-repo suggestions, a quick-wins checklist, and a 7-day improvement plan.

### Profile README Rewrite
Produce a profile README with: hero section, value proposition, main projects, tech stack, proof/metrics (only if the user provides them), open source / products / clients / content, CTA, and contact. Provide a short version and a long version, and an EN/FR variant when asked. Follow `references/github-profile-optimization-playbook.md`.

### Repository SEO Audit
Analyze repo name, GitHub short description, topics, README H1/H2, badges, install, usage, demo, screenshots/GIFs, license, releases, contribution guide, examples, search intent, and differentiation from similar repos.
Output: optimized GitHub description, a topics list, a README outline, a tagline, a short pitch, a long pitch, a publication checklist, and naming suggestions if the current name is weak. Follow `references/repository-seo-playbook.md`.

### Agent Skill SEO & Registry Submission (central mode)
Two deliverables:
1. A **skill-repository-seo-kit** (`templates/skill-repository-seo-kit.md`): kebab-case skill name, optimized frontmatter description, optimized README, tagline, 280-character description, 600-character description, primary and secondary categories, keywords, recommended GitHub topics, badges, usage examples, local Claude Code install, generic Agent Skills install if applicable, explicit compatibility (verified vs to-verify), security notes (tools, network, secrets, files modified), license, a recommended demo/screenshot, and a pre-submission checklist.
2. A **registry-submission-kit** (`templates/registry-submission-kit.md`) per target directory. Use the priority strategy and the target list in `references/agent-skills-registry-playbook.md` and `references/registry-targets.md`. For each target, produce: priority level, strategic reason, likely category, proposed README line format, PR body, PR title, pre-PR checklist, risk of rejection, and required adaptations.
Always verify each directory's current submission rules before submitting; do not assume community contributions are accepted.

### Skill Positioning
Answer, for a given skill: who is it for, what precise pain it solves, what user request should trigger it, what keywords belong in the description, how to avoid a too-generic description, how it differs from a plain prompt, and what examples prove it works.

## Workflow

1. Identify the mode from the request (a request can chain several modes).
2. Gather inputs: username, pasted README, local files, screenshots. If needed, offer the optional `scripts/collect_github_context.py` to collect public context (never required, no token needed).
3. Never invent data. If a metric or a registry rule is not available, say how to obtain it or ask the user for it.
4. Produce the deliverable using the matching template. Fill only what the evidence supports; mark gaps as "to confirm".
5. End with an action plan (quick wins first) and, for skills, a submission kit.

## Output and reliability rules

- Prefer clarity over visual effects. No badge walls without a message. No vague claims ("passionate developer").
- Positioning must be understandable in under 5 seconds. Best projects go to the top, each tied to a concrete result or use case.
- Do not fabricate stars, downloads, or any GitHub metric. Distinguish observed facts from suggestions.
- Network, GitHub CLI, and GitHub API usage are optional, documented, and never required for the base workflow.
- Do not overstate multi-agent compatibility. Separate what is standard Agent Skills, what is Claude Code specific, and what must be verified per platform. See `references/agent-skills-registry-playbook.md`.
- For registries: verify each target's current rules before submitting; frame targets as candidates to confirm, not guarantees.

## Files in this skill

| Load when you need... | File |
|---|---|
| Profile optimization playbook | `references/github-profile-optimization-playbook.md` |
| Repository SEO playbook | `references/repository-seo-playbook.md` |
| Agent Skills discoverability strategy | `references/agent-skills-registry-playbook.md` |
| Structured registry target list | `references/registry-targets.md` |
| Output templates | `templates/*.md` |
| Worked examples | `examples/*.md` |
| Optional context collector | `scripts/collect_github_context.py` (see `scripts/README.md`) |
| Behavioral test cases | `evals/evals.json` |
