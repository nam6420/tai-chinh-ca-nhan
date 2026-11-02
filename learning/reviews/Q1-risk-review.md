# Biên bản phản biện rủi ro — Bài Q1

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; sàng lọc không phải bằng chứng gian lận, hiệu chỉnh Mỹ, Z'' so Z', ngưỡng −1,78/−2,22, độ nhạy, nhãn, đáp án`
- Báo cáo đích: `learning/lessons/Q1-earnings-quality-toolkit.md`
- SHA-256 nội dung đích: `24094d79412f978315831ab00ed85071672e24694c194b4fe6bab8d6fdbe36c3`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 6 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–6: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Các điểm sửa sau vòng 5 (Z' và Bảng 7, độ nhạy một chiều, cổ tức 2024 thực hiện 2025, nhãn Wikipedia) khắc phục thật; bài không cáo buộc HPG, không dạy coi cờ là bằng chứng gian lận.

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `31e2d2c6abdf78e65e4e2352bc406bc20bd9daba1e903529442ebbc5f32d6503`. Sau đó điều phối viên chỉ chuẩn hóa siêu dữ liệu đầu bài (bỏ nhãn nháp, trạng thái ĐẠT, dòng biên bản, dòng "sửa sau các vòng"), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng 1–5 trước đó (tóm lược ở learning/reviews/Q-round-1.md đến Q-round-4.md và Q-round-5-6.md) đã sửa nhiều lỗi; vòng 6 là vòng cuối trên bản này.
- Điểm trung bình còn mở (phản biện): so Z'' và Z' cần nói vị trí trong vùng (Z'' sát cận trên 2,6 của vùng xám, Z' sát cận dưới); mô tả Z' là mô hình "cho công ty sản xuất" chưa nêu lý do Altman bỏ X5 trong Z''; hiệu chỉnh X2 chỉ cộng cổ tức cổ phiếu 2025 nên Z'' 2,69 là cận dưới của hiệu ứng.
- Điểm thấp: Z' chỉ tính trong test, chưa có hàm trong mô-đun; Bảng 7 không phải xếp hạng của HPG; biến thể hệ số TATA 4,679/4,697 ở nguồn thứ cấp; chữ "earnings management" của nghiên cứu Việt Nam.
