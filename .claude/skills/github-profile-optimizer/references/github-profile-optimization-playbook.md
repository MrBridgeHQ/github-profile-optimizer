# GitHub Profile Optimization Playbook

A practical guide to turning a GitHub profile into a clear, credible, conversion-oriented asset. The goal is not decoration. The goal is that the right visitor understands who you are, what you build, and why it matters, in seconds, and then takes one intended action.

## What a profile must communicate in under 5 seconds

A first-time visitor lands on your profile with a specific question in mind (should I hire this person, should I use this tool, should I trust this maintainer). In the first five seconds they should be able to answer three things:

1. **Who you are and what you do.** One role or specialization, not a list of ten technologies.
2. **What you produce.** Concrete artifacts: tools, libraries, agents, studies, products.
3. **What to do next.** One obvious action (hire, install, contact, read, follow).

If any of these three is missing or buried, the visitor leaves with no memory of the profile. Treat the first screen (avatar, name, headline, bio, pinned repos) as the entire pitch. Everything below the fold is supporting evidence.

## The bio

The bio is the single highest-leverage field. It appears on your profile, in search hovercards, and next to your comments across GitHub.

**Formula:** `[what you do] + [for whom / in what domain] + [proof or specialization] + [optional signal or CTA]`.

Examples of the shape (adapt to your reality):
- `I build MCP servers and scrapers. TypeScript / Python. Focus on anti-bot and data pipelines.`
- `Backend engineer. Payments infrastructure. Ex-fintech. Open to consulting.`

**Length:** GitHub caps the bio around 160 characters. Aim to use most of it, but every word must carry information. One or two short lines beat a paragraph you cannot fit.

**What to cut:**
- Empty self-labels: `passionate developer`, `tech enthusiast`, `lifelong learner`, `coding ninja`, `problem solver`. They describe nobody and differentiate no one.
- Long technology lists. Three named specialties read as expertise. Twelve read as a beginner listing a curriculum.
- Motivational filler and quotes. They cost characters and add zero information.
- Emoji spam. One or two functional emoji are fine; a row of ten is noise.

**Rule of thumb:** if a sentence would be equally true for ten thousand other developers, delete it.

## Identity fields: avatar, name, headline, location, website, social links

These are the frame around the bio. Each one is a small trust signal, and empty or careless ones subtract credibility.

- **Avatar.** A real, recognizable image (a clear photo for a person, a clean logo for a project or company account). The default identicon signals a throwaway account. Avoid a blurry crop or a meme if the profile is meant to convert clients or employers.
- **Name.** Use the name people will recognize or search for. Consistency with LinkedIn, your site, and your commit author name helps people connect the dots.
- **Headline / status.** The status emoji and message are optional but usable: a short `Available for contract work` or `Building X` is a lightweight CTA that most people never set.
- **Location.** Useful for hiring, timezone, and local relevance. Optional if you deliberately want to stay region-neutral, but an empty field where clients expect one can read as evasive.
- **Website.** Point it at the single best destination: your portfolio, your product, your company, or your best repo. Do not leave it blank if you have anything to link. One strong link beats none.
- **Social / links block.** GitHub lets you pin a few links. Choose the ones that reinforce your positioning (site, LinkedIn, X, a key project). Do not list every account you have ever created; dead or empty profiles hurt more than they help.

## The profile README (the special `<username>/<username>` repo)

GitHub renders the README of a repository whose name exactly matches your username at the top of your profile. This is your longest-form, fully controlled real estate. If you do not have it, create a public repo named exactly your username and add a `README.md`.

Keep it scannable. A visitor skims; they do not read top to bottom. Suggested sections, in priority order:

1. **Headline line.** One sentence that repeats and sharpens the bio. This is the thesis.
2. **What I do / what I build.** Two to four bullets tying you to concrete outcomes, not adjectives.
3. **Selected work.** Three to six items, each a link plus a one-line result (`X - reduced Y by Z`, `X - used by team T for use case U`). This overlaps with pinned repos on purpose; reinforce, do not contradict.
4. **Stack / specialties.** A short, honest list of what you actually work in. Group it; do not dump a badge wall.
5. **Contact / CTA.** How to reach you and for what (hire, collaborate, sponsor, follow).

