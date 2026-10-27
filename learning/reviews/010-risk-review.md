# Biên bản phản biện rủi ro — Bài 010

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-26 17:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 17:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; kiểm giả định, trường hợp công thức không còn đúng, giới hạn quốc gia/ngành, điều kiện bác bỏ và nguy cơ hiểu thành lời khuyên cá nhân; tự tìm nguồn phản chứng.`
- Báo cáo đích: `learning/lessons/010-cost-of-capital.md`
- SHA-256 nội dung đích: `dd420c92058815cc9820994fcf999b8aba467b62fea8543e125f9588d0b43614`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Damodaran — Definitions](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/definitions.html) | NYU, Hoa Kỳ; tài liệu phương pháp, ngày phiên bản CHƯA_BIẾT | 2026-10-26 | Phản chứng và giới hạn áp dụng |
| [Damodaran — Cost of Capital (US)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html) | Tháng1/2026; mẫu ngành Hoa Kỳ; không dùng số làm ví dụ | 2026-10-26 | Phản chứng và giới hạn áp dụng |

## Phát hiện và kiểm tra

CAPM9%, WACC7,425%, không dùng lá chắn thuế7,8%, độ nhạy8,825% khớp; trọng số thị trường và tiền tệ được giới hạn.

Các phát hiện cần sửa đã được xử lý và nhánh kiểm xác nhận lại đúng mã băm trên; giữ nhận định ĐẠT trong phạm vi đã giao. Phép tính theo đầu vào bài không chứng minh dự báo thị trường.

## Hạn chế của lần kiểm duyệt

Không kiểm duyệt toàn bộ giáo trình cũ, không đo hiệu quả học thực tế, không xác nhận thuế/phí hiện hành ngoài phạm vi bài.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản này lưu kết quả kiểm, không tự chứng minh hiệu quả học tập hay cho phép đặt lệnh.

