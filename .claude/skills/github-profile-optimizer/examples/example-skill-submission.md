# Example: Registry Submission Kit for wine-offer-hunter

This worked example shows the github-profile-optimizer skill producing a filled
Registry Submission Kit for a Claude Code skill named `wine-offer-hunter`. It covers
three ecosystem targets in priority order. Every registry rule is framed as "verify
current rules before submitting" because directory requirements change over time. No
GitHub metrics are invented; any count that would appear is left as user-provided or
`[not available]`.

---

## Positioning summary

- Who it is for: wine buyers, collectors, and small merchants who want help finding and
  comparing wine offers and deals, and deciding whether an offer is actually worth it.
- The precise pain: good wine offers are scattered, availability shifts hour to hour,
  and listed prices move; it is hard to tell a genuine deal from noise without
  structured comparison.
- The trigger query: "find me a good deal on this wine", "compare these wine offers",
  "is this bottle a fair price right now".
- Keywords: wine deals, wine offers, price comparison, wine buying, offer discovery,
  wine value assessment, availability caution, Claude Code skill.

Scope and honesty guardrails carried into every asset below:
- Clear niche: discovering and structuring wine offers, then comparing them.
- It searches for opportunities and organizes them; it does not promise automatic
  purchase.
- It cautions about availability and price volatility on every result.
- It never bypasses site restrictions, paywalls, or access controls, and never claims to.

---

## Input (as supplied to the skill)

```yaml
skill_name: wine-offer-hunter
type: claude-code-skill
summary_from_user: "Helps me find wine offers/deals, structure them, and compare, with
  clear caveats that availability and price change and that it won't auto-buy anything."
repo_url: <repo-url>
license: user-provided (MIT)
stars: "[not available]"
```

---

## Output: Registry Submission Kit

### Target 1 (Priority 1): curated awesome list of Claude Code skills

- Priority: 1 (highest quality signal per link; hand-reviewed audience).
- Why submit here: a curated awesome list reaches exactly the people looking for
  vetted, single-purpose skills. A single accepted entry is a strong trust signal and
  a durable discovery path.
- Category: Data and Research / Shopping and Commerce helpers (confirm the list's actual
  section names before submitting; taxonomies vary).
- Proposed README line:
  > **[wine-offer-hunter](repo-url)** - Finds and compares wine offers and deals,
  > structures each opportunity, and flags availability and price volatility. Does not
  > auto-purchase and does not bypass site restrictions.
- PR title:
  > Add wine-offer-hunter (wine offer discovery and comparison skill)
- PR body:
  > This PR adds `wine-offer-hunter`, a Claude Code skill that helps users discover wine
  > offers, structure each opportunity into a comparable format, and assess value.
  >
  > What it does: searches for wine offers, organizes them, and compares them so the
  > user can decide.
  >
  > What it deliberately does not do: it does not promise or perform automatic purchase,
  > and it does not bypass site restrictions, paywalls, or access controls. Every result
  > carries a caution that availability and price can change quickly.
  >
  > Entry follows the list's alphabetical/category ordering. License: user-provided
  > (MIT). Happy to adjust wording or placement to match the list's conventions.
- Required changes before submitting: fork the list, add the one-line entry in the
  correct section, keep alphabetical order if the list requires it, run any lint/format
  check the list ships, and confirm the entry link resolves.
- Risk of rejection: low to moderate. Curated lists reject entries that are too broad,
  unmaintained, or duplicative. Mitigate by emphasizing the tight niche and the
  honesty guardrails. Verify current contribution rules before submitting.
- Submission status: not yet submitted (draft ready).

### Target 2 (Priority 2): searchable skills/agent catalog

- Priority: 2 (larger reach, lower per-link trust; discovery via search).
- Why submit here: a searchable catalog surfaces the skill to people typing queries like
  "wine deals" or "price comparison", which matches the trigger queries above.
- Category: Shopping / Commerce, secondary Data and Research (confirm the catalog's real
  category list before submitting).
- Proposed README line:
  > wine-offer-hunter: discover, structure, and compare wine offers with clear caveats
  > about availability and price volatility. No auto-buy. No bypassing site restrictions.
- PR title:
  > Add listing: wine-offer-hunter
- PR body:
  > Submitting `wine-offer-hunter` for the catalog. It is a Claude Code skill focused on
  > one job: finding wine offers, structuring them, and comparing them so a buyer can
  > judge value.
  >
  > Positioning notes for reviewers: the skill searches and organizes opportunities; it
  > explicitly does not promise automatic purchase, and it does not bypass any site
  > restriction or access control. Results always warn that wine availability and price
  > are volatile.
  >
  > Metadata (title, description, category, keywords) is filled per the catalog template.
  > License: user-provided (MIT). Metrics such as installs or stars are `[not available]`
  > and left blank rather than estimated.
- Required changes before submitting: complete the catalog's listing template (title,
  short and long description, category, keywords, repo link), verify no field expects a
  fabricated metric, and leave count fields blank or user-sourced.
- Risk of rejection: low. Searchable catalogs are more permissive but reject listings
  with missing metadata or inflated claims. Keep claims factual and guardrails visible.
  Verify current listing rules before submitting.
- Submission status: not yet submitted (metadata drafted).

### Target 3 (Priority 3, optional): general topic on GitHub itself

- Priority: 3 (passive discovery; complements, does not replace, the two PRs above).
- Why submit here: adding accurate GitHub topics to the repo makes it findable through
  GitHub's own search without any external review process.
- Category: not applicable (GitHub topics rather than a curated section).
- Proposed README line: not applicable; instead add repo topics such as
  `wine`, `price-comparison`, `deals`, `claude-code`, `agent-skills` (add only topics
  that genuinely match, and confirm each is a valid topic first).
- PR title: not applicable (topics are set in repo settings, not via PR).
- PR body: not applicable.
- Required changes before submitting: add verified topics, ensure the repo description
  and README carry the same niche and guardrail language used above.
- Risk of rejection: none (self-service), but irrelevant or misleading topics hurt
  discoverability and trust, so keep them accurate.
- Submission status: topics not yet added.

---

### Cross-target notes

- Consistency: the niche sentence and the two guardrails (no auto-purchase, no bypassing
  restrictions) must read identically across the repo description, README, and every
  submission. Reviewers and users should meet the same honest framing everywhere.
- Metrics discipline: wherever a count would appear (stars, installs, downloads), leave
  it as user-provided or `[not available]`. Do not estimate.
- Rules discipline: before opening any PR or listing, re-read the target's current
  contribution guidelines. Directory rules, category names, and formatting requirements
  change; verify current rules before submitting rather than trusting this kit's
  snapshot.