Optional, only if they earn their space: a short now section (current focus), writing or talks, and lightweight stats. Avoid auto-generated widgets that add color but no information (long streak graphs, trophy walls, quote-of-the-day boxes). They read as filler and slow the page.

**Keep it current.** A README that says `currently learning React` from three years ago actively damages trust. Stale beats empty, but current beats both.

## Pinned repositories

You can pin up to six repositories. They are the visual center of the profile and the fastest proof of what you do.

**How to choose:**
- Pin your **strongest and most representative** work, not your most recent commit. Relevance and quality over recency.
- Each pin should map to your positioning. If your bio says data engineering, the pins should back that claim, not show a half-finished game jam.
- Prefer repos with a clean README, a clear description, and evidence they work (demo, screenshot, install line, usage example).
- If a repo is empty, unfinished, or embarrassing, do not pin it. An unpinned slot is better than a weak one.

**Order:** put the best first. Visitors read left to right, top to bottom, and attention decays fast. The first pin does the most work.

**Tie each pin to a concrete result.** GitHub shows the repo description under each pin, so make that description a benefit, not a restatement of the name. `parser` is a name; `Fast CSV parser, handles 1M rows/s, zero dependencies` is a reason to click. Where you can, anchor to a real outcome: users, adoption, a measurable improvement, a problem solved.

## Coherence between profile, README, pinned repos, and activity

The four surfaces (identity block, profile README, pinned repos, public activity) are read together, and mismatches are noticed.

- If the bio claims a specialty, the pins and README should demonstrate it.
- If the README lists a flagship project, it should be pinned.
- If the profile positions you as an active builder, the contribution activity should not be a flat empty graph for the last year. Activity does not need to be constant, but a total mismatch between claim and visible work undermines the claim.
- Descriptions, wording, and links should agree across surfaces. A visitor who spots a contradiction stops trusting all of it.

Coherence is a multiplier: three consistent signals reinforce each other; one contradiction discounts the rest.

## Trust and credibility signals

Beyond raw claims, visitors look for proof that costs effort to fake:

- Repositories with real READMEs, licenses, and working install steps.
- Recent, meaningful commits (substance over cosmetic streaks).
- Issues and discussions that are triaged and answered, not abandoned.
- Consistency between GitHub, a personal site, and other public profiles.
- Clear ownership and maintenance signals (changelog, releases, responsive replies).

Do not fabricate signals. Inflated or invented credibility is fragile and easy to catch, and one exposed exaggeration poisons the whole profile.

## Call to action (CTA)

Every profile should make one intended next step obvious. Decide what you want a visitor to do and remove friction around it:

- Hiring or freelance: a clear `Open to work / contact me at ...` and a direct channel.
- Product or tool: an install line or a `Try it` link near the top.
- Open source: `Star`, `Open an issue`, `Read the docs`, `Sponsor`.
- Audience building: `Follow`, `Read my writing`, `Subscribe`.

One primary CTA beats five competing ones. If everything is a CTA, nothing is.

## Differentiation

Most profiles are interchangeable because they describe generic developers with generic stacks. You stand out by being specific:

- Name a niche or a hard problem you solve, not a broad category.
- Show a distinctive result or artifact that others do not have.
- Use concrete numbers and named use cases instead of adjectives.
- Have a point of view (what you build, how, and why) rather than a feature list.

Specificity is the cheapest differentiator available and almost nobody uses it.

## Presentation debt

Presentation debt is the accumulated gap between the quality of your work and the quality of how it is presented. Symptoms:

- Strong repos with empty or one-line READMEs.
- A blank profile README while your best work is invisible.
- Pinned repos that no longer represent what you do.
- Stale bio, dead links, outdated now sections.
- Great code that a visitor cannot understand, run, or evaluate in under a minute.

Presentation debt is invisible to you (you know the work) and glaring to visitors (they do not). Paying it down is often higher ROI than writing more code, because it converts work you already did into work people can see.

## Audience-specific guidance

