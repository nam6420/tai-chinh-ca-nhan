# Bài Q3 — Chuẩn hóa lợi nhuận và công ty chu kỳ

- Ngày viết: `2026-11-01`; sửa sau các vòng kiểm duyệt 2–6 ngày `2026-11-02`.
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Nguồn số HPG: BCTC hợp nhất kiểm toán FY2025, báo cáo thường niên 2019 và 2023, tổng quan Q3/2026 và một bài báo về Q1/2026 (bảng cuối bài).
- Mục tiêu: Phân biệt lợi nhuận một năm với mức "bình thường"; chuẩn hóa bằng trung bình, biên, trung vị, bỏ năm cực đoan, ROE; biết mỗi cách sai ở đâu.
- Thời lượng: 3 phiên.
- Tệp thực hành: [cyclical.py](../practice/models/cyclical.py) và [hpg_cycle_inputs.csv](../practice/models/hpg_cycle_inputs.csv); kiểm bằng `python3 -m unittest discover tests`.
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/Q3-fact-check.md), [phản biện](../reviews/Q3-risk-review.md)
- Câu hỏi cốt lõi: **Nếu năm nay không phải năm điển hình, thì lợi nhuận "điển hình" là bao nhiêu và ta nên tin con số ấy đến đâu?**

## Hiểu bài này trong 1 phút

Người bán kem kiếm 100 triệu mùa hè và lỗ 20 triệu mùa đông; lấy một mùa nhân bốn đều sai. Công ty chu kỳ và hàng hóa (như thép) giống vậy ở quy mô năm. Chuẩn hóa lợi nhuận (*normalizing earnings*) trả lời: **một năm bình thường thì công ty kiếm được bao nhiêu?** Câu trả lời luôn là một khoảng. Bài dạy các cách chuẩn hóa và giới hạn của từng cách trên HPG; không kết luận đắt/rẻ, đỉnh/đáy hay dự báo.

## 1. Vì sao một năm không đủ

`SỰ_THẬT` Chương 22 của *Investment Valuation* (Damodaran, bản 3): với công ty chu kỳ, lợi nhuận theo định nghĩa biến động theo nền kinh tế; với hàng hóa, giá cao thường nối tiếp giá thấp; dùng lợi nhuận năm hiện tại làm năm cơ sở có thể cho ước tính giá trị sai lệch (trang 617, diễn đạt lại). Ông nêu hai lối: chỉnh tốc độ tăng trưởng gần hạn, hoặc định giá theo lợi nhuận chuẩn hóa (trang 617–619).

`SUY_LUẬN` Thước đo dựng trên một năm (P/E, dòng tiền năm cơ sở của DCF) mượn vị trí của năm đó trong chu kỳ: ở đỉnh P/E trông thấp, ở đáy trông cao. Chuẩn hóa là cách dễ nhất cho công ty chu kỳ trưởng thành (trang 619), giả định lợi nhuận sớm về mức bình thường.

## 2. Các cách chuẩn hóa

`SỰ_THẬT` Trang 619 liệt kê ít nhất hai cách: (a) trung bình lợi nhuận tuyệt đối các kỳ trước, đủ dài để phủ một chu kỳ, khoảng 5 đến 10 năm; (b) trung bình tỷ suất lợi nhuận hay lợi nhuận trên vốn đầu tư rồi nhân với quy mô hiện tại (ROC trung bình 12% với vốn 1.000 triệu cho lợi nhuận hoạt động chuẩn hóa 120 triệu). Cách (a) phù hợp nhất khi quy mô không đổi; biên theo doanh thu ít bị thao túng hơn (diễn đạt lại). Dùng lợi nhuận chuẩn hóa là giả định mức chuẩn **ngay lập tức**; nếu phải mất nhiều kỳ thì giá trị quá cao, và Damodaran chiết khấu lùi giá trị theo số kỳ cần.

`PHÉP_TÍNH` Ta dùng các công thức sau, mỗi công thức là một hàm trong [cyclical.py](../practice/models/cyclical.py):

