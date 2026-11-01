# Biên bản kiểm nguồn — Bài F2 (bản viết lại 2026-10-31)

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; số liệu Apple FY2025, phép tính, đáp án, nhãn nhận định, nguồn dẫn; mô hình learning/practice/models/valuation.py. Bốn vòng: vòng 1 trên bản viết lại đầu, các vòng 2–4 trên bản đã sửa; vòng 4 trên bản có mã băm tệp d4f37324, f8101b5a và tương ứng.`
- Báo cáo đích: `learning/lessons/F2-valuation-ddm-residual-sotp.md`
- SHA-256 nội dung đích: `60b77fa667dbc15da20b6572b12c15c130c58674dc0945f22681a065c429b13e`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 31/10/2026; người kiểm không sửa bài. Hai nhánh không đọc kết luận của nhau.

## Kết quả

Gordon 57,14/66,67/50; hai giai đoạn 54,47; RIM 1.114,56 (và 1.000 khi ROE=ke); SOTP 820/590/11,8; ROE Apple 151,9%/171,4%; chi trả 94,8% tái tính khớp. Gordon dẫn Damodaran ddm.html; RIM dẫn CFA (công thức); SOTP dẫn Wikipedia (định nghĩa). SBC 13.246 (vốn chủ) so với 12.863 (dòng tiền) và 5.960 khớp 10-K. Quan hệ sạch, thiểu số, chi phí trụ sở chưa có nguồn mở được (bài đã ghi CHƯA_BIẾT).

## Hạn chế

- Giá AAPL ngày 30/10/2026 (344,63) chỉ có từ nguồn thứ cấp stockanalysis.com, chưa đối chiếu sàn.
- Người phản biện không có công cụ tính mã băm; mã băm do điều phối viên tính bằng `scripts/validate_report.py --print-hash`. Sau vòng 4 điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (tách dòng chốt dữ liệu, tách hai dòng trạng thái kiểm duyệt, bỏ nhãn nháp), không đổi nội dung dạy.
- Điểm còn mở mức Thấp: chưa có nguồn mở được cho Fisher dạng nhân, điều kiện quan hệ sạch của RIM, xử lý thiểu số và chi phí trụ sở trong SOTP, chiết khấu tập đoàn 15%; hoàn thuế quan một lần ở biên gộp quý 3 FY2026 chưa nhắc; quyết định pháp lý cụ thể chưa nêu tên.
- Không đo hiệu quả học thực tế; chưa thử với người học.
