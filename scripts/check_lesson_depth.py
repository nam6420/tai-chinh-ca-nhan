#!/usr/bin/env python3
"""Báo cáo chiều sâu bài học theo docs/LESSON_DEPTH_STANDARD.md.

Mặc định chỉ báo cáo (mã thoát 0). Dùng --strict NAME... để buộc các bài
đã nêu phải đạt bậc S (mã thoát 1 nếu thiếu).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "learning" / "lessons"

MIN_WORDS, MAX_WORDS, MIN_EXERCISES = 2500, 6500, 8
REQUIRED_HEADINGS = {
    "ví dụ nguồn thật": r"^## (?:\d+\.\s*)?Ví dụ(?: từ nguồn| doanh nghiệp) thật",
    "bài tập": r"^## (?:\d+\.\s*)?Bài tập",
    "đáp án": r"^## (?:\d+\.\s*)?Đáp án",
    "bài bẩn": r"^## (?:\d+\.\s*)?Bài làm với dữ liệu thiếu hoặc lệch",
    "sai ở đâu": r"^## (?:\d+\.\s*)?Sai ở đâu",
    "kiểm tra chuyển bài": r"^## (?:\d+\.\s*)?Kiểm tra chuyển bài",
}


def count_exercises(text: str) -> int:
    match = re.search(r"^## (?:\d+\.\s*)?Bài tập.*?(?=^## )", text, re.M | re.S)
    if not match:
        return 0
    return len(re.findall(r"^\d+\.\s", match.group(0), re.M))


def check(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems = []
    words = len(text.split())
    if words < MIN_WORDS:
        problems.append(f"{words} từ < {MIN_WORDS}")
    elif words > MAX_WORDS:
        problems.append(f"{words} từ > {MAX_WORDS}")
    n = count_exercises(text)
    if n < MIN_EXERCISES:
        problems.append(f"{n} câu bài tập < {MIN_EXERCISES}")
    for name, pattern in REQUIRED_HEADINGS.items():
        if not re.search(pattern, text, re.M):
            problems.append(f"thiếu mục: {name}")
    if "practice/models/" not in text:
        problems.append("chưa liên kết tệp mẫu practice/models/")
    return problems


def main(argv: list[str]) -> int:
    strict = []
    if argv and argv[0] == "--strict":
        strict = argv[1:]
    exit_code = 0
    tier_s = 0
    files = sorted(LESSONS.glob("*.md"))
    for path in files:
        problems = check(path)
        if not problems:
            tier_s += 1
        stem = path.stem
        required = any(stem == s or stem.startswith(s + "-") for s in strict)
        if required and problems:
            exit_code = 1
            print(f"THIẾU {stem}: " + "; ".join(problems))
        elif not strict and problems:
            print(f"P  {stem}: " + "; ".join(problems))
    print(f"Bậc S: {tier_s}/{len(files)} bài")
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