| Cách | Công thức | Hàm |
|---|---|---|
| Trung bình số tuyệt đối | `Σ LN / n` | `avg_dollar` |
| Biên trung bình × doanh thu nay | `DT_nay × (Σ biên / n)` | `avg_margin_norm` |
| Biên gia quyền × doanh thu nay | `DT_nay × Σ LN / Σ DT` | `weighted_margin_norm` |
| Biên trung vị × doanh thu nay | `DT_nay × trung vị biên` | `median_margin_norm` |
| Bỏ năm cực đoan rồi trung bình | cắt giá trị lớn nhất (và nhỏ nhất nếu đặt `drop_min=1`) trước khi tính | `trimmed` |
| ROE trung bình × vốn chủ nay | `Vốn_nay × Σ ROE / n` | `roe_norm` |
| Chiết khấu lùi (minh họa) | `Giá trị_chuẩn / (1+r)^số năm` | `discount_back` |

Không cách nào tự đúng: mỗi cách trả lời câu hỏi khác (đô la, trên mỗi đồng doanh thu, trên mỗi đồng vốn); khi xa nhau, đó là thông tin về mức bất định.

## 3. Ví dụ hư cấu có đủ dữ kiện

`KỊCH_BẢN` Công ty Thép Xanh (hư cấu) có 10 triệu cổ phiếu. Doanh thu (tỷ đồng) năm 1–5 là 60, 70, 80, 100, 120; biên lợi nhuận ròng là 18%, 6%, 5%, 8%, 10%.

`PHÉP_TÍNH` Lợi nhuận mỗi năm `= doanh thu × biên`: 10,8; 4,2; 4,0; 8,0; 12,0 (tỷ đồng).

| Cách | Kết quả (tỷ đồng) | Tính |
|---|---:|---|
| Năm 5 báo cáo | 12,0 | |
| Trung bình số tuyệt đối 5 năm | 7,8 | 39,0 / 5 |
| Biên trung bình × 120 | 11,28 | 9,4% × 120 |
| Biên trung bình bỏ năm 1 × 120 | 8,70 | 7,25% × 120 |
| Biên trung vị × 120 | 9,60 | 8% × 120 |

Hai điều rút ra. Một: trung bình số tuyệt đối (7,8) thấp nhất vì doanh thu gấp đôi trong 5 năm, đúng lời cảnh báo của Damodaran về quy mô. Hai: năm 1 có biên 18%, gấp 1,8 đến 3,6 lần các năm khác; bỏ nó làm kết quả giảm từ 11,28 xuống 8,70 (khoảng 23%). Bỏ cả đỉnh lẫn đáy (năm 3, biên 5%) cho `(6+8+10)/3 = 8%`, × 120 `= 9,6`. Các biến thể (7,8 đến 11,28) khác nhau phần lớn do chọn mẫu, nên đặt quy tắc loại **trước** khi xem kết quả và báo cả dải, đừng chọn điểm mình thích; bạn phải giải thích được vì sao một năm là bất thường.

`PHÉP_TÍNH` Dùng mức chuẩn trung vị 9,6: lợi nhuận năm 5 cao hơn chuẩn `12,0/9,6 − 1 = 25%`. Giá giả định 12.000 đồng: EPS báo cáo `12,0 tỷ / 10 triệu = 1.200` đồng, P/E `= 10`; EPS chuẩn `9,6 tỷ / 10 triệu = 960` đồng, P/E `= 12,5`. Cùng một giá, năm lợi nhuận cao hơn chuẩn cho P/E thấp hơn 20%; công ty không đổi.

Nếu phải mất hai năm mới về chuẩn, Damodaran chiết khấu lùi **giá trị tính từ lợi nhuận chuẩn hóa**; bài minh họa số học trên con số 9,6 (r = 10%, `9,6/1,1² ≈ 7,93`, `discount_back`), không phải quy trình nguyên văn.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Bảng dưới (tỷ VND, hợp nhất). FY2021–FY2023 lấy từ trang "Tóm tắt các chỉ số tài chính" của [Báo cáo thường niên 2023](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) (đã làm tròn đến tỷ). FY2024–FY2025 lấy từ [báo cáo tài chính hợp nhất kiểm toán FY2025](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) (Deloitte, ký 24/03/2026, VND, trang in 5–8; FY2024 là cột "năm trước", có thể đã trình bày lại, vốn chủ cuối FY2024 theo cột trình bày lại). Trộn hai nguồn là một giới hạn.

| Năm | Doanh thu thuần | Lợi nhuận gộp | LNST công ty mẹ | Vốn chủ cuối năm |
|---|---:|---:|---:|---:|
| FY2021 | 149.680 | 41.108 | 34.478 | 90.781 |
| FY2022 | 141.409 | 16.763 | 8.484 | 96.113 |
| FY2023 | 118.953 | 12.938 | 6.835 | 102.836 |
| FY2024 | 138.855,1 | 18.497,5 | 12.021,4 | 114.647,5 |
| FY2025 | 156.116,1 | 24.497,8 | 15.453,2 | 131.220,0 |

