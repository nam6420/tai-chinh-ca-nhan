# BẢN NHÁP - CHƯA KIỂM DUYỆT: Bài Q3 — Chuẩn hóa lợi nhuận và công ty chu kỳ

- Ngày viết: `2026-11-01`. Bài mới của Đợt 3.
- Chốt dữ liệu lúc: `2026-11-01 (Asia/Ho_Chi_Minh)`
- Nguồn số HPG: báo cáo tài chính hợp nhất kiểm toán FY2025, báo cáo thường niên 2023 và bản tổng quan Q3/2026, đều mở ngày `2026-11-01` (xem bảng cuối bài).
- Mục tiêu: Phân biệt lợi nhuận của một năm với mức lợi nhuận "bình thường"; chuẩn hóa bằng trung bình số tuyệt đối, biên trung bình, trung vị, bỏ năm cực đoan, ROE; biết mỗi cách sai ở đâu; không dùng P/E của năm đỉnh hay năm đáy làm kết luận.
- Thời lượng: 3 phiên (A: mục 1–3; B: ví dụ nguồn thật và mục 4–7; C: bài tập).
- Tệp thực hành: [cyclical.py](../practice/models/cyclical.py) và [hpg_cycle_inputs.csv](../practice/models/hpg_cycle_inputs.csv); kiểm bằng `python3 -m unittest discover tests`.
- Kiểm nguồn: `CHƯA`
- Phản biện rủi ro: `CHƯA`
- Câu hỏi cốt lõi: **Nếu năm nay không phải năm điển hình, thì lợi nhuận "điển hình" là bao nhiêu và ta nên tin con số ấy đến đâu?**

## Hiểu bài này trong 1 phút

Người bán kem kiếm 100 triệu mùa hè và lỗ 20 triệu mùa đông; lấy một mùa nhân bốn để "quy năm" đều sai. Công ty chu kỳ (*cyclical*) và công ty hàng hóa (*commodity*, như thép) giống vậy ở quy mô năm. Chuẩn hóa lợi nhuận (*normalizing earnings*) trả lời câu hỏi: **một năm bình thường thì công ty kiếm được bao nhiêu?** Câu trả lời luôn là một khoảng, không phải một con số.

## Bài này làm gì và chưa làm gì

Làm: dạy các cách chuẩn hóa và giới hạn của từng cách, thực hành trên chuỗi FY2021–FY2025 cùng 9 tháng 2026 của Hòa Phát (HPG). Chưa làm: không kết luận đắt/rẻ hay đỉnh/đáy, không dự báo.

## 1. Vì sao một năm không đủ

`SỰ_THẬT` Trong chương 22 của giáo trình *Investment Valuation* (Damodaran, bản 3), với công ty chu kỳ, ông viết rằng lợi nhuận, theo định nghĩa, biến động và phụ thuộc trạng thái nền kinh tế; với công ty hàng hóa, giá cao thường nối tiếp giá thấp; và nếu dùng lợi nhuận năm hiện tại làm năm cơ sở bạn có thể nhận ước tính giá trị sai lệch (trang 617, diễn đạt lại). Ông nêu hai lối: chỉnh tốc độ tăng trưởng gần hạn, hoặc định giá theo lợi nhuận chuẩn hóa (trang 617–619).

`SUY_LUẬN` Mọi thước đo dựng trên một năm (P/E, tỷ suất lợi nhuận, dòng tiền năm cơ sở của DCF) mượn vị trí của năm đó trong chu kỳ: ở đỉnh P/E trông thấp, ở đáy trông cao hoặc không tính được. Chuẩn hóa là cách dễ nhất cho công ty chu kỳ trưởng thành (trang 619), với giả định đi kèm rằng năm hiện tại không bình thường và lợi nhuận sẽ sớm về mức bình thường.

## 2. Các cách chuẩn hóa

`SỰ_THẬT` Trang 619 của chương trên liệt kê ít nhất hai cách chính: (a) lấy trung bình lợi nhuận tuyệt đối của các kỳ trước, đủ dài để phủ một chu kỳ, khoảng 5 đến 10 năm, và (b) lấy trung bình tỷ suất lợi nhuận hay lợi nhuận trên vốn đầu tư của các kỳ trước rồi nhân với quy mô hiện tại; ví dụ ROC trung bình 12% với vốn đầu tư 1.000 triệu cho lợi nhuận hoạt động chuẩn hóa 120 triệu. Cách (a) chỉ hợp khi quy mô công ty không đổi; biên theo doanh thu ít dễ bị thao túng hơn (diễn đạt lại). Điểm hay bị bỏ qua: dùng lợi nhuận chuẩn hóa là giả định về mức chuẩn **ngay lập tức**; nếu phải mất nhiều kỳ thì giá trị quá cao, và cách sửa đơn giản là chiết khấu lùi theo số kỳ cần.

