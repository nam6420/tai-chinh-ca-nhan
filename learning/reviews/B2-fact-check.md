# Biên bản kiểm duyệt: Bài B2 — Margin và đòn bẩy

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:10 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-27 11:07 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Khái niệm và rủi ro margin; quy định Việt Nam, biểu phí VFS và toàn bộ phép tính.
- Báo cáo đích: `learning/lessons/B2-margin-leverage.md`
- SHA-256 nội dung đích: `42338ff511e4fd58b8c14b94c71fc2537c9fdf7f094ed9d7ecb223292712ae4a`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [FINRA — Margin Debt](https://syndication.finra.org/content/margin-debt-record-levels-know-risks) | 18/01/2018; Hoa Kỳ | 27/10/2026 | Khoản vay và rủi ro |
| [SEC — Understanding Margin Accounts](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-29) | 10/06/2021; Hoa Kỳ | 27/10/2026 | Lỗ, gọi bổ sung, bán tài sản |
| [VFS — biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi) | Không ghi ngày hiệu lực chung | 27/10/2026 | Lãi ký quỹ tham khảo |
| [Công báo — Thông tư 120 và sửa đổi](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/29/469538-1779683486_v1_1780016834_signed.pdf) | 29/05/2026; sửa đổi đến TT08/2026 | 27/10/2026 | Điều 9, hợp đồng và xử lý tài sản |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Margin và rủi ro | Nợ, lãi, gọi bổ sung và nguy cơ bán tài sản được trình bày có giới hạn Hoa Kỳ/Việt Nam. | FINRA, SEC và Điều 9 TT120 | Không cần | Đã kiểm |
| Thấp | Tên tài liệu | Tên đầy đủ là 08/VBHN-BTC, hợp nhất TT120; văn bản hợp nhất không thay thế văn bản gốc. | Công báo 29/05/2026 | Kiểm văn bản gốc khi áp dụng pháp luật. | Còn lưu ý |
| Thấp | Biểu VFS | Hai trang VFS nêu 13,5% và 12,5%, chưa rõ ngày từng mức; bài dùng giả định, không là báo giá. | Biểu phí và điều khoản VFS | Đối chiếu hợp đồng và thời điểm khi áp dụng. | Đã giới hạn |
| Không có lỗi | Lãi và ngưỡng | 13,5% là giả định; VFS công bố mức cho kỳ hạn 90 ngày. Bài không suy thành mức chung; ngưỡng phụ thuộc hợp đồng. | VFS và TT120 | Kiểm hợp đồng cụ thể | Đã kiểm |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Vị thế 200 triệu/vốn 100 triệu = 2 lần; giá trị còn 160 triệu với nợ 100 triệu cho vốn ròng 60 triệu, lỗ 40%. Giải (V − 100)/V = 0,30 được V ≈ 142,86 triệu. Lãi 100 triệu × 13,5% × 30/365 ≈ 1.109.589 đồng; 80 triệu × 12% × 45/365 ≈ 1.183.562 đồng. Vị thế 160 triệu giảm 25%, nợ 80 triệu, vốn ròng 40 triệu, lỗ 50%.

## Hạn chế của lần kiểm duyệt

VFS không nêu ngày hiệu lực tổng quát; [điều khoản ký quỹ VFS](https://www.vfs.com.vn/ho-tro/dieu-khoan-va-dieu-kien-giao-dich-ky-quy) có mức lãi khác biểu phí. Tên văn bản hợp nhất là 08/VBHN-BTC; bản hợp nhất không thay thế văn bản gốc. Không xác minh hợp đồng cá nhân hoặc danh sách mã từng ngày; bài giữ các điểm này là `CHƯA_BIẾT`.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
