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

Trong Qwen Code, ba câu lệnh trên đã có sẵn dưới dạng `/hoc`, `/nghien-cuu-doanh-nghiep` và `/nghien-cuu-nganh`.

Không cần gọi đủ mọi agent cho câu hỏi nhỏ. Nhiều agent tốn thêm thời gian và token; dùng quy trình đầy đủ khi kết luận phụ thuộc nhiều nguồn hoặc có thể ảnh hưởng quyết định tài chính.