`PHÉP_TÍNH` Biên lợi nhuận gộp (lợi nhuận gộp/doanh thu thuần): 27,5%; 11,9%; 10,9%; 13,3%; 15,7%. Biên LNST mẹ/doanh thu thuần: **23,03%; 6,00%; 5,75%; 8,66%; 9,90%**. ROE xấp xỉ (LNST mẹ / vốn chủ cuối năm, vốn chủ gồm cả lợi ích cổ đông không kiểm soát nên chỉ là xấp xỉ): 37,98%; 8,83%; 6,65%; 10,49%; 11,78%.

`PHÉP_TÍNH` Chuẩn hóa lợi nhuận FY2025 (báo cáo: **15.453,2** tỷ) bằng năm cách:

| Cách | Kết quả (tỷ VND) | So với 15.453,2 |
|---|---:|---:|
| Trung bình số tuyệt đối 5 năm | 15.454,3 | +0,0% |
| Trung bình số tuyệt đối bỏ FY2021 | 10.698,4 | −30,8% |
| Biên trung bình giản đơn × 156.116,1 | 16.653,2 | +7,8% |
| Biên gia quyền × 156.116,1 | 17.110,8 | +10,7% |
| Biên trung vị × 156.116,1 | 13.515,8 | −12,5% |
| Biên trung bình bỏ FY2021 × 156.116,1 | 11.826,4 | −23,5% |
| Biên trung bình bỏ FY2021 và FY2023 × 156.116,1 (loại một đỉnh, một đáy; FY2022 gần bằng đáy vẫn giữ) | 12.778,4 | −17,3% |
| ROE trung bình × vốn chủ 131.220,0 | 19.870,6 | +28,6% |

Kết quả trải từ khoảng 10.700 đến 19.900 tỷ, gần gấp đôi; cửa sổ năm năm có một đỉnh và một đáy nên khoảng trải phần lớn do chọn mẫu; năm năm là cận dưới của 5–10 năm Damodaran nêu. `CHƯA_BIẾT` chu kỳ thép dài bao lâu. FY2025 (15.453,2) gần trùng trung bình năm năm (15.454,3) chỉ là trùng hợp số học, không chứng minh "FY2025 là năm bình thường": trung bình đó chứa năm 2021 với biên ròng 23,03%, gấp khoảng ba lần trung bình 7,58% của bốn năm còn lại (`SUY_LUẬN`; chỉ trong cửa sổ này).

`PHÉP_TÍNH` Biên gộp FY2021 `= 41.108/149.680 = 27,5%` rơi xuống 11,9% năm sau (báo cáo thường niên 2023 in 27% và 12%, không nêu nguyên nhân). `CHƯA_BIẾT` nguyên nhân của năm đỉnh.

## 4. Quy mô đã đổi: lý do trung bình tuyệt đối sai

`SỰ_THẬT` Từ cuối FY2021 đến cuối FY2025 vốn chủ tăng từ 90.781 lên 131.220 tỷ (`PHÉP_TÍNH` +44,5%), trong khi doanh thu thuần chỉ tăng +4,3% (149.680 lên 156.116,1). Bảng cân đối FY2025 (trang 6–7): tài sản cố định (mã 220) từ 67.428,4 lên 133.608,1 tỷ trong năm 2025, còn chi phí xây dựng cơ bản dở dang (mã 242) giảm từ 63.655,9 xuống 10.721,1 tỷ. Vay ngắn hạn cộng dài hạn cuối 2025 là `64.695,0 + 27.479,2 = 92.174,2` tỷ; chi phí đi vay 3.114,9 so với 2.287,4 tỷ năm trước (+36,2%).

