# Biên bản kiểm nguồn — Bài 011 (bản viết lại 2026-10-31)

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; số liệu Apple FY2025, phép tính, đáp án, nhãn nhận định, nguồn dẫn; mô hình learning/practice/models/valuation.py. Bốn vòng: vòng 1 trên bản viết lại đầu, các vòng 2–4 trên bản đã sửa; vòng 4 trên bản có mã băm tệp d4f37324, f8101b5a và tương ứng.`
- Báo cáo đích: `learning/lessons/011-dcf-reverse-dcf.md`
- SHA-256 nội dung đích: `7ab38cae7ce69ee3e52101d09bc63a7b64d14638fe8018faa496579c71abfb6c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 31/10/2026; người kiểm không sửa bài. Hai nhánh không đọc kết luận của nhau.

## Kết quả

Mọi số Apple khớp 10-K; EV 1.667.254, TV/EV 76,6%, 115,12 USD, độ nhạy 3×3, định giá ngược (11,5/18,7/24,6/33,5%) và WACC hàm ý (7,4/6,3/5,7/4,9%) tái tính khớp; giá 345 (đóng cửa 30/10/2026 = 344,63) khớp nguồn thứ cấp stockanalysis.com. Cảnh báo FCF0 thô khớp 10-K (thuế tiền mặt 43.369 so với chi phí 20.719); phép kiểm NOPAT/chi đầu tư ròng 1.017 khớp; tăng trưởng quý 3 FY2026 khớp 10-Q. Slide fcff.pdf trang 4 nêu g/ROC.

## Hạn chế

- Giá AAPL ngày 30/10/2026 (344,63) chỉ có từ nguồn thứ cấp stockanalysis.com, chưa đối chiếu sàn.
- Người phản biện không có công cụ tính mã băm; mã băm do điều phối viên tính bằng `scripts/validate_report.py --print-hash`. Sau vòng 4 điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (tách dòng chốt dữ liệu, tách hai dòng trạng thái kiểm duyệt, bỏ nhãn nháp), không đổi nội dung dạy.
- Điểm còn mở mức Thấp: chưa có nguồn mở được cho Fisher dạng nhân, điều kiện quan hệ sạch của RIM, xử lý thiểu số và chi phí trụ sở trong SOTP, chiết khấu tập đoàn 15%; hoàn thuế quan một lần ở biên gộp quý 3 FY2026 chưa nhắc; quyết định pháp lý cụ thể chưa nêu tên.
- Không đo hiệu quả học thực tế; chưa thử với người học.
