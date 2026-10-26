---
description: "Nghiên cứu một ngành trên phạm vi toàn cầu với điều phối và kiểm duyệt đầy đủ"
argument-hint: "<ngành, các thị trường>"
---

Ngành và thị trường: $ARGUMENTS

Phiên chính đóng vai `research-coordinator`: đọc và làm đúng `.claude/agents/research-coordinator.md`.

1. Nếu chưa rõ ngành hoặc thị trường, hỏi lại người dùng trước khi thu thập dữ liệu.
2. Giao song song trong cùng một lượt bằng công cụ `Agent`: `company-analyst` phân tích đặc tính kinh tế của ngành, `macro-market-researcher` nghiên cứu vĩ mô; mỗi prompt tự chứa.
3. Tất cả vai trò phải tự tìm kiếm Internet trong lượt này (`WebSearch` rồi `WebFetch` mở nguồn gốc chính thức), ghi thời điểm chốt dữ liệu và trả lời hoàn toàn bằng tiếng Việt.
4. Nghiên cứu trên phạm vi toàn cầu; chỉ rõ khác biệt tại từng thị trường, đồng tiền và chuẩn kế toán được nêu.
5. Tổng hợp bản nháp cố định giữ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT`, rồi giao độc lập cho `source-fact-checker` xác minh và `risk-bear-reviewer` phản biện trên cùng bản nháp.
6. Tổng hợp kịch bản thuận lợi/cơ sở/bất lợi, điều chưa biết và điều kiện làm luận điểm mất hiệu lực; giữ lại bất đồng chưa giải quyết.
7. Lưu đề bài, sổ nguồn, biên bản và báo cáo theo mẫu trong `templates/`; chỉ bỏ nhãn nháp khi đủ hai biên bản `ĐẠT`, cùng mã băm hiện tại và `python3 scripts/validate_report.py` thông qua.

Không khuyến nghị mua/bán/nắm giữ, không cam kết lợi nhuận.