`PHÉP_TÍNH` Ta dùng các công thức sau, mỗi công thức là một hàm trong [cyclical.py](../practice/models/cyclical.py):

| Cách | Công thức | Hàm |
|---|---|---|
| Trung bình số tuyệt đối | `Σ LN / n` | `avg_dollar` |
| Biên trung bình × doanh thu nay | `DT_nay × (Σ biên / n)` | `avg_margin_norm` |
| Biên gia quyền × doanh thu nay | `DT_nay × Σ LN / Σ DT` | `weighted_margin_norm` |
| Biên trung vị × doanh thu nay | `DT_nay × trung vị biên` | `median_margin_norm` |
| Bỏ năm cực đoan rồi trung bình | cắt giá trị lớn nhất (và nhỏ nhất nếu đặt `drop_min=1`) trước khi tính | `trimmed` |
| ROE trung bình × vốn chủ nay | `Vốn_nay × Σ ROE / n` | `roe_norm` |
| Chiết khấu lùi | `LN_chuẩn / (1+r)^số năm` | `discount_back` |

Không cách nào tự đúng: mỗi cách trả lời câu hỏi khác (bao nhiêu đô la, bao nhiêu trên mỗi đồng doanh thu, trên mỗi đồng vốn). Khi các câu trả lời xa nhau, đó chính là thông tin về mức bất định.

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

Hai điều rút ra. Một: trung bình số tuyệt đối (7,8) thấp hơn mọi cách còn lại vì công ty tăng doanh thu gấp đôi trong 5 năm; năm 1 nhỏ kéo trung bình xuống. Đây đúng là lời cảnh báo của Damodaran về quy mô. Hai: năm 1 có biên 18%, cao gấp 1,8 đến 3,6 lần các năm khác; bỏ nó làm kết quả giảm từ 11,28 xuống 8,70, khoảng 23%. Bỏ chỉ một phía (đỉnh) là lựa chọn có thiên lệch hướng; bỏ cả đỉnh lẫn đáy (năm 3, biên 5%) cho `(6+8+10)/3 = 8%`, × 120 `= 9,6`. Quyết định này không do công thức đưa ra mà do bạn phải giải thích được vì sao một năm là bất thường hay điển hình.

`PHÉP_TÍNH` Dùng mức chuẩn trung vị 9,6: lợi nhuận năm 5 cao hơn chuẩn `12,0/9,6 − 1 = 25%`. Giả sử giá cổ phiếu là 12.000 đồng (hư cấu, chỉ để minh họa phép chia). EPS báo cáo `= 12,0 tỷ / 10 triệu = 1.200` đồng nên P/E `= 12.000/1.200 = 10`. EPS theo mức chuẩn `= 9,6 tỷ / 10 triệu = 960` đồng nên P/E `= 12.000/960 = 12,5`. Cùng một giá, năm đỉnh cho P/E thấp hơn mức chuẩn 20%; công ty không đổi, chỉ có vị trí trong chu kỳ đổi.

Nếu phải mất hai năm mới về chuẩn, Damodaran đề xuất chiết khấu lùi **giá trị tính từ lợi nhuận chuẩn hóa** theo số kỳ cần thiết. Để minh họa số học, bài áp cùng phép chia lên chính lợi nhuận chuẩn: với r = 10%, `9,6/1,1² ≈ 7,93` (`discount_back`); đây là phép minh họa của bài, không phải quy trình nguyên văn của nguồn.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Bảng dưới (tỷ VND, hợp nhất). FY2021–FY2023 lấy từ trang "Tóm tắt các chỉ số tài chính" của [Báo cáo thường niên 2023](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) (đã làm tròn đến tỷ). FY2024–FY2025 lấy từ [báo cáo tài chính hợp nhất kiểm toán FY2025](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) (Deloitte, ký 24/03/2026, đơn vị gốc VND, trang 5–8; FY2024 là cột "năm trước", có thể đã trình bày lại). Vốn chủ cuối FY2024 là số đầu năm 2025 theo cột trình bày lại.

