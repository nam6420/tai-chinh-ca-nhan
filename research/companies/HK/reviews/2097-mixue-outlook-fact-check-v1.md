# Biên bản kiểm duyệt: MIXUE Group (2097.HK), câu chuyện doanh nghiệp, dòng tiền và triển vọng 3 năm (bản nháp v1)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `source-fact-checker` (lần kiểm 1 của tài liệu này). Giữ nguyên kết luận, mức độ và bằng chứng chính; không thêm nhận định mới. Bản đầy đủ của subagent có thêm bảng đối chiếu từng số trong PDF; các số đó đều khớp, trừ các điểm nêu dưới.

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-25 10:06 +07` (giờ kết thúc; công việc bắt đầu 10:00 +07)
- Chốt dữ liệu lúc: `2026-11-25 10:00 +07`
- Phạm vi: dòng tiền đầu tư/tài chính FY2024–H1 2026 và các phép ròng; FCF, doanh thu, lợi nhuận LTM; giá, biên 52 tuần, vốn hóa, tỷ giá, EV, P/E; công thức Gordon ngược, bảng g hàm ý, ba kịch bản, CAGR (chạy lại bằng `python3 -I`); trích dẫn bài 011, 012, 014, N6; 14 số cũ tái dùng đối chiếu PDF; ngày, kỳ, đơn vị, mã nguồn, sổ nguồn, mã băm. Không kiểm toàn bộ phần đối thủ (chỉ mở lại Luckin).
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-outlook-draft-v1-sha-92b496ae.md`
- SHA-256 nội dung đích: `92b496aecc8b6cd647b8137d4c34318dff36ecc22187b393c393986b21c80136` (agent tự tính lại bằng `validate_report.py --print-hash`, khớp)
- Kết luận: `ĐẠT` (có điều kiện: sửa 4 điểm TRUNG_BÌNH và xử lý các điểm THẤP trước khi bỏ nhãn nháp; giá chưa đối chiếu được với sàn)
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [HKEXnews, báo cáo thường niên 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf) (tải trực tiếp) | 2026-04-23 | 2026-11-25 | SHA-256 `55f7ed40…` trùng bản lưu; đọc lại trang in 107, 114–117, 199 |
| [HKEXnews, báo cáo giữa kỳ 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0923/2026092300280.pdf) (tải trực tiếp) | 2026-09-23 | 2026-11-25 | SHA-256 `0e1ddcd2…` trùng bản lưu; đọc trang in 8, 15–17, 32, 46, 50–54 |
| PDF HKEXnews đã lưu (cổ tức, EGM, quyền thưởng, cáo bạch) | 2025-02 đến 2026-09 | 2026-11-25 | `shasum -a 256 -c SHA256SUMS.txt`: 16/16 tệp OK |
| [Investing.com UK, MIXUE](https://uk.investing.com/equities/mixue) và [lịch sử giá](https://uk.investing.com/equities/mixue-historical-data) | đến 25/11/2026 | 2026-11-25 | Giá 23/11 và 24/11, biên 52 tuần, vốn hóa, P/E |
| [StockAnalysis, 2097](https://stockanalysis.com/quote/hkg/2097/) và [lịch sử](https://stockanalysis.com/quote/hkg/2097/history/) | 25/11/2026 10:43 HKT | 2026-11-25 | Nguồn thứ cấp thứ hai cho giá, EPS |
| [Google Finance, 2097:HKG](https://www.google.com/finance/quote/2097:HKG) | n/a | 2026-11-25 | **Không mở được** (từ chối thiết bị); 158,20 và P/E 9,30 chỉ được xác nhận gián tiếp |
| hkexnews.hk (trang báo giá) | n/a | 2026-11-25 | Không hiển thị dữ liệu; không xác minh giá từ sàn |
| [KrASIA/Nikkei, Mixue shuts more stores](https://kr-asia.com/china-bubble-tea-chain-mixue-shuts-more-stores-as-growth-model-falters) | 2026-11-17 | 2026-11-25 | Giá IPO, đỉnh 618,5, −57%, tỷ giá ước tính, quán Mong Kok |
| [Investing.com, consensus](https://uk.investing.com/equities/mixue-consensus-estimates), [Investing.com, Macquarie](https://ng.investing.com/news/analyst-ratings/macquarie-initiates-coverage-on-mixue-stock-with-underperform-rating-93CH-2093336) | 2025-09-05; 2026-08-31 | 2026-11-25 | Macquarie |
| [SEC, Luckin 6-K](https://www.sec.gov/Archives/edgar/data/0001767582/000110465926121665/tm2628441d1_ex99-1.htm) | 2026-11-03 | 2026-11-25 | Doanh số cùng cửa hàng tự vận hành −11,1% (so với +14,3%) |
| [Mitrade, tỷ giá](https://www.mitrade.com/insights/news/live-news/article-1-2260889-20261118) | không rõ ngày | 2026-11-25 | USD/CNY 6,7118 để so với 0,851 |
| `learning/lessons/011`, `012`, `014`, `N6` | repo | 2026-11-25 | Đối chiếu trích dẫn bài học |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| TRUNG_BÌNH | FCF0 trừ lãi nhận (3,75 tỷ) | Nháp ghi lãi nhận LTM "CHƯA_BIẾT" rồi giả định 0,25 tỷ. Số có trong PDF: lãi nhận trong OCF 135,412 (FY2025, trang in 114), 42,914 (H1 2025), 58,262 (H1 2026). LTM = 150,8 triệu; giả định cao hơn ≈ 99 triệu | FCF trừ lãi nhận thực = 3.845; g hàm ý ở WACC 8/10/12% = −4,4 / −2,6 / −0,85% (thay vì −4,1 / −2,3 / −0,6) | Thay bằng 150,8 triệu `SỰ_THẬT`/`PHÉP_TÍNH`; nêu thêm biến thể sau thuế (≈ 118) hoặc giữ 3,75 làm biên bất lợi | Mở |
| TRUNG_BÌNH | Cổ tức đặc biệt | Câu "đã chi trả ngày 6/11" gắn nhãn `SỰ_THẬT [S10, S11]`; nguồn chỉ nói "dự kiến chi trả" (EGM trang 2; thông báo 27/8); không có nguồn xác nhận đã chi | Hai nơi trong nháp nhất quán khác nhau | Sửa: "được ĐHĐCĐ thông qua 30/9, dự kiến chi trả 6/11; việc đã chi trả `CHƯA_XÁC_MINH`"; nêu cả EV nếu chưa trả (28,7 tỷ), EV đổi 3,4% | Mở |
| TRUNG_BÌNH | Sổ nguồn T9 | Ghi vốn hóa 60,06 tỷ HKD cho Investing.com; trang đó ghi 59,11B (60,06 = 158,20 × 379,6188, thuộc giá 23/11) | 155,70 × 379,6188 = 59.107 | Sửa T9 thành 59,1; chuyển 60,06 sang T10 có chú thích | Mở |
| TRUNG_BÌNH | Tỷ giá 0,851 | 0,851 = 6,68/7,85 là thương số hai ước tính của tác giả bài báo, không phải tỷ giá tham chiếu. HKEXnews có tỷ giá PBoC "HK$1 to RMB0.85954" (EGM trang 3); USD/CNY 6,7118 ÷ 7,85 = 0,855 | Với 0,85954: vốn hóa 50,8 tỷ RMB; EV 30,2 tỷ; g hàm ý (FCF0 4,0/3,75; WACC 8/10/12%) = −4,6/−2,9/−1,1 và −3,9/−2,2/−0,4; chênh ≤ 0,2 điểm % | Dùng tỷ giá tham chiếu đúng ngày 24/11 hoặc ghi dải 0,851–0,860 với độ nhạy | Mở |
| THẤP | Gửi ròng tiền kỳ hạn FY2024 | Ghi +2.930,0; chính xác 2.940,000 − 10,056 = 2.929,9 | Trang in 115 | Sửa +2.929,9 | Mở |
| THẤP | Capex LTM | Công thức chỉ cộng đất H1 2026 (38,4), bỏ đất FY2025 (6,4) rơi vào H2 2025: capex + đất LTM = 713,4; FCF LTM = 3.989,7 (không phải 3.996,0); OCF LTM chính xác 4.813,5 | PDF | Sửa công thức; kết quả vẫn ≈ 4,0 tỷ, g đổi dưới 0,03 điểm % | Mở |
| THẤP | OCF H1 2026 "chủ yếu do phải trả người bán" | Phải trả người bán −1.118,1 so với mức giảm OCF 1.225,6, nhưng tồn kho bù +632,8 (−176,1 so với −808,9) và lợi nhuận trước thuế giảm 492,6 | Giữa kỳ trang in 50–51 | Dùng "một nguyên nhân lớn nhất" và nêu tồn kho bù trừ | Mở |
| THẤP | Trích dẫn trang | OCF thường niên ở trang in 114; nháp ghi "115–116". Số trang PDF = trang in + 1 | pdftotext | Ghi "trang in 114–116" và "trang in 51–53" | Mở |
| THẤP | Macquarie | Khởi đầu độ phủ Underperform xảy ra 2025-09-05 (mục tiêu HK$279); không nằm trong KrASIA. Hiện Macquarie Sell, mục tiêu HK$180 (duy trì 31/08/2026) | Investing | Thêm ngày và nguồn; tách khỏi câu KrASIA | Mở |
| THẤP | Luckin | 6-K gốc: −11,1% so với +14,3%, nguyên nhân khớp. Nayuki, Chagee, Guming, Auntea Jenny chưa tự mở | SEC 6-K | Có thể nâng Luckin lên `SỰ_THẬT [6-K]`; còn lại giữ `CHƯA_XÁC_MINH` | Mở |
| THẤP | Giá 23/11 "giữa phiên" | Investing và StockAnalysis cho 158,20 là **đóng cửa cả ngày 23/11**; Google Finance không mở được; P/E 155,70 ÷ EPS TTM 16,69 = 9,33 | Hai trang giá | Ghi "158,20 đóng cửa 23/11; Google Finance chưa mở được" | Mở |
| THẤP | "Giá hiện tại" | Phiên 25/11 đang chạy 161,2–161,4 (+3,5% đến +3,7%); nháp dùng đóng cửa 24/11 (đúng) nhưng cụm "giá hiện tại" dễ hiểu lầm. Tiền ròng dùng số dư 30/6/2026, chưa cập nhật 5 tháng; P/E dùng lợi nhuận gồm cổ đông thiểu số (theo lợi nhuận mẹ cao hơn ≈ 0,7%) | Quan sát trang | Thay bằng "giá đóng cửa 24/11"; nêu số dư tiền 30/6 và dòng tiền H2 chưa công bố | Mở |
| THẤP | Nhãn | Hai câu thiếu nhãn: "mở mới giảm 29,3% là dấu hiệu pha bùng nổ đầu tư đang hạ nhiệt" (`SUY_LUẬN`) và "rủi ro sống còn nằm ở niềm tin hệ sinh thái…" (`SUY_LUẬN`). Bài 014 nói về chu kỳ công suất nặng; áp vào chủ quán chỉ là phép so sánh | Đọc bài 014 | Gắn nhãn, ghi "phép so sánh" | Mở |
| THẤP | Điều kiện bác bỏ và kịch bản | Hai chỉ báo đã thỏa ngay ở H1 2026 (OCF/lợi nhuận 0,88; chi phí 11,4%) trong khi luận điểm cơ sở là "đứng vững"; khoảng chi phí 10–12% của cơ sở chồng lên điều kiện bất lợi ≥ 11% | Đọc nháp | Tách ngưỡng cơ sở (10–11%) và bất lợi (≥ 11%) | Mở |
| THẤP | "Doanh thu hàng hóa mỗi quán giảm 15–17%" | Công thức chỉ có ở bản v4. Tái tính: −14,6% (tổng, cuối kỳ), −16,5% (đại lục, cuối kỳ), −17,2% (bình quân) | Tái tính | Đưa phép tính vào tệp phép tính | Mở |
| THẤP | Góp vốn liên kết 109,0 triệu; SBC | Thuyết minh 19 không nêu tên: giữ `CHƯA_BIẾT` (đúng). FCF chưa trừ SBC (≈ 4,6 triệu H1 2026, nhỏ) | PDF | Một dòng chú thích | Mở |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

- **Dòng tiền:** mọi số trong bảng khớp PDF ở mức RMB triệu một chữ số thập phân (trang in 114–116 thường niên, 51–53 giữa kỳ), trừ 2.929,9 ở trên. Các dòng đầu tư và tài chính cộng lại bằng dòng thuần ở cả bốn kỳ. Mua ròng FVTPL: 2.700,4; 5.332,6; 1.581,3; −908,0. Capex/đầu tư FY2025 = 10,77%; thuế/doanh thu = 4,84%; 87,5% dòng đầu tư 2025 đi vào tiền gửi và sản phẩm tài chính.
- **100 đồng doanh thu:** giá vốn 68,86%, bán hàng 6,07%, quản lý 3,22%, thuế 4,84%, lợi nhuận 17,66%; khoản còn lại +0,65 điểm %. Chi phí bán hàng + quản lý H1: 11,39% (H1 2026), 9,08% (H1 2025).
- **LTM:** OCF 4.813,5; gốc thuê 110,3; doanh thu 33.900,9; lợi nhuận 5.528,2.
- **Giá và EV:** 155,70 và 158,20 khớp Investing và StockAnalysis (có thể cùng nguồn gốc); biên 52 tuần 154,50–464,00 khớp; −66,4% và −23,1% đúng. Vốn hóa 59,1 tỷ HKD; EV = 29,66 tỷ RMB (28,66 nếu cổ tức chưa trả); P/E 9,10.
- **Định giá ngược:** công thức đúng; kết quả chạy lại: −4,82 / −3,06 / −1,30% (FCF0 3,996) và −4,11 / −2,33 / −0,56% (FCF0 3,746), khớp sau làm tròn.
- **Ba kịch bản:** doanh thu 2028 32,228 / 37,726 / 43,781 tỷ; CAGR doanh thu −1,34 / +3,98 / +9,27%; lợi nhuận 4,028 / 5,847 / 7,443 tỷ; CAGR lợi nhuận −12,08 / −0,45 / +7,89%; P/E 12,49 / 8,60 / 6,76. Khớp nháp.
- **Bài học:** bài 011 (g = tái đầu tư × ROIC; cảnh báo cộng tiền hai lần), bài 014 (bẫy P/E ngược; năm pha chu kỳ vốn), bài 012, bài N6: các trích đúng. Ví dụ quán 100/50%/35 là số hư cấu của nháp, tính đúng.
- **14 số cũ tái dùng** (93,7/4,0/2,4%; 485,1 triệu; 21,6 tỷ; 59.823 và 63.987 quán; 20.001; mở mới −29,3%; tỷ lệ đóng quán; quán nước ngoài 4.895 → 4.378; ≈ 81%; quyền thưởng; cổ tức; FULU; thuế): tất cả khớp PDF.

## Hạn chế của lần kiểm duyệt

- Không xác minh giá từ sàn: trang báo giá HKEX không hiển thị dữ liệu, Google Finance từ chối; giá chỉ được hai nguồn thứ cấp có thể dùng chung nguồn dữ liệu xác nhận.
- Tỷ giá 0,851 và việc cổ tức đã chi không xác minh được từ nguồn gốc.
- Phần đối thủ: chỉ mở lại Luckin; Nayuki, Chagee, Guming, Auntea Jenny, Meituan và lời ban lãnh đạo chưa mở lại.
- Không đọc toàn văn báo cáo thường niên (254 trang) và giữa kỳ (86 trang).
- Không đánh giá tính hợp lý của WACC 8–12% và biên ròng 12,5/15,5/17% (việc của phản biện rủi ro).
- Không có chỉ dẫn lạ nào trong các nguồn đã đọc.

## Kết luận của agent kiểm duyệt

**ĐẠT, có điều kiện.** Số công ty và phần mới khớp PDF HKEXnews và tính lại độc lập; bản tải trực tiếp của hai PDF trọng yếu có SHA-256 trùng `SHA256SUMS.txt`. Không có lỗi số liệu nghiêm trọng làm đổi kết luận. Điều kiện trước khi bỏ nhãn nháp: sửa 4 điểm TRUNG_BÌNH và xử lý các điểm THẤP. Nếu điều phối viên coi giá từ sàn là bắt buộc, điểm đó nên ghi `CHƯA_BIẾT`.
