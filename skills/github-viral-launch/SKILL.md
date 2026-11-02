---
name: github-viral-launch
description: Improve a GitHub repository's chances of organic viral growth using a fixed 16-point launch audit, compelling demos, a low-friction first run, and targeted distribution. Use for requests to make a repo go viral, grow GitHub stars, prepare an open-source launch, or audit launch readiness. Ordinary code releases and general SaaS marketing are outside this skill's focus.
license: MIT
---

# GitHub Viral Launch

Turn a repository into something the right developers can understand, try, trust, and share. Pursue organic reach and real use; track stars explicitly when that is the user's goal. Virality is an outcome to pursue, never a guarantee or an excuse for manufactured engagement.

## Establish the assignment

Resolve the intended repository, default branch, and revision. Read its instructions, README, installation metadata, examples, CI, and contribution files; use connected GitHub tools for settings and live state. Prefer existing context over a long interview.

Identify the target developer, concrete problem, demonstrable result, honest difference from alternatives, desired outcome, and maintainer availability. Ask only for missing facts that materially affect the work; continue independent inspection while waiting. State provisional audience or timing assumptions.

- **Audit:** inspect and recommend; do not edit.
- **Improve / make this repo go viral:** audit, complete authorized local improvements, and prepare a concrete launch package. Do not stop at recommendations when implementation is requested.
- **Prepare a launch:** deliver the relevant audit, ready-to-review assets, and schedule.
- **Diagnose a launch:** inspect actual reach, trial, and contribution evidence before proposing another announcement.

Local edits and drafts do not authorize pushes, public issues, releases, settings changes, deployments, or external posts. Complete authorized preparation before asking about a concrete external action. Existing explicit authorization remains valid. History rewrites and credential changes need specific authorization.

## Audit the same 16 points

Always report all 16 rows with their original numbers. Use **PASS** only with evidence, **FAIL** for missing/broken work, **UNKNOWN** for inaccessible or untested facts, and **NOT APPLICABLE** only with a project-specific reason. Never hide missing access or time behind N/A.

When a row has both a known defect and unverified parts, report FAIL and name the remaining unknowns. For example, a missing first-use example is FAIL; a complete documented example that has not been executed is UNKNOWN.

For each row report `# | status | evidence | smallest fix`. Cite files and lines, dated live API observations/links, or commands and actual results. Separate proposed, locally prepared, and live/published state. Badges are not proof of green CI, and local image files are not proof of configured social previews.

| # | Launch point | Evidence and smallest useful improvement |
|---|---|---|
| 1 | Demo GIF near the README top | A working embedded recording shows the main operation and recognizable output. Aim for 5–10 seconds, legible text, and no sensitive data. Never fabricate runtime output. A storyboard or placeholder remains FAIL until real media exists. Explain a suitable visual equivalent when a GIF would hide the project's value. |
| 2 | One-line description | Near the top, say what it does, for whom, and the concrete outcome in plain words. Avoid unsupported superlatives. |
| 3 | One-command install | A copyable project-appropriate command, honest prerequisites, and a nearby smallest working example. Follow through to useful output when execution is authorized and safe. Present-but-unexecuted commands are UNKNOWN for verification. Do not hide setup in opaque remote scripts or add a package manager just to claim one command. |
| 4 | Live demo or immediate trial | A working playground, hosted demo, or short video link. Check accessibility and behavior when possible; a README URL alone is insufficient. Explain N/A when the project cannot sensibly offer a demo. |
| 5 | License | An actual license file with consistent package metadata and clear coverage. Do not choose/replace the license or invent copyright ownership for the maintainer. Identify the decision needed when absent. |
| 6 | Repository topics | Inspect live GitHub topics and propose relevant purpose, ecosystem, and audience terms. Verify current limits if needed; avoid unrelated popular keywords. |
| 7 | Social preview | Verify the configured preview, not just a checked-in image. Prepare a readable project name, one promise, and real visual. GitHub currently recommends PNG/JPG/GIF under 1 MB, 1280×640 for best display; check official guidance before generating/uploading. Inaccessible settings mean UNKNOWN, with an asset or exact manual step supplied. |
| 8 | Passing CI | Inspect the latest relevant default-branch run and commit. Distinguish failure, pending, no CI, and inaccessible state. Fix relevant failures within scope; avoid decorative badges or broad CI rewrites. Documentation-only repos can justify lighter checks. |
| 9 | Secrets absent from git history | Establish existing scan scope, available history/refs, and protection settings. Use approved existing tools with redacted output. A clean tree or no alert is not a history scan. Incomplete evidence means UNKNOWN; PASS must state the actual scan scope and cannot guarantee absence. For a likely live credential, withhold the value, prioritize authorized revocation/rotation, and defer publicity until contained. Deletion/history cleanup alone does not invalidate credentials. History rewrites require separate approval. |
| 10 | Good first issues | Inspect actual open issues carrying `good first issue`, not just label existence. Aim for 3–5 real small tasks with context, code pointers, acceptance criteria, and help. Draft justified issues locally if publication is unauthorized; do not invent busywork to hit a count. |
| 11 | Contributing guide | CONTRIBUTING.md or a linked equivalent explains actual local setup, relevant tests, and the PR process using repository commands. |
| 12 | Issue templates | Usable bug and feature intake in `.github/ISSUE_TEMPLATE`, or an explained alternative. Ask for reproduction, expected/actual behavior, environment, and the feature's problem; route sensitive reports privately. |
| 13 | Discussions | Inspect GitHub's live setting and the documented question route. Propose enabling when useful. An intentional linked existing support channel can justify N/A; do not create an empty community by default. |
| 14 | Tagged release with notes | Verify a real tag and release notes/changelog for what users can install. Local notes and a proposed version are preparation, not a published release. Preserve versioning conventions. |
| 15 | Show HN preparation | Check suitability and current HN/Show HN rules: something people can try, not a signup page. Prepare an author facts brief covering use, audience, motivation, implementation facts, limitations, URLs, and questions to answer in their own words. Current HN rules prohibit generated posts and generated/AI-edited comments: do not supply paste-ready HN titles/posts/comments, rewrite submissions, or automate posting. PASS means a complete compliant preparation brief; report publication separately. Explain N/A when unsuitable. |
| 16 | First issue response within a day | A realistic launch coverage plan names owner, timezone, two daily triage windows, backup/escalation, and a 24-hour first-response target. A first reply acknowledges/routes; it need not resolve. Distinguish plans from observed response times. If capacity is insufficient, record the gap and propose an honest sustainable expectation. |

