# Biên bản kiểm nguồn — Bài Q2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Apple 10-K FY2025 và 10-Q quý 2 FY2025, thẻ XBRL, Damodaran 24/02/2026, BCTC HPG FY2025 (trang in 7, 8, 38, 39), mô hình capital_return.py, CSV và test`
- Báo cáo đích: `learning/lessons/Q2-sbc-dilution-buybacks-dividends.md`
- SHA-256 nội dung đích: `e84b15a0bf43bfad1142dd669bdf1d1e867e8e07ac3d9f70e0860de54b2ca635`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 5 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–5: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Mọi số Apple FY2025 (10-K, 10-Q quý 2, thẻ XBRL), bảng ba năm, phép loại khoản thuế một lần (EPS tăng khoảng 10,6%, tính của bài), phân rã lợi nhuận chưa phân phối của HPG và các trích dẫn Damodaran khớp nguồn. 75 test đạt.

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `40dd98b0c4f9e60718da3b2da15b9fc618fce628675583b0699d5d4104805926`. Sau đó điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (bỏ nhãn nháp, đặt trạng thái ĐẠT, thêm dòng biên bản), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng kiểm duyệt 1–4 (nhật ký ở learning/reviews/Q-round-1.md đến Q-round-4.md) đã sửa nhiều lỗi; vòng 5 là vòng cuối trên bản này.
- Điểm thấp còn mở (kiểm nguồn): câu "chênh 1.732 cũng đã gồm khoản này" nên viết có điều kiện; diễn đạt lại Damodaran về FCFE âm hơi mạnh.
- Điểm trung bình/thấp còn mở (phản biện): nguồn bù khoản vượt (vay ròng) chưa tính nên chưa tới FCFE; mục "Sai ở đâu" 5 hơi nghiêng đánh giá chính sách Apple; "cổ phiếu thưởng" so với "cổ tức bằng cổ phiếu" khác nhau về thuật ngữ pháp lý; chưa có bằng chứng thực nghiệm trái chiều; tiêu đề cột "CFO − capex" chưa đổi.
