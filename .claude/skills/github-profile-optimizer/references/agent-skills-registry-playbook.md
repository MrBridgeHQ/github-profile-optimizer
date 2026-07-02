# Agent Skills Registry Playbook

A strategic guide to making an Agent Skill (also called a Claude Skill) discoverable, without wasting effort on low-signal channels and without making claims you cannot back up. The core insight: discoverability in this ecosystem is won by being featured in a small number of curated, trusted places with an exemplary repo, not by spraying a listing across every catalog that will accept it.

Before anything else, one hard rule that this document repeats because it matters: **verify each directory's current rules before you act.** The ecosystem is young and moving fast. Lists appear, get renamed, change their contribution process, or stop accepting submissions. Nothing in this playbook asserts that a given directory exists today or accepts your submission. Confirm before you invest time.

## Why curated awesome lists matter more than noisy mega-catalogs

Not all directories are equal, and volume is not the goal.

- **Curated awesome lists** are maintained by a human or small team who reject junk. Being accepted there is itself a quality signal, the audience trusts the list, and the list often ranks in search. A single line in a respected awesome list can outperform a hundred auto-generated catalog entries.
- **Noisy mega-catalogs** ingest everything automatically. Your entry sits among thousands of undifferentiated, often broken entries. Little curation means little trust and little qualified traffic. Presence there is cheap and worth roughly what it costs.
- **Low-signal auto-generated catalogs** scrape GitHub and republish READMEs with no review. They add near-zero discovery value and sometimes misrepresent your project. Being in them rarely helps and occasionally hurts.

The asymmetry is the whole point: effort spent making one clean, exemplary repo and landing it in a few curated lists beats effort spent submitting a mediocre repo everywhere.

## Priority strategy

Work the tiers in order. Do not skip tier 1 to chase volume in tier 3.

- **Priority 1 - Curated quality lists.** Human-maintained awesome lists with real editorial standards and a trusted audience. These are the highest-value targets. Aim to be accepted here first, which usually means your repo must already be exemplary.
- **Priority 2 - Installable catalogs or searchable catalogs.** Directories or sites where users can actually find and install skills, and that have real (even if lighter) curation or a functioning search. Good secondary reach.
- **Priority 3 - Noisy mega-catalogs.** Broad, low-curation aggregators. Low effort, low return. Submit if it is nearly free; do not build strategy around them.
- **Avoid - Low-signal auto-generated catalogs.** Scrape-and-republish sites with no review. Not worth pursuing; sometimes worth requesting removal if they misrepresent you.

**Across every tier, the prerequisite is the same:** a clean pull request pointing to an exemplary repo, with a real README, a working demo or reproducible example, a clear license, and a short honest description. The repo does most of the persuading. A great repo in a good list compounds; a weak repo everywhere does not.

## How to prepare a clean PR

Most curated lists are GitHub repos that accept contributions by pull request. A clean, minimal PR is far more likely to be merged quickly.

1. **Read the rules first.** Open the list's `CONTRIBUTING` file (or its README contribution section) and read exactly how entries are formatted and where they go.
2. **Fork the list repo.**
3. **Add one line in the correct category.** Match the existing format character for character: the same link style, the same description length, the same punctuation. Put it in the right section, and respect alphabetical or other ordering if the list uses one.
4. **Keep the diff minimal.** Change only what you need to add your entry. Do not reformat the file, reorder other entries, fix unrelated typos, or touch the table of contents unless the rules ask you to. A one-line diff is easy to review and merge; a sprawling diff invites rejection.
5. **Write a short, honest PR description.** Say what the skill does in one or two sentences and link the repo. Do not oversell.
6. **Meet their bar.** If the list requires a license, a demo, or a minimum README, make sure your repo already has it before you open the PR.

A reviewer approving a one-line diff that follows the format is a five-second decision. Make it that easy.

## How to write a frontmatter description that triggers usage

For Agent Skills, the frontmatter `description` is not marketing copy. In compatible agents it is the text the model reads to decide whether to activate the skill. Write it to trigger correctly, not to impress a human.

