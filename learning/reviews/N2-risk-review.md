# Biên bản phản biện rủi ro — Bài N2

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-26, trong khoảng 18:30–18:33 UTC+7 (Asia/Ho_Chi_Minh) — nhánh không có đồng hồ; điều phối viên ghi khoảng theo giờ hệ thống`
- Chốt dữ liệu lúc: `2026-10-26 18:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Ba vòng phản biện độc lập; vòng cuối xác nhận N2-1 đến N2-5 đã đóng và không có lỗi mới; mở lại R7 của Apple.`
- Báo cáo đích: `learning/lessons/N2-statement-line-items.md`
- SHA-256 nội dung đích: `a9d024fae64699e528754507fd58ac966757acd79fdb5b18fba526f554fa218a`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên (phiên Claude Code), chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Apple 10-K FY2025 — R7](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R7.htm), [R5](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R5.htm) | FY2025; triệu USD | 2026-10-26 | Bảng thay đổi vốn chủ, bảng cân đối |
| [McDonald's 10-K FY2024 — R7](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R7.htm) / [R3](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R3.htm) | 2024; USD; nguồn gốc | 2026-10-26 | Phản ví dụ ROE vốn chủ âm |
| [VNM — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) | 27/02/2026; đồng; TT 202; KPMG chấp nhận toàn phần; PDF quét | 2026-10-26 | Phản chứng EPS và quỹ khen thưởng, phúc lợi |
| [BIS — Basel III leverage ratio](https://www.bis.org/press/p140112a.htm) | 12/01/2014 | 2026-10-26 | Phạm vi ngân hàng |

## Phát hiện và kiểm tra

- Vòng 1: **ĐẠT CÓ ĐIỀU KIỆN** — 6 điểm cần sửa (đòn bẩy → hệ số nhân vốn chủ và nợ không chịu lãi; ROE vô nghĩa khi vốn chủ âm; phạm vi phi tài chính; ROE tập đoàn; EPS Việt Nam; mã 30 không phải EBIT) cùng 3 điểm nhẹ. Đã sửa.
- Vòng 2: **ĐẠT** — còn N2-1 (EPS VNM nâng lên `SỰ_THẬT`) và 4 điểm thấp. Đã sửa.
- Vòng cuối (bản trên): N2-1 đến N2-5 đã đóng; không có lỗi nội dung mới.

## Ghi chú mở (thấp, không chặn)

- N2-6: bảng nguồn mục 13 chưa có dòng cho báo cáo VNM 2025 (dẫn ở dòng EPS); giờ chốt dòng 4 chưa ghi lần bổ sung dữ kiện VNM/R7.

- Xác nhận sau cùng: nhánh phản biện đọc lại các dòng sửa trên mã băm này và giữ kết luận ĐẠT; các ghi chú thấp ở mục trên đã đóng (riêng N3-8 về lộ trình: đã đồng bộ `learning/roadmap.md` §5.1 với `learning/README.md`).

## Hạn chế của lần kiểm duyệt

Nhánh không có Bash nên không tự kiểm mã băm (mã băm do điều phối viên cung cấp, khớp `shasum -a 256` lúc 18:33). Không đo hiệu quả học thực tế.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản không chứng minh hiệu quả học tập và không cho phép đặt lệnh.
