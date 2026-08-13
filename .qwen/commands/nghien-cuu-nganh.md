---
description: Nghiên cứu một ngành trên phạm vi toàn cầu với quy trình điều phối và kiểm duyệt đầy đủ
---

Dùng subagent research_coordinator để nghiên cứu ngành: {{args}}.

Yêu cầu bắt buộc:

- Nếu {{args}} chưa nêu rõ ngành hoặc thị trường cần so sánh, hỏi lại tôi trước khi thu thập dữ liệu.
- Một nhánh phân tích đặc tính kinh tế của ngành (company_analyst), một nhánh nghiên cứu vĩ mô (macro_market_researcher); sau đó source_fact_checker xác minh và risk_bear_reviewer phản biện trên cùng bản nháp cố định.
- Tất cả agent phải tự tìm kiếm Internet trong lượt này, mở nguồn gốc chính thức, ghi thời điểm chốt dữ liệu và trả lời hoàn toàn bằng tiếng Việt.
- Nghiên cứu trên phạm vi toàn cầu và chỉ rõ khác biệt tại các thị trường được nêu.
- Tổng hợp kịch bản thuận lợi/cơ sở/bất lợi, điều chưa biết và điều kiện làm luận điểm mất hiệu lực; giữ lại bất đồng chưa giải quyết.
- Lưu đề bài, sổ nguồn, biên bản và báo cáo theo mẫu trong `templates/`; chỉ bỏ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT` khi đủ hai biên bản ĐẠT và `scripts/validate_report.py` thông qua.
