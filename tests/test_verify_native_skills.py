"""Kiểm tra lớp skill native của DeepSeek Harness trong .agents/skills/."""

from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify.py"
SKILL_DIR = ROOT / ".agents" / "skills"
ROLE_SKILLS = (
    "research-coordinator",
    "business-tutor",
    "macro-market-researcher",
    "company-analyst",
    "source-fact-checker",
    "risk-bear-reviewer",
)
COMMANDS = ("hoc", "nghien-cuu-doanh-nghiep", "nghien-cuu-nganh")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise AssertionError(f"{path} thiếu frontmatter")
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    raise AssertionError(f"{path} thiếu dấu đóng frontmatter")


class KiemTraSkillNative(unittest.TestCase):
    def test_verify_passes_for_whole_project(self) -> None:
        run = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("6 skill vai trò native", run.stdout)
        self.assertIn("3 lệnh tắt native", run.stdout)

    def test_role_skills_use_kebab_case_names(self) -> None:
        for role in ROLE_SKILLS:
            with self.subTest(role=role):
                fields = frontmatter(SKILL_DIR / role / "SKILL.md")
                self.assertEqual(fields.get("name"), role)
                self.assertRegex(role, KEBAB)
                self.assertTrue(fields.get("description", "").strip())

    def test_shortcuts_are_human_only(self) -> None:
        for command in COMMANDS:
            with self.subTest(command=command):
                fields = frontmatter(SKILL_DIR / f"{command}.md")
                self.assertEqual(fields.get("name"), command)
                self.assertEqual(fields.get("user-invocable"), "true")
                self.assertEqual(fields.get("disable-model-invocation"), "true")

    def test_frontmatter_scalars_are_yaml_safe(self) -> None:
        """DSH bỏ qua im lặng skill có YAML sai, nên frontmatter phải an toàn."""
        for path in sorted(SKILL_DIR.rglob("*.md")):
            lines = path.read_text(encoding="utf-8").splitlines()
            for number, line in enumerate(lines[1:], start=2):
                if line.strip() == "---":
                    break
                if line.startswith(" ") or line.lstrip().startswith("- ") or ":" not in line:
                    continue
                _, _, value = line.partition(":")
                value = value.strip()
                if ": " not in value:
                    continue
                with self.subTest(file=str(path.relative_to(ROOT)), line=number):
                    self.assertTrue(
                        value.startswith(("\"", "'")),
                        f"{path.relative_to(ROOT)}:{number} cần quote giá trị chứa ': '",
                    )

    def test_no_unexpected_native_entries(self) -> None:
        expected = {*ROLE_SKILLS, *(f"{command}.md" for command in COMMANDS)}
        existing = {entry.name for entry in SKILL_DIR.iterdir() if not entry.name.startswith(".")}
        self.assertEqual(existing, expected)


if __name__ == "__main__":
    unittest.main()
