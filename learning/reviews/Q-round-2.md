# Biên bản điều phối: vòng kiểm duyệt 2 cho bài Q1–Q4

- Loại: tóm lược của điều phối viên; KHÔNG phải biên bản ĐẠT của source-fact-checker hay risk-bear-reviewer. Toàn văn tám báo cáo nằm trong tin nhắn của phiên làm việc, chưa được lưu từng biên bản riêng.
- Ghi lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Mã băm bản cố định vòng 2: Q1 `4ca62163…06f`, Q2 `8e6858c2…98`, Q3 `3d2c5b7c…748`, Q4 `ee2bb260…d51`. Sau khi sửa các mã này đã đổi; không dùng báo cáo vòng 2 để bỏ nhãn nháp.

## Kết luận vòng 2

| Bài | Kiểm nguồn | Phản biện | Lỗi nghiêm trọng |
|---|---|---|---|
| Q1 | KHÔNG_ĐẠT (LEVER của Piotroski phải cộng nợ dài hạn đến hạn: F HPG thành 6/5, không phải 7/6) | KHÔNG_ĐẠT (3 phát hiện cao: vùng Z'' khi cộng 3,25; độ nhạy định nghĩa TATA; tỷ lệ gắn cờ nền ở Việt Nam 40–48%) | 1 |
| Q2 | ĐẠT | ĐẠT có điều kiện (2 cao: dòng tiền FY2025 có thể bị nén bởi khoản nộp thuế State Aid, mẫu một năm Apple) | 0 |
| Q3 | ĐẠT | ĐẠT có điều kiện (5 cao: quy mô 9T/2026, tên dự án HPDQ2, lãi vay 9T/2026, biên theo quý, điều kiện "trưởng thành") | 0 |
| Q4 | ĐẠT | ĐẠT có điều kiện (1 cao: nhãn Thông tư 96) | 0 |

## Xử lý

- Q4: đã sửa toàn bộ phát hiện (nhãn Thông tư 96 hạ xuống thứ cấp chưa hợp nhất và thêm dự thảo thay thế; số 24.497,79 là số làm tròn chứ không phải số in; "đến nghìn đồng"; "e.g."; ZIP; 0,2 giây; ngày sớm nhất 29/09/2018; điều kiện hết hiệu lực). Cần chạy lại vòng 3.
- Q1: đã sửa (LEVER gồm nợ dài hạn đến hạn: F HPG 6/5, thêm `lever_def`, cột `no_dai_han_den_han` từ thuyết minh 23 trang in 35 đã mở lại; hạ nhãn vùng Z''; độ nhạy TATA ghi CHƯA_BIẾT; tỷ lệ nền Việt Nam; bảng hai trục −1,78/−2,22; lý do chọn Z''; điều làm đổi kết luận); cần chạy lại vòng 3.
- Q2, Q3: chưa sửa tại thời điểm ghi; xem "Việc cần làm".

## Việc cần làm

- Q1: thêm cột `no_dai_han_den_han` (thuyết minh 23: 3.298,8 đầu năm; 8.826,2 cuối năm, đơn vị tỷ VND) và tính LEVER theo Piotroski; hạ nhãn vùng Z''; thêm độ nhạy TATA; thêm tỷ lệ gắn cờ nền; bảng 2×2 cho ngưỡng −1,78/−2,22; lý do chọn Z''; B/M của HPG là CHƯA_BIẾT; mục điều làm đổi kết luận.
- Q2: bảng ba năm cho "trả vượt dòng tiền"; số quý 4 của Item 5; tách 1.283,9 của HPG từ biến động vốn chủ; ví dụ chỉ để minh họa; "EPS tăng… giữ lợi nhuận cố định".
- Q3: bảng biên theo quý, lãi vay, quy mô mới; tên dự án; điều kiện "trưởng thành"; kịch bản thuận lợi dùng biên thép; chiết khấu lùi áp lên giá trị; chiều đòn bẩy cho ROE × vốn chủ.
