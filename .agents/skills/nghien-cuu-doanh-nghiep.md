---
name: nghien-cuu-doanh-nghiep
description: "Lệnh tắt /nghien-cuu-doanh-nghiep: nghiên cứu doanh nghiệp đầy đủ với research-coordinator điều phối analyst, macro, kiểm nguồn và phản biện."
disable-model-invocation: true
user-invocable: true
---

# `/nghien-cuu-doanh-nghiep` — nghiên cứu một doanh nghiệp

Phần văn bản còn lại sau lệnh là mã chứng khoán, tên công ty và thị trường. Nếu thiếu mã hoặc thị trường, hỏi lại người dùng trước khi thu thập dữ liệu.

## Cách thực hiện

1. Nạp kỹ năng `research-coordinator` và làm đúng vai trò điều phối.
2. Tạo Đề bài nghiên cứu theo `templates/research-brief.md`, lưu vào `research/`; nêu câu hỏi, thị trường, kỳ phân tích, thời điểm chốt dữ liệu, tiêu chí hoàn thành.
3. Chia nhánh độc lập cho `company-analyst`, `macro-market-researcher`, `source-fact-checker`, `risk-bear-reviewer`. Trong Agent Teams, dùng `spawn_teammate` cho từng nhánh với prompt tự chứa (yêu cầu teammate nạp đúng skill), giao việc qua shared task, và chỉ cấp write scope cho tài liệu của điều phối viên. Teammate chuyên môn chỉ đọc và trả gói bằng chứng.
4. Tất cả vai trò phải tự tìm kiếm Internet trong chính lượt này (`web_search` rồi `web_fetch` mở nguồn gốc chính thức), ghi thời điểm chốt dữ liệu và trả lời hoàn toàn bằng tiếng Việt.
5. Tạo bản nháp cố định giữ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT`; chạy kiểm nguồn và phản biện độc lập trên cùng bản nháp, mỗi bên ghi biên bản theo `templates/review-record.md`.
6. Chỉ bỏ nhãn nháp khi cả hai biên bản `ĐẠT`, cùng trỏ tới mã băm hiện tại, và `scripts/validate_report.py` thông qua.
7. Báo cáo cuối theo `templates/company-report.md`, viết cho người mới học, có kịch bản bất lợi/cơ sở/thuận lợi, rủi ro, bằng chứng trái chiều, điều chưa biết và điều kiện làm luận điểm mất hiệu lực.

Không khuyến nghị mua/bán/nắm giữ, không cam kết lợi nhuận, không đặt lệnh.
