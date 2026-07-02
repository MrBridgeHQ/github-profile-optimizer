# Contributing

Thanks for helping improve github-profile-optimizer. This guide explains how to
propose changes and the quality bar every contribution has to meet.

## How to propose an improvement

1. Open an issue using the improvement template. Describe the problem and the
   change you have in mind, and pick the matching type in the form.
2. Once the direction is agreed, open a pull request that implements it.
3. Keep the change focused. One idea per PR is easier to review and to revert.

## How to add a registry target

Add the new target to `references/registry-targets.md` and fill in every
required field:

- name
- type
- audience
- priority
- submission conditions to verify
- probable format
- notes

Any rule you have not confirmed against the target's own current documentation
must be marked as "to verify". Do not present unconfirmed submission rules as
settled fact.

## How to add an example

Add a realistic worked example under `examples/`, following the format of the
existing examples. It should show a concrete input and the resulting output, not
a generic outline. Match the structure, headings, and level of detail of the
examples already in the folder.

## Quality rules

- English for all public files.
- Clean Markdown that renders correctly.
- Actionable guidance: tell the reader what to do, not just what exists.
- Specific, not generic. Avoid filler that applies to any repository.
- No em-dashes. Use hyphens, commas, colons, or parentheses.
- No invented GitHub metrics. Do not fabricate stars, followers, traffic, or
  ranking numbers.
- No assumed registry acceptance. Submission does not equal listing; never claim
  a target accepts an entry unless it is confirmed.

## Firm rule

No auto-generated dumps: every addition needs a test (an eval entry) or a worked
example. Content that cannot be pointed to by an eval or an example does not
belong in the skill.

## Pull requests

Every PR should update the items in the PR checklist so reviewers can confirm
what changed. Check off each item that applies, and leave a short note for any
item you intentionally skipped.
