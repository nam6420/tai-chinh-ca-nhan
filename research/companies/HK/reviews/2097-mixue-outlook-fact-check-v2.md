# Biên bản kiểm duyệt: MIXUE Group (2097.HK), câu chuyện doanh nghiệp, dòng tiền và triển vọng 3 năm (bản nháp v2)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `source-fact-checker` (lần kiểm 2 của tài liệu này). Giữ nguyên kết luận, mức độ và bằng chứng chính; không thêm nhận định mới.

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-25 10:22 +07` (bắt đầu 10:15 +07)
- Chốt dữ liệu lúc: `2026-11-25 10:00 +07` (khớp báo cáo đích)
- Phạm vi: sửa các phát hiện lượt 1; chạy lại script kịch bản và định giá ngược bằng `python3 -I`; đối chiếu PDF HKEXnews đã lưu; mở lại nguồn ngoài T5, T9, T11–T17; trích dẫn bài học 011, 012, 014, N6; nhãn và tính nhất quán nội bộ. Không kiểm báo cáo gốc Nayuki, Chagee, Guming, Auntea Jenny, Meituan; không đọc toàn văn báo cáo thường niên và giữa kỳ.
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-outlook-draft-v2-sha-a7d15d67.md`
- SHA-256 nội dung đích: `a7d15d676e8a5f33641c1324ea8261d6f505fe18d896a57d35be7e70eb57d59c` (agent tự chạy `validate_report.py --print-hash`, khớp)
- Kết luận: `ĐẠT` (có điều kiện: sửa M1–M5 và xử lý L1–L11 trước khi bỏ nhãn nháp; giá cổ phiếu vẫn chỉ có nguồn thứ cấp)
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL / tệp | Kết quả |
|---|---|
| 16 PDF HKEXnews đã lưu (`shasum -a 256 -c SHA256SUMS.txt`) | 16/16 OK; đối chiếu EGM poll results 2026-09-30, báo cáo giữa kỳ 2026, báo cáo thường niên 2025, thông báo cổ tức, công bố H1 2025, cấp quyền thưởng |
| EGM poll results 2026-09-30, trang in 2–3 | Xác nhận: tỷ giá `HK$1 to RMB0.85954`, trung bình 5 ngày làm việc của PBoC tính cả ngày họp (30/9); ngày ghi nhận 12/10/2026, "dự kiến chi trả" 6/11/2026, tổng ≈ RMB 1.006,0 triệu; 379.618.800 cổ phiếu; không chỗ nào xác nhận đã chi trả |
| Script mục "Tái lập" của tệp phép tính v2, chạy `python3 -I` | Khớp từng số trong báo cáo |
| [SEC, Luckin 6-K](https://www.sec.gov/Archives/edgar/data/0001767582/000110465926121665/tm2628441d1_ex99-1.htm) (mở 2 lần) | Xác nhận: SSSG tự vận hành −11,1% (so với +14,3%); biên hoạt động GAAP +3,8 điểm % lên 15,4%; biên cấp quán tự vận hành +5,8 điểm % lên 23,3%; doanh thu +17,0%; SSSG theo quý −0,1% / −5,3% / −11,1% (Q1–Q3 2026). **6-K không có xu hướng theo tháng** |
| [Quartr, Luckin Q3 2026](https://quartr.com/events/luckin-coffee-inc-lknc-q3-2026_FPuPKDZO) | Có câu "cải thiện từng tháng từ tháng 7 đến 9"; tóm tắt thứ cấp, không phải bản ghi cuộc họp |
| [KrASIA/Nikkei](https://kr-asia.com/china-bubble-tea-chain-mixue-shuts-more-stores-as-growth-model-falters) | GoodMe (Guming) +32%, Auntea Jenny +42% doanh thu H1 2026; giá IPO 202,5; đỉnh 618,5 (6/2025); −57% đến 9/11; tỷ giá ước tính 7,85 và 6,68 (16/11); quán nước ngoài 4.378; quán Mong Kok là "lần đóng thứ sáu ở Hồng Kông năm nay" |
| [BNext](https://www.bnext.com.tw/article/93087/mixue-profit-decline-store-expansion-2026) | 17/11/2026; đóng cửa 16/11 HK$170,1; −17,2% (557 nghìn → 461 nghìn RMB mỗi quán, **tác giả tự ước tính**); ban lãnh đạo nêu hai lý do (nền trợ giá 2025; cạnh tranh trà và cà phê làm giảm giá); không nêu lý do mở mới chậm |
| [Investing.com UK, MIXUE](https://uk.investing.com/equities/mixue), [lịch sử](https://uk.investing.com/equities/mixue-historical-data) | Đóng cửa 24/11 155,70; 23/11 158,20; 20/11 165,30; 16/11 170,10; biên 52 tuần 154,50–464,00; vốn hóa 59,11 tỷ HKD; P/E tự mâu thuẫn (11,1x và 9,1x) |
| [StockAnalysis, 2097](https://stockanalysis.com/quote/hkg/2097/), [lịch sử](https://stockanalysis.com/quote/hkg/2097/history/) | Cùng số đóng cửa; EPS TTM 16,69; 379,62 triệu cổ phiếu |
| Google Finance; hkex.com.hk (trang báo giá) | Không mở được; **giá vẫn chỉ có nguồn thứ cấp, hai nguồn có thể chung dữ liệu** |
| [Investing.com, consensus](https://uk.investing.com/equities/mixue-consensus-estimates) | Mua 10 / Giữ 7 / Bán 4; Macquarie Sell 180 (31/8/2026); JPMorgan 190; Deutsche 203; Jefferies 252 (hạ xuống Hold, 28/8); Goldman Buy 285; **không có dòng CLSA** |
| [Investing.com, Macquarie](https://ng.investing.com/news/analyst-ratings/macquarie-initiates-coverage-on-mixue-stock-with-underperform-rating-93CH-2093336) | 2025-09-05, Underperform, HK$279 |
| [CBNData](https://www.cbndata.com/information/295975) | 5/11/2026 (nguồn gốc 36Kr): Lucky Cup còn ≈ 8.000 quán, dừng mở quán huyện/xã, đóng ≈ 2.000 quán đuôi; Mixue tốn 500 triệu RMB cho máy cà phê; tất cả từ người giấu tên; **không có** 33.000/37.000 và quỹ 1 tỷ |
| [Jiemian](https://m.jiemian.com/article/15187458.html), [Sina](https://t.cj.sina.com.cn/articles/view/2098807780/7d1943e4027019d08) | Chủ quán có tên (Qian Qi) nói quán mới mở cách ≈ 400 m; "bán kính bảo hộ 300 m; trong 900 m ba quán là thường", hoa hồng 30%, máy 33.000/37.000/40 ly là lời tác giả không nêu nguồn; quỹ 1 tỷ RMB trợ cấp máy cà phê, đã lắp hơn 6.000 quán đến cuối tháng 6 |
| [Sohu](https://m.sohu.com/a/1002991393_122014422) | Repost 长江商报, 30/3/2026: 11.216 khiếu nại tích lũy đến 29/3/2026; "30 ngày gần nhất" trên 70% an toàn thực phẩm; Sha Tin bị ngừng bán vì coliform (6/2025); 2.527 quán đóng 2025, +57,1% |
| [China Briefing](https://www.china-briefing.com/news/chinas-food-franchising-market-in-2026/) | Đăng 12/8/2026; có dự thảo SAMR 6/2026; **không có** hạn lấy ý kiến 17/7 |
| [Lexis](https://www.lexiscn.com/latest_message.php?id=512877) | Dự thảo "Ten Rules for Subsidy Practices of Food Delivery Platforms", ban hành 18/6/2026, hạn lấy ý kiến 17/7/2026 (thứ cấp; chưa mở văn bản gốc SAMR) |

## Trạng thái sửa các phát hiện lượt 1

| Phát hiện lượt 1 | Trạng thái | Ghi chú |
|---|---|---|
| Lãi nhận LTM 150,8 triệu | ĐÃ_SỬA | 135,412 − 42,914 + 58,262; FCF0 3.989,7 và 3.871,4; khớp bài 011 |
| Cổ tức "đã chi trả" gắn `SỰ_THẬT` | ĐÃ_SỬA, kèm lưu ý | Đúng "thông qua 30/9, dự kiến chi trả 6/11, đã chi trả `CHƯA_XÁC_MINH`"; xem L6 |
| T9 (60,06 gán nhầm) | SỬA_CHƯA_ĐỦ (THẤP) | T9 = 59,1 đúng; T10 chưa có 60,06 và vẫn ghi 158,20 là "giữa phiên"; xem L9 |
| Tỷ giá 0,851 | ĐÃ_SỬA | Gốc 0,85954 (EGM trang 3); 0,851 làm biên so sánh |
| Gửi ròng FY2024 2.929,9 | ĐÃ_SỬA | 2.940.000 − 10.056 |
| Capex LTM 713,4; FCF 3.989,7 | ĐÃ_SỬA | Tái tính khớp |
| Nguyên nhân giảm OCF | ĐÃ_SỬA | Nêu tồn kho bù +632,8 |
| Trang in | ĐÃ_SỬA | "114–116" và "51–53"; sổ nguồn S13 ghi "50–53" nhất quán với footer |
| Macquarie | ĐÃ_SỬA | 2025-09-05, HK$279; hiện Sell HK$180 |
| Luckin | ĐÃ_SỬA | Các số mới đã xác nhận từ 6-K; có thể bỏ ghi chú "chờ kiểm nguồn" |
| Giá 23/11 "giữa phiên" | SỬA_CHƯA_ĐỦ (THẤP) | Thân bài đã sửa, T10 chưa |
| Cụm "giá hiện tại" | SỬA_CHƯA_ĐỦ (THẤP) | Chú thích (*) bảng kịch bản và tệp phép tính vẫn có "so với giá hiện tại" |
| Nhãn thiếu | ĐÃ_SỬA phần lớn | Còn vài dòng (L8) |
| Ngưỡng cơ sở/bất lợi chồng lấn | SỬA_CHƯA_ĐỦ | Bảng ngưỡng đã tách nhưng mâu thuẫn với danh sách "Điều gì phải đúng" (M3) |
| "15–17%" thiếu công thức | ĐÃ_SỬA | Tái tính khớp; dải 15–17 / 15–18 chưa nhất quán (L8) |
| Góp vốn liên kết; SBC | ĐÃ_SỬA | Góp vốn vẫn `CHƯA_BIẾT`; có chú thích SBC |

## Phát hiện mới

| Mức độ | Mã | Phần | Phát hiện | Cách khắc phục |
|---|---|---|---|---|
| TRUNG_BÌNH | M1 | Luckin "cải thiện từng tháng từ tháng 7 đến 9 (6-K)" | Gán sai nguồn: 6-K không có xu hướng theo tháng và cho SSSG theo quý xấu đi (−0,1%, −5,3%, −11,1%); ý "cải thiện từng tháng" chỉ có trong tóm tắt thứ cấp của Quartr | Bỏ "(6-K)"; ghi `CHƯA_XÁC_MINH` [Quartr] và nêu chuỗi theo quý |
| TRUNG_BÌNH | M2 | "quán đầu tiên tại Hồng Kông đóng đầu tháng 10" | KrASIA không nói "đầu tiên"; quán Mong Kok là "lần đóng thứ sáu ở Hồng Kông năm nay" | Sửa theo KrASIA |
| TRUNG_BÌNH | M3 | "Điều gì phải đúng" so với bảng ngưỡng | Không nhất quán: bất lợi 2026 "< −16%" so với "dưới −17%"; mở mới ròng 2027 "dưới 3.000" so với "dưới 2.000"; chi phí "từ 11% trở lên" trùng cơ sở "10–11%" tại đúng 11%; giá trị kịch bản bất lợi nằm đúng ở biên dải cơ sở | Dùng một bộ ngưỡng nửa mở, không chồng lấn; ngưỡng bất lợi nằm ngoài giá trị kịch bản bất lợi |
| TRUNG_BÌNH | M4 | Hàng "Mật độ quán", "Dòng tiền ra" (T14/T15) | Nguồn gốc sai: "ẩn danh" không đúng (400 m là lời chủ quán có tên Qian Qi); "400–900 m", "phổ biến", hoa hồng 30%, máy 33.000/37.000 là lời tác giả; hai nguồn mâu thuẫn về máy cà phê (CBNData: miễn phí, chi 500 triệu; Jiemian/Sina: trả trước 33.000, nộp thêm 37.000); CBNData không chứa 33.000/37.000 hay quỹ 1 tỷ | Tách nguồn gốc từng ý; nêu mâu thuẫn; gán quỹ 1 tỷ cho Jiemian/Sina, 500 triệu cho CBNData |
| TRUNG_BÌNH | M5 | "Mở mới thấp có thể là chủ ý (lời ban lãnh đạo)" | Gán sai nguồn: BNext chỉ ghi "đã giảm tốc mở quán" (tác giả) không nêu lý do; "nâng chất lượng quán hiện hữu" trong KrASIA chỉ nói về quán nước ngoài | Bỏ "lời ban lãnh đạo" cho mở mới; có thể thêm hai lý do ban lãnh đạo tự nêu cho doanh số mỗi quán giảm (nền trợ giá; cạnh tranh làm giảm giá), làm giả thuyết "đặc thù Mixue" yếu hơn một chút |
| THẤP | L1 | Biên ròng "−3,1 điểm %" | 18,274% → 15,243% là −3,03 (tệp nền ghi −3,0) | Sửa −3,0 điểm % |
| THẤP | L2 | 21.650,8 và chênh 10,1 | Tổng thành phần = 21.650,7; chênh 10,0 | Sửa |
| THẤP | L3 | "mở mới ròng 13.344 năm 2025" | Là tổng quán và gồm 1.354 quán FULU mua lại; nhượng quyền 14.496 − 2.527 = 11.969; RPS 2025 bị hạ nhẹ do mẫu số gồm quán FULU | Ghi "gồm 1.354 quán mua lại"; thêm hạn chế |
| THẤP | L4 | Hàng T12 | CLSA Outperform HK$324 không có trên trang đã mở; Goldman Buy 285 chưa nêu; JPMorgan hiện là "Sell" trên Investing | Bỏ CLSA hoặc hạ nhãn; thêm Goldman Buy 285 |
| THẤP | L5 | Hàng T17 | "Lấy ý kiến đến 17/7" không có trong China Briefing; bài đăng 12/8/2026; hạn 17/7 có trong Lexis | Thêm Lexis; sửa ngày xuất bản |
| THẤP | L6 | EV "nếu cổ tức chưa trả" 29,2 | Diễn giải dễ gây hiểu lầm: ngày ghi nhận 12/10 nên giá 24/11 đã ex-dividend; phần tiền ròng của người đang giữ cổ phiếu vẫn là 20,6 tỷ; EV 29,2 chỉ có nghĩa nếu giá còn cum-dividend | Ghi rõ "chỉ để thấy độ nhạy, không phải trường hợp thực tế", hoặc bỏ |
| THẤP | L7 | "139 triệu (2,4%) mức tăng 2025" | 139 triệu ≈ 2,4% lợi nhuận 2025 nhưng chỉ ≈ 9,4% của mức tăng tuyệt đối 1.472,9 | Viết "bằng khoảng 2,4% lợi nhuận 2025" |
| THẤP | L8 | Nhãn và dải | Thiếu nhãn ở các dòng 19, 182, 184, 232; dải giảm doanh thu mỗi quán không nhất quán (15–17%, 15–18%, −15% đến −18%); đo được −14,6% đến −17,8% | Gắn nhãn; dùng một dải "khoảng −15% đến −18%" kèm mẫu số |
| THẤP | L9 | Sổ nguồn T10, T5 | T10 vẫn "giữa phiên"; T5 còn "chờ kiểm nguồn" dù đã xác nhận; chưa có 60,06 ở T10 | Sửa T10; đánh dấu Luckin biên và +17,0% đã kiểm nguồn nhưng giữ khác biệt ở M1 |
| THẤP | L10 | Giá 25/11 và EV | Giá 25/11 lúc ≈ 09:59 +07 là 162,30–162,50 (không ảnh hưởng vì dùng đóng cửa 24/11); EV chưa trừ lợi ích thiểu số 332,3 (≈ 1,1%) và nợ thuê 227,8 (≈ 0,8%), bản báo cáo không nêu; "đỉnh trong ngày 6/2025": KrASIA ghi đỉnh 618,5 vào tháng 6/2025 | Sửa chữ hoặc thêm chú thích |
| THẤP | L11 | Hàng T11 | KrASIA gọi Guming là "GoodMe"; có thể thay "do bên phản biện đọc" bằng "bên kiểm nguồn đã mở KrASIA, khớp +32% và +42%" | Cập nhật ghi chú, giữ `CHƯA_XÁC_MINH` cho nguồn gốc |

## Kiểm tra phép tính và số cũ

- **Script v2 khớp mọi số trong báo cáo:** FCF 3.989,7 / 3.871,4; lãi nhận 150,8; lợi nhuận LTM 5.528,2; vốn hóa 50.805; EV 30.170; P/E 9,19; EV/lợi nhuận 5,46; tỷ giá so sánh 0,851: EV 29.665 và 28.659; EV nếu cổ tức chưa trả 29.164; toàn bộ bảng g hàm ý; ngưỡng g = 0 (95/47/15% và 88/41/10%).
- **Kịch bản (DT / LN / CAGR DT / CAGR LN / P/E / EV÷LN):** Đuôi 23.117 / 2.081 / −11,7% / −29,5% / 24,4 / 14,5; Bất lợi 31.953 / 4.154 / −1,6% / −11,2% / 12,2 / 7,3; Cơ sở 39.223 / 5.726 / +5,3% / −1,1% / 8,9 / 5,3; Thuận lợi 46.916 / 7.741 / +11,8% / +9,3% / 6,6 / 3,9. Tăng trưởng từng năm và quán cuối 2028 khớp bảng. RPS 2025 = 0,6314.
- **Nhất quán nội bộ:** H2 2026 hàm ý −3,8% / +1,9% / +9,8%; nền H2 2025 +32,04%; biên H2 2025 17,17%; doanh thu hàng hóa mỗi quán −14,63% / −16,54% / −17,18% / −17,8%; cổ tức 43,4% lợi nhuận H1 và 816,2 triệu cho hai nhà sáng lập; hiệu ứng thuế H1 ≈ 0,47 điểm %.
- **Số cũ:** số đóng quán, bảng cân đối H1 2026 (phải trả người bán 1.859,9; tồn kho 3.828,2; nợ hợp đồng 594,0; nợ ngắn hạn 5.350,3; lợi ích thiểu số 332,3), 87,5%, 10,8%, 4,8%, 485,1, số quán, chủ nhượng quyền, quyền thưởng, FULU, lỗ tỷ giá: đều khớp PDF.
- **Trích bài học 011, 012, 014, N6:** đúng, chỉ mượn phương pháp; ví dụ quán 100/50%/35 là số hư cấu, tính đúng.
- **Giá:** đóng cửa 24/11 155,70, 23/11 158,20, biên 52 tuần, vốn hóa 59,11 tỷ HKD khớp Investing và StockAnalysis; −23,1% và −66,4% đúng.

## Hạn chế của lần kiểm duyệt

- Giá chưa đối chiếu với sàn; tỷ giá đúng ngày 24/11 chưa có (tham chiếu USD/CNY 6,7118 ÷ 7,85 ≈ 0,855, lệch dưới 1% so với 0,85954).
- Chưa mở báo cáo gốc Guming, Nayuki, Chagee, Auntea Jenny, Meituan; "Nayuki −13,1%", "Chagee sụt hai chữ số" chưa kiểm lại.
- Chưa mở Digrin, văn bản gốc SAMR; Quartr chỉ là tóm tắt.
- CBNData, Jiemian, Sina, Sohu là nguồn thứ cấp với người giấu tên; chỉ xác nhận bài viết nói như vậy.
- Chưa đọc toàn văn báo cáo thường niên (254 trang) và giữa kỳ (86 trang).
- Không đánh giá tính hợp lý của WACC 8–12%, biên giả định, kịch bản (việc của phản biện rủi ro).
- Không phát hiện chỉ dẫn lạ trong nguồn web hoặc PDF.

## Kết luận của agent kiểm duyệt

**ĐẠT, có điều kiện, 0 lỗi nghiêm trọng.** Mọi số công ty và mọi phép tính khớp PDF và tái tính độc lập. Các phát hiện lượt 1 về cơ bản đã sửa; còn ba chỗ sửa chưa đủ (T9/T10, "giá hiện tại", ngưỡng chồng lấn). Điều kiện trước khi bỏ nhãn nháp: sửa M1–M5, rồi xử lý L1–L11. M1, M2 là câu sai nguồn trong mục bằng chứng trái chiều (không đổi kết luận nhưng cần sửa); M3 phải thống nhất ngưỡng bác bỏ; M4 phải tách đúng nguồn gốc và nêu mâu thuẫn giữa các bài báo; M5 phải bỏ gán lời ban lãnh đạo cho việc mở mới chậm. Giá từ nguồn thứ cấp là điểm yếu còn lại; nếu điều phối viên coi giá sàn là bắt buộc thì ghi `CHƯA_BIẾT` cho bước này.
