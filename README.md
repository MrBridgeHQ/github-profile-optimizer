# github-profile-optimizer

A Claude Code Agent Skill that audits and optimizes your GitHub presence, then makes your repositories and your own skills discoverable. It turns a username, a pasted README, or local files into concrete deliverables: profile audits, README rewrites, repository SEO kits, and registry-submission kits for the Agent Skills / Claude Skills ecosystem.

Built to the `SKILL.md` Agent Skills format. Works offline: network, GitHub CLI, and GitHub API are optional and never required.

## Value proposition

- Stop guessing why your GitHub profile does not convert. Get a scored audit and a rewritten bio, profile README, and pinned-repo plan.
- Make each repository findable by GitHub search, Google, humans, and directories: better name, description, topics, and README outline.
- Publish your skills the right way: an SEO kit per skill repo and a per-directory submission kit, with a priority strategy so you do not waste time on low-signal catalogs.
- Position a skill so its description actually triggers usage, instead of reading like generic marketing.

## Usage examples

- "Optimize my GitHub profile, my username is `octocat`."
- "Here is my profile README, rewrite it for a freelance AI engineer." (paste the text)
- "Which of my repositories should I pin and how should I describe them?"
- "Help me list my `scraping-expert` skill in the Claude skills awesome lists."
- "Improve the `SKILL.md` frontmatter for my `wine-offer-hunter` skill so it gets discovered."

## Installation

### Claude Code, project level
Open this repository as a project in Claude Code. The skill at `.claude/skills/github-profile-optimizer/` is auto-discovered. To add it to another project, copy that folder into the project's `.claude/skills/` directory:

```bash
cp -r .claude/skills/github-profile-optimizer /path/to/your-project/.claude/skills/
```

### Claude Code, global level
Copy the skill into your user skills directory so every session can use it:

```bash
cp -r .claude/skills/github-profile-optimizer ~/.claude/skills/
```

### Invoke the skill
Just describe the task in natural language (see the prompts above). The skill activates on GitHub-profile, repository-SEO, and skill-publishing requests. You can also name it explicitly: "use the github-profile-optimizer skill to audit my profile".

## Repository structure

```
.
├── .claude/skills/github-profile-optimizer/
│   ├── SKILL.md
│   ├── references/          # playbooks + registry target list
│   ├── templates/           # output templates for each mode
│   ├── examples/            # worked examples
│   ├── scripts/             # optional public-context collector (no token)
│   └── evals/               # behavioral test cases
├── .github/                 # PR template + issue template
├── README.md
├── LICENSE
├── CHANGELOG.md
└── CONTRIBUTING.md
```

## Available modes

1. **Profile Audit** - scored review of positioning, bio, links, pinned repos, trust signals, plus a 7-day plan.
2. **Profile README Rewrite** - hero, value proposition, projects, stack, proof, CTA; short and long versions, EN/FR variant on request.
3. **Repository SEO Audit** - name, description, topics, README outline, badges, and a publication checklist.
4. **Agent Skill SEO & Registry Submission** - a per-skill SEO kit and per-directory submission kit for awesome lists and registries.
5. **Skill Positioning** - who the skill is for, what triggers it, and how it differs from a plain prompt.

## Example output (excerpt)

Input: "Optimize my GitHub profile, I am an AI/agents engineer, username `octocat`."

```
Positioning diagnosis: Medium. The bio names a role but not a specialization or an outcome.
Score: Positioning 3/5, Bio 2/5, Pinned repos 3/5, Trust signals 2/5, CTA 1/5.
Proposed bio: "AI agents and MCP tooling. I build Claude Code skills and scrapers that ship. Open to collaborations."
Pinned repos (suggested order): 1) your flagship skill, 2) an MCP server, 3) a demo with a GIF.
Quick wins: add a website link, add 5 relevant topics per repo, add one GIF to the top repo.
7-day plan: Day 1 bio + links, Day 2 profile README, Day 3-4 top-3 repo READMEs, Day 5 topics, Day 6 one demo GIF, Day 7 submit the flagship skill to one curated list.
```

Metrics such as stars or followers are never invented. If a number is needed and not provided, the skill asks for it or explains how to get it.

## Security

- The base workflow reads text you provide. It does not require network access.
- The optional `scripts/collect_github_context.py` calls public GitHub endpoints only, needs no token, and can also run in a local mode that just reads README files already on disk. It performs no writes.
- No secrets are read or stored. The skill never modifies your repositories; it proposes changes for you to apply.

## Compatibility

- Standard Agent Skills: the `SKILL.md` frontmatter (`name`, `description`) and progressive-disclosure structure follow the Agent Skills format.
- Claude Code specific: auto-discovery from `.claude/skills/` (project) and `~/.claude/skills/` (global), and the invocation phrasing above.
- To verify per platform: any non-Claude runner (other agents, IDE plugins) should be tested before you claim support. This skill does not assume cross-agent compatibility; it flags it as "to verify".

## Roadmap

- Optional GitHub CLI (`gh`) mode for richer context when a user opts in.
- More worked examples (data, design, and founder profiles).
- A topics-suggestion helper grounded in the repo's own content.

## Contribution

Improvements, new registry targets, and new examples are welcome. See `CONTRIBUTING.md`. No auto-generated dumps: every addition needs a test or a worked example.

## License

MIT. See `LICENSE`.

---

## Résumé en français

`github-profile-optimizer` est un skill Claude Code (format Agent Skills, basé sur `SKILL.md`) qui audite et optimise un profil GitHub, améliore la découvrabilité des dépôts, et prépare la publication de vos propres skills dans les annuaires et awesome lists de l'écosystème Agent Skills / Claude Skills. Il fonctionne sans accès réseau : il travaille à partir d'un nom d'utilisateur, de README collés ou de fichiers locaux. Il n'invente jamais de métriques GitHub et rappelle de vérifier les règles de chaque annuaire avant toute soumission. Cinq modes : audit de profil, réécriture du README de profil, audit SEO d'un dépôt, kit SEO et soumission aux annuaires pour un skill, et positionnement d'un skill. Installation : copiez `.claude/skills/github-profile-optimizer/` dans le dossier `.claude/skills/` d'un projet, ou dans `~/.claude/skills/` pour un usage global.

---

Part of the **[mr-bridge.com](https://mr-bridge.com)** toolkit for scraping, data, and content automation:
[Scrapers](https://mr-bridge.com/scrapers) · [MCP servers](https://mr-bridge.com/mcp-servers) · [AI workflows](https://mr-bridge.com/ai-workflows) · [Studies](https://mr-bridge.com/studies) · [Articles](https://mr-bridge.com/articles) · [Solutions](https://mr-bridge.com/solutions)

---

*Part of the [MrBridge Agent Skills catalog](https://github.com/MrBridgeHQ/skills). Browse them all at [mr-bridge.com/skills](https://mr-bridge.com/skills).*
