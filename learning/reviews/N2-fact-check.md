# Biên bản kiểm nguồn — Bài N2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-26 18:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 18:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Ba vòng kiểm độc lập; vòng cuối xác nhận phần sửa (EPS VNM, đối chiếu vốn chủ Apple, IAS 7.34A, McDonald's, giờ chốt) và tái tính toàn bộ phép tính.`
- Báo cáo đích: `learning/lessons/N2-statement-line-items.md`
- SHA-256 nội dung đích: `a9d024fae64699e528754507fd58ac966757acd79fdb5b18fba526f554fa218a`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên (phiên Claude Code), chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Apple 10-K FY2025 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | FY kết thúc 27/09/2025; triệu USD; US GAAP; nguồn gốc | 2026-10-26 | Bảng thay đổi vốn chủ, lưu chuyển tiền tệ, bảng cân đối |
| [McDonald's 10-K FY2024 — R7](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R7.htm) / [R3](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R3.htm) | 2024; USD; nguồn gốc | 2026-10-26 | Vốn chủ âm, lợi nhuận ròng |
| [VNM — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) | 27/02/2026; đồng; TT 202; KPMG chấp nhận toàn phần; PDF quét | 2026-10-26 | EPS và quỹ khen thưởng, phúc lợi (VI.11) |
| [KPMG — IFRS 18 changes to the statement of cash flows](https://kpmg.com/us/en/articles/2026/ifrs-18-changes-statement-cash-flows.html) | 01/06/2026; nguồn thứ cấp | 2026-10-26 | Đáp án Bài 6 |
| [BDO — IFR Bulletin 2026/05](https://www.bdo.global/getmedia/d27359ee-5875-45ff-9d36-18b8aa59c8fd/IFRB_2026_05.pdf?ext=.pdf) | 08/2026; nguồn thứ cấp | 2026-10-26 | IAS 7.34A |

## Phát hiện và kiểm tra

- Vòng 1 (bản `a2aec207…`): **KHÔNG_ĐẠT** — câu Apple ghi mua lại + cổ tức "lớn hơn" lợi nhuận (thực tế 105.465 < 112.010). Đã sửa.
- Vòng 2 (bản `c4056833…`): **KHÔNG_ĐẠT** — mốc giờ chốt ở tương lai. Đã sửa bằng giờ hệ thống.
- Vòng cuối (bản trên): mọi nhận định `SỰ_THẬT` khớp nguồn; đối chiếu vốn chủ Apple `56.950 + 112.010 + 1.601 + 13.246 + 1.498 − 4.452 − 1.655 − 90.052 − 15.413 = 73.733` khớp từng dòng 10-K; EPS VNM 4.027,5 → 4.028 và 4.502,6 → 4.503 khớp thuyết minh VI.11; toàn bộ phép tính quán cà phê, Apple, Bài 1–6 tái tính không lệch.

- Xác nhận sau cùng (18:35): bản trên chỉ khác bản đã kiểm ở dòng mốc chốt (gộp thành một giá trị), hai dòng trạng thái vòng đời và các ghi chú thấp (thêm dòng nguồn; ghi chú làm tròn; cột 2024 B03 mã 36 = (8.159,6) khớp trang 12 báo cáo VNM 2025; tách câu ghi chú). Nhánh kiểm chạy `--print-hash` khớp mã băm trên.

## Hạn chế của lần kiểm duyệt

Không kiểm lại ở vòng cuối các nguồn đã đạt ở vòng trước (SEC Beginners' Guide, ACCA, Damodaran, thư KBR, khoản thuế 10,2 tỷ USD). Trang C&DI 103.01 gốc trả HTTP 404; bài giữ `CHƯA_BIẾT`.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản không chứng minh hiệu quả học tập và không cho phép đặt lệnh.
