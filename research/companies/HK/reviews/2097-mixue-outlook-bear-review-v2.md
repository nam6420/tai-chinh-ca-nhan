# Biên bản kiểm duyệt: MIXUE Group (2097.HK), câu chuyện doanh nghiệp, dòng tiền và triển vọng 3 năm (bản nháp v2)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `risk-bear-reviewer` (lần phản biện 2 của tài liệu này). Giữ nguyên kết luận, mức độ, ý kiến bất đồng và bằng chứng chính; không thêm nhận định mới. Các con số do agent tự tính tay (không có `Bash`).

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-25`, giờ chính xác `CHƯA_BIẾT` (agent không đọc được đồng hồ; một trang giá hiển thị "Nov 25, 2026, 10:59 AM HKT" ≈ 09:59 +07, nên lượt chạy sau mốc chốt)
- Chốt dữ liệu lúc: `2026-11-25 10:00 +07` (khớp báo cáo đích; trang web mở trong lượt có thể mới hơn vài giờ)
- Phạm vi: toàn bộ bản nháp v2; trọng tâm: sửa các phát hiện lượt 1, kịch bản số quán × doanh thu mỗi quán × biên (bốn cột), độ nhạy chiết khấu tiền mặt, ba lớp "chết", bảng ngưỡng và điều kiện bác bỏ, bảng bằng chứng trái chiều ngoài, tuân thủ AGENTS.md
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-outlook-draft-v2-sha-a7d15d67.md`
- SHA-256 nội dung đích: `a7d15d676e8a5f33641c1324ea8261d6f505fe18d896a57d35be7e70eb57d59c` (giá trị do điều phối viên cung cấp; agent không tự băm; đã đọc đúng tệp có tên chứa `sha-a7d15d67`)
- Kết luận: `ĐẠT` (có điều kiện: xử lý N1–N7 trước khi bỏ nhãn nháp; không còn lỗi CAO)
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet và tệp đã tự mở trong lượt kiểm duyệt

