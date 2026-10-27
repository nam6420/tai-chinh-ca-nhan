# Biên bản kiểm duyệt: A1 — Tiền gửi và trái phiếu

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:33 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài; bảo hiểm tiền gửi, rủi ro trái phiếu, nguồn và phép tính.
- Báo cáo đích: `learning/lessons/A1-deposits-government-corporate-bonds.md`
- SHA-256 nội dung đích: `bd4073d72bbd5d624edc6cc565906d829a2d32ba9fc8b7843e57464f41750b9c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [DIV — phạm vi bảo hiểm](https://www.div.gov.vn/bao-hiem-tien-gui-chi-ap-dung-doi-voi-tien-gui-cua-ca-nhan-bang-dong-viet-nam) | 16/06/2026 | 27/10/2026 | Tiền gửi cá nhân VND |
| [DIV — hạn mức 350 triệu](https://www.div.gov.vn/tu-ngay-13-7-2026-han-muc-chi-tra-tien-bao-hiem-cua-bao-hiem-tien-gui-viet-nam-la-350-trieu-dong) | 15/07/2026 | 27/10/2026 | Phạm vi và hạn mức |
| [Chính phủ — cảnh báo trái phiếu](https://xaydungchinhsach.chinhphu.vn/nong-bo-tai-chinh-khuyen-cao-cac-chu-the-tham-gia-thi-truong-trai-phieu-doanh-nghiep-119221114165946867.htm) | 17/11/2022 | 27/10/2026 | Tổ chức phát hành và bên phân phối |
| [SEC — Bonds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds) | Không ghi ngày; Hoa Kỳ | 27/10/2026 | Khái niệm, rủi ro |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Thấp | Ngày nguồn trái phiếu | Ngày đăng đã được sửa từ 14 thành 17/11/2022; hai nhánh xác nhận lại trên hash hiện tại. | Trang Chính phủ | Không cần sửa thêm. | Đã xử lý |
| Không có lỗi | Phạm vi bảo hiểm | Mức 350 triệu tính gộp gốc và lãi thuộc diện bảo hiểm theo người tại một tổ chức. | DIV | Đối chiếu điều kiện cụ thể. | Đã kiểm |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

100 triệu × 5% = 5 triệu; 10,5/1,06 ≈ 9,906 triệu; 10,5/1,04 ≈ 10,096 triệu; 20 triệu × 4,5% × 9/12 = 675.000; 21,2/1,08 ≈ 19,63 triệu.

## Hạn chế của lần kiểm duyệt

Không xác định điều khoản trái phiếu, tài khoản hay ngân hàng cụ thể; nguồn SEC giới hạn ở Hoa Kỳ. Bài giữ thông tin chưa kiểm là `CHƯA_BIẾT`.

## Kết luận của agent kiểm duyệt

`ĐẠT` trên bản hiện tại; không có lỗi nghiêm trọng chưa xử lý.
