# Đội agent nghiên cứu

## Vai trò

| Agent | Sản phẩm chính | Quyền ghi tệp |
|---|---|---:|
| `research_coordinator` | Đề bài, phân công, bản tổng hợp cuối | Có |
| `business_tutor` | Bài học, ví dụ, bài tập | Không |
| `macro_market_researcher` | Gói bằng chứng vĩ mô/ngành/thị trường | Không |
| `company_analyst` | Gói bằng chứng doanh nghiệp/tài chính/định giá | Không |
| `source_fact_checker` | Bảng kiểm nguồn và phép tính | Không |
| `risk_bear_reviewer` | Phát hiện phản biện độc lập | Không |

## Quy tắc chung cho cả đội

- Luôn trả lời bằng tiếng Việt.
- Bắt buộc tìm kiếm Internet trong lượt hiện tại trước mọi câu trả lời có nội dung.
- Không dùng trí nhớ mô hình, kiến thức nhúng trong agent hoặc dữ liệu cũ của repo làm bằng chứng.
- Nghiên cứu theo phạm vi toàn cầu; dùng nguồn chính thức tại thị trường liên quan và nguồn so sánh quốc tế khi hữu ích.
- Nếu không truy cập được Internet, báo `KHÔNG THỂ XÁC MINH TRỰC TUYẾN`; không tự điền câu trả lời từ trí nhớ.

## Dùng trong DeepSeek Harness (bản native)

- Vai trò được khai báo thành project skill trong `.agents/skills/`, mỗi vai trò một thư mục `SKILL.md` (riêng ba lệnh tắt là tệp phẳng `<ten>.md`). DSH tự quét thư mục này của repo và nạp cùng `AGENTS.md` làm ngữ cảnh chung; không cần cấu hình thêm.
- Tên skill là kebab-case, khác tên vai trò ở bản Qwen/Codex (gạch nối thay gạch dưới): `research-coordinator`, `business-tutor`, `macro-market-researcher`, `company-analyst`, `source-fact-checker`, `risk-bear-reviewer`.
- Gọi vai trò bằng Agent Teams: `spawn_teammate` với `description` một dòng và `prompt` tự chứa, yêu cầu teammate nạp skill tương ứng trước khi làm. Giao việc qua shared task; `writeScopes` chỉ cấp cho `research-coordinator` trên tài liệu của mình.
- Ba lệnh tắt là skill do con người gọi nên không hiện trong danh mục cho model: gõ `/` rồi chọn, hoặc gõ thẳng `/hoc`, `/nghien-cuu-doanh-nghiep`, `/nghien-cuu-nganh`.
- Skill không giới hạn được công cụ như `tools` của Qwen Code hay `sandbox_mode` của Codex. Ở bản native, "năm vai trò chuyên môn chỉ đọc, điều phối viên là người ghi duy nhất" là ràng buộc hướng dẫn: phải ghi rõ trong prompt giao việc và tự kiểm khi nhận kết quả. Chạy `python3 scripts/verify.py` để kiểm tra cấu hình của cả bốn bản.

## Dùng trong Claude Code

- `CLAUDE.md` nạp `AGENTS.md` bằng `@AGENTS.md`, nên Claude Code dùng chung toàn bộ chính sách dự án.
- Vai trò là subagent trong `.claude/agents/`, tên kebab-case giống bản DSH. Quyền được buộc bằng trường `tools`: năm vai trò chuyên môn không có `Write`/`Edit`; riêng `source-fact-checker` có `Bash` để tái tính và kiểm mã băm. `research-coordinator` là vai trò duy nhất có `Write`/`Edit`.
- Subagent không gọi được subagent khác, nên khi nghiên cứu nhiều nhánh **phiên chính** đóng vai điều phối viên và giao nhánh bằng công cụ `Agent`; các nhánh độc lập chạy song song.
- Lệnh tắt trong `.claude/commands/`: `/hoc <khái niệm>`, `/nghien-cuu-doanh-nghiep <mã, thị trường>`, `/nghien-cuu-nganh <ngành, thị trường>`.
- `.claude/settings.json` cho phép sẵn `WebSearch`, `WebFetch` và các lệnh kiểm tra của repo; chặn đọc `.env` và `journal/private/`. Cấu hình cá nhân để ở `.claude/settings.local.json` (đã gitignore).

## Dùng trong Qwen Code

- Agent được khai báo trong `.qwen/agents/` (Markdown + YAML frontmatter). Qwen Code tự đọc `AGENTS.md` của repo làm ngữ cảnh chung.
- Quyền chỉ đọc được buộc bằng danh sách `tools` trong frontmatter: năm agent chuyên môn không có công cụ ghi tệp; riêng `source_fact_checker` được chạy shell để tái tính phép tính và kiểm mã băm nhưng vẫn không có công cụ ghi. `research_coordinator` là agent duy nhất có `write_file`/`edit`.
- Lệnh tắt của dự án (định nghĩa trong `.qwen/commands/`): `/hoc <khái niệm>`, `/nghien-cuu-doanh-nghiep <mã, thị trường>`, `/nghien-cuu-nganh <ngành, thị trường>`.
- Trong phiên không có sẵn công cụ tìm kiếm, agent dùng `web_fetch` mở trang kết quả (ví dụ DuckDuckGo hoặc Bing) rồi mở từng trang nguồn thực tế; nếu phiên có MCP tìm kiếm thì ưu tiên dùng MCP.

## Câu lệnh mẫu

### Học một khái niệm

```text
Dùng business_tutor dạy tôi cách đọc báo cáo lưu chuyển tiền tệ.
Bắt buộc tìm kiếm Internet, dùng nguồn chính thức quốc tế và ví dụ từ
một doanh nghiệp thật. Giải thích bằng tiếng Việt, có bài tập và đáp án.
```

### Nghiên cứu một doanh nghiệp

```text
Dùng research_coordinator điều phối company_analyst,
macro_market_researcher, source_fact_checker và risk_bear_reviewer để
nghiên cứu [MÃ CHỨNG KHOÁN] tại [THỊ TRƯỜNG]. Tất cả agent phải tự tìm
kiếm Internet trong lượt này, mở nguồn gốc chính thức, đối chiếu bối cảnh
toàn cầu, ghi thời điểm chốt dữ liệu và trả lời hoàn toàn bằng tiếng Việt.
Chờ tất cả agent rồi tạo báo cáo cho người mới học. Không khuyến nghị mua/bán.
```

### Nghiên cứu một ngành toàn cầu

```text
Nghiên cứu ngành [TÊN NGÀNH] trên phạm vi toàn cầu và chỉ rõ khác biệt tại
[CÁC THỊ TRƯỜNG]. Một agent phân tích đặc tính kinh tế của ngành, một agent
nghiên cứu vĩ mô, sau đó agent kiểm nguồn xác minh và agent rủi ro phản biện.
Agent điều phối tổng hợp kịch bản thuận lợi/cơ sở/bất lợi và điều chưa biết.
```

Trong DeepSeek Harness, Claude Code và Qwen Code, ba câu lệnh trên đã có sẵn dưới dạng `/hoc`, `/nghien-cuu-doanh-nghiep` và `/nghien-cuu-nganh`.

Không cần gọi đủ mọi agent cho câu hỏi nhỏ. Nhiều agent tốn thêm thời gian và token; dùng quy trình đầy đủ khi kết luận phụ thuộc nhiều nguồn hoặc có thể ảnh hưởng quyết định tài chính.