| URL / tệp | Ngày / kỳ | Mục đích |
|---|---|---|
| [SEC, Luckin 6-K](https://www.sec.gov/Archives/edgar/data/0001767582/000110465926121665/tm2628441d1_ex99-1.htm) (mở 2 lần) | 2026-11-03 | SSSG −11,1% (so với +14,3%), biên +3,8 và +5,8 điểm %, doanh thu +17,0%, chi phí giao hàng −38,1%, dãy SSSG theo quý; **không có số liệu theo tháng 7–9** |
| [Earnings Whispers, bản ghi cuộc họp Luckin Q3 2026](https://www.earningswhispers.com/transcript/LKNCY/Q32026) | 2026-11 | Nơi có câu "decline narrowing month by month from July to September" và cải thiện Q4; bản ghi lỗi, trùng lặp, thứ cấp |
| [KrASIA/Nikkei, Mixue shuts more stores](https://kr-asia.com/china-bubble-tea-chain-mixue-shuts-more-stores-as-growth-model-falters) | 2026-11-17 | Quán Hồng Kông, −57%, GoodMe +32%, Auntea Jenny +42%, số quán nước ngoài 4.895 (cuối 2024) và 4.378 (30/6/2026) |
| [KrASIA, GoodMe](https://kr-asia.com/goodme-pushes-beyond-lower-tier-markets-with-efficiency-gains-in-hand) | 2026-08-31 | Doanh thu H1 +31,9%; GMV bình quân ngày mỗi quán RMB 7.800 (gần như phẳng); 14.351 quán (+28,4%); lợi nhuận điều chỉnh +44,4% |
| [BNext](https://www.bnext.com.tw/article/93087/mixue-profit-decline-store-expansion-2026) | 2026-11-17 | Đóng cửa 16/11 HK$170,1; −17,2% (tác giả tự ước tính); hai lý do của ban lãnh đạo (nền trợ giá giao hàng; cạnh tranh trà và cà phê); "đã chủ động giảm tốc mở quán" |
| [The Standard, H1 2026](https://www.thestandard.com.hk/finance/article/341107/Mixues-net-profit-drops-15pc-in-H1-shares-slide-12pc) | 2026-08-27 | Giá vốn tăng do "đầu tư chất lượng nguyên liệu thật"; chi phí bán hàng +22,9% do IP và nhân sự |
| [Inside Retail, Yum China Q3 2026](https://insideretail.asia/2026/11/05/how-yum-china-keeps-growing-profits-while-its-restaurants-take-in-less/) | 2026-11-05 | SSSG −3%; CFO nói trợ giá giao hàng giảm nhanh hơn dự kiến |
| [StockAnalysis, thống kê 2097](https://stockanalysis.com/quote/hkg/2097/statistics/) | 25/11/2026 10:59 HKT | Giá 162,30 (+4,24%) nên đóng cửa 24/11 là 155,70; vốn hóa 61,61 tỷ HKD; ngày không hưởng cổ tức 5/10/2026 |
| [Investing.com, cổ tức MIXUE](https://www.investing.com/equities/mixue-dividends) | 2026 | HK$3,08304 mỗi cổ phiếu; chi trả 6/11/2026 (lịch, không phải xác nhận đã chi); 2,65 / 3,08304 = 0,85955 khớp 0,85954 |
| [Investing.com, đồng thuận](https://uk.investing.com/equities/mixue-consensus-estimates) | 2026-08-28 đến 31 | Macquarie Sell 180; Goldman Buy 285 (từ 450); JPM Sell 190; Deutsche Hold 203; Jefferies Hold 252; Mua 10, Giữ 7, Bán 4; mục tiêu trung bình HK$250,58 |
| PDF báo cáo giữa kỳ 2026 (trang PDF 47–48, 62–64, 67–68) | H1 2026 | Bảng cân đối; thuyết minh 11 (tiền bị hạn chế, cơ cấu tiền tệ); thuyết minh 6, 7 |
| PDF thông báo H-share full circulation 2026-05-03; tệp phép tính v2; nghiên cứu nền v4 | 2026 | Đối chiếu |

Chỉ thấy trên kết quả tìm kiếm, chưa mở được, không dùng làm bằng chứng: Huxiu (405), The Bamboo Works (403), Futu (rỗng), Quartr, Tiger, 36kr, Winshang, bản thảo SAMR 17/6/2026, Digrin, Chagee Q2 2026 (SSSG −16,1%), các tuyên bố ban lãnh đạo về giảm tốc mở quán và chuyển địa điểm hơn 2.000 quán. Không tìm thấy tin hay số liệu riêng của Mixue tháng 10–11/2026 ngoài các bài thứ cấp; không có thông báo mua lại cổ phiếu hay bản chính thức quy định SAMR.

## Trạng thái sửa các phát hiện lượt 1

| Mã | Đánh giá | Lý do |
|---|---|---|
| C1 (CAO) | **ĐÃ_SỬA, không còn CAO** | Doanh thu dựng từ quán bình quân × RPS, tái tính bốn cột khớp; có Đuôi; bỏ "cận dưới/cận trên"; biên 14,6% có cơ sở. Còn hai dư lượng ở N1, N2 |
| T1 | SỬA_CHƯA_ĐỦ (nhẹ) | Đã có bảng chiết khấu, ngưỡng đảo dấu, bỏ câu "bi quan hơn thực tế". Chưa xong: tiền bị hạn chế (11,5 triệu) và cơ cấu tiền tệ có sẵn trong PDF, neo cho chiết khấu, dòng tiền tháng 7–11 (N7) |
| T2 | ĐÃ_SỬA | Lãi nhận LTM 150,760; FCF0 3.989,7 và 3.871,4 khớp |
| T3 | SỬA_CHƯA_ĐỦ | Đã tách ba lớp; chưa có ngưỡng số cho lớp 2 và 3; điều kiện bác bỏ "khó chết" lẫn lớp 3 (N3, N10) |
| T4 | SỬA_CHƯA_ĐỦ | Đã thêm bảng bằng chứng ngoài nhưng còn một chiều, Luckin sai nguồn, thiếu mẫu số và bằng chứng bên ủng hộ (N4–N6) |
| T5 | ĐÃ_SỬA | Tiêu đề trung tính; EV/lợi nhuận 5,46; thuế hạ vai trò (ETR H1 2026 22,1%, đóng góp 0,5 điểm %). Còn chữ "chỉ 5,5 lần" (N9) |
| T6 | SỬA_CHƯA_ĐỦ | Đã đổi sang cùng đơn vị RPS nhưng sinh lệch biên, khe hở, hai chỗ lệch chữ và bảng, vùng cơ sở hàm ý biên 15,4–16,9% (N2) |
| T7 | ĐÃ_SỬA | Bỏ "khả dĩ nhất"; có chú thích (*); tách nhãn; dư ô "Rủi ro thật" chưa nhãn (N9) |
| L1, L2 | ĐÃ_SỬA | Ví dụ −10%: lãi 15 → 10 (−33%); vốn hóa 59.106,6 triệu HKD; Macquarie có ngày |
| Bất đồng 1 (cơ sở không trung tính) | Sửa một phần, **giữ bất đồng ở RPS** | Biên 14,6% đúng mức đang chạy nhưng cơ sở 2026 hàm ý RPS H2 cải thiện ≈ 5 điểm % so với H1 mà không nêu (N1) |
| Bất đồng 2 (tỷ lệ đóng quán) | ĐÃ_SỬA | Đã nêu số đóng tuyệt đối và mẫu số |
| Bất đồng 3 (giá hàm ý giảm) | ĐÃ_SỬA, còn lệch giọng nhỏ | Tái tính bảng đúng; dư N7, N9 |
| Bất đồng 4 (biên 15,5%) | ĐÃ_SỬA | Cơ sở 14,6% |

## Phát hiện mới

| Mức độ | Mã | Phát hiện | Bằng chứng | Cách khắc phục |
|---|---|---|---|---|
| TRUNG_BÌNH (cao) | N1 | Kịch bản bất lợi ≈ xu hướng H1 kéo dài; cơ sở ngầm cần RPS H2 cải thiện ≈ 5 điểm %. Quy sang RPS H2 (`PHÉP_TÍNH`): H1 2026 đã −17,8%; **cơ sở H2 ≈ −12,7%; bất lợi H2 ≈ −17,0%; thuận lợi H2 ≈ −6,7%; đuôi H2 ≈ −23%**. Bảng ngưỡng ghi bất lợi "dưới −17%" còn H1 là −17,8%, tức chỉ báo RPS cũng đã ở vùng bất lợi. Từ 2027 cơ sở giả định RPS −2% rồi 0% trong khi quán bình quân vẫn +10% và +6% | RPS H2 = (doanh thu H2 2026 / 18.685,1) ÷ (quán bình quân H2 2026 / quán bình quân H2 2025 ≈ 56.400). Cơ sở: H2 = 19.038 (+1,9%), quán bình quân 65.905 (+16,8%), RPS −12,7%. Bất lợi: H2 = 17.970 (−3,8%), quán 65.405 (+15,9%), RPS −17,0% | Nêu RPS H2 hàm ý của từng kịch bản, nói thẳng "bất lợi = H1 kéo dài"; thêm mốc "xu hướng H1 kéo dài"; ghi "cơ sở cần H2 cải thiện ≈ 5 điểm %" |
| TRUNG_BÌNH (cao) | N2 | Bảng ngưỡng không tự nhất quán: (i) tham số kịch bản nằm đúng ranh giới vùng (RPS 2026 bất lợi −17% so với vùng cơ sở "−13% đến −17%"; mở mới 2026 bất lợi 7.000 so với "dưới 7.000"; 2027 +2.000 so với "dưới 2.000"; đuôi −20% so với "dưới −20%"); (ii) khe hở chưa phân loại (RPS 2027 từ −8% đến −5% và +2% đến +3%; mở mới 2026 7.000–9.000; 2027 2.000–5.000); (iii) chữ lệch bảng ("< −16%" so với "< −17%"; "dưới 3.000" so với "dưới 2.000"); (iv) vùng cơ sở của biên gộp 30–31% và chi phí 10–11% hàm ý biên ròng ≈ 15,4% (30 − 11) đến 16,9% (31 − 10), chạm biên thuận lợi 16,5%, trong khi giả định cơ sở là 14,6% | Công thức biên ròng ≈ (biên gộp − chi phí + 0,5–0,7) × (1 − 0,22); H1 2026: (30,4 − 11,4 + 0,5) × 0,779 = 15,2% khớp | Dựng ngưỡng bằng cách đảo từ biên cơ sở 14,6%; dùng "≥" và "<" không đóng hai đầu; đồng bộ chữ và bảng; đặt ngưỡng bất lợi lệch vào trong, không trùng tham số kịch bản |
| TRUNG_BÌNH | N3 | Điều kiện bác bỏ "bão hòa" và "khó chết" khó hoặc không thể kích hoạt. "Bão hòa": RPS H2 2026 ≥ 0% **và** mở mới ròng ≥ 5.000 mỗi nửa năm, trong khi ngay thuận lợi chỉ đạt RPS H2 ≈ −6,7% và mở mới 9.000 mỗi năm → không với tới kể cả ở kịch bản tốt nhất; "luận điểm cần kiểm" là "trưởng thành", còn "bão hòa" là luận điểm đối lập, dễ nhầm. "Khó chết": "tiền ròng giảm quá 25% trong hai kỳ" tức mất ≈ 5 tỷ mỗi kỳ trong khi FCF dương ≈ 4 tỷ mỗi năm; "kỳ" không định nghĩa; "không do cổ tức đã thông báo" làm cổ tức mới chưa công bố thành điều kiện; "giao dịch bên liên quan lớn mới" thuộc lớp 3, chưa có ngưỡng "lớn"; độ trễ 3–6 tháng | Bảng ngưỡng; thuận lợi mở mới 2026 9.000, 2027 6.500 | Đặt điều kiện bác bỏ "bão hòa" ở ngưỡng vùng thuận lợi; định nghĩa "kỳ" và "lớn" bằng số; tách điều kiện lớp 3 khỏi lớp 1 |
| TRUNG_BÌNH | N4 | Luckin: nguồn gán sai, trích một phần, suy luận biên quá tay. (a) "SSSG cải thiện từng tháng từ tháng 7 đến 9 (6-K)" không có trong 6-K; nằm trong bản ghi cuộc họp (lời ban lãnh đạo, thứ cấp). (b) Bỏ sót dãy SSSG tự vận hành Q1 −0,1%, Q2 −5,3%, Q3 −11,1% (xấu dần theo quý); ban lãnh đạo Luckin còn nói SSSG theo kiểu sóng (bị ép khi mở quán nhanh, hồi phục khi giảm tốc), ủng hộ cả giả thuyết mật độ lẫn giả thuyết trợ giá. (c) "'Nền trợ giá' không giải thích được sụt biên riêng của Mixue" là `SUY_LUẬN` viết như kết luận: Luckin tự vận hành gánh chi phí giao hàng (−38,1%, còn 10% doanh thu từ 19%), Mixue là nhà cung ứng; công ty giải thích chi phí bán hàng +22,9% do IP và nhân sự, giá vốn do chất lượng nguyên liệu (The Standard): lý do chủ động, một phần có thể đảo ngược. Các số biên Luckin nay đã xác nhận từ 6-K | SEC 6-K; Earnings Whispers; The Standard | Sửa nguồn câu "cải thiện hàng tháng" thành lời ban lãnh đạo `CHƯA_XÁC_MINH`; thêm dãy SSSG Q1–Q3; gắn `SUY_LUẬN` cho vế biên và nêu lời giải thích của công ty |
| TRUNG_BÌNH | N5 | Bảng bằng chứng trái chiều chưa đủ công bằng cả hai phía. (a) So doanh thu +32%/+42% với +2,3% nhưng GoodMe mở quán +28,4%; số đo ngang hàng là GMV bình quân mỗi quán (phẳng ở RMB 7.800 mỗi ngày); bỏ sót lợi nhuận GoodMe (tin mâu thuẫn: +44,4% điều chỉnh, một nguồn khác −3,6%). (b) Bỏ sót bằng chứng độc lập ủng hộ "nền trợ giá ngành": Yum China Q3 2026 SSSG −3%, CFO nói trợ giá giảm nhanh hơn dự kiến; lời ban lãnh đạo Mixue (BNext). (c) "11.216 khiếu nại" không có mẫu số (≈ 0,19 mỗi quán trên kỳ tích lũy không rõ độ dài). (d) Hồng Kông 5–9 quán trên 63.987 (< 0,02% mạng lưới), không nên đọc thành "làn sóng". (e) Lucky Cup ≈ 8.000 / 64.000 ≈ 12,5% mạng lưới. (f) Nhà phân tích: thiếu Goldman Buy 285 (cắt từ 450) và mục tiêu trung bình HK$250,58; mọi mục tiêu chốt cuối tháng 8, trước đợt giảm giá. (g) Nayuki chỉ nêu ca thất bại | Các nguồn đã mở | Thêm các điểm bên ủng hộ; đổi cột so sánh sang trên mỗi quán; thêm mẫu số; nêu Goldman và trung bình; nói rõ Hồng Kông không đại diện |
| TRUNG_BÌNH | N6 | Diễn giải "mở mới −29,3%" mâu thuẫn với việc công ty chủ động giảm tốc; thiếu việc đổi CEO. Mục "Cơ chế bão hòa" đọc −29,3% là dấu hiệu "pha bùng nổ đầu tư đang hạ nhiệt", trong khi bảng bên ủng hộ nói mở mới thấp "có thể là chủ ý". Tháng 3/2026 CEO mới (Zhang Yuan, thay Zhang Hongfu; có ở nghiên cứu nền v4, S17) tuyên bố giảm tốc mở quán trong nước; BNext ghi "đã chủ động giảm tốc mở quán". Nếu phần lớn là quyết định của Mixue thì không phải bằng chứng chủ quán bỏ cuộc; chuyển địa điểm có thể làm tăng cả số đóng lẫn số mở (chưa xác minh cách tính). Mục "Ban lãnh đạo" của nháp không nhắc đổi CEO | BNext; nghiên cứu nền v4 dòng 151 | Thống nhất cách đọc −29,3% theo hai hướng, gắn `Ý_KIẾN` và nêu lời công ty; bổ sung đổi CEO; ghi `CHƯA_BIẾT` việc đóng quán có gồm chuyển địa điểm |
| TRUNG_BÌNH | N7 | Định giá ngược còn mục đóng được và mục chưa neo. (a) Tiền bị hạn chế đóng được từ PDF: thuyết minh 11 (trang in 66) chỉ RMB 11,5 triệu (≈ 0,05% của 21.650,8); chênh 10,1 giữa MD&A và bảng cân đối có khả năng chủ yếu là khoản này (dư ≈ 1,4 chưa giải thích). (b) Cơ cấu tiền tệ (trong tiền và tiền gửi 13.554,7 chưa gồm FVTPL 8.096,1): RMB 8.890,6 (65,6%), HKD 3.505,1 (25,9%), USD 855,3 (6,3%), còn lại IDR, MYR, THB, VND và khác; lỗ tỷ giá H1 2026 153,8 so với 42,2; quy đổi 0,85954 là giả định (±1% = ±0,5 tỷ). (c) Thuế khấu trừ chưa có mức pháp định; bảng 0/10/30/50% không có neo nên người đọc không biết ngưỡng "mong manh ở 12%" nằm ở vùng khả dĩ hay cực đoan. (d) Dòng tiền tháng 7–11: v1 từng nêu ≈ +1,6–1,7 tỷ, v2 bỏ phần định lượng; nếu giữ hoàn toàn thì EV ≈ 28,5 tỷ và g hàm ý âm hơn. (e) Cổ tức 6/11: đã chi `CHƯA_XÁC_MINH` (đã ghi đúng) | PDF giữa kỳ trang in 61, 66, 47; Investing.com | Điền (a)–(b) từ PDF; nêu neo cho chiết khấu; khôi phục dòng tiền tháng 7–11 dưới dạng độ nhạy; nêu mức thuế khấu trừ hoặc ghi `CHƯA_BIẾT` kèm cách tra |
| THẤP | N8 | Biên cơ sở chưa tách phần ngoại hối và thuế ưu đãi. Lỗ tỷ giá thêm 153,8 − 42,2 = 111,6 triệu ≈ 0,57 điểm % biên ròng, phi hoạt động, đã nằm trong mức giảm biên đang được ngoại suy; làm phép tách "chi phí bán hàng và quản lý giải thích 77,5% mức giảm lợi nhuận trước thuế" bỏ lửng phần ngoại hối (≈ 22,7%). Một số công ty con hưởng thuế 15% (miền Tây, Hải Nam), kịch bản giữ 22% cố định, rủi ro hết ưu đãi chưa nêu | PDF giữa kỳ trang in 61–63 | Nêu thành phần ngoại hối của biên cơ sở, nhãn `Ý_KIẾN` |
| THẤP | N9 | Giọng văn còn nghiêng, chưa gắn nhãn: "EV/lợi nhuận LTM **chỉ** 5,5 lần" (Tóm tắt 5) ngụ ý rẻ; Rủi ro #3 "trong mắt thị trường" khẳng định thị trường đang chiết khấu khi mức chiết khấu `CHƯA_BIẾT`; ô "Rủi ro thật" (lớp 2) và "Không loại trừ" (lớp 3) không có nhãn | Dòng 21, 197, 109–110 | Bỏ "chỉ"; gắn `SUY_LUẬN` |
| THẤP | N10 | Đuôi: "mô hình hóa vòng phản hồi" nói quá; Tóm tắt 4 dễ hiểu nhầm. RPS và mở mới là hai chuỗi tham số tự chọn, không có hàm nối giữa lãi quán, số đóng và mở mới. Đuôi 2028 vẫn còn 56.823 quán, doanh thu 23,1 tỷ, lợi nhuận 2,08 tỷ, tiền ròng nguyên vẹn: suy giảm nặng, **không phải "chết"** lớp 2; Tóm tắt 4 viết hai lớp còn lại "có kịch bản đuôi" trong khi đuôi chỉ đại diện lớp 2. Biên 9% là `Ý_KIẾN` tùy ý (2022: biên ròng 14,8% ở biên gộp 28,3%). Đuôi an toàn thực phẩm/quy định chưa mô hình hóa chấp nhận được nếu có một độ nhạy một dòng kèm tiền lệ | Tái tính đuôi khớp | Đổi mô tả thành "đường đi giả định"; sửa Tóm tắt 4; thêm độ nhạy cho đuôi sự cố |
| THẤP | N11 | Số quán nước ngoài "4.895 → 4.378" ở mục "Điểm ngoặt H1 2026": 4.895 là cuối 2024 (4.467 cuối 2025); trong H1 2026 chỉ giảm 89 (−2,0%); phần lớn thu hẹp xảy ra năm 2025 (−428) | KrASIA; nghiên cứu nền v4 | Nêu mốc từng giai đoạn |
| THẤP | N12 | H-share full circulation: công ty nộp hồ sơ 30/4/2026 để chuyển 22.823.988 cổ phiếu chưa niêm yết (6,01%) thành H-share (thông báo 3/5/2026, đã có trong `data/raw`), chưa được nhắc trong nháp; liên quan lớp 3, tác động `CHƯA_BIẾT` | PDF thông báo 3/5/2026 | Nêu và ghi `CHƯA_BIẾT` ý định |

## Kiểm tra phép tính và bằng chứng trái chiều

- **Phép tính tự làm tay khớp nháp:** bốn cột kịch bản (doanh thu từng năm, CAGR, lợi nhuận, P/E 24,4 / 12,2 / 8,9 / 6,6, EV/lợi nhuận 14,5 / 7,3 / 5,3 / 3,9); vốn hóa 50.804, EV 30.170; toàn bảng g hàm ý và ngưỡng đảo dấu (≈ 95/47/15% và 88/41/10%); FCF LTM 3.989,7; lợi nhuận gộp giảm 76,7; −66,4%, −23,1%, −8,5% so với mốc. Kết luận "vững ở WACC 8–10% khi chiết khấu dưới ≈ 40%, mong manh ở 12%" đúng về số học; neo của WACC 8–12% và của mức chiết khấu chưa có.
- **Bằng chứng ủng hộ luận điểm của nháp (nêu để công bằng):** thanh khoản; tỷ lệ đóng quán thấp hơn H1 2025; ban lãnh đạo Luckin nói cải thiện Q4; ban lãnh đạo Mixue giải thích giảm RPS bằng nền trợ giá và cạnh tranh; giảm mở quán là chủ ý; Yum China Q3 ghi nhận hiệu ứng trợ giá; Goldman vẫn Buy.
- **Câu "tài liệu không kết luận thị trường bi quan hay lạc quan hơn thực tế":** phần lớn được giữ; chỗ ngược ý: "chỉ 5,5 lần" (Tóm tắt 5), Rủi ro #3, và việc đặt "cơ sở lợi nhuận phẳng/giảm nhẹ" cạnh "giá hàm ý g âm" khiến người đọc rút ra thị trường không quá bi quan; nên thêm một câu nêu rõ không rút suy ra đó. Thiên lệch tổng thể: chọn bằng chứng nghiêng bi quan (chín dòng ngược, ba gạch bên ủng hộ; thiếu Yum, Goldman, lời công ty); RPS 2026 cơ sở nghiêng lạc quan nhẹ (N1); biên cơ sở trung tính (đã gồm lỗ ngoại hối, N8); mở mới 8.000 / 5.000 / 3.500 hợp lý, có thể hơi thận trọng (H2 2026 ngầm 3.834, thấp hơn ≈ 44% so với H2 2025 ≈ 6.840), điểm yếu là mở mới và RPS độc lập nhau trong mô hình.
- Số quán: 63.987 − 59.823 = 4.164 so với mở mới ròng 5.455 − 1.289 = 4.166 (lệch 2, nhỏ).

## Hạn chế của lần kiểm duyệt

- Không có `Bash`: tính tay, có thể lệch làm tròn.
- Chưa mở được Huxiu, The Bamboo Works, Futu; các lời ban lãnh đạo về chuyển địa điểm quán, giảm mở, RPS giảm hai chữ số chỉ thấy qua tóm tắt tìm kiếm.
- Không có số Chagee Q3 2026, không có cập nhật vận hành Mixue tháng 10–11/2026, không xác nhận độc lập việc chi cổ tức 6/11, không có bản chính thức quy định SAMR.
- Không dựng lại WACC; không đọc toàn văn báo cáo thường niên và giữa kỳ.
- Số quán 30/6/2025 suy từ +20,7% (≈ 53.000), không đọc trực tiếp.
- Nội dung web được coi là dữ liệu không đáng tin; không có chỉ dẫn nào trong nguồn bị làm theo.

## Kết luận của agent kiểm duyệt

**`ĐẠT` có điều kiện, 0 lỗi nghiêm trọng.** C1 đã được sửa đúng hướng: kịch bản dựng từ động lực, có đuôi, biên có cơ sở; các phát hiện lượt 1 khác phần lớn đã xử lý. Chưa nên bỏ nhãn nháp trước khi xử lý N1–N7. Điểm cần giữ lại: (1) N1: "bất lợi" 2026 chỉ là đà H1 kéo dài, "cơ sở" cần RPS H2 cải thiện ≈ 5 điểm %; (2) N2, N3: bảng ngưỡng và điều kiện bác bỏ chưa dùng được; (3) N4, N5: Luckin gán sai nguồn, trích một phần, bảng bằng chứng trái chiều nghiêng một phía; (4) N7: đóng các mục có sẵn trong PDF.

**Ý kiến bất đồng còn giữ:**
- Không đồng ý rằng cơ sở 2026 là trung tính ở chiều RPS: nó ngầm giả định H2 hồi phục.
- Đồng ý biên 14,6% là mức đang chạy, nhưng chưa tách ngoại hối.
- Đồng ý đuôi an toàn thực phẩm chưa mô hình hóa là chấp nhận được **nếu** có một độ nhạy minh họa.
- Đồng ý một phần với "giá hàm ý dòng tiền giảm": vững ở WACC 8–10%, mong manh ở 12%; nên nêu neo cho WACC và chiết khấu tiền.
- Đồng ý với nhận định thanh khoản thấp rủi ro.

Tuân thủ AGENTS.md: không có chỉ dẫn mua/bán/nắm giữ cá nhân hóa, không cam kết lợi nhuận, kịch bản có nhãn `KỊCH_BẢN` và không gắn xác suất, có "Điều chưa biết", điều kiện mất hiệu lực và nhãn nháp; cần bổ sung nhãn ở N9.
