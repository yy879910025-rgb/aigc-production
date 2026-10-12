from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
for name in ["SKILL.md", "agents/openai.yaml", "references/creative.md", "references/screenplay.md", "references/art.md", "references/storyboard.md", "references/coordination.md", "assets/avatar.png"]:
    assert (root / name).is_file(), name
text = (root / "SKILL.md").read_text()
assert text.startswith("---\n") and "name: aigc-production" in text.split("---", 2)[1]
for path in [root / "SKILL.md", * (root / "references").glob("*.md")]:
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if "://" not in link:
            assert (path.parent / link.split("#")[0]).exists(), (path, link)
print("Skill structure and reference links passed; behavior requires maintainer review.")