| Năm | Doanh thu thuần | Lợi nhuận gộp | LNST công ty mẹ | Vốn chủ cuối năm |
|---|---:|---:|---:|---:|
| FY2021 | 149.680 | 41.108 | 34.478 | 90.781 |
| FY2022 | 141.409 | 16.763 | 8.484 | 96.113 |
| FY2023 | 118.953 | 12.938 | 6.835 | 102.836 |
| FY2024 | 138.855,1 | 18.497,5 | 12.021,4 | 114.647,5 |
| FY2025 | 156.116,1 | 24.497,8 | 15.453,2 | 131.220,0 |

Hai nguồn khác chuẩn trình bày (làm tròn khác nhau, chuẩn bị báo cáo khác nhau); bài này trộn nguồn như vậy và coi đây là một giới hạn, không phải điều đã kiểm.

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
| Biên trung bình bỏ cả FY2021 và FY2023 (đáy) × 156.116,1 | 12.778,4 | −17,3% |
| ROE trung bình × vốn chủ 131.220,0 | 19.870,6 | +28,6% |

Kết quả trải từ khoảng 10.700 đến khoảng 19.900 tỷ, tức gần gấp đôi; cửa sổ năm năm chỉ có đúng một đỉnh và một đáy nên khoảng trải này phần lớn do lựa chọn mẫu, và năm năm là cận dưới của khoảng 5–10 năm mà Damodaran nêu. `CHƯA_BIẾT` chu kỳ thép dài bao lâu. Báo cáo FY2025 (15.453,2) nằm giữa khoảng; ngẫu nhiên nó gần trùng với trung bình năm năm (15.454,3), và đó là một sự trùng hợp số học, không phải bằng chứng "FY2025 là năm bình thường". `SUY_LUẬN` Nếu bạn dừng ở trung bình năm năm, bạn sẽ kết luận lợi nhuận đang đúng mức chuẩn, nhưng trung bình đó chứa năm 2021 có biên ròng 23,03%, gấp khoảng ba lần trung bình 7,58% của bốn năm còn lại.

`PHÉP_TÍNH` Biên gộp FY2021 `= 41.108/149.680 = 27,5%` rơi xuống 11,9% năm sau (báo cáo thường niên 2023 in tỷ suất làm tròn 27% và 12%, và phần bảng tóm tắt không nêu nguyên nhân). `CHƯA_BIẾT` nguyên nhân của năm đỉnh; cần mở thuyết minh và báo cáo thường niên FY2021 để kiểm.

## 4. Quy mô đã đổi: lý do trung bình tuyệt đối sai

`SỰ_THẬT` Từ cuối FY2021 đến cuối FY2025 vốn chủ tăng từ 90.781 lên 131.220 tỷ (`PHÉP_TÍNH` +44,5%), trong khi doanh thu thuần chỉ tăng +4,3% (149.680 lên 156.116,1). Bảng cân đối FY2025 (trang 6–7): tài sản cố định (mã 220) từ 67.428,4 lên 133.608,1 tỷ trong năm 2025, còn chi phí xây dựng cơ bản dở dang (mã 242) giảm từ 63.655,9 xuống 10.721,1 tỷ. Vay và nợ thuê tài chính ngắn hạn cộng dài hạn cuối 2025 là `64.695,0 + 27.479,2 = 92.174,2` tỷ; chi phí đi vay FY2025 là 3.114,9 tỷ so với 2.287,4 tỷ năm trước (+36,2%).

`SUY_LUẬN` Công ty đã đưa vào hoạt động một khối tài sản lớn vốn trước đó là dở dang (nhiều khả năng dự án mới, nhưng nguồn đã mở không nêu tên dự án nên nhãn này chỉ là suy luận). Hệ quả cho chuẩn hóa: (1) cách ROE nhân vốn chủ nay (19.870,6) có thể sai theo hai chiều: cao hơn thực tế nếu tài sản mới chưa chạy hết công suất, nhưng ROE các năm trước lại bị kéo thấp bởi vốn dở dang chưa sinh lời (mã 242 cuối FY2024: 63.655,9 tỷ); (2) cách biên × doanh thu nay giả định cấu trúc chi phí cũ, trong khi chi phí lãi và khấu hao có thể đã đổi lên; (3) trung bình số tuyệt đối trộn các năm với bảng cân đối khác hẳn nhau. Không cách nào sửa trọn vẹn chuyện này; ta chỉ có thể nêu giả định và đối chiếu.

