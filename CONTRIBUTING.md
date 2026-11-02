# Contributing

Clone the repository and create a branch. The skill lives in `skills/github-viral-launch/`; its entry point links to the launch playbook. No build is required to edit Markdown.

Run the same check as CI with Python 3.11 or newer:

```bash
python3 scripts/check.py
```

To inspect skill discovery without installing:

```bash
npx skills add . --list
```

For behavior changes, include a realistic input, the expected observable decision, and the reason for the change. Use synthetic repositories or sanitized artifacts; do not attach credentials or customer data. Keep all 16 checks numbered consistently. Preserve the distinction between missing evidence, failed work, and live verification.

Open a focused pull request explaining the problem, the resulting behavior, and the validation performed. Report bugs and ideas in Issues; use Discussions for questions. Response time is best effort; this project does not promise a 24-hour support SLA.

To reproduce media, see `docs/media.md`. Media tooling is optional for skill changes.
