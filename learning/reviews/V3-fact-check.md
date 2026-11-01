# Biên bản kiểm duyệt: Bài V3 — Sự kiện doanh nghiệp và quyền của cổ đông

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:00 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-27 10:53 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài, nhận định, nguồn, ngày và phép tính trọng yếu; xác nhận thay đổi dòng biên bản.
- Báo cáo đích: `learning/lessons/V3-corporate-actions.md`
- SHA-256 nội dung đích: `407eff684ca514e1940c9ff7b1412c3c377f6ea43b00cd5035c13feb04cb6fbc`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [VSDC — ngày hưởng quyền](https://vsdc.vn/vi/ad/195688) | 14/05/2026 | 27/10/2026 | Mốc quyền |
| [VSDC — HCM](https://vsdc.vn/vi/ad/197826) | 07/07/2026 | 27/10/2026 | Tỷ lệ, giá, ngày quyền và cổ tức |
| [VSDC — NSC](https://vsdc.vn/vi/ad1/190893) | 09/01/2026; cổ tức đợt 2 năm 2024 | 27/10/2026 | Tiền và mốc thực hiện |
| [Nghị quyết Vinaseed](https://storage.vinaseed.com.vn/Data/2026/01/06/20260106-nsc-cbtt-nq-hdqt-thong-qua-viec-chi-tra-co-tuc-bang-tien-dot-2-nam-2024-639033287333700115.pdf) | 06/01/2026; cổ tức đợt 2 năm 2024 | 27/10/2026 | Đối chiếu NSC |
| [SEC — Stock Split](https://www.investor.gov/introduction-investing/investing-basics/glossary/stock-split) | Không ghi ngày; giáo dục Hoa Kỳ | 27/10/2026 | Tách cổ phiếu |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | HCM | Ngày 17/07/2026, quyền 4:1 giá 10.000 đồng, cổ tức 400 đồng, thanh toán 12/08 phù hợp. | VSDC HCM | Không cần | Đã xác minh |
| Không có lỗi | NSC | Mức 2.000 đồng, ngày 19/01 và 28/01 khớp hai nguồn; không suy ra từng tài khoản đã nhận. | VSDC và nghị quyết | Không cần | Đã xác minh |
| Không có lỗi | Liên kết biên bản | Chỉ đổi mô tả dòng liên kết; nhận định và thời điểm chốt không đổi. | Bản hiện tại | Không cần | Đã xác nhận |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Đối chiếu: 100.000 − 5.000 = 95.000; 95.000 + 5.000 = 100.000; (4 × 100.000 + 20.000) / 5 = 84.000; 100 × 2.000 = 200.000; 2.000 / 10.000 = 20%; 200 × 1.500 = 300.000; 50.000 − 2.000 = 48.000. Các ví dụ có giả định hoặc giới hạn.

## Hạn chế của lần kiểm duyệt

Chưa kiểm điều kiện pháp lý chi tiết từng dạng phát hành, thuế từng người, giá điều chỉnh chính thức từng mã hoặc ghi có tài khoản cụ thể; bài ghi `CHƯA_BIẾT`.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi kiểm nguồn; không có lỗi nghiêm trọng chưa xử lý.