## 5. Chi phí cứng và đòn bẩy vận hành

`PHÉP_TÍNH` Doanh thu thuần FY2023 giảm 15,9% so với FY2022 (141.409 xuống 118.953). Chi phí bán hàng giảm 26,4% (2.666 xuống 1.961) còn chi phí quản lý tăng 28,3% (1.019 xuống 1.307), nên hai khoản này gộp lại không phải bằng chứng gọn về chi phí cứng. Bằng chứng mạnh hơn trong cùng bảng tóm tắt: chi phí khấu hao gần như không đổi (6.772 so với 6.773 tỷ) khi doanh thu giảm gần 16%. `SUY_LUẬN` Phần chi phí cố định không co theo doanh thu nên khi doanh thu và biên cùng giảm, lợi nhuận giảm nhanh hơn doanh thu; điều đó có thể khiến biên × doanh thu đánh giá thấp mức rơi ở đáy. Nguyên nhân chính của biên gộp rơi từ 27,5% xuống 11,9% là giá bán so với giá nguyên liệu, mà bài chưa có nguồn gốc: `CHƯA_BIẾT`.

## 6. Cái gì cần chuẩn hóa, cái gì chỉ là một lần

Chu kỳ khác khoản bất thường một lần. Damodaran tách hai nhóm: sự cố riêng của công ty (đình công, vụ kiện; trang 615) thì loại phần chi phí đó cùng lá chắn thuế khỏi lợi nhuận; còn khi nguyên nhân là chu kỳ ngành hay hàng hóa thì dùng mức chuẩn hóa (trang 617–619). `Ý_KIẾN` Khoản lãi hay lỗ một lần nên loại trước khi tính biên, kẻo lẫn vào mức chuẩn.

Khi gặp một khoản lạ, hỏi: có lặp lại ngoài chu kỳ không; nằm trong hoạt động chính hay thu nhập khác/tài chính; thuyết minh nêu gì. Lợi nhuận khác (mã 40) FY2025 chỉ 134,8 tỷ trên lợi nhuận trước thuế 18.040,6 tỷ (`PHÉP_TÍNH` 0,7%), nên không chi phối FY2025; điều đó không nói gì về kỳ khác.

## 7. Dùng lợi nhuận chuẩn hóa vào định giá, và chín tháng 2026

`SỰ_THẬT` [Tổng quan tình hình kinh doanh Q3/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/10/tong-quan-tinh-hinh-kinh-doanh-quy3-2026-vn.pdf) (HPG; tệp PDF tạo ngày 29/10/2026 theo siêu dữ liệu; tỷ VND): 9 tháng 2026 doanh thu 171.539, giá vốn 139.499, lợi nhuận gộp 30.775, LNST 23.746; 9 tháng 2025 doanh thu 111.031, lợi nhuận gộp 18.101, LNST 11.627; vốn chủ cuối tháng 9/2026 149.568. Nhóm thép đóng góp doanh thu 165.784 và LNST 18.396 (96% và 77% của tập đoàn); bất động sản 1% doanh thu và 19% LNST; nông nghiệp 3% và 4%. `SUY_LUẬN` Trang nguồn không ghi "chưa kiểm toán" và chỉ ghi "LNST" mà không nói có tách cổ đông không kiểm soát hay không; bài coi là số chung, chưa kiểm toán (`CHƯA_BIẾT` xác nhận).

`PHÉP_TÍNH` Biên gộp 9 tháng 2026 là `30.775/171.539 = 17,94%`; biên LNST/doanh thu `= 23.746/171.539 = 13,84%`; so với trung bình biên bỏ FY2021 là 7,58%, gấp `13,84/7,58 ≈ 1,83` lần. Vốn chủ cuối quý 3 cao hơn cuối FY2025 `149.568/131.220 − 1 = 14,0%`. Hai lưu ý: (a) `171.539 − 139.499 = 32.040` khác lợi nhuận gộp công bố 30.775 (lệch 1.265), nên "doanh thu" của bản tổng quan nhiều khả năng chưa trừ giảm trừ (`SUY_LUẬN`); với doanh thu thuần ngầm định `139.499 + 30.775 = 170.274`, biên LNST là 13,95%, biên gộp 18,07%; (b) biên hợp nhất 13,84% trộn nhiều nhóm: biên LNST riêng nhóm thép chỉ `18.396/165.784 = 11,10%`, vì bất động sản đóng góp 19% LNST trên 1% doanh thu. Biên hợp nhất không phải biên chu kỳ thép thuần, và không so đồng nhất với FY2021–FY2025 vì cơ cấu nhóm các năm đó `CHƯA_BIẾT` (cần thông tin bộ phận).

