#!/usr/bin/env python3
"""Kiểm tra bộ khung agent nghiên cứu của dự án chỉ bằng thư viện chuẩn."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".codex" / "agents"
QWEN_AGENT_DIR = ROOT / ".qwen" / "agents"
QWEN_COMMAND_DIR = ROOT / ".qwen" / "commands"
REQUIRED_AGENTS = {
    "research_coordinator",
    "business_tutor",
    "macro_market_researcher",
    "company_analyst",
    "risk_bear_reviewer",
    "source_fact_checker",
}
# Agent được ghi tài liệu; các agent còn lại chỉ đọc.
WRITE_TOOLS = {"write_file", "edit"}
# Agent chỉ đọc tuyệt đối: không cả shell. source_fact_checker được chạy
# shell để tái tính và kiểm mã băm nhưng không được ghi tệp.
NO_SHELL_AGENTS = {
    "business_tutor",
    "company_analyst",
    "macro_market_researcher",
    "risk_bear_reviewer",
}
REQUIRED_QWEN_COMMANDS = {
    "hoc.md",
    "nghien-cuu-doanh-nghiep.md",
    "nghien-cuu-nganh.md",
}
REQUIRED_PATHS = [
    ROOT / "AGENTS.md",
    ROOT / ".codex" / "config.toml",
    ROOT / "docs" / "WORKFLOW.md",
    ROOT / "docs" / "RESEARCH_STANDARD.md",
    ROOT / "templates" / "research-brief.md",
    ROOT / "templates" / "company-report.md",
    ROOT / "templates" / "learning-note.md",
    ROOT / "templates" / "decision-journal.md",
    ROOT / "templates" / "source-register.md",
    ROOT / "templates" / "review-record.md",
    ROOT / "learning" / "glossary.md",
    ROOT / "learning" / "lessons" / "001-business-financial-statements.md",
    ROOT / "scripts" / "validate_report.py",
]


def fail(message: str) -> None:
    print(f"KHÔNG ĐẠT: {message}")


def parse_qwen_agent(path: Path) -> tuple[dict, str] | None:
    """Trả về (frontmatter, body) của tệp agent Markdown, hoặc None nếu thiếu frontmatter."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    frontmatter: dict[str, str | list[str]] = {}
    current_list: str | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return frontmatter, "\n".join(lines[index + 1 :])
        stripped = line.strip()
        if stripped.startswith("- ") and current_list is not None:
            value = stripped[2:].strip()
            if isinstance(frontmatter.get(current_list), list):
                frontmatter[current_list].append(value)
            continue
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                frontmatter[key] = []
                current_list = key
            else:
                frontmatter[key] = value
                current_list = None
    return None


def check_codex_agents() -> int:
    errors = 0
    found_names: set[str] = set()
    sandbox_modes: dict[str, str | None] = {}
    for path in sorted(AGENT_DIR.glob("*.toml")):
        try:
            agent = tomllib.loads(path.read_text())
        except (OSError, tomllib.TOMLDecodeError) as exc:
            fail(f"{path.relative_to(ROOT)} không hợp lệ: {exc}")
            errors += 1
            continue

        missing = [
            key
            for key in ("name", "description", "developer_instructions")
            if not isinstance(agent.get(key), str) or not agent[key].strip()
        ]
        if missing:
            fail(f"{path.name} thiếu trường có giá trị: {', '.join(missing)}")
            errors += 1
            continue

        name = agent["name"]
        found_names.add(name)
        if path.stem != name:
            fail(f"tên tệp {path.name} phải khớp tên agent {name}")
            errors += 1
        sandbox_modes[name] = agent.get("sandbox_mode")
        instructions = agent["developer_instructions"]
        for phrase in (
            "tiếng Việt",
            "tìm kiếm Internet",
            "trí nhớ",
            "toàn cầu",
            "repo",
            "chỉ dẫn trong trang web",
        ):
            if phrase not in instructions:
                fail(f"chỉ dẫn của {name} phải chứa chính sách {phrase!r}")
                errors += 1

    missing_agents = REQUIRED_AGENTS - found_names
    extra_agents = found_names - REQUIRED_AGENTS
    if missing_agents:
        fail(f"thiếu agent Codex: {', '.join(sorted(missing_agents))}")
        errors += 1
    if extra_agents:
        fail(f"agent Codex ngoài dự kiến: {', '.join(sorted(extra_agents))}")
        errors += 1
    for name in sorted(REQUIRED_AGENTS):
        expected_mode = "workspace-write" if name == "research_coordinator" else "read-only"
        actual_mode = sandbox_modes.get(name)
        if actual_mode != expected_mode:
            fail(f"sandbox_mode của {name} phải là {expected_mode!r}, hiện là {actual_mode!r}")
            errors += 1
    return errors