Read [launch-playbook.md](references/launch-playbook.md) for launch assets, channel selection, response coverage, measurement, and diagnosis.

## Choose what to fix

Lead with the three changes most likely to improve **understanding → trial → trust → sharing** for this repo. Explain mechanism, effort, and evidence without invented growth forecasts.

Resolve actual secret exposure, misleading claims, a broken promised first run, and unresolved permission to distribute before recommending a traffic push. Favor items 1–5 for initial polish, discovery/credibility in 6–8, then contribution and launch operations in 10–16. Item 9 belongs before publication.

This is not a universal 16/16 gate. A missing GIF need not delay a useful release; a compromised credential cannot be offset by a great README. Separate blockers from acceptable omissions. Do not expand into trademark clearance, a general security audit, or product rebuilding without a concrete reason and scope.

## Implement and deliver

Reuse existing assets, conventions, and tools. Make the smallest coherent edits and validate proportionally: inspect changed links/assets and run relevant existing checks for changed behavior. Inspect first-run commands before execution; avoid unapproved external effects or dependency changes.

Update the audit with actual post-change evidence. Remote settings and releases remain unverified until inspected live. Stop after relevant verification; do not add speculative infrastructure or recurring automations.

Deliver in the user's language:

1. The concrete shareable angle and readiness verdict with actual blockers.
2. All 16 audit rows with evidence and smallest fixes, including UNKNOWNs.
3. Changes, relevant files, actual verification, and outstanding external actions.
4. When in scope, the launch package and capacity-aware schedule.
5. A baseline and day-1/7/30 measurement plan with missing data identified.

Never buy stars, fabricate users/testimonials, coordinate votes, spam communities, or require stars to use the project. GitHub Trending's selection formula is unpublished: no invented thresholds, placement guarantees, or claims that a schedule controls ranking.

## Sources

Original synthesis of the user's 16-point checklist, informed by [open-source-marketing](https://github.com/jonathimer/devmarketing-skills/blob/main/skills/open-source-marketing/SKILL.md) and [oss-launch](https://github.com/samber/developer-relations-skills/blob/main/skills/oss-launch/SKILL.md). Neither upstream skill is required or installed.

Verify changing platform rules against primary sources when applying them:

- [GitHub social preview guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [GitHub sensitive-data removal](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [HN guidelines](https://news.ycombinator.com/newsguidelines.html) and [Show HN rules](https://news.ycombinator.com/showhn.html)

When access/tools cannot establish a fact, preserve UNKNOWN and give the smallest next verification step.
