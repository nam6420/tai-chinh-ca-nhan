# Tiêu chuẩn nghiên cứu

## Bắt buộc tìm kiếm trực tuyến

Mọi định nghĩa, dữ kiện, số liệu và nhận định phải được nghiên cứu lại trên Internet trong lượt hiện tại. Tài liệu cũ trong repo chỉ là lịch sử, không phải bằng chứng hiện hành. Nếu không thể truy cập mạng, không được xuất bản câu trả lời nội dung như đã xác minh.

## Thứ tự ưu tiên nguồn toàn cầu

1. Công bố doanh nghiệp, báo cáo kiểm toán và trang quan hệ nhà đầu tư gốc.
2. Cơ quan quản lý, sở giao dịch, ngân hàng trung ương và cơ quan thống kê của thị trường liên quan.
3. Tổ chức chính thức quốc tế như IMF, World Bank, OECD, BIS, IOSCO và IFRS Foundation khi phù hợp.
4. Dữ liệu chuyên ngành có phương pháp luận rõ.
5. Báo chí và phân tích bên thứ ba để lấy bối cảnh hoặc góc nhìn phản biện.
6. Mạng xã hội chỉ là đầu mối cần xác minh, không phải bằng chứng cuối.

## Thông tin nguồn bắt buộc

- `Chốt dữ liệu lúc` kèm múi giờ.
- URL trang nguồn đã mở, ngày xuất bản và ngày truy cập.
- Kỳ báo cáo, tiền tệ, đơn vị và lần sửa đổi nếu có.
- Công thức và đầu vào của phép tính.
- Quốc gia, thị trường và chuẩn kế toán liên quan.

## Nhãn phát biểu

- `SỰ_THẬT`: nguồn trực tiếp xác nhận.
- `PHÉP_TÍNH`: kết quả tái lập được từ đầu vào đã dẫn nguồn.
- `SUY_LUẬN`: diễn giải hợp lý nhưng nguồn không nói trực tiếp.
- `KỊCH_BẢN`: giả định có điều kiện, không phải dự báo chắc chắn.
- `Ý_KIẾN`: đánh giá chủ quan, phải ghi rõ tiêu chí.

## Cổng kiểm soát xuất bản

Một báo cáo được coi là đã kiểm duyệt chỉ khi:

- Nhận định trọng yếu có nguồn trực tuyến đã mở trong lượt nghiên cứu.
- Phép tính trọng yếu được tái lập.
- Có kịch bản thuận lợi/cơ sở/bất lợi, rủi ro, bằng chứng trái chiều, điều chưa biết và điều kiện làm luận điểm mất hiệu lực.
- `source_fact_checker` đã mở lại nguồn và xử lý/công khai lỗi nghiêm trọng.
- `risk_bear_reviewer` đã tìm nguồn phản chứng độc lập trên Internet.
- Hai biên bản ghi agent kiểm duyệt, thời gian, phạm vi, mã băm nội dung đích, kết luận và số lỗi nghiêm trọng chưa xử lý; chúng cùng khớp phiên bản báo cáo được xuất bản.
- Báo cáo không chứa lệnh giao dịch, cam kết lợi nhuận hoặc che giấu độ không chắc chắn.

`scripts/validate_report.py` là cổng cấu trúc tối thiểu. Nó không thay thế nhận định của agent kiểm duyệt hoặc chứng minh nguồn là đúng; nó ngăn việc bỏ nhãn bản nháp khi thiếu bằng chứng kiểm duyệt hợp lệ.
