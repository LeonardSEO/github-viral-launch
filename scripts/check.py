"""Validate the published skill package and repository-local Markdown links."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / "skills/github-viral-launch/SKILL.md"
text = skill.read_text()
assert text.startswith("---\nname: github-viral-launch\ndescription: ")
assert len(text.split("---", 2)[1].split("description: ", 1)[1].strip()) > 0
rows = [int(n) for n in re.findall(r"^\| (\d+) \|", text, re.M)]
assert rows == list(range(1, 17)), "The launch audit must keep all 16 points in order"
for md in root.rglob("*.md"):
    if ".git" in md.parts:
        continue
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", md.read_text()):
        if "://" in target or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        assert (md.parent / path).is_file(), f"Broken link in {md.relative_to(root)}: {target}"
for file in ["README.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md"]:
    assert (root / file).is_file(), file
print("Skill structure, all 16 audit points, and local Markdown links passed.")