- **Activation-oriented.** Describe the situations in which the skill should be used, in the words a user would actually use. The model matches the user's request against this text.
- **Include real trigger phrases.** Name the concrete tasks, tools, error messages, or file types that should invoke the skill. If it handles PDF tables, say `extract tables from PDF`, not `document intelligence`.
- **Concrete, not marketing.** Avoid `powerful`, `seamless`, `next-generation`. They never appear in a user's request, so they never trigger activation and they waste the description's budget.
- **Cover the real cases, skip the rest.** List the genuine triggers; do not pad with situations the skill does not handle, or it will mis-fire.

A good description reads like a precise `use this when ...` clause, packed with the exact phrases a user would type.

## How to tell a real skill from an auto-generated dump

Curators and users both filter hard, and so should you when studying the field. Signals of a real skill:

- A README written for a human, with what it does, when to use it, install, and a real example.
- A reproducible example with real input and real output.
- A license, and honest statements of scope and limits.
- Evidence it works and is maintained (commits, issues addressed, releases).

Signals of an auto-generated dump:

- A boilerplate or template README with placeholders left in.
- No example, or an example that clearly cannot run.
- Grandiose claims with no proof and no limits stated.
- No license, no activity, one commit, and a description full of adjectives.

Build the real version. It is the thing curated lists accept and users keep.

## Documenting compatibility, security, and limits honestly

This ecosystem is skeptical for good reason, and honest documentation is a competitive advantage.

- **Compatibility.** State exactly what you tested it with. Be precise about the layers (see the next section): what is standard Agent Skill behavior, what is specific to a particular agent or client, and what you have not verified. Do not imply broad cross-agent support you have not confirmed.
- **Security.** Spell out what the skill can access and do: network calls, filesystem access, credentials, external services, code execution. Say what it does not touch. Users and curators read this carefully; vagueness reads as a red flag.
- **Limits.** State what it does not do, where it breaks, and known constraints. Admitting limits raises trust. Hiding them gets you found out on first use and burns credibility permanently.

## How to organize multiple skills: separate repos vs monorepo

If you publish several skills, the packaging choice has real trade-offs.

**Separate repos (one skill per repo):**
- Each skill gets its own name, README, topics, stars, and issue tracker, which is better for per-skill search and discovery.
- Cleaner for listing in awesome lists that expect one repo per entry.
- Easier for a user to adopt exactly one skill.
- More overhead to maintain (many repos, duplicated scaffolding).

**Monorepo (many skills in one repo):**
- One place to maintain, shared tooling and CI, easier cross-skill consistency.
- Concentrates stars and attention on a single repo, which can help a flagship.
- Harder to list individual skills in directories that expect a single-skill repo, and a user wanting one skill gets the whole repo.
- Discovery is coarser: search surfaces the repo, not each skill.

**Rule of thumb:** if the skills are independent and you want each to be found on its own, prefer separate repos. If they are a cohesive suite maintained together, a monorepo is fine, with a strong top-level README that indexes each skill.

## Warning: verify before you submit

This is the rule that overrides convenience. Restated because it is the most common way to waste effort or cause friction:

- **Always read each directory's current `CONTRIBUTING` and submission rules before acting.** Formats, categories, and acceptance policies change.
- **Do not assume community contributions are accepted.** Many repos are reference material, not open submission queues.
- **This is especially true for the official `anthropics/skills` repository.** Treat it as the canonical reference to study and align with, and possibly a distribution surface, but do not assume it accepts community pull requests. Verify its current policy before attempting anything; do not open a PR on an assumption.

When in doubt, the safe default is: study the target, confirm it accepts submissions, follow its exact format, or do not submit.

## Distinguishing the layers: standard vs Claude Code specific vs to verify

Be precise about what your claims rest on, because this audience checks.

- **Standard Agent Skills.** The general Agent Skills format and behavior (a skill directory with a frontmatter `description` that an agent reads to decide activation). This is the portable, cross-compatible layer, to the extent a given agent implements the standard. Even here, do not overstate: an agent supports it only if it actually implements the format.
- **Claude Code specific.** Behaviors, paths, packaging, or invocation details that are particular to Claude Code (or to a specific client). These do not automatically carry over to other agents. Label them as such.
- **To verify per platform.** Anything you have not personally tested on a given agent or client. Mark it explicitly as unverified rather than implying it works everywhere.

The honest framing is three buckets: this is standard and portable, this is specific to one platform, and this I have not verified. State which bucket each claim falls in. That precision is exactly the credibility signal this ecosystem rewards.
