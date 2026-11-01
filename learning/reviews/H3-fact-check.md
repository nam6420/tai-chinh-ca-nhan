# Biên bản kiểm duyệt: H3 — Biến động, sụt giảm và thanh khoản

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:47 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:39 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài; định nghĩa drawdown, thanh khoản, biến động và phép tính.
- Báo cáo đích: `learning/lessons/H3-risk-volatility-drawdown-liquidity.md`
- SHA-256 nội dung đích: `7dac5d06fd657894c3ce251d78f6b5ecf0ec4e24555f438d766dd927f2271cb4`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Goldberg & Mahmoud — Drawdown](https://arxiv.org/abs/1404.7493) | Nộp 2014, v5 sửa 2016 | 27/10/2026 | Định nghĩa sụt giảm từ đỉnh đến đáy |
| [SEC — Liquidity](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability) | Không ghi ngày; Hoa Kỳ | 27/10/2026 | Khả năng bán và tác động giá |
| [SEC — hồ sơ quỹ](https://www.sec.gov/Archives/edgar/data/875610/000110465907023410/a07-7718_14485bpos.htm) | 2007 | 27/10/2026 | Độ lệch chuẩn và biến động |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Drawdown và thanh khoản | Định nghĩa, giới hạn cửa sổ/tần suất và điều kiện thanh khoản phù hợp nguồn. | ArXiv và SEC | Không cần | Đã kiểm |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

88/110 − 1 = −20%; 110/88 − 1 = +25%; 90/120 − 1 = −25%; 120/90 − 1 ≈ +33,33%.

## Hạn chế của lần kiểm duyệt

Nguồn ArXiv là bản nghiên cứu; chưa xác định trạng thái bình duyệt. Nguồn SEC là Hoa Kỳ; không suy quy định Hoa Kỳ sang Việt Nam.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
