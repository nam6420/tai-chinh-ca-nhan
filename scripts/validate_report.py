#!/usr/bin/env python3
"""Kiểm tra báo cáo không còn nhãn nháp có hai biên bản ĐẠT phù hợp."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


FIELD_RE = re.compile(r"^- ([^:]+):\s*`?([^`]+?)`?\s*$")
ROOT = Path(__file__).resolve().parents[1]


def canonical_report(text: str) -> str:
    """Chuẩn hóa nội dung trọng yếu, bỏ qua thay đổi trạng thái vòng đời."""
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
    return "\n".join(normalized).strip() + "\n"


def content_hash(path: Path) -> str:
    canonical = canonical_report(path.read_text(encoding="utf-8"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def fields(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = FIELD_RE.match(line)
        if match:
            result[match.group(1).strip()] = match.group(2).strip()
    return result


def validate_review(
    path: Path,
    expected_type: str,
    expected_hash: str,
    expected_report: Path,
    expected_as_of: str,
) -> list[str]:
    problems: list[str] = []
    if not path.is_file():
        return [f"thiếu biên bản kiểm duyệt: {path}"]
    record = fields(path)
    expected_agent = {
        "KIỂM_NGUỒN": "source_fact_checker",
        "PHẢN_BIỆN_RỦI_RO": "risk_bear_reviewer",
    }[expected_type]
    checks = {
        "Loại kiểm duyệt": expected_type,
        "Agent kiểm duyệt": expected_agent,
        "SHA-256 nội dung đích": expected_hash,
        "Chốt dữ liệu lúc": expected_as_of,
        "Kết luận": "ĐẠT",
        "Lỗi nghiêm trọng chưa xử lý": "0",
    }
    for key, expected in checks.items():
        actual = record.get(key)
        if actual != expected:
            problems.append(f"{path}: {key} phải là {expected!r}, hiện là {actual!r}")
    for key in ("Kiểm duyệt lúc", "Phạm vi", "Báo cáo đích"):
        actual = record.get(key, "")
        if not actual or actual.startswith("<"):
            problems.append(f"{path}: phải điền {key}")
    target_value = record.get("Báo cáo đích", "")
    if target_value and not target_value.startswith("<"):
        target_path = Path(target_value)
        if not target_path.is_absolute():
            target_path = ROOT / target_path
        if target_path.resolve() != expected_report.resolve():
            problems.append(
                f"{path}: Báo cáo đích phải trỏ tới {expected_report.resolve()}"
            )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--fact-check", type=Path)
    parser.add_argument("--bear-review", type=Path)
    parser.add_argument("--print-hash", action="store_true")
    args = parser.parse_args()

    if not args.report.is_file():
        print(f"KHÔNG ĐẠT: thiếu báo cáo: {args.report}")
        return 1

    report_text = args.report.read_text(encoding="utf-8")
    if not report_text.strip():
        print(f"KHÔNG ĐẠT: báo cáo rỗng: {args.report}")
        return 1

    digest = content_hash(args.report)
    if args.print_hash:
        print(digest)
        return 0

    first_line = report_text.splitlines()[0]
    if "BẢN NHÁP - CHƯA KIỂM DUYỆT" in first_line:
        print(f"BẢN NHÁP: chưa áp dụng cổng xuất bản; mã băm nội dung {digest}")
        return 0

    if args.fact_check is None or args.bear_review is None:
        print("KHÔNG ĐẠT: báo cáo không còn nhãn nháp cần --fact-check và --bear-review")
        return 1

    report_fields = fields(args.report)
    problems = []
    as_of = report_fields.get("Chốt dữ liệu lúc", "")
    if not as_of or as_of.startswith("<"):
        problems.append("báo cáo phải điền Chốt dữ liệu lúc")
    for status_field in ("Kiểm nguồn", "Phản biện rủi ro"):
        actual = report_fields.get(status_field)
        if actual != "ĐẠT":
            problems.append(
                f"trạng thái {status_field} trên báo cáo phải là 'ĐẠT', hiện là {actual!r}"
            )
    problems.extend(
        validate_review(args.fact_check, "KIỂM_NGUỒN", digest, args.report, as_of)
    )
    problems.extend(
        validate_review(
            args.bear_review,
            "PHẢN_BIỆN_RỦI_RO",
            digest,
            args.report,
            as_of,
        )
    )
    if problems:
        for problem in problems:
            print(f"KHÔNG ĐẠT: {problem}")
        return 1
    print(f"ĐẠT: biên bản kiểm duyệt xuất bản khớp mã băm nội dung {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
