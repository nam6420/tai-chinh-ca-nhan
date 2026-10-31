# Biên bản phản biện rủi ro — Bài F1 (bản viết lại 2026-10-31)

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; số liệu Apple FY2025, phép tính, đáp án, nhãn nhận định, nguồn dẫn; mô hình learning/practice/models/valuation.py. Bốn vòng: vòng 1 trên bản viết lại đầu, các vòng 2–4 trên bản đã sửa; vòng 4 trên bản có mã băm tệp d4f37324, f8101b5a và tương ứng.`
- Báo cáo đích: `learning/lessons/F1-three-statement-model-sensitivity.md`
- SHA-256 nội dung đích: `3f2c5014c1bfcb7b679375d9cb4936839f0b76726e6b51b53c6c1abaa87bc61b`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 31/10/2026; người kiểm không sửa bài. Hai nhánh không đọc kết luận của nhau.

## Kết quả

Vòng 1: 2 lỗi nghiêm trọng (gọi sai 'đòn bẩy vận hành'; CCC bỏ phải thu phi thương mại) và vòng 2: 1 lỗi trung bình (chi trả/FCF chưa nhắc méo thuế), tất cả đã sửa và xác nhận. Không còn lỗi nghiêm trọng hay trung bình.

## Hạn chế

- Giá AAPL ngày 30/10/2026 (344,63) chỉ có từ nguồn thứ cấp stockanalysis.com, chưa đối chiếu sàn.
- Người phản biện không có công cụ tính mã băm; mã băm do điều phối viên tính bằng `scripts/validate_report.py --print-hash`. Sau vòng 4 điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (tách dòng chốt dữ liệu, tách hai dòng trạng thái kiểm duyệt, bỏ nhãn nháp), không đổi nội dung dạy.
- Điểm còn mở mức Thấp: chưa có nguồn mở được cho Fisher dạng nhân, điều kiện quan hệ sạch của RIM, xử lý thiểu số và chi phí trụ sở trong SOTP, chiết khấu tập đoàn 15%; hoàn thuế quan một lần ở biên gộp quý 3 FY2026 chưa nhắc; quyết định pháp lý cụ thể chưa nêu tên.
- Không đo hiệu quả học thực tế; chưa thử với người học.
