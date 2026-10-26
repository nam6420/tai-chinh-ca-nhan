---
name: nghien-cuu-nganh
description: "Lệnh tắt /nghien-cuu-nganh: nghiên cứu một ngành trên phạm vi toàn cầu với quy trình điều phối và kiểm duyệt đầy đủ."
disable-model-invocation: true
user-invocable: true
---

# `/nghien-cuu-nganh` — nghiên cứu một ngành

Phần văn bản còn lại sau lệnh là tên ngành và các thị trường cần so sánh. Nếu chưa rõ ngành hoặc thị trường, hỏi lại người dùng trước khi thu thập dữ liệu.

## Cách thực hiện

1. Nạp kỹ năng `research-coordinator` và làm đúng vai trò điều phối.
2. Một nhánh phân tích đặc tính kinh tế của ngành (`company-analyst`), một nhánh nghiên cứu vĩ mô (`macro-market-researcher`); sau đó `source-fact-checker` xác minh và `risk-bear-reviewer` phản biện trên cùng bản nháp cố định. Trong Agent Teams, dùng `spawn_teammate` cho từng nhánh với prompt tự chứa (yêu cầu teammate nạp đúng skill) và giao việc qua shared task.
3. Tất cả vai trò phải tự tìm kiếm Internet trong chính lượt này (`web_search` rồi `web_fetch` mở nguồn gốc chính thức), ghi thời điểm chốt dữ liệu và trả lời hoàn toàn bằng tiếng Việt.
4. Nghiên cứu trên phạm vi toàn cầu; chỉ rõ khác biệt tại từng thị trường, đồng tiền và chuẩn kế toán được nêu.
5. Tổng hợp kịch bản thuận lợi/cơ sở/bất lợi, điều chưa biết và điều kiện làm luận điểm mất hiệu lực; giữ lại bất đồng chưa giải quyết.
6. Lưu đề bài, sổ nguồn, biên bản và báo cáo theo mẫu trong `templates/`; chỉ bỏ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT` khi đủ hai biên bản `ĐẠT` cùng mã băm hiện tại, và sau khi bỏ nhãn `python3 scripts/validate_report.py <báo-cáo> --fact-check <biên-bản-kiểm-nguồn> --bear-review <biên-bản-phản-biện>` in `ĐẠT`.

Không khuyến nghị mua/bán/nắm giữ, không cam kết lợi nhuận.