### Business / freelance / founder profiles

The visitor is a potential client, partner, or hire. They are evaluating whether to trust you with money or a project.

- **CTA first.** Make it trivial to contact you and to understand what you sell. `Available for contract work in X` plus a direct channel near the top.
- **Proof over claims.** Case-style pins: `Built X for a client in domain Y, result Z`. Concrete outcomes, real use cases, and where possible named results. Testimonials or links to shipped products help.
- **Specialization.** Position on one clear domain. A specialist commands trust and rate; a generalist competes on price. Cut the everything-list.
- **Professionalism.** Real photo, consistent name, working links, clean flagship repos. Nothing signals a serious operator faster than a profile that is coherent and maintained.

### Open-source profiles

The visitor is a potential user or contributor deciding whether to adopt and invest in your project.

- **Install.** Lead the flagship repos with a copy-pasteable install and a minimal working example. Time-to-first-success is the metric.
- **Contribution.** Make contributing legible: a `CONTRIBUTING` guide, good first issues, clear scope, and a visible response pattern to PRs.
- **Roadmap.** A short roadmap or `now / next / later` shows the project is alive and directed, which reduces adoption risk.
- **Issues and discussions.** Triaged issues and active discussions are strong health signals. Abandoned issue trackers are strong warning signals. Show that maintenance is real.
- **Trust.** License, releases, changelog, and responsiveness. Adopters are underwriting future maintenance; give them reasons to believe it will continue.

### AI / agents / MCP / skills profiles

The visitor wants to know if your tool actually works with their setup, is safe to run, and is honest about its limits. This audience is skeptical because the space is full of hype and non-working demos.

- **Compatibility.** State precisely what it runs with. Distinguish a standard Agent Skill (portable across compatible agents) from something that is Claude Code specific, from anything you have not verified. Do not imply broad cross-agent support you have not tested; say what you confirmed and what you did not.
- **Reproducible examples.** Show a real invocation and its real output. A concrete, runnable example beats any description. If the reader cannot reproduce it, they will assume it does not work.
- **Security.** Be explicit about what the tool can access and do (network, filesystem, credentials, external calls), and what it does not touch. This audience reads permission and data-flow claims carefully.
- **Limits.** State the honest edges: what it does not do, where it fails, known constraints. Admitting limits raises credibility; hiding them destroys it on first contact.
- **Concrete usage.** Real trigger phrases, real inputs, real outputs. Not marketing adjectives about being powerful or seamless.

## Quick wins

- Fill or rewrite the bio using the formula; cut every generic self-label.
- Create the `<username>/<username>` profile README if it does not exist.
- Set a real avatar and a working website link.
- Pin your six strongest repos, best first, unpin the weak ones.
- Rewrite each pinned repo description as a benefit or result, not a name restatement.
- Add a single, obvious CTA aligned with your goal.
- Remove dead links and stale now / learning statements.
- Add a license and a one-line install to your flagship repo.
- Check coherence: bio, README, pins, and activity should tell one story.

## 7-day plan

- **Day 1 - Positioning.** Decide the one thing this profile is for (hire, adopt, follow, sell) and the single primary CTA. Write the one-sentence thesis.
- **Day 2 - Identity block.** Rewrite the bio with the formula. Fix avatar, name, location, website, and social links. Cut generic filler.
- **Day 3 - Profile README.** Create or overhaul `<username>/<username>`: headline, what I do, selected work, stack, CTA. Keep it scannable.
- **Day 4 - Pinned repos.** Choose the six strongest, order best first, unpin weak ones, align them with the positioning.
- **Day 5 - Repo descriptions and READMEs.** Rewrite each pinned repo's short description as a benefit. Ensure each flagship repo has a real README, license, and install line. (See the Repository SEO Playbook.)
- **Day 6 - Coherence and CTA.** Read the profile as a stranger would. Fix contradictions across bio, README, pins, and activity. Verify the CTA is obvious and reachable.
- **Day 7 - Trust and polish.** Add proof (results, links, examples), remove dead links and stale claims, confirm every link resolves, and do a final under-5-seconds test.