`SUY_LUẬN` Biên 13,84% đã cao hơn mọi năm FY2022–FY2025, nhưng thấp hơn năm 2021 (23,03%). Điều đó không cho phép kết luận ở đỉnh hay chưa đến đỉnh: đáp án phụ thuộc vào việc quy mô mới có đổi mức chuẩn hay không. Cách an toàn hơn là nêu hai khả năng: (i) chu kỳ đang thuận lợi và biên sẽ về gần mức các năm trước, (ii) quy mô mới và cấu trúc chi phí mới làm mức chuẩn cao hơn các năm FY2022–FY2025. `Ý_KIẾN` Hai giả thuyết đều cần số mới để kiểm: công suất thực chạy, giá bán trừ chi phí nguyên liệu, các biện pháp thương mại, và phần lợi nhuận bất động sản có lặp lại không. Điều kiện làm kết luận mất hiệu lực: bản tổng quan nêu tháng 9/2026 là tháng thứ năm liên tiếp Trung Quốc xuất khẩu thép thành phẩm trên 10 triệu tấn, và CBAM của EU từ 2026; dư nợ và lãi vay tăng; số 9 tháng chưa kiểm toán; giả định chuẩn hóa tức thời.

`KỊCH_BẢN` Chuẩn hóa không thay cho kịch bản. Khi định giá bằng DCF (011), hãy dựng ít nhất ba kịch bản biên (ví dụ 7,6% là mức bỏ-đỉnh, 8,7% là trung vị, và một mức gần biên 13,84% hiện tại; đều là giả định minh họa) và xem giá trị nhạy ra sao, thay vì chọn một mức rồi coi là sự thật. Với bội số (009) hãy tính P/E trên lợi nhuận chuẩn hóa song song với P/E trên lợi nhuận báo cáo và nêu khoảng cách.

## Bài tập — làm trước khi mở đáp án

