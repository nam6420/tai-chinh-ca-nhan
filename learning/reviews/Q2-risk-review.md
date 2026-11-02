# Biên bản phản biện rủi ro — Bài Q2

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; cơ chế mua lại, SBC, cổ phiếu thưởng, mẫu một công ty, nhãn nhận định, đáp án`
- Báo cáo đích: `learning/lessons/Q2-sbc-dilution-buybacks-dividends.md`
- SHA-256 nội dung đích: `e84b15a0bf43bfad1142dd669bdf1d1e867e8e07ac3d9f70e0860de54b2ca635`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 5 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–5: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Năm điểm sửa sau vòng 4 (State Aid trong ba năm, FCF đơn giản, ô SBC, đáp án 8, 10-Q) khắc phục thật. Không có đáp án sai.

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `40dd98b0c4f9e60718da3b2da15b9fc618fce628675583b0699d5d4104805926`. Sau đó điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (bỏ nhãn nháp, đặt trạng thái ĐẠT, thêm dòng biên bản), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng kiểm duyệt 1–4 (nhật ký ở learning/reviews/Q-round-1.md đến Q-round-4.md) đã sửa nhiều lỗi; vòng 5 là vòng cuối trên bản này.
- Điểm thấp còn mở (kiểm nguồn): câu "chênh 1.732 cũng đã gồm khoản này" nên viết có điều kiện.
- Điểm còn mở (phản biện): vay ròng chưa tính; mục "Sai ở đâu" 5; thuật ngữ cổ tức bằng cổ phiếu; thiếu bằng chứng thực nghiệm trái chiều.
