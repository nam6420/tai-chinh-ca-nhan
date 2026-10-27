# Biên bản kiểm duyệt: Bài V2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 09:46 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 09:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Biên độ, bước giá, phiên, lệnh, lô, T+2 và phép tính.
- Báo cáo đích: `learning/lessons/V2-vietnam-trading-rules.md`
- SHA-256 nội dung đích: `a646be11cd89bb6ca7e899ba9123fdb4d4281f67caebb243903a0c7419237a3e`
- Kết luận: `CHƯA_BIẾT`
- Lỗi nghiêm trọng chưa xử lý: `1`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [VNX — danh mục quy chế](https://vnx.vn/vi/van-ban-phap-ly/6) | QĐ 22 hiệu lực 16/03/2026, QĐ 23 hiệu lực 18/03/2026 | 2026-10-27 | Phiên bản và ngày hiệu lực |
| [VNX — QĐ 22/2026](https://stream.vnx.vn/VNX//Legal/2026031816145088VNX.Quy-che-niem-yet_QD22.pdf); [QĐ 23/2026](https://stream.vnx.vn/VNX//Legal/20260324164637497VNX.-Quy-che-CK-CNY_QD23....pdf) | 16 và 18/03/2026 | 2026-10-27 | Đối chiếu ảnh trang gốc làm tròn và thông số UPCoM |
| [HOSE — hướng dẫn T2.2026](https://staticfile.hsx.vn/Uploads/UploadDocuments/2453338/HTGD_Quy%20dinh%20can%20biet%20khi%20GDCK%20tren%20HOSE_T2.2026.pdf) | Nhãn T2.2026; ngày phát hành chưa rõ | 2026-10-27 | Đọc PDF do điều phối viên tải bằng `pdftotext` |
| [HOSE — các loại lệnh](https://staticfile.hsx.vn/Uploads/UploadDocuments/2372203/6.Cac%20loai%20lenh%20.pdf); [HOSE — quy định giao dịch](https://staticfile.hsx.vn/Uploads/News/437a3bc734a845fc853283b0c627a593/20250429_20250429%20-%20HOSE%20-%20Quy%20dinh%20giao%20dich%20dang%20website%20HOSE.pdf) | 2025 | 2026-10-27 | Các loại lệnh và ưu tiên |
| [VNX — lịch chuyển sàn](https://vnx.vn/vi/thong-tin-tu-sgdck/VNX_QLHD/10005424) | 30/09/2026 | 2026-10-27 | Lịch và phạm vi chuyển giao |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Cao | Thông số HOSE hiện hành | PDF HOSE mang nhãn T2.2026 dẫn QĐ 22 năm 2025; VNX liệt kê QĐ 22 năm 2026 thay thế. PDF không ghi rõ ngày phát hành; chưa đủ chứng minh toàn bộ thông số vẫn hiện hành | PDF HOSE, danh mục VNX | Đối chiếu văn bản/thông báo HOSE sau QĐ 22/2026; xác minh ngày tài liệu | Chưa xử lý |
| Trung bình | Làm tròn, UPCoM | Ảnh QĐ22 xác nhận hướng làm tròn; QĐ23 xác nhận UPCoM 100 đồng, ±15% thường và ±40% trường hợp đặc biệt | Ảnh trang gốc | Giữ điều kiện và kiểm trường hợp giá chuyển vùng bước giá | Một phần đạt; vùng bước giá chưa biết |
| Trung bình | HNX, T+2 | HNX FAQ và VSDC chưa mở trực tiếp được; HOSE có sơ đồ nhận chứng khoán chiều T+2 trong hướng dẫn cũ | Hướng dẫn HOSE; giới hạn truy cập | Đối chiếu nguồn HNX/VSDC hiện hành | Chưa biết |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Các phép tính giá đúng theo đầu vào, kể cả 48.639 làm tròn lên 48.650 nếu giả định bước 50 đồng; giả định này chưa được xác nhận là quy tắc khi giá chuyển vùng.

## Hạn chế của lần kiểm duyệt

Chưa kiểm đầy đủ phụ lục QĐ22/2026, thông báo HOSE cập nhật, quy tắc HNX và lịch VSDC hiện hành. PDF HOSE đọc được bằng `pdftotext`, nhưng ngày và căn cứ phiên bản không rõ.

## Kết luận của agent kiểm duyệt

`CHƯA_BIẾT`, với một lỗi nghiêm trọng chưa xử lý về căn cứ hiệu lực của thông số HOSE. Không thể coi phép tính đúng là xác nhận quy tắc hiện hành.
