# Skill Repository SEO Kit

> Placeholder convention: replace every `[placeholder]` with real content. Where a number belongs, use `[metric: provided by user or 'not available']`. Never invent stars, installs, or dates. Any compatibility or registry claim is marked `verified` or `to verify`, never assumed.

## Skill name (kebab-case)
The canonical identifier used in the skill directory and frontmatter.

- Name: [my-skill-name]

## Frontmatter description (activation-oriented trigger, not marketing)
Describe when the skill should activate, using trigger phrases, not sales language.

- Description: [Use when the user ... Triggers on "...", "...".]

## Repository description
The GitHub repo description for the skill's hosting repository.

- Description: [one clear sentence, keyword-aware]

## Tagline
A short memorable line for listings and headers.

- Tagline: [short line]

## Short listing description (280 characters)
Note: keep this at or under 280 characters.

- Description: [<=280 chars]

## Long listing description (600 characters)
Note: keep this at or under 600 characters.

- Description: [<=600 chars]

## Categories
Where the skill belongs in a directory taxonomy.

- Primary: [primary category]
- Secondary: [secondary category]

## Keywords
Search terms a user would use to find this skill.

- Keywords: [keyword-1], [keyword-2], [keyword-3], [keyword-4]

## GitHub topics (recommended, pick real ones)
Suggest topics, then keep only the accurate ones.

- Suggested: [topic-1], [topic-2], [topic-3], [topic-4]
- Note: pick only real, accurate topics.

## Badges
Badges to display, only where the underlying fact is true.

- Suggested badges: [license], [version], [platform], [status]
- Note: add a badge only if the claim behind it is real and current.

## Compatibility table
State support honestly. Use `verified` when tested, `to verify` when assumed.

| Platform | Status verified/to-verify | Notes |
|---|---|---|
| Claude Code (project) | [verified / to verify] | [notes] |
| Claude Code (global) | [verified / to verify] | [notes] |
| Generic Agent Skills runner | [verified / to verify] | [notes] |
| Other agents | [verified / to verify] | [notes] |

## Security notes
Be explicit about what the skill touches.

- Tools used: [tools the skill invokes]
- Network: [none / describe outbound calls]
- Secrets: [none / describe what is read and from where]
- Files modified: [none / describe what is written or changed]

## Install instructions
How to install in each supported context.

- Claude Code (project): [steps to place the skill under the project's skills directory]
- Claude Code (global): [steps to place the skill under the user's global skills directory]
- Generic Agent Skills (if applicable): [steps, only if the runner is verified compatible]

## Example prompts
Prompts that reliably trigger and exercise the skill.

- [example prompt 1]
- [example prompt 2]
- [example prompt 3]

## Demo idea
A concrete, reproducible demo a visitor can run or watch.

- Idea: [what the demo shows and how]

## Submission readiness checklist
Confirm each item before submitting the skill anywhere.

- [ ] Skill name is kebab-case and unique
- [ ] Frontmatter description is activation-oriented
- [ ] Short (<=280) and long (<=600) descriptions written and within limits
- [ ] Categories and keywords chosen
- [ ] GitHub topics are real and accurate
- [ ] Compatibility table filled with verified/to-verify markers
- [ ] Security notes complete (tools, network, secrets, files)
- [ ] Install instructions tested
- [ ] Example prompts confirmed to trigger the skill
- [ ] Demo available or described
- [ ] License present in the repository
