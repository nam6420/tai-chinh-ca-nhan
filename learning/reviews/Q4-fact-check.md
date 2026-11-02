# Biên bản kiểm nguồn — Bài Q4

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Trang SEC (EDGAR APIs, Accessing EDGAR Data, webmaster FAQ, developer-resources), companyfacts Apple, 10-K và 8-K, Thông tư 96/2020 bản đăng lại, BCTC HPG, data_pull.py, CSV và test`
- Báo cáo đích: `learning/lessons/Q4-getting-data-edgar-xbrl-vietnam.md`
- SHA-256 nội dung đích: `d08f14b282f9be4cec2af02cce8f5f9e79e683b1a8e597193cf3fd88a24e4d7c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 5 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–5: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Mọi số Apple (companyfacts, 10-K, 8-K), 14 chỉ tiêu × 2 năm của HPG so với PDF, Thông tư 96 bản đăng lại (Điều 10, 14) và quy tắc SEC khớp nguồn; `ytd_value` làm đúng điều bài mô tả. 12 test đạt; SHA-256 của JSON và PDF khớp bài.

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `283f16b2904a730535dd24c609597343823c4a6fc18e94e967fc11867a5e1020`. Sau đó điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (bỏ nhãn nháp, đặt trạng thái ĐẠT, thêm dòng biên bản), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng kiểm duyệt 1–4 (nhật ký ở learning/reviews/Q-round-1.md đến Q-round-4.md) đã sửa nhiều lỗi; vòng 5 là vòng cuối trên bản này.
- Điểm thấp còn mở (kiểm nguồn): diễn đạt Điều 14 khoản 4c ("hoặc soát xét") ; docstring `fetch_companyfacts` nói "yêu cầu" mạnh hơn SEC; câu 20-F chưa gắn nhãn SUY_LUẬN.
- `CHƯA_BIẾT` còn mở: văn bản gốc và các sửa đổi 18/2025, 08/2026 của Thông tư 96, dự thảo thay thế.
