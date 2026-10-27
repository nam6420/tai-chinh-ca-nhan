# Biên bản kiểm nguồn — Bài 010

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-26 17:05 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 17:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; tìm kiếm/mở nguồn trọng yếu; tái tính ví dụ và toàn bộ đáp án; kiểm kỳ, đơn vị, phạm vi và giới hạn nguồn.`
- Báo cáo đích: `learning/lessons/010-cost-of-capital.md`
- SHA-256 nội dung đích: `dd420c92058815cc9820994fcf999b8aba467b62fea8543e125f9588d0b43614`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Damodaran — Definitions](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/definitions.html) | NYU, Hoa Kỳ; tài liệu phương pháp, ngày phiên bản CHƯA_BIẾT | 2026-10-26 | Đối chiếu nhận định và dữ liệu |
| [Damodaran — Cost of Capital (US)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html) | Tháng1/2026; mẫu ngành Hoa Kỳ; không dùng số làm ví dụ | 2026-10-26 | Đối chiếu nhận định và dữ liệu |

## Phát hiện và kiểm tra

CAPM9%, WACC7,425%, không dùng lá chắn thuế7,8%, độ nhạy8,825% khớp; trọng số thị trường và tiền tệ được giới hạn.

Các phát hiện cần sửa đã được xử lý và nhánh kiểm xác nhận lại đúng mã băm trên; giữ nhận định ĐẠT trong phạm vi đã giao. Phép tính theo đầu vào bài không chứng minh dự báo thị trường.

## Hạn chế của lần kiểm duyệt

Không kiểm duyệt toàn bộ giáo trình cũ, không đo hiệu quả học thực tế, không xác nhận thuế/phí hiện hành ngoài phạm vi bài.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản này lưu kết quả kiểm, không tự chứng minh hiệu quả học tập hay cho phép đặt lệnh.

