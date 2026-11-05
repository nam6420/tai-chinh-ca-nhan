from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_lesson_depth as depth  # noqa: E402


def good_lesson() -> str:
    body = "từ " * 2600
    exercises = "\n".join(f"{i}. Câu {i}" for i in range(1, 9))
    return (
        f"# Bài\n\n{body}\n\n## Ví dụ từ nguồn thật\nx practice/models/a.csv\n\n"
        f"## Bài tập\n{exercises}\n\n## Đáp án\nx\n\n"
        "## Bài làm với dữ liệu thiếu hoặc lệch\nx\n\n## Sai ở đâu\nx\n\n"
        "## Kiểm tra chuyển bài\nx\n"
    )


class KiemTraChieuSau(unittest.TestCase):
    def check_text(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x.md"
            path.write_text(text, encoding="utf-8")
            return depth.check(path)

    def test_bai_dat_chuan(self) -> None:
        self.assertEqual(self.check_text(good_lesson()), [])

    def test_bai_ngan_bi_bao(self) -> None:
        problems = self.check_text("# Bài\n\n## Bài tập\n1. a\n\n## Đáp án\nx\n")
        self.assertTrue(any("từ <" in p for p in problems))
        self.assertTrue(any("câu bài tập" in p for p in problems))

    def test_thieu_muc_bai_ban(self) -> None:
        text = good_lesson().replace("## Sai ở đâu", "## Khác")
        self.assertIn("thiếu mục: sai ở đâu", self.check_text(text))

    def test_tieu_de_co_danh_so_va_do_dai_5000_tu(self) -> None:
        body = "từ " * 4800
        exercises = "\n".join(f"{i}. Câu {i}" for i in range(1, 9))
        text = (
            f"# Bài\n\n{body}\n\n## 4. Ví dụ doanh nghiệp thật: Công ty A\n"
            "x practice/models/a.csv\n\n"
            f"## 6. Bài tập (8 câu)\n{exercises}\n\n## 7. Đáp án\nx\n\n"
            "## 8. Bài làm với dữ liệu thiếu hoặc lệch\nx\n\n"
            "## 9. Sai ở đâu\nx\n\n## 10. Kiểm tra chuyển bài\nx\n"
        )
        self.assertEqual(self.check_text(text), [])


if __name__ == "__main__":
    unittest.main()
