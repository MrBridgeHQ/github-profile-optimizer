# Repository SEO Playbook

A guide to making a repository findable and convincing for four different audiences at once: GitHub's own search, external search engines (mainly Google), human readers who land on the page, and directories or awesome lists that might feature it. Each audience reads different signals. A repo optimized for only one of them underperforms.

Two ideas run through everything below:

- **GitHub topics and the short description drive on-platform discovery.** They are the primary signals GitHub search and the topic pages use to surface your repo inside GitHub.
- **A clear README drives off-platform discovery.** Google indexes the rendered README heavily, so its structure, headings, and wording are what surface the repo in external search and what convince a human once they arrive.

Optimize both. They do not overlap.

## Repository name

The name is the strongest and least changeable signal. Get it right early; renaming later breaks links and stars context.

- **Explicit over clever.** The name should hint at what the thing is. A person scanning search results should be able to guess the purpose from the name alone.
- **Searchable.** Include the words people would actually type. If it is a Postgres backup tool, having `postgres` or `backup` in or near the name helps.
- **Avoid clever-but-opaque names.** Mythological, punning, or invented names (project `Prometheus-Nova`, `flumox`, `zap42`) carry zero meaning to a newcomer and win nothing in search. Internal codenames are fine for private work and bad for discoverability. If you love a brand name, pair it with a descriptive description and topics so the meaning is still recoverable.
- **Conventions.** Lowercase, hyphen-separated, no spaces. Keep it short enough to type and remember.

Weak but memorable brand names can work once the project is famous. Before fame, descriptive wins.

## The GitHub short description field

The one-line description under the repo name appears in GitHub search results, on your profile pins, in the repo header, and often in Google's snippet. It is prime real estate and most repos waste it.

- **Keyword-forward.** Front-load the words a searcher uses. `Fast, dependency-free CSV parser for Node.js` beats `A little project I made for parsing`.
- **One line.** It is truncated; put the value in the first half.
- **State the benefit, not the obvious.** Do not restate the name. Say what it does and for whom.
- **No filler.** Skip `A simple`, `My`, `Just a`, `awesome`. They consume the visible characters and add nothing.

## GitHub topics

Topics are the tags GitHub uses to power topic pages and refine search. They are a direct on-platform discovery lever.

- **Choose real, existing topics.** Prefer topics that already have a populated topic page (`nodejs`, `web-scraping`, `mcp`, `cli`). Real topics connect you to real browsing traffic.
- **Cover the dimensions.** Language, domain, use case, and category. A scraper might use `web-scraping`, `python`, `crawler`, `data-extraction`.
- **Do not stuff.** Ten precise topics beat thirty loose ones. Irrelevant topics dilute relevance and can look spammy. Every topic should be something a real person might browse to find a tool like yours.
- **Match user vocabulary.** Use the words your audience searches, not internal jargon.

## README structure

The README is both the Google-facing document and the human decision page. Structure it so a skimmer gets the point and a search engine gets clean headings.

- **H1 = name + tagline.** The top line should be the project name and a one-sentence value statement. This is what Google weights and what a human reads first.
- **H2 sections, in this order:**
  1. **What it does.** Two or three sentences. Plain language. What problem it solves.
  2. **When to use it (and when not).** Positions the repo against alternatives and sets expectations. Honest scope builds trust.
  3. **Install.** Copy-pasteable. The single most important block for adoption.
  4. **Usage.** The minimal path to a working result. One clear example beats an exhaustive API dump up front.
  5. **Demo.** A GIF, screenshot, or link that shows it working.
  6. **Examples.** A few real, runnable cases covering common scenarios.
  7. **License.** State it plainly and link the file.

Keep prose tight and headings descriptive; both readers (human and crawler) navigate by headings.

## Badges

Badges can add credible, at-a-glance signals, or they can be visual noise.

- **Use a badge only if it carries a message.** Build passing, version, license, coverage, downloads: each tells the visitor something.
- **Avoid badge walls.** A row of fifteen badges reads as insecurity, buries the tagline, and pushes the real content below the fold. Keep a small, meaningful set near the top.
- **Do not fake signals.** A green badge that does not reflect reality is worse than no badge.

