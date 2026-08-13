---
description: Nghiên cứu doanh nghiệp đầy đủ - research_coordinator điều phối analyst, macro, kiểm nguồn và phản biện
---

Dùng subagent research_coordinator điều phối company_analyst, macro_market_researcher, source_fact_checker và risk_bear_reviewer để nghiên cứu: {{args}}.

Yêu cầu bắt buộc:

- Nếu {{args}} thiếu mã chứng khoán hoặc thị trường, hỏi lại tôi trước khi thu thập dữ liệu.
- Tất cả agent phải tự tìm kiếm Internet trong lượt này, mở nguồn gốc chính thức, đối chiếu bối cảnh toàn cầu, ghi thời điểm chốt dữ liệu và trả lời hoàn toàn bằng tiếng Việt.
- Tạo Đề bài nghiên cứu theo `templates/research-brief.md` và lưu vào `research/`.
- Chờ tất cả agent hoàn tất; chạy kiểm nguồn và phản biện rủi ro trên cùng một bản nháp cố định với biên bản theo `templates/review-record.md`.
- Chỉ bỏ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT` khi cả hai biên bản đều ĐẠT và `scripts/validate_report.py` thông qua.
- Báo cáo cuối theo `templates/company-report.md`, viết cho người mới học. Không khuyến nghị mua/bán.
