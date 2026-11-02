# Biên bản kiểm nguồn — Bài Q3

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `BCTC HPG FY2025, báo cáo thường niên 2019, tổng quan Q3/2026, Bizhub/Vietnam News 22/04/2026, tái tính từ CSV, cyclical.py và test`
- Báo cáo đích: `learning/lessons/Q3-normalizing-earnings-cyclical.md`
- SHA-256 nội dung đích: `3b543db8af30c603e9826e2f7968e4b440753045ef64c8f01af35a9d6b82dbbc`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 6 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–6: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Mọi số HPG (BCTC FY2025, báo cáo thường niên 2019, tổng quan Q3/2026), bảng tám cách chuẩn hóa, khoản một lần Phố Nối (Bizhub/Vietnam News, thứ cấp), lãi vay theo quý, dư nợ/vốn chủ 0,70–0,71 và các phép tính tái lập từ CSV khớp. 76 test đạt.

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `ae5b1af9badcc4f57798280bcf81952b5ea0bf42fe83489ff534e850453cc8db`. Sau đó điều phối viên chỉ chuẩn hóa siêu dữ liệu đầu bài (bỏ nhãn nháp, trạng thái ĐẠT, dòng biên bản, dòng "sửa sau các vòng"), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng 1–5 trước đó (tóm lược ở learning/reviews/Q-round-1.md đến Q-round-4.md và Q-round-5-6.md) đã sửa nhiều lỗi; vòng 6 là vòng cuối trên bản này.
- Điểm thấp còn mở (kiểm nguồn): "19% LNST ≈ 4.400 tỷ" tính lại ra 4.512 (khoảng 4.393–4.630 do làm tròn); phần chênh khoảng 0,2 nghìn tỷ giữa tổng thành phần và tổng "hơn 9 nghìn tỷ" của bài Bizhub; định nghĩa "dư nợ vay" của bản tổng quan chưa đối chiếu; biên và lãi vay theo quý đọc từ nhãn biểu đồ.
- Chưa mở lại ở vòng 6: báo cáo thường niên 2023 và Damodaran chương 22 (đã kiểm ở các vòng trước).
