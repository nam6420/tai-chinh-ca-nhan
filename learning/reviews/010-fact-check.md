# Biên bản kiểm nguồn — Bài 010 (bản viết lại 2026-10-31)

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; số liệu Apple FY2025, phép tính, đáp án, nhãn nhận định, nguồn dẫn; mô hình learning/practice/models/valuation.py. Bốn vòng: vòng 1 trên bản viết lại đầu, các vòng 2–4 trên bản đã sửa; vòng 4 trên bản có mã băm tệp d4f37324, f8101b5a và tương ứng.`
- Báo cáo đích: `learning/lessons/010-cost-of-capital.md`
- SHA-256 nội dung đích: `fe0471055e63f3c2595a4ba43b4474193fc11462e2dd9ee2f1a4c37707f50834`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 31/10/2026; người kiểm không sửa bài. Hai nhánh không đọc kết luận của nhau.

## Kết quả

Số liệu, đáp án và các tỷ lệ (WACC 7,425/7,8/8,825%; βu 0,9455; 8,81% so với 5,99%; Fisher 5,52/9,12/4,91%) tái tính khớp. CAPM dẫn Damodaran val.html (đã mở). Hamada: ví dụ ở trang 4 slide fcff.pdf khớp; công thức tổng quát chưa đối chiếu ngoài ví dụ. Fisher dạng nhân chưa có nguồn chính thức (bài đã ghi CHƯA_BIẾT). Nguyên nhân vốn chủ Apple thấp là SUY_LUẬN.

## Hạn chế

- Giá AAPL ngày 30/10/2026 (344,63) chỉ có từ nguồn thứ cấp stockanalysis.com, chưa đối chiếu sàn.
- Người phản biện không có công cụ tính mã băm; mã băm do điều phối viên tính bằng `scripts/validate_report.py --print-hash`. Sau vòng 4 điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (tách dòng chốt dữ liệu, tách hai dòng trạng thái kiểm duyệt, bỏ nhãn nháp), không đổi nội dung dạy.
- Điểm còn mở mức Thấp: chưa có nguồn mở được cho Fisher dạng nhân, điều kiện quan hệ sạch của RIM, xử lý thiểu số và chi phí trụ sở trong SOTP, chiết khấu tập đoàn 15%; hoàn thuế quan một lần ở biên gộp quý 3 FY2026 chưa nhắc; quyết định pháp lý cụ thể chưa nêu tên.
- Không đo hiệu quả học thực tế; chưa thử với người học.