## Install and usage clarity

Adoption is gated by time-to-first-success. The faster a visitor gets a working result, the more likely they stay.

- Provide a copy-pasteable install command with no hidden prerequisites, or list the prerequisites explicitly.
- Give the smallest possible working example immediately after install.
- Show expected output so the reader knows it worked.
- Keep the happy path free of caveats; push edge cases and configuration lower in the document.

## Demo, screenshots, and GIFs

Visual proof converts far better than prose, especially for tools with any UI or observable output.

- A short GIF of the tool running answers `does this actually work` instantly.
- Screenshots work for anything visual; keep them current so they do not misrepresent the tool.
- Put one visual near the top, above or just after the tagline, so skimmers see it.
- For CLI or library tools, a clean terminal capture of a real run serves the same purpose.

## License, releases, contribution guide

These are maintenance and trust signals that adopters and directories look for.

- **License.** No license means legally unusable for many. Add one (a `LICENSE` file) and name it in the README. Its absence is a common reason a repo is skipped.
- **Releases.** Tagged releases and a changelog show the project is versioned and maintained, and give users something stable to depend on.
- **Contribution guide.** A `CONTRIBUTING` file, clear scope, and good first issues lower the barrier for contributors and signal an active project. Many awesome lists check for these before featuring a repo.

## Search intent

For every repo, answer one question: **what query should surface this repo, and does the repo actually satisfy that query?**

- Write down the two or three searches your ideal visitor would run.
- Verify the name, description, topics, and README H1/H2 headings contain the words in those searches.
- Make sure the page then delivers on the intent: someone searching `python pdf table extraction` should, on landing, immediately see that this extracts tables from PDFs in Python and how to do it.

Aligning the page to real search intent is most of on- and off-platform SEO.

## Differentiation from similar repos

Discovery gets you seen; differentiation gets you chosen. Most categories have several similar tools.

- State plainly what makes this one different: faster, simpler, zero-dependency, better docs, a specific niche it handles that others do not.
- The `when to use it` section is the place to position honestly against alternatives.
- Concrete differentiators (benchmarks, a supported case others miss, a cleaner API) beat generic claims of being better.

## Conversion

Once a visitor is on the page, conversion is whatever action you want: star, install, open an issue, read the docs, contact you.

- Make the intended action obvious and near the top.
- Reduce friction to it (a one-line install, a `Try it` link, a clear CTA).
- Proof (demo, results, adoption context) lowers hesitation.
- A clear, well-structured README is itself a conversion tool: it signals that the project is cared for and safe to depend on.

## Repository publication checklist

- Name is explicit and searchable, not clever-but-opaque.
- Short description is one keyword-forward line stating the benefit.
- Topics are real, relevant, and cover language, domain, and use case (no stuffing).
- README H1 is name plus a one-sentence tagline.
- H2 sections present: what it does, when to use, install, usage, demo, examples, license.
- Copy-pasteable install command and a minimal working example.
- At least one visual (GIF or screenshot) near the top.
- License file present and named in the README.
- Releases tagged and a changelog if the project is used by others.
- Contribution guide or good first issues if you want contributors.
- The target search query is answered by name, description, topics, and README.
- Differentiation from similar repos is stated.
- One clear conversion action is present and easy to take.

## Naming: weak vs strong

The following pairs are illustrative and hypothetical; they are made up to show the pattern, not real projects.

- Weak: `Prometheus-Nova`  -  Strong: `s3-backup-cli`
- Weak: `flumox`  -  Strong: `csv-stream-parser`
- Weak: `helper-utils`  -  Strong: `react-form-validation`
- Weak: `my-cool-scraper`  -  Strong: `amazon-price-tracker`
- Weak: `zap42`  -  Strong: `pdf-table-extractor`
- Weak: `the-thing`  -  Strong: `postgres-migration-runner`

The strong versions win because a stranger reading a search result can tell what the tool is and whether it fits, and because the words match what people actually type.