`SUY_LUẬN` Công ty đã đưa vào hoạt động một khối tài sản lớn vốn trước đó là dở dang (BCTC FY2025 không nêu dự án nào được kết chuyển; `SỰ_THẬT` tổng quan Q3/2026 nêu hai dự án thép còn dở dang: ray và thép đặc biệt 700.000 tấn/năm (tiến độ 80%, sản phẩm đầu Q1/2027) và cán thép chất lượng cao thuộc HPDQ2, 500.000 tấn/năm, đang chạy thử). Hệ quả cho chuẩn hóa: (1) ROE nhân vốn chủ nay (19.870,6) có thể sai hai chiều: cao hơn thực tế nếu tài sản mới chưa chạy hết công suất, nhưng ROE FY2024 bị kéo thấp bởi vốn dở dang (mã 242 cuối FY2024: 63.655,9 tỷ; các năm trước `CHƯA_BIẾT`); chiều thứ ba là đòn bẩy: dư nợ tuyệt đối tăng (105.737 tỷ cuối Q3/2026) nhưng dư nợ vay/vốn chủ vẫn khoảng 0,70–0,71 (FY2025 và Q3/2026), nên đòn bẩy tăng chưa chứng minh, còn lãi vay chắc chắn tăng, (2) biên × doanh thu nay giả định cấu trúc chi phí cũ, trong khi lãi và khấu hao đã tăng; (3) trung bình số tuyệt đối trộn các năm với bảng cân đối khác hẳn nhau. Không cách nào sửa trọn vẹn; chỉ nêu giả định và đối chiếu.

## 5. Chi phí cứng và đòn bẩy vận hành

`PHÉP_TÍNH` Doanh thu thuần FY2023 giảm 15,9% so với FY2022 (141.409 xuống 118.953). Chi phí bán hàng giảm 26,4% còn chi phí quản lý tăng 28,3% (1.019 lên 1.307), nên hai khoản này không phải bằng chứng gọn về chi phí cứng. Mạnh hơn: khấu hao gần như không đổi (6.772 so với 6.773 tỷ) khi doanh thu giảm gần 16%. `SUY_LUẬN` Chi phí cố định không co theo doanh thu nên khi doanh thu và biên cùng giảm, lợi nhuận giảm nhanh hơn doanh thu; biên × doanh thu có thể đánh giá thấp mức rơi ở đáy. Nguyên nhân biên gộp rơi từ 27,5% xuống 11,9% (giá bán so với nguyên liệu?) `CHƯA_BIẾT`.

## 6. Cái gì cần chuẩn hóa, cái gì chỉ là một lần

Chu kỳ khác khoản bất thường một lần. Damodaran: sự cố riêng của công ty (đình công, vụ kiện; trang 615) thì loại chi phí đó cùng lá chắn thuế; nguyên nhân là chu kỳ ngành hay hàng hóa thì chuẩn hóa (trang 617–619). `Ý_KIẾN` Loại khoản lãi/lỗ một lần trước khi tính biên.

Với một khoản lạ, hỏi: có lặp lại ngoài chu kỳ không; thuộc hoạt động chính hay thu nhập khác/tài chính. Lợi nhuận khác (mã 40) FY2025 là 134,8 tỷ trên lợi nhuận trước thuế 18.040,6 tỷ (`PHÉP_TÍNH` 0,7%), không chi phối FY2025; Q1/2026 thì khác (mục 7).

## 7. Dùng lợi nhuận chuẩn hóa vào định giá, và chín tháng 2026

`SỰ_THẬT` [Tổng quan tình hình kinh doanh Q3/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/10/tong-quan-tinh-hinh-kinh-doanh-quy3-2026-vn.pdf) (HPG; PDF tạo 29/10/2026; tỷ VND): 9 tháng 2026 doanh thu 171.539, giá vốn 139.499, lợi nhuận gộp 30.775, LNST 23.746; 9 tháng 2025 doanh thu 111.031, lợi nhuận gộp 18.101, LNST 11.627; vốn chủ cuối tháng 9/2026 149.568. Nhóm thép: doanh thu 165.784, LNST 18.396 (96% và 77% của tập đoàn); bất động sản 1% doanh thu và 19% LNST. `SUY_LUẬN` Nguồn ghi "LNST hợp nhất của tập đoàn", không ghi "chưa kiểm toán"; bài coi là số chung chưa kiểm toán.

`PHÉP_TÍNH` Biên gộp 9 tháng `30.775/171.539 = 17,94%`; biên LNST `23.746/171.539 = 13,84%`, gấp `13,84/7,58 ≈ 1,83` lần trung bình biên bỏ FY2021 (chưa loại khoản một lần, xem dưới). (a) `171.539 − 139.499 = 32.040` khác lợi nhuận gộp 30.775 (lệch 1.265): "doanh thu" nhiều khả năng chưa trừ giảm trừ (`SUY_LUẬN`); với doanh thu thuần ngầm định 170.274, biên LNST 13,95%, biên gộp 18,07%. (b) Biên hợp nhất trộn nhiều nhóm: biên riêng nhóm thép `18.396/165.784 = 11,10%`; không so đồng nhất với FY2021–FY2025 (cơ cấu các năm đó `CHƯA_BIẾT`).

