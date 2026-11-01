# Biên bản kiểm duyệt: Bài B2 — Margin và đòn bẩy

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 11:08 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:07 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài, phép tính và Điều 9 Thông tư 120 trong văn bản trích xuất đã lưu.
- Báo cáo đích: `learning/lessons/B2-margin-leverage.md`
- SHA-256 nội dung đích: `42338ff511e4fd58b8c14b94c71fc2537c9fdf7f094ed9d7ecb223292712ae4a`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Công báo — hợp nhất TT120](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/29/469538-1779683486_v1_1780016834_signed.pdf) | 29/05/2026; sửa đổi đến TT08/2026 | 27/10/2026 | Điều 9; đọc bản trích xuất đã lưu do web không tải trực tiếp được |
| [FINRA — Margin](https://www.finra.org/investors/alerts/investing-borrowed-funds-no-margin-error) | Hoa Kỳ; mốc 04/06/2026 | 27/10/2026 | Rủi ro vay và sự khác biệt pháp lý |
| [VFS — biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi) | Không ghi ngày hiệu lực chung | 27/10/2026 | Lãi của một công ty |
| [PHS — lãi ký quỹ](https://www.phs.vn/san-pham-dich-vu/lai-suat-giao-dich-ky-quy-chung-khoan-co-so/61) | Không ghi ngày hiệu lực chung | 27/10/2026 | Cơ sở tính ngày |
| [HOSE — chứng khoán không đủ điều kiện](https://staticfile.hsx.vn/Uploads/UploadDocuments/2489777/20260817%20-%20Danh%20sach%20bo%20sung%20khong%20duoc%20giao%20dich%20ky%20quy-MCP-NHA-SMA.pdf) | 17/08/2026 | 27/10/2026 | Danh sách thay đổi theo kỳ |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Thấp | Gọi bổ sung và xử lý tài sản | Bản mới bổ sung đúng quy định Việt Nam về hợp đồng, gọi và xử lý; giảm nguy cơ áp nguyên quy tắc Hoa Kỳ. | Điều 9 TT120 | Giữ phân biệt luật và hợp đồng. | Đã xử lý |
| Thấp | Mức nền pháp lý | Chưa kiểm toàn văn quy chế 87/QĐ-UBCK, không thể chốt mức nền và ngoại lệ. Bài giữ `CHƯA_BIẾT` về công ty/mã cụ thể. | TT120, HOSE | Kiểm quy chế và danh sách hiện hành trước khi nêu con số chung. | Còn mở |
| Thấp | Cơ sở tính lãi | Ví dụ giả định 365 ngày; PHS công bố cơ sở 360 ngày. | PHS | Dùng cơ sở tính trong hợp đồng thực tế. | Đã giới hạn |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

200 − 100 = 100 triệu vốn; vị thế giảm 20% còn 160 triệu, vốn ròng 60 triệu, lỗ 40%; (V − 100)/V = 30% cho V ≈ 142,86 triệu. Lãi 100 triệu × 13,5% × 30/365 ≈ 1.109.589 đồng; 80 triệu × 12% × 45/365 ≈ 1.183.562 đồng.

## Hạn chế của lần kiểm duyệt

Đối chiếu Điều 9 từ tệp trích xuất do điều phối viên lưu sẵn; web không mở được PDF trực tiếp. Không xác định ngưỡng hoặc thời hạn hợp đồng của khách hàng cụ thể.

## Kết luận của agent kiểm duyệt

`ĐẠT`; điểm pháp lý Việt Nam đã được bổ sung; không có lỗi nghiêm trọng chưa xử lý.
