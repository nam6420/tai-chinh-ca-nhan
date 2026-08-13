# Quy trình nghiên cứu

```text
Câu hỏi -> Đề bài nghiên cứu -> Các nhánh bằng chứng song song -> Bản tổng hợp nháp
        -> Kiểm nguồn + Phản biện rủi ro -> Khắc phục -> Bản tổng hợp cuối
        -> Nhật ký học tập/quyết định
```

## 1. Đề bài nghiên cứu

Agent điều phối xác định câu hỏi, mục tiêu học, phạm vi toàn cầu, thời điểm chốt dữ liệu, nguồn ưu tiên, tài liệu đầu ra và tiêu chí hoàn thành. Nếu chưa rõ mã chứng khoán, thị trường hoặc mục tiêu, phải làm rõ trước khi thu thập dữ liệu lớn.

## 2. Các nhánh bằng chứng

Chỉ chạy song song các phần độc lập. Mỗi agent phải tự tìm kiếm Internet trong lượt hiện tại và mở trang nguồn thực tế. Mỗi nhánh trả gói bằng chứng có URL, ngày xuất bản/kỳ dữ liệu/ngày truy cập; không cùng sửa báo cáo.

## 3. Bản tổng hợp nháp

Agent điều phối tổng hợp bằng chứng thành đúng tài liệu sẽ được xuất bản và giữ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT`. Tạo sẵn liên kết tới sổ nguồn và hai biên bản kiểm duyệt. Mọi thay đổi nội dung trọng yếu sau đó đều làm kiểm duyệt cũ hết hiệu lực.

## 4. Kiểm tra nguồn và số liệu

Agent kiểm nguồn phải mở lại nguồn trên Internet, xác minh nhận định trọng yếu, kỳ, đơn vị và phép tính. `KHÔNG_ĐẠT` hoặc `CHƯA_BIẾT` phải được sửa hoặc giữ rõ trong báo cáo; không được âm thầm lấp bằng giả định.

## 5. Phản biện rủi ro

Agent phản biện phải tự tìm nguồn trái chiều trên Internet, kiểm tra giả định ẩn và điều kiện làm luận điểm mất hiệu lực. Agent điều phối phải giữ lại bất đồng chưa giải quyết.

Hai bước kiểm nguồn và phản biện có thể chạy song song trên **cùng một bản nháp đã cố định**. Mỗi agent dùng [biên bản kiểm duyệt](../templates/review-record.md), ghi đường dẫn báo cáo tính từ gốc repo, thời điểm chốt dữ liệu, mã băm nội dung đích, thời gian, phạm vi, kết luận và số lỗi nghiêm trọng chưa xử lý.

## 6. Khắc phục và bản tổng hợp cuối

Nếu khắc phục làm thay đổi nội dung trọng yếu, tạo mã băm mới và kiểm duyệt lại. Chỉ bỏ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT` khi cả hai biên bản đều `ĐẠT`, cùng trỏ tới mã băm hiện tại và không có lỗi nghiêm trọng chưa xử lý. Kiểm tra bằng:

```bash
python3 scripts/validate_report.py duong-dan/bao-cao.md \
  --fact-check duong-dan/kiem-nguon.md \
  --bear-review duong-dan/phan-bien-rui-ro.md
```

## 7. Nhật ký học tập

Ghi điều đã học, điều đã sai, dữ kiện cần theo dõi và điều gì sẽ thay đổi quan điểm. Danh sách theo dõi chỉ là hàng đợi nghiên cứu, không phải danh sách khuyến nghị.
