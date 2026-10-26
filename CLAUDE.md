@AGENTS.md

## Claude Code (bản native)

- Vai trò là subagent trong `.claude/agents/<ten-vai-tro>.md`, tên kebab-case giống DeepSeek Harness: `research-coordinator`, `business-tutor`, `macro-market-researcher`, `company-analyst`, `source-fact-checker`, `risk-bear-reviewer`.
- Quyền được buộc bằng trường `tools` trong frontmatter: năm vai trò chuyên môn không có `Write`/`Edit`; bốn vai trò không có cả `Bash`; riêng `source-fact-checker` có `Bash` chỉ để tái tính và kiểm mã băm. `research-coordinator` là vai trò duy nhất có `Write`/`Edit`.
- Subagent của Claude Code không gọi được subagent khác. Vì vậy khi nghiên cứu nhiều nhánh, **phiên chính** đóng vai `research-coordinator` (làm theo `.claude/agents/research-coordinator.md`) và giao từng nhánh cho subagent chuyên môn bằng công cụ `Agent`. Chỉ giao cho subagent `research-coordinator` khi việc là tổng hợp/ghi một tài liệu từ các gói bằng chứng đã có.
- Chạy song song các nhánh độc lập (ví dụ `company-analyst` và `macro-market-researcher`) trong cùng một lượt; `source-fact-checker` và `risk-bear-reviewer` chạy độc lập trên cùng bản nháp cố định, không cho bên này thấy kết luận của bên kia.
- Ba lệnh tắt trong `.claude/commands/`: `/hoc <khái niệm>`, `/nghien-cuu-doanh-nghiep <mã, thị trường>`, `/nghien-cuu-nganh <ngành, thị trường>`.
- Tìm kiếm Internet bằng `WebSearch`, mở trang nguồn bằng `WebFetch`. Không dùng đoạn trích trên trang kết quả làm bằng chứng.
- Kiểm tra cấu hình: `python3 scripts/verify.py` và `python3 -m unittest discover tests`.