`SỰ_THẬT` Biên LNST theo quý (đọc nhãn biểu đồ): Q3/25 10,9%, Q4/25 8,5%, Q1/26 17,0%, Q2/26 12%, Q3/26 13%; biên gộp 13,7% (Q4/25) đến 19% (Q3/26). `SỰ_THẬT` (thứ cấp) [Bizhub/Vietnam News, 22/04/2026](https://bizhub.vietnamnews.vn/hoa-phat-reports-strongest-ever-quarterly-earnings-eyes-vnd22-trillion-profit-in-2026-post402098.html) (mở 02/11/2026): gần 3,8 nghìn tỷ lợi nhuận Q1/2026 đến từ chuyển nhượng cổ phần một dự án đô thị ở Phố Nối (Hưng Yên), mô tả là khoản một lần; lợi nhuận cốt lõi khoảng 5 nghìn tỷ; không nói trước hay sau thuế. `SUY_LUẬN` Khoản này giải thích biên ròng Q1 (17,0%) cao hơn biên gộp (15,7%) và nhiều khả năng là phần lớn lợi nhuận bất động sản (19% LNST, khoảng 4.400 tỷ), không nằm trong biên thép 11,10%. `PHÉP_TÍNH` thô: `23.746 − 3.800 ≈ 19.946`, biên khoảng 11,6% (thuế chưa kiểm).

`SỰ_THẬT` Chi phí lãi vay theo quý (tỷ VND): Q1–Q4/2025 là 627, 439, 812, 1.237 (cộng 3.115, khớp mã 23 của FY2025); Q1–Q3/2026 là 1.333, 1.520, 1.774 (cộng 4.627). `PHÉP_TÍNH` Lãi vay/doanh thu: 2,70% (9T/2026), 2,00% (FY2025), 1,69% (9T/2025): tỷ lệ cùng kỳ gấp khoảng 1,6 lần, lãi vay tuyệt đối gấp khoảng 2,5 lần (4.627/1.878). Doanh thu 9 tháng +54%: biên cũ nhân doanh thu FY2025 chuẩn hóa một quy mô cũ. `SUY_LUẬN` Nên chuẩn hóa ở **EBIT (sau khấu hao)** rồi trừ lãi và thuế riêng (EBITDA bỏ khấu hao, đang lớn vì tài sản cố định gấp đôi; Damodaran trang 620 dùng lợi nhuận hoạt động), hoặc theo chênh lệch giá bán trừ giá nguyên liệu (trang 622: một trong ba lựa chọn; giá có thể ở trên hoặc dưới mức bình quân rất lâu). Damodaran dành chuẩn hóa tức thời cho công ty chu kỳ **đã trưởng thành**; HPG đang mở rộng, và cửa sổ 5 năm chỉ chứa một vòng bùng nổ–suy thoái. `CHƯA_BIẾT` EBIT và khấu hao từng năm của HPG.

`SỰ_THẬT` [Báo cáo thường niên 2019](https://static2.vietstock.vn/data/HOSE/2019/BCTN/VN/HPG_Baocaothuongnien_2019.pdf) (mở 02/11/2026) in doanh thu bán hàng (chưa trừ giảm trừ) và lợi nhuận sau thuế hợp nhất 2017–2019: 46.855 và 8.015, 56.580 và 8.600, 64.678 và 7.578 tỷ VND, tức 17%, 15%, 12% (trên doanh thu thuần 46.162, 55.836, 63.658 vẫn như vậy). `SUY_LUẬN` Biên 13,84% cao hơn FY2022–FY2025 nhưng thấp hơn 2021 (23,03%); cửa sổ FY2021–FY2025 loại 2017–2019 nên "13,84% cao hay thấp" và "23,03% gấp ba lần" chỉ đúng trong cửa sổ. Biên 2016 và 2020 `CHƯA_BIẾT`. Hai khả năng: (i) chu kỳ thuận lợi, biên về mức cũ; (ii) quy mô và chi phí mới nâng mức chuẩn. GDP 9 tháng +9,01% và xuất khẩu 23% doanh thu là yếu tố chu kỳ, chưa chứng minh mức chuẩn đổi; ngược lại một số báo chí ngành (thứ cấp, chưa kiểm) nêu thừa công suất dai dẳng và bảo hộ. Chu kỳ thép đã đổi cấu trúc hay chưa là `CHƯA_BIẾT`; số 9T chỉ có một nguồn gốc. `Ý_KIẾN` Cả hai cần số mới (công suất thực chạy, giá bán trừ nguyên liệu, lợi nhuận bất động sản). Mất hiệu lực nếu: Trung Quốc xuất khẩu thép thành phẩm trên 10 triệu tấn/tháng kéo dài (tháng 9/2026 là tháng thứ năm liên tiếp); CBAM; dư nợ và lãi vay tăng.

`KỊCH_BẢN` Chuẩn hóa không thay cho kịch bản; với DCF (011) dựng ba mức biên tham chiếu, không phải dự báo: **A** 5,75–6% (FY2022–FY2023; đáy trên cấu trúc chi phí và đòn bẩy mới có thể thấp hơn, `SUY_LUẬN`); **B** 8,7% (trung vị cửa sổ FY2021–2025); **C** 11,1% (LNST nhóm thép/doanh thu nhóm theo bản tổng quan, chưa đối chiếu thuyết minh bộ phận: thép 165.784 cộng nông nghiệp 5.064 là 170.848 trên tổng 171.539, chỉ còn khoảng 691 cho bất động sản trong khi nguồn ghi 1%, nên số nhóm có thể chưa trừ loại trừ nội bộ). A và B là biên hợp nhất, C là biên nhóm thép, nên chưa cùng gốc. Biên 9T/2026 (13,84%; khoảng 11,6% sau khi trừ thô khoản một lần) nằm trên A và B, gần C; chưa mức nào đại diện năm bùng nổ FY2021 (23,03%). Với bội số (009), tính cả P/E chuẩn hóa lẫn P/E báo cáo.

## Bài tập — làm trước khi mở đáp án

1. Vì sao P/E tính trên lợi nhuận một năm gây hiểu nhầm với công ty chu kỳ ở đỉnh và ở đáy?
2. Thép Xanh: tính lợi nhuận mỗi năm từ doanh thu và biên ở mục 3.
3. Tính trung bình số tuyệt đối 5 năm và giải thích vì sao thấp hơn lợi nhuận năm 5.
4. Tính biên trung bình × doanh thu năm 5, và so sánh khi bỏ năm 1.
5. Tính biên trung vị × doanh thu năm 5 và mức chênh của lợi nhuận năm 5 so với chuẩn đó.
6. Giả sử một giá trị tính từ lợi nhuận chuẩn là 9,6 tỷ và phải mất 3 năm mới về mức đó; với r = 10%, giá trị quy về hiện tại là bao nhiêu (phép minh họa, chưa tính các năm chuyển tiếp)?
7. HPG: tính biên LNST mẹ/doanh thu thuần của FY2023 và FY2025 (đơn vị tỷ VND, số ở mục "Ví dụ từ nguồn thật").
8. HPG: tính lợi nhuận chuẩn hóa FY2025 theo biên trung bình bỏ FY2021 và theo trung bình số tuyệt đối bỏ FY2021, rồi giải thích vì sao hai số khác nhau.
9. Biên LNST 9 tháng 2026 của HPG là 13,84% (hợp nhất; nhóm thép 18.396/165.784). Tính biên nhóm thép và nêu bốn câu hỏi cần trả lời trước khi gọi là "đỉnh chu kỳ".
10. Nêu hướng sai của ROE trung bình × vốn chủ nay theo mỗi chiều (cao quá, thấp quá, đòn bẩy) khi công ty vừa đưa nhà máy mới vào hoạt động.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. Ở đỉnh P/E trông thấp, ở đáy trông cao; P/E đổi vì lợi nhuận, không vì giá trị công ty.
2. 10,8; 4,2; 4,0; 8,0; 12,0 tỷ.
3. `39,0/5 = 7,8`. Thấp hơn năm 5 vì các năm đầu quy mô nhỏ; trung bình tuyệt đối không tính việc công ty đã lớn gấp đôi.
4. Biên TB `(18+6+5+8+10)/5 = 9,4%`, × 120 `= 11,28`. Bỏ năm 1: `(6+5+8+10)/4 = 7,25%`, × 120 `= 8,70`. Chênh khoảng 23%: phải giải thích được năm 1 vì sao bất thường.
5. Trung vị của 18, 6, 5, 8, 10 là 8%; `8% × 120 = 9,6`. Lợi nhuận năm 5 cao hơn `12/9,6 − 1 = 25%`.
6. `9,6/1,1³ = 9,6/1,331 ≈ 7,21` tỷ; đây là phép minh họa số học, vì Damodaran chiết khấu lùi giá trị chứ không phải lợi nhuận một năm.
7. FY2023: `6.835/118.953 = 5,75%`. FY2025: `15.453,2/156.116,1 = 9,90%`.
8. Biên trung bình bỏ FY2021 `(6,00+5,75+8,66+9,90)/4 = 7,58%` × 156.116,1 `≈ 11.826`. Trung bình tuyệt đối bỏ FY2021 `(8.484+6.835+12.021,4+15.453,2)/4 ≈ 10.698`. Khác nhau vì cách thứ nhất nhân biên với doanh thu FY2025 (lớn hơn), cách thứ hai giữ số tuyệt đối cũ.
9. Biên nhóm thép `18.396/165.784 = 11,10%`. Ví dụ câu hỏi (kèm khoản chuyển nhượng dự án Phố Nối ở Q1/2026): công suất thực chạy so với lắp đặt; giá bán trừ giá nguyên liệu các quý gần nhất; lãi vay và khấu hao sau khi tài sản mới vào hoạt động; lợi nhuận bất động sản (19% LNST) có lặp lại không; khoản một lần trong 9 tháng. Số nhóm có thể chưa trừ loại trừ nội bộ.
10. Cao quá: vốn mới chưa chạy hết công suất nên ROE lịch sử nhân vốn lớn hơn giả định mọi đồng vốn mới sinh lợi như đồng vốn cũ. Thấp quá: ROE FY2024 bị kéo thấp bởi vốn dở dang chưa sinh lời (mã 242: 63.655,9 tỷ). Chiều thứ ba là đòn bẩy: vốn mới nhờ vay nhiều nên ROE cũ không áp dụng.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty thép M có lợi nhuận (tỷ đồng) các năm 2021–2025 là 3.450; 850; 680; 1.200; 1.545. Doanh thu FY2025 là 156 triệu đồng. Biên LNST 9 tháng 2026 là 13,8%. Chuẩn hóa lợi nhuận 2025 và cho biết 9 tháng 2026 có phải đỉnh."

Phát hiện: (a) lợi nhuận tỷ đồng nhưng doanh thu "triệu đồng": lệch ba bậc; (b) thiếu doanh thu các năm trước nên không tính được biên; (c) không rõ mẹ hay hợp nhất; (d) 9 tháng 2026 chưa kiểm toán; (e) không có vốn chủ để kiểm quy mô; (f) "có phải đỉnh" không trả lời được từ các số này.

`Đáp án` Không chuẩn hóa được theo biên. Chỉ tính được trung bình số tuyệt đối 5 năm (`(3.450+850+680+1.200+1.545)/5 = 1.545`) và bỏ năm 2021 (`1.068,75`), kèm cảnh báo quy mô. Cần doanh thu cùng đơn vị và phạm vi, vốn chủ và nguồn kỳ 9 tháng; câu hỏi đỉnh hay không ghi `CHƯA_BIẾT`.

## Sai ở đâu

Một học viên viết: "HPG FY2025 lãi 15.453 tỷ. Trung bình 5 năm là 15.454 tỷ. Vậy FY2025 đúng mức bình thường, không cần chuẩn hóa. Chín tháng 2026 lãi 23.746 tỷ, đem nhân 4/3 ra 31.661 tỷ, cứ vậy mà định giá. P/E dùng giá hôm nay chia lợi nhuận đó."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. Trùng số giữa lợi nhuận FY2025 và trung bình năm năm là ngẫu nhiên; trung bình đó chứa năm 2021 (biên 23,03%, gấp khoảng ba lần 7,58% của bốn năm còn lại, trong cửa sổ này); 2017–2019 có biên 12–17%.
2. Trung bình số tuyệt đối bỏ qua vốn chủ tăng 44,5% từ 2021 đến 2025.
3. Quy năm bằng 4/3 giả định quý cuối giống ba quý đầu (biên LNST theo quý 8,5%–17%); Q1/2026 còn có khoản một lần khoảng 3,8 nghìn tỷ.
4. 23.746 là LNST hợp nhất, nhiều khả năng chưa kiểm toán, không phải lợi nhuận cổ đông công ty mẹ (FY2025: 15.514,9 và 15.453,2); 13,84% còn trộn bất động sản và khoản một lần (biên nhóm thép 11,10%).
5. Nếu 9 tháng 2026 là đỉnh thì P/E trên lợi nhuận quy năm thấp giả tạo; có phải đỉnh chưa biết. Thiếu nguồn và ngày của giá.
6. Không nêu điều kiện làm luận điểm mất hiệu lực.

</details>

## Kiểm tra chuyển bài

1. Công ty có doanh thu 200, 220, 240 và lợi nhuận 20, 11, 24 (cùng đơn vị). Tính biên trung bình × doanh thu 240.
2. Cùng số liệu, tính trung bình số tuyệt đối và nêu một lý do nó có thể sai.
3. Nêu hai việc phải kiểm trước khi coi lợi nhuận của năm cuối là "bình thường".

<details>
<summary>Mở sau khi tự làm</summary>

Đạt khi đúng cả ba: câu 1 biên `10%; 5%; 10%` trung bình `8,33%`, × 240 `= 20,0`. Câu 2 `(20+11+24)/3 = 18,33`; có thể sai nếu quy mô doanh thu đã đổi (200 lên 240). Câu 3: có năm cực đoan nào kéo trung bình không; quy mô hoặc cấu trúc chi phí đã đổi chưa; phạm vi (mẹ hay hợp nhất) và đơn vị có thống nhất không.

</details>

## Ranh giới an toàn

- Không phải khuyến nghị mua/bán/nắm giữ; Hòa Phát chỉ là dữ liệu thực hành.
- Chuẩn hóa là phép tính trên quá khứ kèm giả định, không phải dự báo; số 9 tháng 2026 chưa kiểm toán; bài không có giá cổ phiếu.

## Điều tôi vẫn chưa hiểu

- Bao nhiêu năm phủ một chu kỳ của ngành này, và vì sao?

## Nguồn Internet đã mở

Truy cập `2026-11-01`, mở lại `2026-11-02`.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Damodaran, *Investment Valuation* 3rd ed., chương 22 (PDF)](https://pages.stern.nyu.edu/~adamodar/pdfiles/val3ed/c22.pdf) | Phương pháp; bản in 2011; đã đọc trang 611–619 | Công ty chu kỳ, chuẩn hóa lợi nhuận, chiết khấu lùi |
| [BCTC hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) | FY2025 và cột FY2024; VND; VAS; đã đọc trang in 4–8 | Doanh thu, lợi nhuận, vốn chủ, tài sản cố định, vay |
| [Báo cáo thường niên 2019 của Hòa Phát](https://static2.vietstock.vn/data/HOSE/2019/BCTN/VN/HPG_Baocaothuongnien_2019.pdf) | 2017–2019; tỷ VND; hợp nhất | Doanh thu và LNST 2017–2019 |
| [Báo cáo thường niên 2023 của Hòa Phát](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) | FY2021–FY2023; tỷ VND làm tròn; trang tóm tắt chỉ số tài chính và báo cáo kết quả kinh doanh 2023 | Chuỗi lịch sử FY2021–FY2023 |
| [Bizhub/Vietnam News, 22/04/2026](https://bizhub.vietnamnews.vn/hoa-phat-reports-strongest-ever-quarterly-earnings-eyes-vnd22-trillion-profit-in-2026-post402098.html) | Thứ cấp; Q1/2026 | Khoản một lần Phố Nối |
| [Tổng quan tình hình kinh doanh Q3/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/10/tong-quan-tinh-hinh-kinh-doanh-quy3-2026-vn.pdf) | Q3 và 9 tháng 2026; chưa kiểm toán | Số 9 tháng 2026; biên theo quý; lãi vay theo quý; dự án thép (trang 2–6) |

`CHƯA_BIẾT` Nguyên nhân của biên đỉnh FY2021, phạm vi các số 9 tháng (nguồn gọi cả "doanh thu" lẫn "doanh thu thuần"), việc FY2024 trình bày lại, biên 2016 và 2020. Biên và lãi vay theo quý đọc từ nhãn biểu đồ trong PDF ảnh. Trung vị, biên gia quyền và bỏ năm cực đoan là biến thể của bài, không phải công thức nguyên văn ở chương 22; chưa có nguồn thứ hai độc lập.