1. Vì sao P/E tính trên lợi nhuận một năm có thể gây hiểu nhầm với công ty chu kỳ ở đỉnh và ở đáy?
2. Thép Xanh: tính lợi nhuận mỗi năm từ doanh thu và biên ở mục 3.
3. Tính trung bình số tuyệt đối 5 năm và giải thích vì sao thấp hơn lợi nhuận năm 5.
4. Tính biên trung bình × doanh thu năm 5, và so sánh khi bỏ năm 1.
5. Tính biên trung vị × doanh thu năm 5 và mức chênh của lợi nhuận năm 5 so với chuẩn đó.
6. Nếu phải mất 3 năm mới về mức chuẩn 9,6 tỷ và r = 10%, giá trị quy về hiện tại là bao nhiêu?
7. HPG: tính biên LNST mẹ/doanh thu thuần của FY2023 và FY2025 (đơn vị tỷ VND, số ở mục "Ví dụ từ nguồn thật").
8. HPG: tính lợi nhuận chuẩn hóa FY2025 theo biên trung bình bỏ FY2021 và theo trung bình số tuyệt đối bỏ FY2021, rồi giải thích vì sao hai số khác nhau.
9. (Chuyển giao) Biên LNST/doanh thu 9 tháng 2026 của HPG là 13,84% (hợp nhất; nhóm thép 18.396/165.784). Tính biên nhóm thép và liệt kê bốn câu hỏi cần trả lời trước khi gọi đây là "đỉnh chu kỳ".
10. (Chuyển giao) Nêu một hướng sai của ROE trung bình × vốn chủ nay theo mỗi chiều (cao quá, thấp quá) khi công ty vừa đưa nhà máy mới vào hoạt động.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. Ở đỉnh, lợi nhuận cao nên P/E trông thấp; ở đáy, lợi nhuận thấp nên P/E trông cao. P/E thay đổi vì lợi nhuận, không vì giá trị công ty.
2. 10,8; 4,2; 4,0; 8,0; 12,0 tỷ.
3. `39,0/5 = 7,8`. Thấp hơn năm 5 vì năm 5 có doanh thu cao nhất (120) còn các năm đầu quy mô nhỏ; trung bình tuyệt đối không tính đến việc công ty đã lớn gấp đôi.
4. Biên TB `(18+6+5+8+10)/5 = 9,4%`, × 120 `= 11,28`. Bỏ năm 1: `(6+5+8+10)/4 = 7,25%`, × 120 `= 8,70`. Chênh khoảng 23%: nên bạn phải giải thích được năm 1 vì sao bất thường.
5. Trung vị của 18, 6, 5, 8, 10 là 8%; `8% × 120 = 9,6`. Lợi nhuận năm 5 cao hơn `12/9,6 − 1 = 25%`.
6. `9,6/1,1³ = 9,6/1,331 ≈ 7,21` tỷ.
7. FY2023: `6.835/118.953 = 5,75%`. FY2025: `15.453,2/156.116,1 = 9,90%`.
8. Biên trung bình bỏ FY2021 `(6,00+5,75+8,66+9,90)/4 = 7,58%` (theo số lẻ đầy đủ ra 7,577%), × 156.116,1 `≈ 11.826`. Trung bình tuyệt đối bỏ FY2021 `(8.484+6.835+12.021,4+15.453,2)/4 ≈ 10.698`. Khác nhau vì cách thứ nhất nhân biên các năm với doanh thu FY2025 (lớn hơn), cách thứ hai giữ số tuyệt đối cũ (doanh thu FY2022–FY2023 thấp hơn nhiều).
9. Biên nhóm thép `18.396/165.784 = 11,10%`. Ví dụ câu hỏi: (a) công suất thực chạy so với công suất lắp đặt; (b) giá bán trừ giá nguyên liệu các quý gần nhất; (c) chi phí lãi vay và khấu hao sau khi tài sản mới vào hoạt động; (d) phần lợi nhuận bất động sản (19% LNST) có lặp lại không, và có khoản bất thường một lần trong 9 tháng không. Chấp nhận câu hỏi khác nếu có lý do và nguồn kiểm được.
10. Cao quá: vốn mới chưa chạy hết công suất nên ROE lịch sử nhân vốn lớn hơn giả định mọi đồng vốn mới sinh lợi như đồng vốn cũ. Thấp quá: ROE các năm trước bị kéo thấp bởi vốn dở dang chưa sinh lời (mã 242 cuối FY2024: 63.655,9 tỷ), nên mức "chuẩn" lịch sử thấp hơn khả năng của vốn đã hoàn thành.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty thép M có lợi nhuận (tỷ đồng) các năm 2021–2025 là 3.450; 850; 680; 1.200; 1.545. Doanh thu FY2025 là 156 triệu đồng. Biên LNST 9 tháng 2026 là 13,8%. Chuẩn hóa lợi nhuận 2025 và cho biết 9 tháng 2026 có phải đỉnh."

Phát hiện: (a) lợi nhuận tỷ đồng nhưng doanh thu "triệu đồng": lệch đơn vị ba bậc; (b) thiếu doanh thu các năm trước nên không tính được biên; (c) không rõ lợi nhuận của mẹ hay hợp nhất; (d) 9 tháng 2026 chưa kiểm toán; (e) không biết vốn chủ nên không kiểm được đổi quy mô; (f) "có phải đỉnh" không trả lời được từ các con số này.

`Đáp án` Không chuẩn hóa được theo biên. Chỉ tính được trung bình số tuyệt đối 5 năm (`(3.450+850+680+1.200+1.545)/5 = 1.545`) và bỏ năm 2021 (`1.068,75`), kèm cảnh báo quy mô. Cần bổ sung doanh thu cùng đơn vị và phạm vi từng năm, vốn chủ, và nguồn kỳ 9 tháng; ghi `CHƯA_BIẾT` cho câu hỏi đỉnh hay không.

## Sai ở đâu

