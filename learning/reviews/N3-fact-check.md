# Biên bản kiểm nguồn — Bài N3

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-26 18:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 18:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Ba vòng kiểm độc lập; vòng cuối xác nhận phần B (thời điểm áp dụng mẫu, phân loại lại, mã mới, công thức mã 30, EBIT cốt lõi, lợi thế thương mại, EPS, cột 2024, B03 mã 27/36, IAS 7.34A(b)), phần A bổ sung, giờ chốt; tái tính toàn bộ.`
- Báo cáo đích: `learning/lessons/N3-vietnam-vas-statements.md`
- SHA-256 nội dung đích: `4a9358fa88191689ec2062d7ef957f6a2333f149175f36b95ecc41431197409a`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên (phiên Claude Code), chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [VNM — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) | 27/02/2026; đồng; TT 202; KPMG chấp nhận toàn phần; PDF quét | 2026-10-26 | B01/B02/B03 2025–2024; thuyết minh VI.3, VI.11 |
| [VNM — BCTC hợp nhất soát xét Q1/2026](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf) | 29/04/2026; mẫu TT 43 | 2026-10-26 | Cột 1/1/2026 phân loại lại; mã mới; phân bổ lợi thế thương mại |
| [VNM — BCTC hợp nhất soát xét Q2/2026](https://d8um25gjecm9v.cloudfront.net/cms/20260730_VNM_BCTC_da_soat_xet_Q2_2026_Hop_nhat_76ef2e29c1.pdf) | 30/07/2026; mẫu TT 43 | 2026-10-26 | Mã 279/280/313/321 |
| [LuatVietnam — TT 43/2026/TT-BTC](https://luatvietnam.vn/tai-chinh/thong-tu-43-2026-tt-btc-sua-doi-bao-cao-tai-chinh-hop-nhat-hieu-luc-20-04-2026-432924-d1.html) | 20/04/2026; bản sao trên trang thứ ba | 2026-10-26 | Hiệu lực, phạm vi, công thức mã 30 |
| [BDO — IFR Bulletin 2026/05](https://www.bdo.global/getmedia/d27359ee-5875-45ff-9d36-18b8aa59c8fd/IFRB_2026_05.pdf?ext=.pdf) | 08/2026; nguồn thứ cấp | 2026-10-26 | IAS 7.34A |
| [AASB — IAS 7/AASB 107, Interest and dividends](https://standards.aasb.gov.au/node/6600) | Bản quốc gia của văn bản IASB, đã sửa theo AASB 18 | 2026-10-26 | Nguyên văn 33A, 34A(a)(b), 34B |

## Phát hiện và kiểm tra

- Vòng 1 (bản `fbdb98b8…`): **ĐẠT CÓ ĐIỀU KIỆN** — 5 lỗi cần sửa (công thức mã 30 thiếu `+21`; nguồn mã 21; chữ "chỉ" ở Điều 24.6; thiếu bẫy mã 150/tài sản sinh học; khẳng định quý I/2026 dùng TT 43). Đã sửa.
- Vòng 2 (bản `2ae1ee21…`): **KHÔNG_ĐẠT** — mốc giờ bổ sung ở tương lai. Đã sửa.
- Vòng cuối (bản trên): mọi mã cũ/mới khớp báo cáo VNM; số VNM 2025/2024 khớp đến từng đồng sau làm tròn; tiền ròng 14.229,2 tính từ số đồng gốc (14.229,186); EPS 4.028 sau trừ quỹ 992,8 tỷ khớp VI.11; IAS 7.34A(b) khớp nguyên văn AASB.

- Xác nhận sau cùng (18:35): bản trên chỉ khác bản đã kiểm ở dòng mốc chốt (gộp thành một giá trị), hai dòng trạng thái vòng đời và các ghi chú thấp (thêm dòng nguồn; ghi chú làm tròn; cột 2024 B03 mã 36 = (8.159,6) khớp trang 12 báo cáo VNM 2025; tách câu ghi chú). Nhánh kiểm chạy `--print-hash` khớp mã băm trên.

## Hạn chế của lần kiểm duyệt

Văn bản gốc TT 43 (Công báo) và phụ lục mẫu biểu TT 99 chưa mở được; công thức mã 30 lấy từ bản sao LuatVietnam. PDF VNM là bản quét, đọc bằng ảnh trang (mọi tổng kiểm khớp đến từng đồng). Không kiểm lại ở vòng cuối: KPMG VN, MISA, Tạp chí Kinh tế – Tài chính, QĐ 345, Thời báo Tài chính, Tạp chí Quản lý Nhà nước.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản không chứng minh hiệu quả học tập và không cho phép đặt lệnh.
