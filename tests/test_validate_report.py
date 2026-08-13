from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_report.py"


def canonical_hash(text: str) -> str:
    lines = text.replace("\r\n", "\n").splitlines()
    if lines:
        lines[0] = lines[0].replace("# BẢN NHÁP - CHƯA KIỂM DUYỆT: ", "# ", 1)
    normalized = []
    for line in lines:
        if line.startswith("- Kiểm nguồn:"):
            normalized.append("- Kiểm nguồn: <TRẠNG_THÁI_VÒNG_ĐỜI>")
        elif line.startswith("- Phản biện rủi ro:"):
            normalized.append("- Phản biện rủi ro: <TRẠNG_THÁI_VÒNG_ĐỜI>")
        else:
            normalized.append(line.rstrip())
    payload = "\n".join(normalized).strip() + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class KiemTraCongXuatBan(unittest.TestCase):
    def run_gate(self, *args: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *(str(arg) for arg in args)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def make_review(
        self, path: Path, kind: str, agent: str, report: Path, digest: str
    ) -> None:
        path.write_text(
            "\n".join(
                [
                    "# Biên bản kiểm duyệt",
                    f"- Loại kiểm duyệt: `{kind}`",
                    f"- Agent kiểm duyệt: `{agent}`",
                    "- Kiểm duyệt lúc: `2026-08-10 16:00 Asia/Ho_Chi_Minh`",
                    "- Chốt dữ liệu lúc: `2026-08-10 15:00 Asia/Ho_Chi_Minh`",
                    "- Phạm vi: `toàn bộ báo cáo`",
                    f"- Báo cáo đích: `{report}`",
                    f"- SHA-256 nội dung đích: `{digest}`",
                    "- Kết luận: `ĐẠT`",
                    "- Lỗi nghiêm trọng chưa xử lý: `0`",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    def test_bao_cao_rong_khong_dat(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir) / "rong.md"
            report.write_text("", encoding="utf-8")
            result = self.run_gate(report)
            self.assertEqual(result.returncode, 1)
            self.assertIn("báo cáo rỗng", result.stdout)

    def test_ban_nhap_duoc_nhan_dien(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            report = Path(temp_dir) / "nhap.md"
            report.write_text(
                "# BẢN NHÁP - CHƯA KIỂM DUYỆT: Ví dụ\n",
                encoding="utf-8",
            )
            result = self.run_gate(report)
            self.assertEqual(result.returncode, 0)
            self.assertIn("BẢN NHÁP", result.stdout)

    def test_trang_thai_dang_cho_khong_the_xuat_ban(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            report = folder / "bao-cao.md"
            text = (
                "# Ví dụ\n"
                "- Chốt dữ liệu lúc: `2026-08-10 15:00 Asia/Ho_Chi_Minh`\n"
                "- Kiểm nguồn: `ĐANG_CHỜ`\n"
                "- Phản biện rủi ro: `ĐANG_CHỜ`\n"
            )
            report.write_text(text, encoding="utf-8")
            digest = canonical_hash(text)
            fact = folder / "kiem-nguon.md"
            bear = folder / "phan-bien.md"
            self.make_review(fact, "KIỂM_NGUỒN", "source_fact_checker", report, digest)
            self.make_review(bear, "PHẢN_BIỆN_RỦI_RO", "risk_bear_reviewer", report, digest)
            result = self.run_gate(report, Path("--fact-check"), fact, Path("--bear-review"), bear)
            self.assertEqual(result.returncode, 1)
            self.assertIn("trạng thái Kiểm nguồn", result.stdout)

    def test_hai_bien_ban_dat_va_khop_duoc_xuat_ban(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            report = folder / "bao-cao.md"
            text = (
                "# Ví dụ\n"
                "- Chốt dữ liệu lúc: `2026-08-10 15:00 Asia/Ho_Chi_Minh`\n"
                "- Kiểm nguồn: `ĐẠT`\n"
                "- Phản biện rủi ro: `ĐẠT`\n"
            )
            report.write_text(text, encoding="utf-8")
            digest = canonical_hash(text)
            fact = folder / "kiem-nguon.md"
            bear = folder / "phan-bien.md"
            self.make_review(fact, "KIỂM_NGUỒN", "source_fact_checker", report, digest)
            self.make_review(bear, "PHẢN_BIỆN_RỦI_RO", "risk_bear_reviewer", report, digest)
            result = self.run_gate(report, Path("--fact-check"), fact, Path("--bear-review"), bear)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("ĐẠT", result.stdout)


if __name__ == "__main__":
    unittest.main()
