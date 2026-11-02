# Biên bản điều phối: vòng kiểm duyệt 4 cho bài Q1–Q4

- Loại: tóm lược của điều phối viên; KHÔNG phải biên bản ĐẠT của source-fact-checker hay risk-bear-reviewer. Toàn văn tám báo cáo nằm trong tin nhắn của phiên làm việc.
- Ghi lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Tiêu chí vòng 4 (đặt bởi điều phối viên, thấp hơn vòng 2–3): ĐẠT khi không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp liệt kê nhưng không chặn.
- Mã băm bản cố định: Q1 `6605b4da…`, Q2 `be410f87…`, Q3 `e064e7cd…`, Q4 `f4288ccb…` (cả tám nhánh khớp mã).

| Bài | Kiểm nguồn | Phản biện | Phát hiện còn mở đáng chú ý |
|---|---|---|---|
| Q1 | ĐẠT (0 cao; 1 trung bình, 6 thấp) | ĐẠT (0 cao; 5 trung bình, 6 thấp) | Z'' loại thu nhập tài chính chỉ hạ Z'' (2,47–2,56), không đổi vùng; độ nhạy thật nằm ở X2 khi cộng lại 12.792,2 tỷ cổ tức bằng cổ phiếu (Z'' khoảng 2,69, trên 2,6; phép tính của nhánh phản biện, chưa đọc thuyết minh 26 để chắc); mã 338 năm 2024 sai chữ số (27.080,443, bài ghi 27.080,5); hai nghiên cứu Việt Nam cùng nhóm tác giả, mẫu chồng lấn; cột nợ phải trả và vốn chủ ghi "Trình bày lại" |
| Q2 | ĐẠT (0 cao; 0 trung bình, 3 thấp) | ĐẠT (0 cao; 5 trung bình, 3 thấp) | "Ba năm gần cân bằng" cũng đã gồm khoản State Aid; CFO − capex chưa phải FCFE; thiếu ví dụ trái chiều; 10-Q chưa vào bảng nguồn |
| Q3 | ĐẠT (0 cao; 2 trung bình, 2 thấp) | ĐẠT (0 cao; 5 trung bình, 4 thấp; M3 có thể lên cao) | Biên nhóm thép 11,10% chưa chắc là biên thép sạch (165.784 + 5.064 = 170.848 trên 171.539 chỉ còn khoảng 691 cho bất động sản trong khi nguồn ghi 1%); "gấp ba lần" chỉ đúng trong cửa sổ FY2021–FY2025 (2019: 64.678 doanh thu, 7.578 LNST); biên LNST Q1/26 (17,0%) cao hơn biên gộp (15,7%); lỗi chính tả "chưa tôi kiểm" |
| Q4 | ĐẠT (0 cao; 0 trung bình, 6 thấp) | ĐẠT (0 cao; 4 trung bình, 3 thấp) | `ytd_value` không dùng cùng quy tắc chọn hồ sơ với `annual_series`; năm đẳng thức chỉ kiểm quan hệ giữa các tổng; FAQ/developer-resources chưa vào bảng nguồn; giả thuyết 90.052 nay có bằng chứng (thẻ cùng tên, chiều `RetainedEarningsMember`, `decimals="-6"`; 89,3 có `decimals="-8"`) |

## Trạng thái

Cả bốn bài có hai biên bản ĐẠT khớp mã băm theo tiêu chí vòng 4, nhưng chưa bỏ nhãn nháp vì các phát hiện còn mở ở trên chưa được xử lý. Mỗi lần sửa bài là đổi mã băm và hết hiệu lực của biên bản.
