---
description: "Nghiên cứu doanh nghiệp đầy đủ - điều phối analyst, macro, kiểm nguồn và phản biện"
argument-hint: "<mã chứng khoán, thị trường>"
---

Đối tượng nghiên cứu: $ARGUMENTS

Phiên chính đóng vai `research-coordinator`: đọc và làm đúng `.claude/agents/research-coordinator.md`.

1. Nếu thiếu mã chứng khoán hoặc thị trường, hỏi lại người dùng trước khi thu thập dữ liệu.
2. Tạo Đề bài nghiên cứu theo `templates/research-brief.md` và lưu vào `research/`.
3. Giao song song trong cùng một lượt cho subagent `company-analyst` và `macro-market-researcher` bằng công cụ `Agent`, mỗi prompt tự chứa (đối tượng, thị trường, kỳ, thời điểm chốt dữ liệu, định dạng gói bằng chứng).
4. Tất cả vai trò phải tự tìm kiếm Internet trong lượt này (`WebSearch` rồi `WebFetch` mở nguồn gốc chính thức), đối chiếu bối cảnh toàn cầu, ghi thời điểm chốt dữ liệu và trả lời hoàn toàn bằng tiếng Việt.
5. Tổng hợp thành bản nháp cố định giữ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT`; tính mã băm nội dung bằng `python3 scripts/validate_report.py <báo-cáo> --print-hash`.
6. Giao độc lập cho `source-fact-checker` và `risk-bear-reviewer` trên cùng bản nháp đó; không đưa kết luận của bên này cho bên kia. Ghi hai biên bản theo `templates/review-record.md`.
7. Chỉ bỏ nhãn nháp khi cả hai biên bản `ĐẠT` và cùng trỏ tới mã băm hiện tại; sau khi bỏ nhãn, `python3 scripts/validate_report.py <báo-cáo> --fact-check <biên-bản-kiểm-nguồn> --bear-review <biên-bản-phản-biện>` phải in `ĐẠT`. Trên bản còn nhãn nháp, script chỉ in `BẢN NHÁP`, không phải là thông qua.
8. Báo cáo cuối theo `templates/company-report.md`, viết cho người mới học, có kịch bản bất lợi/cơ sở/thuận lợi, rủi ro, bằng chứng trái chiều, điều chưa biết và điều kiện làm luận điểm mất hiệu lực.

Không khuyến nghị mua/bán/nắm giữ, không cam kết lợi nhuận, không đặt lệnh.
