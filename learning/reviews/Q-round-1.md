# Biên bản điều phối: vòng kiểm duyệt 1 cho bài Q1–Q4

- Loại: tóm lược của điều phối viên (`research-coordinator`); KHÔNG phải biên bản ĐẠT của source-fact-checker hay risk-bear-reviewer.
- Vòng: 1 (tám nhánh độc lập, mỗi bài một nhánh kiểm nguồn và một nhánh phản biện, trên bản cố định đã commit)
- Ghi lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Hiệu lực: mã băm của bản vòng 1 đã lỗi thời vì cả bốn bài đã sửa; biên bản này chỉ ghi lịch sử xử lý, không dùng để bỏ nhãn nháp.
- Ghi chú trung thực: toàn văn tám báo cáo của subagent không được lưu trong repo; bảng dưới là tóm lược của điều phối viên theo trí nhớ phiên làm việc trước, cộng phần tự kiểm lại với nguồn trong phiên này.

## Kết luận vòng 1

| Bài | Kiểm nguồn | Phản biện rủi ro | Hành động |
|---|---|---|---|
| Q1 | KHÔNG_ĐẠT | KHÔNG_ĐẠT | Sửa |
| Q2 | ĐẠT có điều kiện | KHÔNG_ĐẠT | Sửa |
| Q3 | ĐẠT có điều kiện | KHÔNG_ĐẠT | Sửa |
| Q4 | KHÔNG_ĐẠT | KHÔNG_ĐẠT | Sửa (xong ở phiên 2026-11-02) |

## Xử lý các phát hiện chính

| Bài | Phát hiện | Xử lý |
|---|---|---|
| Q1 | AQI của HPG cộng trùng đầu tư ngắn hạn (mã 120 đã nằm trong mã 100); test khóa số sai nên vẫn xanh | Ánh xạ A làm mặc định (−1,575) kèm B, C; test tái tính độc lập bằng cách cộng thành phần |
| Q1 | `piotroski()` thiếu cờ phát hành cổ phiếu; Z'' hai biến thể; nhãn nguồn thứ cấp; nguyên nhân dòng tiền gán SỰ_THẬT; "chấp nhận toàn phần" | Bắt buộc tham số; nêu cả hai biến thể; sửa nhãn; hạ nguyên nhân thành SUY_LUẬN; đổi thành "ý kiến không ngoại trừ" |
| Q2 | Ba số mua lại Apple FY2025 (89.300 / 90.052 / 90.711) bị gộp thành hai | Ghi cả ba, nguyên nhân CHƯA_BIẾT |
| Q2 | "Tính hai lần" SBC; "EPS tăng bất kể giá"; thuế trả hộ lẫn tiền trả cổ đông; thuế một lần FY2024 | Hạ nhãn, sửa câu, tách số, thêm cảnh báo |
| Q3 | Thiếu biến thể bỏ cả đỉnh lẫn đáy; biên nhóm thép so biên hợp nhất; mẫu số doanh thu; chiết khấu lùi; nhãn "chưa kiểm toán" | Thêm biến thể, biên riêng 11,10%, nêu rõ phép minh họa, hạ nhãn, thêm điều kiện mất hiệu lực |
| Q4 | Số mua lại nói sai ("89.300 là giá trị trong báo cáo vốn chủ", trong khi báo cáo ghi 90.052) | Ghi ba số; sửa cạm bẫy 8, bài tập 6, "Sai ở đâu" 5, test |
| Q4 | Thời hạn công bố gắn sai điều luật; chưa nêu sửa đổi thông tư | Điều 10 khoản 1(c), Điều 14 khoản 1, 2(c), 3(c); nêu Thông tư 68/2024/TT-BTC; các sửa đổi khác CHƯA_BIẾT |
| Q4 | Thiếu cạm bẫy 10–13; `annual_series` không tie-break; `fetch_companyfacts` thiếu giới hạn tần suất/cache; dung sai đẳng thức; thiếu cột trang | Thêm; sửa mã và test; thêm cột `trang_in` |
| Q4 | Số quý 4 chưa đối chiếu | Đã đối chiếu với phụ lục 99.1 của 8-K (27.466 triệu USD) |

## Việc kế tiếp

Vòng 2: chạy lại tám nhánh độc lập trên bản cố định mới (mã băm tính bằng `validate_report.py --print-hash` tại thời điểm giao việc).