Một học viên viết: "HPG FY2025 lãi 15.453 tỷ. Trung bình 5 năm là 15.454 tỷ. Vậy FY2025 đúng mức bình thường, không cần chuẩn hóa. Chín tháng 2026 lãi 23.746 tỷ, đem nhân 4/3 ra 31.661 tỷ, cứ vậy mà định giá. P/E dùng giá hôm nay chia lợi nhuận đó."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. Trùng số giữa lợi nhuận FY2025 và trung bình năm năm là ngẫu nhiên; trung bình đó chứa năm 2021 có biên 23,03%, gấp khoảng ba lần trung bình bốn năm còn lại (7,58%).
2. Trung bình số tuyệt đối bỏ qua việc vốn chủ tăng khoảng 44,5% từ 2021 đến 2025.
3. Quy năm 9 tháng bằng 4/3 giả định quý cuối giống ba quý đầu; không có cơ sở.
4. 23.746 là LNST của bản tổng quan, nhiều khả năng số chung chưa kiểm toán, không phải lợi nhuận cổ đông công ty mẹ; hai khái niệm khác nhau (FY2025: 15.514,9 chung so với 15.453,2 mẹ). Và 13,84% hợp nhất trộn cả bất động sản (biên nhóm thép 11,10%).
5. Nếu 9 tháng 2026 là đỉnh chu kỳ thì P/E trên lợi nhuận quy năm trông thấp một cách giả tạo; còn có phải đỉnh hay không thì chưa biết. Thiếu nguồn và ngày của giá.
6. Không nêu điều kiện làm luận điểm mất hiệu lực.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Công ty có doanh thu 200, 220, 240 và lợi nhuận 20, 11, 24 (cùng đơn vị). Tính biên trung bình × doanh thu 240.
2. Cùng số liệu, tính trung bình số tuyệt đối và nêu một lý do nó có thể sai.
3. Nêu hai việc phải kiểm trước khi coi lợi nhuận của năm cuối là "bình thường".

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 biên `10%; 5%; 10%` trung bình `8,33%`, × 240 `= 20,0`. Câu 2 `(20+11+24)/3 = 18,33`; có thể sai nếu quy mô doanh thu đã đổi (200 lên 240). Câu 3: có năm cực đoan nào kéo trung bình không; quy mô hoặc cấu trúc chi phí đã đổi chưa; phạm vi (mẹ hay hợp nhất) và đơn vị có thống nhất không.

</details>

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ. Hòa Phát chỉ là dữ liệu thực hành.
- Mọi mức chuẩn hóa là phép tính trên quá khứ kèm giả định, không phải dự báo.
- Số 9 tháng 2026 chưa kiểm toán.
- Không có giá cổ phiếu hiện hành trong bài; người học tự lấy nguồn và ngày nếu cần.

## Điều tôi vẫn chưa hiểu

- Tôi chọn bao nhiêu năm để phủ một chu kỳ của ngành này, và vì sao?
- Quy mô mới của công ty đã đổi mức lợi nhuận chuẩn chưa?

## Nguồn Internet đã mở

Truy cập `2026-11-01`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Damodaran, *Investment Valuation* 3rd ed., chương 22 (PDF)](https://pages.stern.nyu.edu/~adamodar/pdfiles/val3ed/c22.pdf) | Phương pháp; bản in 2011; đã đọc trang 611–619 | Công ty chu kỳ, chuẩn hóa lợi nhuận, chiết khấu lùi |
| [BCTC hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) | FY2025 và cột FY2024; VND; VAS; đã đọc trang in 4–8 | Doanh thu, lợi nhuận, vốn chủ, tài sản cố định, vay |
| [Báo cáo thường niên 2023 của Hòa Phát](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) | FY2021–FY2023; tỷ VND làm tròn; trang tóm tắt chỉ số tài chính và báo cáo kết quả kinh doanh 2023 | Chuỗi lịch sử FY2021–FY2023 |
| [Tổng quan tình hình kinh doanh Q3/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/10/tong-quan-tinh-hinh-kinh-doanh-quy3-2026-vn.pdf) | Q3 và 9 tháng 2026; chưa kiểm toán | Số 9 tháng 2026 |

`CHƯA_BIẾT` Nguyên nhân của biên đỉnh FY2021, phạm vi các số 9 tháng (doanh thu có thể là doanh thu gộp, xem hồ sơ HPG), và việc FY2024 trình bày lại. `CHƯA_BIẾT` Trung vị, biên gia quyền và bỏ năm cực đoan là biến thể do bài này đề xuất, không phải công thức nêu nguyên văn ở chương 22; chưa có nguồn thứ hai độc lập cho từng biến thể.
