# Example: Repository SEO Kit for scraping-expert

This worked example shows the github-profile-optimizer skill producing a filled
Skill Repository SEO Kit for a Claude Code skill repository named `scraping-expert`.
The positioning surfaces ethical, compliant, resilient scraping throughout. No GitHub
metrics are invented; any count that would appear is left as user-provided or
`[not available]`, and every registry or marketplace rule is framed as "verify before
submitting."

---

## Input (as supplied to the skill)

```yaml
repo_name: scraping-expert
type: claude-code-skill
one_liner_from_user: "A skill that helps design and build ethical, resilient web scrapers."
capabilities:
  - ethical scraping decisions (robots.txt, ToS, legitimate use)
  - structured data extraction from HTML and JSON endpoints
  - Playwright, requests, and parsing (selectors, schemas)
  - anti-fragile selectors and graceful degradation
  - security and compliance guardrails
runtime: Claude Code (verified by user); other runners not tested
stars: "[not available]"
```

---

## Output: Skill Repository SEO Kit

### Name (kebab-case)

`scraping-expert`

Already kebab-case and descriptive. Keep it. If a namespace is required by a target
directory, prefer `scraping-expert` unqualified and add the owner handle at submission
time rather than baking it into the repo name.

### Frontmatter description (activation-oriented)

This is the `description:` in the skill's `SKILL.md` frontmatter. It is written so
Claude activates the skill at the right moment, and it leads with the compliance framing.

```yaml
description: >-
  Use when the user wants to design, build, or debug a web scraper the right way:
  choosing an ethical, compliant approach (check robots.txt and Terms of Service,
  confirm a legitimate use case), extracting structured data from HTML or JSON
  endpoints, writing anti-fragile resilient selectors, and handling the work with
  Playwright, requests, and parsing libraries. Triggers on "build a scraper",
  "extract data from a site", "resilient selectors", "is this scraping allowed",
  "robots.txt", "respect ToS", or any request that pairs data extraction with a
  concern for legality, reliability, or security.
```

### Repository description (GitHub "About")

> Claude Code skill for building ethical, compliant, anti-fragile web scrapers:
> structured extraction with Playwright, requests, and parsing, with robots.txt and
> ToS checks built into the workflow.

### Tagline

> Scrape the right things, the right way: resilient, structured, and compliant.

### 280-character description

> A Claude Code skill for building web scrapers that hold up in production and stay on
> the right side of the rules. It guides ethical decisions (robots.txt, Terms of
> Service, legitimate use), structured extraction with Playwright and requests, and
> anti-fragile selectors that degrade gracefully. (275 characters)

### 600-character description

> scraping-expert is a Claude Code skill for engineers who need to extract web data
> responsibly. It starts where good scraping starts: does robots.txt and the site's
> Terms of Service allow it, and is the use case legitimate? From there it helps you
> pick the right tool (Playwright for rendered pages, requests for JSON endpoints),
> write resilient selectors that survive markup churn, and structure the output into a
> clean schema. Security and compliance are treated as first-class concerns, not
> afterthoughts: no credential leaks, no bypassing of access controls, and graceful
> degradation when a page changes. The result is a scraper that is maintainable,
> auditable, and defensible. (about 660 characters; trim the final sentence to fit a
> 600-character limit if a target enforces it.)

### Categories

- Primary category: Developer Tools / Data Extraction
- Secondary category: Web Automation and Testing (Playwright-based flows)

Verify the exact category taxonomy of each target directory before submitting; category
names differ between GitHub Topics, awesome lists, and searchable catalogs.

### Keywords

ethical web scraping, compliant data extraction, robots.txt, Terms of Service,
structured extraction, resilient selectors, anti-fragile scraping, Playwright, requests,
HTML parsing, JSON endpoint extraction, Claude Code skill, agent skill, data pipeline
compliance, graceful degradation.

### Recommended GitHub topics

Pick only topics that genuinely match the repo, and confirm each is an accepted topic
before adding it:

`web-scraping`, `playwright`, `data-extraction`, `python`, `claude-code`,
`agent-skills`, `robots-txt`, `web-automation`, `structured-data`, `compliance`

### Badges

Use only badges whose value is real and verifiable. Avoid star/download-count badges
unless the number is user-sourced and current.

- License badge (once a LICENSE file is present): `![License](license-shield)`
- "Claude Code skill" badge (static label, no fabricated count).
- "Compatibility: Claude Code verified" static badge (see table below).
- Do NOT add a star-count or install-count badge here; those figures are
  `[not available]` and must not be fabricated.

### Compatibility table

| Runner / host | Status | Notes |
|---|---|---|
| Claude Code | Verified | Tested by the author; primary target. |
| Generic MCP-capable runner | To verify | Not yet tested; confirm before claiming support. |
| Other agent frameworks | To verify | No compatibility asserted until tested. |

### Security notes

- Tools used: browser automation (Playwright) and HTTP (requests). The skill selects
  the lighter tool when a JSON endpoint makes a browser unnecessary.
- Network access: yes, when actually scraping a target. The skill does not make network
  calls during setup or planning.
- Secrets required: none. The skill does not require API keys or credentials to
  function; if a target site requires authenticated access, the skill flags that
  authenticated scraping needs explicit authorization and must respect access controls
  rather than circumvent them.
- Files modified: none by default. Output is written only to paths the user specifies.
- Guardrails: checks robots.txt and Terms of Service, confirms a legitimate use case,
  never bypasses login walls, CAPTCHAs, or other access-control mechanisms, and never
  advises on circumventing rate limits in a way that harms the target.

### Install

Project-level (skill available inside one repository):

```bash
mkdir -p .claude/skills
git clone <repo-url> .claude/skills/scraping-expert
```

Global (skill available across all projects):

```bash
mkdir -p ~/.claude/skills
git clone <repo-url> ~/.claude/skills/scraping-expert
```

Confirm the target directory's expected install path before publishing install
instructions; conventions differ between hosts.

### Example prompts

- "I need to pull product prices from this catalog page. Is scraping it allowed, and
  what's the most resilient way to do it?"
- "This site loads data from a JSON endpoint. Should I use Playwright or just requests?"
- "My selectors keep breaking when the site updates. Make them anti-fragile."
- "Check this target's robots.txt and Terms of Service and tell me whether my use case
  is legitimate before I write any code."
- "Structure the extracted rows into a clean schema and handle missing fields
  gracefully."

### Demo idea

A short, self-contained demo against a scraping-sandbox site that explicitly permits
automated access (for example a documented "quotes to scrape" style practice site).
The demo walks through the full skill flow: read robots.txt, confirm the practice site
permits scraping, choose requests over Playwright because the data is server-rendered,
write a resilient selector, and emit a structured JSON schema with graceful handling of
a missing field. The demo deliberately uses only a site that authorizes automated
access, reinforcing the compliance framing.

### Submission readiness checklist

- [ ] LICENSE file present and correct.
- [ ] README opens with the tagline and a "what and why" paragraph.
- [ ] Frontmatter description is activation-oriented and leads with compliance framing.
- [ ] Compatibility table reflects only tested runners (Claude Code verified; others
      marked "to verify").
- [ ] Security notes section present and accurate (tools, network, secrets, files).
- [ ] Topics added match the repo and are confirmed valid.
- [ ] No fabricated metrics anywhere; counts left as user-provided or `[not available]`.
- [ ] Demo runs against a site that authorizes automated access.
- [ ] Target directory's current submission rules reviewed and met (verify before
      submitting; rules change).
