# Biên bản kiểm duyệt: Bài V2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 10:24 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 10:23 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Biên độ, bước giá, phiên, lệnh, lô, T+2 và phép tính.
- Báo cáo đích: `learning/lessons/V2-vietnam-trading-rules.md`
- SHA-256 nội dung đích: `f7e01717e1a8acae0413ad8f076d21d0b876a73a31c4a68d2c8419eb7523ec8c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [VNX — danh mục quy chế](https://vnx.vn/vi/van-ban-phap-ly/6) | QĐ 22 hiệu lực 16/03/2026, QĐ 23 hiệu lực 18/03/2026 | 2026-10-27 | Phiên bản và ngày hiệu lực |
| [VNX — Phụ lục III QĐ22](https://stream.vnx.vn/VNX//Legal/20260318161451415VNX.-PL-Quy-che-niem-yet_QD22.pdf) | 16/03/2026 | 2026-10-27 | Ảnh gốc: bước giá, biên độ, giờ phiên HOSE/HNX |
| [VNX — QĐ 22/2026](https://stream.vnx.vn/VNX//Legal/2026031816145088VNX.Quy-che-niem-yet_QD22.pdf); [QĐ 23/2026](https://stream.vnx.vn/VNX//Legal/20260324164637497VNX.-Quy-che-CK-CNY_QD23....pdf) | 16 và 18/03/2026 | 2026-10-27 | Đối chiếu ảnh trang gốc làm tròn và thông số UPCoM |
| [HOSE — hướng dẫn T2.2026](https://staticfile.hsx.vn/Uploads/UploadDocuments/2453338/HTGD_Quy%20dinh%20can%20biet%20khi%20GDCK%20tren%20HOSE_T2.2026.pdf) | Nhãn T2.2026; ngày phát hành chưa rõ | 2026-10-27 | Đọc PDF do điều phối viên tải bằng `pdftotext` |
| [HOSE — các loại lệnh](https://staticfile.hsx.vn/Uploads/UploadDocuments/2372203/6.Cac%20loai%20lenh%20.pdf); [HOSE — quy định giao dịch](https://staticfile.hsx.vn/Uploads/News/437a3bc734a845fc853283b0c627a593/20250429_20250429%20-%20HOSE%20-%20Quy%20dinh%20giao%20dich%20dang%20website%20HOSE.pdf) | 2025 | 2026-10-27 | Các loại lệnh và ưu tiên |
| [VNX — lịch chuyển sàn](https://vnx.vn/vi/thong-tin-tu-sgdck/VNX_QLHD/10005424) | 30/09/2026 | 2026-10-27 | Lịch và phạm vi chuyển giao |
| [VSDC — Bù trừ và thanh toán](https://vsdc.vn/vi/sd/XAz40d2Q-9j569TvBgLQaQ) | Không thấy ngày cập nhật | 2026-10-27 | Chu kỳ cổ phiếu T+2 |
| [Báo Pháp luật — HBS](https://doanhnhan.baophapluat.vn/chung-khoan-hoa-binh-hbs-bi-dinh-chi-mot-phan-hoat-dong-giao-dich-89201.html) | 26/11/2025; thứ cấp | 2026-10-27 | Ví dụ lịch sử hạn chế cổ phiếu HBS |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Đã xử lý | Thông số HOSE/HNX | Ảnh Phụ lục III QĐ22/2026 xác nhận bước giá, biên độ, giờ và lô của các sở | Phụ lục gốc VNX | Giữ mốc và phạm vi | ĐẠT |
| Đã xử lý | Làm tròn, UPCoM, lệnh | Ảnh QĐ22/23 xác nhận nguyên tắc, thông số UPCoM, giá tham chiếu và loại lệnh | Ảnh trang gốc | Giữ câu hỏi chuyển vùng là CHƯA_BIẾT | ĐẠT cho nội dung đã kiểm |
| Đã xử lý | Chu kỳ T+2 | Trang dịch vụ VSDC xác nhận T+2 cho cổ phiếu; giờ khả dụng vẫn chưa biết | VSDC | Không suy ra thời điểm ghi có | ĐẠT về chu kỳ |
| Đã xử lý | Ví dụ HBS | Bản mới giới hạn sự kiện là lịch sử, không suy trạng thái hiện hành | Báo Pháp luật; bản nháp | Kiểm thông báo mới theo mã khi dùng | ĐẠT |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Các phép tính giá và ngày khớp đầu vào. Ví dụ chuyển vùng đã được thay bằng giá 60.000 đồng với trần 64.200 và sàn 55.800, cùng vùng bước giá 100 đồng; quy tắc chuyển vùng giữ `CHƯA_BIẾT`.

## Hạn chế của lần kiểm duyệt

Đã đối chiếu ảnh các trang gốc QĐ22/23 và Phụ lục III; chưa xác minh giờ cổ phiếu khả dụng, T+0, xử lý lệnh sai bước, điều kiện từng mã, ngoại lệ tiền/margin và bước giá khi chuyển vùng. Bài giữ các điểm đó ở trạng thái `CHƯA_BIẾT`.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi các nhận định đang khẳng định; các khoảng trống vẫn `CHƯA_BIẾT` và không dùng làm đáp án.