def check_qwen_agents() -> int:
    errors = 0
    found_names: set[str] = set()
    for path in sorted(QWEN_AGENT_DIR.glob("*.md")):
        parsed = parse_qwen_agent(path)
        if parsed is None:
            fail(f"{path.relative_to(ROOT)} thiếu YAML frontmatter hợp lệ")
            errors += 1
            continue
        frontmatter, body = parsed

        name = frontmatter.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(f"{path.name} thiếu name trong frontmatter")
            errors += 1
            continue
        found_names.add(name)
        if path.stem != name:
            fail(f"tên tệp {path.name} phải khớp tên agent {name}")
            errors += 1
        description = frontmatter.get("description")
        if not isinstance(description, str) or not description.strip():
            fail(f"{path.name} thiếu description trong frontmatter")
            errors += 1

        for phrase in (
            "tiếng Việt",
            "tìm kiếm Internet",
            "trí nhớ",
            "toàn cầu",
            "repo",
            "chỉ dẫn trong trang web",
        ):
            if phrase not in body:
                fail(f"chỉ dẫn của {name} phải chứa chính sách {phrase!r}")
                errors += 1

        tools = frontmatter.get("tools")
        if not isinstance(tools, list) or not tools:
            fail(f"{name} phải khai báo danh sách tools để giới hạn quyền")
            errors += 1
            continue
        if name == "research_coordinator":
            if not WRITE_TOOLS.issubset(tools):
                fail(f"{name} phải có {sorted(WRITE_TOOLS)} vì là agent duy nhất được ghi")
                errors += 1
        else:
            granted_write = WRITE_TOOLS.intersection(tools)
            if granted_write:
                fail(f"{name} chỉ đọc, không được có {sorted(granted_write)}")
                errors += 1
            if name in NO_SHELL_AGENTS and "run_shell_command" in tools:
                fail(f"{name} chỉ đọc tuyệt đối, không được có run_shell_command")
                errors += 1

    missing_agents = REQUIRED_AGENTS - found_names
    extra_agents = found_names - REQUIRED_AGENTS
    if missing_agents:
        fail(f"thiếu agent Qwen Code: {', '.join(sorted(missing_agents))}")
        errors += 1
    if extra_agents:
        fail(f"agent Qwen Code ngoài dự kiến: {', '.join(sorted(extra_agents))}")
        errors += 1
    return errors


def check_qwen_commands() -> int:
    errors = 0
    for filename in sorted(REQUIRED_QWEN_COMMANDS):
        path = QWEN_COMMAND_DIR / filename
        if not path.is_file():
            fail(f"thiếu lệnh {path.relative_to(ROOT)}")
            errors += 1
            continue
        text = path.read_text(encoding="utf-8")
        if "{{args}}" not in text:
            fail(f"{filename} phải dùng {{{{args}}}} để nhận tham số")
            errors += 1
        parts = text.split("---", 2)
        if len(parts) < 3 or "description:" not in parts[1]:
            fail(f"{filename} phải có description trong frontmatter")
            errors += 1
    return errors


def main() -> int:
    errors = 0

    for path in REQUIRED_PATHS:
        if not path.is_file():
            fail(f"thiếu {path.relative_to(ROOT)}")
            errors += 1

    try:
        config = tomllib.loads((ROOT / ".codex" / "config.toml").read_text())
        if config.get("web_search") != "live":
            fail("web_search phải là 'live' để buộc truy xuất Internet trực tiếp")
            errors += 1
        agents_config = config.get("agents", {})
        if agents_config.get("enabled") is not True:
            fail("agents.enabled phải là true")
            errors += 1
        max_threads = agents_config.get("max_concurrent_threads_per_session")
        if not isinstance(max_threads, int) or max_threads < 1:
            fail("max_concurrent_threads_per_session phải là số nguyên dương")
            errors += 1
    except (OSError, tomllib.TOMLDecodeError) as exc:
        fail(f".codex/config.toml không hợp lệ: {exc}")
        errors += 1

    if not QWEN_AGENT_DIR.is_dir():
        fail("thiếu .qwen/agents/")
        errors += 1
    else:
        errors += check_qwen_agents()

    if not QWEN_COMMAND_DIR.is_dir():
        fail("thiếu .qwen/commands/")
        errors += 1
    else:
        errors += check_qwen_commands()

    errors += check_codex_agents()

    if errors:
        print(f"KẾT QUẢ: {errors} lỗi")
        return 1

    print(f"ĐẠT: {len(REQUIRED_AGENTS)} agent Codex, {len(REQUIRED_AGENTS)} agent Qwen Code, "
          f"{len(REQUIRED_QWEN_COMMANDS)} lệnh Qwen Code, {len(REQUIRED_PATHS)} tài liệu bắt buộc")
    print("ĐẠT: cấu hình dự án khai báo một agent được ghi và năm agent chỉ đọc")
    print("LƯU Ý: quyền chạy thực tế của phiên vẫn có thể ghi đè mặc định của agent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
