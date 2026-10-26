#!/usr/bin/env python3
"""Kiểm tra bộ khung agent nghiên cứu của dự án chỉ bằng thư viện chuẩn."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT_DIR = ROOT / ".codex" / "agents"
QWEN_AGENT_DIR = ROOT / ".qwen" / "agents"
QWEN_COMMAND_DIR = ROOT / ".qwen" / "commands"
NATIVE_SKILL_DIR = ROOT / ".agents" / "skills"
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
# DeepSeek Harness đặt tên skill theo kebab-case, khác tên vai trò Qwen/Codex.
NATIVE_ROLE_SKILLS = {
    "research_coordinator": "research-coordinator",
    "business_tutor": "business-tutor",
    "macro_market_researcher": "macro-market-researcher",
    "company_analyst": "company-analyst",
    "source_fact_checker": "source-fact-checker",
    "risk_bear_reviewer": "risk-bear-reviewer",
}
REQUIRED_NATIVE_COMMANDS = {
    "hoc",
    "nghien-cuu-doanh-nghiep",
    "nghien-cuu-nganh",
}
# Chính sách tối thiểu phải có trong mọi vai trò, ở cả ba bản khai báo.
POLICY_PHRASES = (
    "tiếng Việt",
    "tìm kiếm Internet",
    "trí nhớ",
    "toàn cầu",
    "repo",
    "chỉ dẫn trong trang web",
)
KEBAB_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
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
    ROOT / "learning" / "roadmap.md",
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


def unquoted_colon_values(path: Path) -> list[int]:
    """Trả về số dòng frontmatter có ': ' chưa quote — kiểu YAML dễ parse sai."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    unsafe: list[int] = []
    for number, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            break
        if line.startswith(" ") or line.lstrip().startswith("- ") or ":" not in line:
            continue
        _, _, value = line.partition(":")
        value = value.strip()
        if ": " in value and not value.startswith(("\"", "'")):
            unsafe.append(number)
    return unsafe


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
        for phrase in POLICY_PHRASES:
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

        for phrase in POLICY_PHRASES:
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


def check_native_skills() -> int:
    """Kiểm tra lớp native của DeepSeek Harness trong .agents/skills/."""
    errors = 0
    expected = set(NATIVE_ROLE_SKILLS.values())

    for role, skill_name in sorted(NATIVE_ROLE_SKILLS.items()):
        path = NATIVE_SKILL_DIR / skill_name / "SKILL.md"
        if not path.is_file():
            fail(f"thiếu skill native {path.relative_to(ROOT)}")
            errors += 1
            continue
        parsed = parse_qwen_agent(path)
        if parsed is None:
            fail(f"{path.relative_to(ROOT)} thiếu YAML frontmatter hợp lệ")
            errors += 1
            continue
        frontmatter, body = parsed
        for number in unquoted_colon_values(path):
            fail(f"{path.relative_to(ROOT)}:{number} có ': ' chưa quote trong frontmatter YAML")
            errors += 1

        if not KEBAB_NAME.match(skill_name):
            fail(f"{skill_name!r} không phải tên skill kebab-case hợp lệ")
            errors += 1
        name = frontmatter.get("name")
        if name != skill_name:
            fail(f"{path.relative_to(ROOT)}: name phải là {skill_name!r}, hiện là {name!r}")
            errors += 1
        description = frontmatter.get("description")
        if not isinstance(description, str) or not description.strip():
            fail(f"{path.relative_to(ROOT)} thiếu description trong frontmatter")
            errors += 1

        for phrase in POLICY_PHRASES:
            if phrase not in body:
                fail(f"skill {skill_name} phải chứa chính sách {phrase!r}")
                errors += 1

        if role == "research_coordinator":
            for phrase in ("duy nhất", "BẢN NHÁP - CHƯA KIỂM DUYỆT"):
                if phrase not in body:
                    fail(f"skill {skill_name} phải nêu vai trò người ghi duy nhất và nhãn nháp")
                    errors += 1
                    break
        elif "chỉ đọc" not in body:
            fail(f"skill {skill_name} phải nêu ràng buộc chỉ đọc")
            errors += 1

        for counterpart in (f".qwen/agents/{role}.md", f".codex/agents/{role}.toml"):
            if counterpart not in body:
                fail(f"skill {skill_name} phải trỏ tới bản tương ứng {counterpart}")
                errors += 1

    for command in sorted(REQUIRED_NATIVE_COMMANDS):
        path = NATIVE_SKILL_DIR / f"{command}.md"
        if not path.is_file():
            fail(f"thiếu skill lệnh native {path.relative_to(ROOT)}")
            errors += 1
            continue
        parsed = parse_qwen_agent(path)
        if parsed is None:
            fail(f"{path.relative_to(ROOT)} thiếu YAML frontmatter hợp lệ")
            errors += 1
            continue
        frontmatter, body = parsed
        for number in unquoted_colon_values(path):
            fail(f"{path.relative_to(ROOT)}:{number} có ': ' chưa quote trong frontmatter YAML")
            errors += 1
        if frontmatter.get("name") != command:
            fail(f"{path.relative_to(ROOT)}: name phải là {command!r}")
            errors += 1
        description = frontmatter.get("description")
        if not isinstance(description, str) or not description.strip():
            fail(f"{path.relative_to(ROOT)} thiếu description trong frontmatter")
            errors += 1
        # Lệnh tắt chỉ do con người gọi, không tự lộ ra cho model.
        if str(frontmatter.get("user-invocable", "")).lower() != "true":
            fail(f"{path.relative_to(ROOT)} phải khai báo 'user-invocable: true'")
            errors += 1
        if str(frontmatter.get("disable-model-invocation", "")).lower() != "true":
            fail(f"{path.relative_to(ROOT)} phải khai báo 'disable-model-invocation: true'")
            errors += 1
        if "{{args}}" in body:
            fail(f"{path.relative_to(ROOT)} không dùng {{{{args}}}}; DSH không thay tham số trong skill")
            errors += 1
        if "spawn_teammate" not in body:
            fail(f"{path.relative_to(ROOT)} phải hướng dẫn gọi vai trò qua Agent Teams")
            errors += 1

    expected |= {f"{command}.md" for command in REQUIRED_NATIVE_COMMANDS}
    existing = {entry.name for entry in NATIVE_SKILL_DIR.iterdir() if not entry.name.startswith(".")}
    if extra := existing - expected:
        fail(f"skill native ngoài dự kiến: {', '.join(sorted(extra))}")
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

    if not NATIVE_SKILL_DIR.is_dir():
        fail("thiếu .agents/skills/")
        errors += 1
    else:
        errors += check_native_skills()

    if errors:
        print(f"KẾT QUẢ: {errors} lỗi")
        return 1

    print(f"ĐẠT: {len(REQUIRED_AGENTS)} agent Codex, {len(REQUIRED_AGENTS)} agent Qwen Code, "
          f"{len(REQUIRED_QWEN_COMMANDS)} lệnh Qwen Code")
    print(f"ĐẠT: {len(NATIVE_ROLE_SKILLS)} skill vai trò native, "
          f"{len(REQUIRED_NATIVE_COMMANDS)} lệnh tắt native cho DeepSeek Harness")
    print(f"ĐẠT: {len(REQUIRED_PATHS)} tài liệu bắt buộc")
    print("ĐẠT: cấu hình dự án khai báo một agent được ghi và năm agent chỉ đọc")
    print("LƯU Ý: quyền chạy thực tế của phiên vẫn có thể ghi đè mặc định của agent; "
          "ở bản native DSH, ràng buộc chỉ đọc là hướng dẫn chứ không phải giới hạn công cụ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
