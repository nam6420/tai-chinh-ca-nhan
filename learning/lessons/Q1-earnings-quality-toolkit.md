# Bài Q1 — Chất lượng lợi nhuận có công cụ (Beneish, Altman, Piotroski)

- Ngày viết: `2026-11-01`; sửa sau kiểm duyệt vòng 2–6 ngày `2026-11-02`.
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Nguồn số HPG: báo cáo tài chính hợp nhất kiểm toán FY2025. **Hệ số Beneish lấy từ nguồn thứ cấp**; hệ số Altman đã đối chiếu với bản sao Altman (2000).
- Mục tiêu: Tính M-score, Z'' và F-score; đọc từng thành phần; phân biệt tín hiệu thật với hiệu ứng cơ học; viết kết luận không vượt quá bằng chứng.
- Bài trước liên quan: Chuỗi định lượng thực hành sau [Bài 012](012-scenarios-margin-of-safety.md) (**Bước 3/4 của chuỗi `Q4 → Q2 → Q1 → Q3`**) — học ngay sau [Bài Q2: Cổ phiếu thưởng nhân viên, pha loãng, mua lại và cổ tức](Q2-sbc-dilution-buybacks-dividends.md) và [Bài Q4: Lấy dữ liệu](Q4-getting-data-edgar-xbrl-vietnam.md) (kế thừa [Bài 004](004-cash-flow-and-earnings-quality.md), [Bài 005](005-debt-liquidity-survival.md) và [Bài 007](007-notes-and-accounting-red-flags.md)). Học tiếp: [Bài Q3: Chuẩn hóa lợi nhuận và công ty chu kỳ](Q3-normalizing-earnings-cyclical.md).
- Thời lượng: 3 phiên.
- Tệp thực hành: [earnings_quality.py](../practice/models/earnings_quality.py) và [hpg_fy2025_statements.csv](../practice/models/hpg_fy2025_statements.csv); kiểm bằng `python3 -m unittest discover tests`.
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/Q1-fact-check.md), [phản biện](../reviews/Q1-risk-review.md)
- Câu hỏi cốt lõi: **Báo cáo này có chỗ nào bất thường đáng đào sâu, và mỗi bất thường đó có lời giải thích đời thường nào không?**

## Hiểu bài này trong 1 phút

Bác sĩ đo huyết áp không kết luận bạn bị bệnh; con số cao chỉ nói "cần khám thêm". Ba điểm số này cũng vậy. Điểm cao là **lý do để mở thuyết minh và đọc kỹ**, không phải bằng chứng gian lận, càng không phải lệnh bán. Bài tính và đọc ba điểm trên báo cáo FY2025 của Hòa Phát, không kết luận gian lận hay khuyến nghị.

## Ôn bài cũ hoặc kiểm tra đầu vào

Ôn lại các bài liền trước ([Bài 004](004-cash-flow-and-earnings-quality.md), [Bài 005](005-debt-liquidity-survival.md), [Bài 007](007-notes-and-accounting-red-flags.md), [Bài Q4](Q4-getting-data-edgar-xbrl-vietnam.md) và [Bài Q2](Q2-sbc-dilution-buybacks-dividends.md)): vì sao khoảng cách giữa lợi nhuận sau thuế và dòng tiền hoạt động (`CFO`) ([Bài 004](004-cash-flow-and-earnings-quality.md)) cần được đọc cùng thuyết minh phải thu, tồn kho ([Bài 007](007-notes-and-accounting-red-flags.md)) và bảng số đã kiểm đẳng thức ([Bài Q4](Q4-getting-data-edgar-xbrl-vietnam.md))?

## 1. Ba công cụ, ba câu hỏi khác nhau

| Công cụ | Câu hỏi | Dữ liệu cần | Kết quả |
|---|---|---|---|
| Beneish M-score | Năm nay báo cáo có giống mẫu của những công ty từng bị phát hiện thổi phồng lợi nhuận không? | Hai năm báo cáo | Một số liên tục; điểm cao hơn ngưỡng là cờ |
| Altman Z (dạng Z'') | Công ty có giống những công ty từng phá sản không? | Một năm báo cáo | Một số liên tục, ba vùng |
| Piotroski F-score | Nền tảng tài chính của công ty đang mạnh lên hay yếu đi? | Hai năm báo cáo | Số nguyên 0–9 |

`SUY_LUẬN` Ba kết quả có thể không đi cùng nhau (mục 3); đừng gộp thành "điểm uy tín".

## 2. Cách tính

### 2.1 Beneish M-score

`SỰ_THẬT` (thứ cấp; chỉ xác nhận nội dung trang, không xác nhận độ đúng của mô hình) Trang [Wikipedia — Beneish M-score](https://en.wikipedia.org/wiki/Beneish_M-score) (mở 02/11/2026; trang dẫn Beneish 1999 qua một bản Scribd, không rõ bản quyền) ghi tám chỉ số so năm `t` với năm `t−1`: DSRI (phải thu trên doanh thu), GMI (biên gộp), AQI (chất lượng tài sản), SGI (tăng doanh thu), DEPI (khấu hao), SGAI (chi phí bán hàng và quản lý trên doanh thu), LVGI (đòn bẩy) và TATA (tổng dồn tích trên tổng tài sản). Công thức trang nêu: `M = −4,84 + 0,92·DSRI + 0,528·GMI + 0,404·AQI + 0,892·SGI + 0,115·DEPI − 0,172·SGAI + 4,679·TATA − 0,327·LVGI`, ngưỡng −1,78. Trang nói mô hình mang tính xác suất; mẫu loại công ty tài chính; và không định nghĩa "chứng khoán" trong AQI. Tôi không mở được toàn văn Beneish (1999) (tóm tắt công khai, toàn văn sau tường phí). `CHƯA_BIẾT` hệ số và ngưỡng có khớp bài gốc không; nguồn thứ cấp khác dùng thêm ngưỡng −2,22 và bất đồng về gốc của nó; một [nghiên cứu Ba Lan](https://czasopisma.uni.lodz.pl/foe/article/view/3090) (24 cặp công ty, chỉ đọc tóm tắt) thấy −2,22 đúng 71% và −1,98 đúng 75%.

Định nghĩa từng chỉ số (cùng trang Wikipedia):

| Chỉ số | Công thức |
|---|---|
| DSRI | `(Phải thu_t/Doanh thu_t) ÷ (Phải thu_{t−1}/Doanh thu_{t−1})` |
| GMI | `Biên gộp_{t−1} ÷ Biên gộp_t` |
| AQI | `[1 − (TSNH+TSCĐ+Chứng khoán)/TTS]_t ÷ [cùng biểu thức]_{t−1}` |
| SGI | `Doanh thu_t ÷ Doanh thu_{t−1}` |
| DEPI | `[KH/(TSCĐ+KH)]_{t−1} ÷ [KH/(TSCĐ+KH)]_t` |
| SGAI | `(CPBH+QLDN)/Doanh thu` của `t` ÷ của `t−1` |
| LVGI | `[(Nợ ngắn hạn+Vay dài hạn)/TTS]_t ÷ [cùng]_{t−1}` |
| TATA | `(Lợi nhuận − Dòng tiền hoạt động)/TTS_t` |

`PHÉP_TÍNH` `beneish()` trong [earnings_quality.py](../practice/models/earnings_quality.py) trả tám chỉ số và M.

### 2.2 Altman Z''

`SỰ_THẬT` (thứ cấp) [Wikipedia — Altman Z-score](https://en.wikipedia.org/wiki/Altman_Z-score) (mở 02/11/2026) ghi dạng không sản xuất (ký hiệu Z'' theo Altman 2000) `Z'' = 6,56·X1 + 3,26·X2 + 6,72·X3 + 1,05·X4` và dạng thị trường mới nổi cộng hằng số 3,25 vào công thức đó; cùng vùng an toàn trên 2,6, xám 1,1–2,6, nguy cơ dưới 1,1. `X1 = (TSNH − Nợ ngắn hạn)/TTS`, `X2 = Lợi nhuận giữ lại/TTS`, `X3 = EBIT/TTS`, `X4 = Vốn chủ sổ sách/Tổng nợ`. Trang nói mô hình không dùng cho công ty tài chính và độ chính xác bị cho là phóng đại. Bản sao Altman (2000) (đã mở): hệ số, hằng số 3,25 và "emerging market scoring model" khớp; cận 2,6/1,1 không thấy trong bản đã đọc. Altman (2017) và độ chính xác tại Việt Nam `CHƯA_BIẾT`.

### 2.3 Piotroski F-score

`SỰ_THẬT` Bài gốc [Piotroski (2000), *Value Investing...*](https://www.chicagobooth.edu/~/media/FE874EE65F624AAEBD0166B1974FD74D.pdf) (Univ. of Chicago Selected Paper 84; mở 02/11/2026), mục 2.3: chín tín hiệu nhị phân, F_SCORE 0–9. Lợi nhuận: ROA dương, CFO dương, ROA tăng, CFO lớn hơn ROA. Đòn bẩy và thanh khoản: tỷ lệ nợ dài hạn (gồm phần đến hạn) trên tài sản bình quân giảm, thanh toán hiện hành tăng, không phát hành cổ phiếu phổ thông. Hiệu quả: biên gộp tăng, vòng quay tài sản tăng. ROA, CFO, vòng quay chia cho tổng tài sản **đầu năm** (bảng biến ghi vòng quay theo tài sản bình quân; HPG kết quả không đổi). ROA dùng mã 60 (gồm cổ đông không kiểm soát). Tóm tắt: chọn công ty mạnh trong nhóm sổ sách/thị giá cao tăng lợi suất trung bình ít nhất 7,5% mỗi năm, mua-bán chênh lệch 23% mỗi năm 1976–1996; phạm vi là cổ phiếu giá trị. Bài gốc không nói cổ tức bằng cổ phiếu có tính là phát hành hay không; bài báo cả hai.

`SUY_LUẬN` Kết quả của Piotroski là lợi suất cổ phiếu Mỹ, không phải bằng chứng cho Việt Nam; bài dùng F-score như chín câu hỏi về xu hướng, không như tín hiệu mua.

## 3. Ví dụ hư cấu: Công ty Cờ Đỏ

`KỊCH_BẢN` Số liệu hư cấu (tỷ đồng):

| Chỉ tiêu | Năm t−1 | Năm t |
|---|---:|---:|
| Doanh thu / giá vốn | 1.000 / 700 | 1.300 / 960 |
| Phải thu | 150 | 330 |
| Tài sản ngắn hạn / TSCĐ | 500 / 400 | 700 / 410 |
| Tổng tài sản | 1.200 | 1.500 |
| Khấu hao | 40 | 38 |
| CPBH + QLDN | 100 | 135 |
| Nợ ngắn hạn / vay dài hạn | 300 / 200 | 450 / 250 |
| Lợi nhuận ròng / CFO | 80 / 90 | 150 / 20 |
| Lợi nhuận giữ lại / vốn chủ | 300 / 700 | 380 / 800 |

Tổng tài sản đầu năm 1.100 và 1.200; không phát hành cổ phiếu. `PHÉP_TÍNH` DSRI `= (330/1.300)/(150/1.000) = 1,692`; GMI `= 1,147`; AQI `= 1,04`; SGI `= 1,3`; DEPI `= 1,072`; SGAI `= 1,038`; LVGI `= 1,12`; TATA `= (150 − 20)/1.500 = 0,0867`. **M ≈ −1,11**, cao hơn −1,78 nên bị cờ; DSRI đóng góp `0,92 × 1,692 ≈ 1,56` và TATA `4,679 × 0,0867 ≈ 0,41`. Z'': `X1 = 0,167`, `X2 = 0,253`, `X3 = 210/1.500 = 0,14` (EBIT giả định 210), `X4 = 1,143`, `Z'' ≈ 4,06`, vùng an toàn. F-score `= 5`: đạt ROA dương, CFO dương, ROA tăng (`12,5%` so với `7,3%`), vòng quay tăng, không phát hành cổ phiếu; trượt dồn tích, biên gộp, đòn bẩy, thanh toán hiện hành. Không có nguy cơ vỡ nợ gần mà chất lượng lợi nhuận vẫn đáng ngờ.

## Ví dụ từ nguồn thật

Ca thực hành: tập đoàn Hòa Phát (HPG), báo cáo tài chính hợp nhất FY2025 kiểm toán bởi Deloitte, [tải từ trang công ty](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf). Đơn vị gốc VND, quy đổi sang tỷ VND. Ca này **không** nghi ngờ HPG gian lận.

`SỰ_THẬT` Ý kiến kiểm toán (trang in 4): Deloitte, ngày 24/03/2026, không ngoại trừ (trung thực và hợp lý trên các khía cạnh trọng yếu); FY2024 do công ty kiểm toán khác kiểm toán. Số chính (tỷ VND; 2025 / 2024): doanh thu thuần 156.116,1 / 138.855,1; phải thu khách hàng (mã 131) 10.971,8 / 4.352,1; TSCĐ hữu hình 133.420,8 / 67.244,2; tổng tài sản 257.899,2 / 224.489,7; lợi nhuận sau thuế 15.514,9 / 12.020,0; dòng tiền hoạt động 17.365,9 / 6.608,3. Đủ chỉ tiêu trong [hpg_fy2025_statements.csv](../practice/models/hpg_fy2025_statements.csv); năm trước là cột "năm trước" của báo cáo FY2025.

`PHÉP_TÍNH` Tám chỉ số và M-score của HPG năm 2025 (cách ánh xạ A: AQI không cộng "chứng khoán" riêng vì tài sản ngắn hạn mã 100 **đã gồm** đầu tư tài chính ngắn hạn mã 120; xem dưới):

| Chỉ số | Giá trị | Đóng góp vào M (hệ số × giá trị) |
|---|---:|---:|
| DSRI | 2,242 | +2,063 |
| GMI | 0,849 | +0,448 |
| AQI | 0,257 | +0,104 |
| SGI | 1,124 | +1,003 |
| DEPI | 1,565 | +0,180 |
| SGAI | 0,932 | −0,160 |
| LVGI | 1,035 | −0,339 |
| TATA | −0,007 | −0,034 |
| **M** | **−1,575** | (hằng số −4,84) |

M `= −1,575` cao hơn ngưỡng −1,78 một khoảng **0,21**, tức công cụ gắn cờ. Ba điều cần đọc kỹ trước khi nói thêm.

**Một: DSRI chi phối.** Phải thu khách hàng tăng 152,1% (4.352,1 lên 10.971,8) trong khi doanh thu tăng 12,4%. DSRI bằng 1 cho M `−2,72`; M đúng −1,78 khi DSRI `≈ 2,02` (thật 2,24). Thay mã 131 bằng tổng phải thu ngắn hạn (mã 130: 15.042,3 và 7.647,8) thì DSRI còn 1,749 và M về −2,03: dưới ngưỡng −1,78 nhưng trên −2,22. Hai trục: (mã 131; −1,78) gắn cờ, (mã 130; −1,78) không, (mã 131; −2,22) gắn cờ, (mã 130; −2,22) gắn cờ. Nguồn thứ cấp bất đồng về gốc của −2,22, nên kết quả phụ thuộc cả định nghĩa phải thu lẫn ngưỡng (cặp đúng cho kế toán Việt Nam `CHƯA_BIẾT`).

**Hai: AQI và DEPI phụ thuộc ánh xạ.** Thuyết minh số 12 (trang in 29): năm 2025 có 73.824,2 tỷ VND công trình **hoàn thành** chuyển sang TSCĐ hữu hình (nguyên giá 108.146,6 lên 182.308,7 tỷ); dở dang (mã 242) giảm từ 63.655,9 xuống 10.721,1 tỷ. Phần tài sản ngoài tài sản ngắn hạn và TSCĐ hữu hình giảm từ 31,4% xuống 8,1% tổng tài sản, nên AQI `= 0,257`; DEPI `= 1,565` vì TSCĐ hữu hình gần gấp đôi còn khấu hao tăng 22%. `SUY_LUẬN` Đó là dở dang chuyển thành TSCĐ, chưa phải chỉnh khấu hao (chưa đọc thuyết minh chính sách khấu hao). Hiệu ứng này phụ thuộc ánh xạ: coi dở dang (mã 240) là PP&E và "chứng khoán" là mã 250 cho AQI `= 1,003`, DEPI `= 0,906`, M `= −1,349` (ánh xạ C; ánh xạ B, chỉ cộng mã 250, cho AQI `= 0,230`, M `= −1,586`). Cả ba cách ánh xạ đều trên −1,78 (cách 0,19 đến 0,43). Định nghĩa TATA chưa được thử: `SUY_LUẬN` chưa kiểm: một định nghĩa dồn tích theo bảng cân đối có thể kéo M sát ngưỡng; `PHÉP_TÍNH` hệ số 4,679 nên TATA chỉ cần lệch `0,205/4,679 ≈ 0,044` (4,4% tổng tài sản) là đổi kết luận cờ; `CHƯA_BIẾT` công thức gốc.

**Ba: lỗi của chính bài này.** Bản đầu cộng mã 120 lần thứ hai vào "chứng khoán" dù mã 100 đã gồm nó (`8.300,9 + 19.484,4 + 15.042,3 + 52.828,2 + 8.003,5 = 103.659,4`), cho AQI 0,023 và M −1,669. Hãy cộng lại thành phần của mọi tỷ lệ.

`SỰ_THẬT` Thuyết minh số 7 (trang in 26), phải thu khách hàng cuối năm (đầu năm), tỷ VND: năm khách hàng nêu tên: Marcegaglia Carbon Steel 1.837,3 (482,4); Thép Minh Phú – Hải Dương 1.641,2 (không số); Thép Minh Phú 679,3 (không số); Kim Khí Nam Hưng 592,6 (60,7); Hoa Sen 617,3 (218,6); khách hàng khác 5.604,1 (3.590,4). `PHÉP_TÍNH` Năm khách hàng nêu tên chiếm `5.367,7/10.971,8 = 48,9%` phải thu cuối năm, so với `761,7/4.352,1 = 17,5%` đầu năm (ô không số coi là bằng 0, chưa xác nhận); nhóm "khác" cũng tăng 56%, nhanh hơn doanh thu 12,4%. `SUY_LUẬN` Tên gọi gợi ngành thép. Nguyên nhân không có trong báo cáo: `CHƯA_BIẾT`.

`SỰ_THẬT` Báo cáo lưu chuyển tiền tệ (trang in 9): dòng tiền hoạt động 17.365,9 tỷ, cao hơn lợi nhuận sau thuế 15.514,9 tỷ; các điều chỉnh gồm khấu hao 8.470,7, lãi vay 3.114,9, thay đổi các khoản phải thu −8.743,1, hàng tồn kho −7.241,8 và các khoản phải trả +11.393,2 tỷ (phải trả người bán ngắn hạn tăng từ 14.046,8 lên 21.183,4 tỷ). `PHÉP_TÍNH` TATA `= (15.514,9 − 17.365,9)/257.899,2 = −0,0072`. `SUY_LUẬN` Khấu hao lớn và khoản phải trả tăng giúp dòng tiền vượt lợi nhuận; chưa biết khoản phải trả tăng có bền không.

**Altman Z'' và F-score của HPG.** `PHÉP_TÍNH` `X1 = 0,0367`, `X2 = 51.037,9/257.899,2 = 0,1979` (lợi nhuận chưa phân phối, mã 421), `X3 = (18.040,6 + 3.114,9)/257.899,2 = 0,0820` (EBIT xấp xỉ bằng lợi nhuận trước thuế cộng lãi vay), `X4 = 131.220,0/126.679,2 = 1,0358`. Dạng không hằng số: Z'' `≈ 2,525`, vùng xám sát cận trên 2,6; dạng thị trường mới nổi (cộng 3,25): `≈ 5,775`. Altman (2000, bản sao) xác nhận hệ số và hằng số 3,25 (đưa điểm 0 về trái phiếu xếp hạng D); cận vùng 2,6 và 1,1 chỉ có ở Wikipedia. Đọc 5,775 là "an toàn" (giữ cận 2,6 sau khi cộng 3,25) không nhất quán; nếu vùng dịch theo hằng số (cận 5,85 và 4,35, phép cộng của bài) thì cả hai biến thể đều xám. Bảng 7 của Altman (2000) liên hệ điểm EM với hạng trái phiếu Mỹ năm 1994: 5,775 nằm giữa BBB− (5,65) và BBB (5,85), chưa hiệu chỉnh cho Việt Nam, VAS hay rủi ro tiền tệ và ngành mà Altman yêu cầu. Mô hình Z' dành cho công ty sản xuất (có X5 doanh thu/tài sản `= 0,605`; hệ số 0,717/0,847/3,107/0,420/0,998; vùng xám 1,23–2,90) cho HPG `Z' ≈ 1,49` (`PHÉP_TÍNH`), vùng xám nhưng thấp hơn nhiều Z''. Đổi mô hình đổi cả mức lẫn vùng; mô hình nào hợp công ty thép ở thị trường mới nổi là `CHƯA_BIẾT`. F-score: `6/9` nếu cổ tức năm 2024 trả bằng cổ phiếu tỷ lệ 20%, thực hiện năm 2025 (thuyết minh số 26) không tính là phát hành cổ phiếu, `5/9` nếu tính; trượt ba tín hiệu: vòng quay tài sản (0,739 xuống 0,695), thanh toán hiện hành (1,152 xuống 1,101) và đòn bẩy. Piotroski (2000) định nghĩa LEVER là nợ dài hạn gồm cả phần đến hạn trên tổng tài sản bình quân: `(27.479,2 + 8.826,2)/241.194,5 = 15,05%` năm 2025 so với `(27.080,4 + 3.298,8)/206.136,4 = 14,74%` năm 2024 (nợ dài hạn đến hạn trả từ thuyết minh 23, trang in 35); đòn bẩy tăng nên tín hiệu trượt. Chỉ lấy mã 338 thì tỷ lệ giảm 13,1% xuống 11,4% và F là 7/6, nhưng lệch bài gốc (`lever_def="hep"`). Đạt các tín hiệu còn lại, trong đó biên gộp tăng 13,3% lên 15,7%. Báo cáo lưu chuyển tiền tệ không có khoản thu từ phát hành cổ phiếu của công ty mẹ. `CHƯA_BIẾT` ROA 2024 dùng tổng tài sản cuối 2023 (187.783 tỷ, báo cáo thường niên 2023) trong khi cột FY2024 có thể đã trình bày lại; tín hiệu "ROA tăng" kém chắc hơn.

**Tỷ lệ nền, độ nhạy.** `SỰ_THẬT` (chỉ đọc phần tóm tắt) Hai nghiên cứu (cùng dùng M-score, cùng nhóm tác giả, cùng kỳ 2013–2014; mẫu 229 và 468 công ty có thể chồng lấn, `SUY_LUẬN`) về công ty phi tài chính niêm yết ở Việt Nam báo cáo 48,4% và khoảng 40% **bị gắn cờ** là có điều chỉnh lợi nhuận; chưa biết ngưỡng. `SUY_LUẬN` Mô hình gắn cờ gần nửa mẫu nên một cờ mang ít thông tin (không phải tỷ lệ gian lận). Một nghiên cứu 2016–2024 (M-score cao, lợi suất thấp hơn) chưa mở được toàn văn. Điều làm đổi kết luận "phải thu tăng": tiền thu sau khóa sổ, hợp đồng, bên liên quan, dự phòng nợ khó đòi (mã 137 giảm từ 160,0 xuống 132,5 tỷ khi phải thu tăng; điểm để hỏi), đổi kiểm toán, và trình bày lại (cột nợ phải trả và vốn chủ năm trước ghi "Trình bày lại", trang in 7; nội dung `CHƯA_BIẾT`). EBIT ở X3 bằng lợi nhuận trước thuế cộng lãi vay nên gồm thu nhập tài chính (2.081,8 tỷ); loại khoản đó (một chiều, chưa loại 1.488,7 tỷ chi phí tài chính ngoài lãi vay) chỉ hạ Z'' xuống khoảng 2,47. Độ nhạy lớn hơn nằm ở X2: năm 2025 cổ tức bằng cổ phiếu chuyển 12.792,2 tỷ từ lợi nhuận chưa phân phối sang vốn góp (thuyết minh 26); cộng lại thì `X2 = 0,2475` và Z'' `≈ 2,69`, qua 2,6 (`PHÉP_TÍNH`; cận 2,6 chỉ có ở Wikipedia). X1 thấp mang tính cấu trúc với công ty nhiều TSCĐ. Tỷ lệ sổ sách/thị giá của HPG `CHƯA_BIẾT` (cần giá cùng ngày), nên chưa biết HPG có thuộc nhóm Piotroski nghiên cứu.

**Kết luận được phép viết.** `Ý_KIẾN` "Theo hệ số và ngưỡng trên Wikipedia (chưa đối chiếu bài gốc), M-score FY2025 của HPG khoảng −1,57, cao hơn ngưỡng −1,78 khoảng 0,2, chủ yếu do phải thu khách hàng tăng nhanh hơn doanh thu; kết quả đổi theo định nghĩa phải thu và cách ánh xạ tài sản. Dòng tiền hoạt động vẫn cao hơn lợi nhuận. Cần đọc thêm điều khoản bán hàng và bên liên quan trước khi nói gì thêm." Không được viết: "HPG thổi phồng lợi nhuận."

## 4. Nhiễu và giới hạn

Trước khi tin một chỉ số: (1) quy mô đổi (công trình hoàn thành, mua bán công ty) làm AQI, DEPI, LVGI, SGI nhảy cơ học; (2) định nghĩa khoản mục (phải thu khách hàng hay tổng phải thu; "chứng khoán" là mã nào; khấu hao trong lưu chuyển tiền tệ gồm cả phân bổ lợi thế thương mại và thuê đất, còn mẫu số chỉ có TSCĐ hữu hình); nhất quán giữa hai năm quan trọng hơn chọn đúng mã; (3) nhiều khoản của VAS không có chỗ tương ứng chuẩn trong công thức xây trên số liệu Mỹ.

`SUY_LUẬN` Beneish và Altman bỏ ngân hàng, bảo hiểm, chứng khoán (theo Wikipedia); F-score thiết kế cho cổ phiếu có tỷ lệ sổ sách/thị giá cao (HPG có thuộc nhóm đó hay không là `CHƯA_BIẾT`). Z'' đổi mạnh khi chia cổ phiếu thưởng hay lỗ lớn (X2). F-score cho biết tiến hay lùi, không cho biết mức.

**Quy trình đọc.** In từng thành phần, tìm biến đóng góp lớn nhất và hỏi có giải thích cơ học không; cộng lại thành phần của mọi tỷ lệ; mở thuyết minh và đối chiếu dòng tiền; nhìn nhiều kỳ; dùng nhãn đúng mức.

## Bài tập — làm trước khi mở đáp án

1. Mỗi công cụ (M-score, Z'', F-score) trả lời câu hỏi nào, và vì sao điểm của chúng có thể mâu thuẫn?
2. Cờ Đỏ: tính DSRI từ bảng ở mục 3.
3. Cờ Đỏ: tính TATA và nói điều nó gợi ý.
4. Cờ Đỏ: biết DSRI 1,6923; GMI 1,1471; AQI 1,04; SGI 1,3; DEPI 1,0718; SGAI 1,0385; LVGI 1,12; TATA 0,0867; tính M.
5. Cờ Đỏ: tính Z'' năm t và cho biết vùng.
6. Cờ Đỏ: hai tín hiệu Piotroski nào trượt trong nhóm dồn tích và thanh khoản? Giải thích.
7. HPG: tính DSRI từ doanh thu thuần và phải thu khách hàng (mã 131) của hai năm.
8. HPG: phải thu tăng bao nhiêu phần trăm, doanh thu tăng bao nhiêu? Biết M hiện −1,575 và mỗi điểm DSRI đóng góp 0,92 vào M, DSRI cần bằng bao nhiêu để M đạt −1,78?
9. Nêu ba lời giải thích không liên quan thao túng cho việc phải thu tăng nhanh hơn doanh thu và với mỗi lời giải thích, nêu tài liệu cần mở để kiểm.
10. Dùng thuyết minh số 12 và bảng cân đối của HPG giải thích vì sao AQI chỉ bằng 0,257 và vì sao việc đó chưa phải dấu hiệu thao túng; nêu một cách ánh xạ khác làm AQI đổi hẳn.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. M-score: giống mẫu thổi phồng lợi nhuận; Z'': giống mẫu phá sản; F-score: nền tảng đang mạnh hay yếu đi. Mâu thuẫn vì đo ba đối tượng khác nhau (mục 1).
2. `(330/1.300)/(150/1.000) = 0,2538/0,15 = 1,692`.
3. `(150 − 20)/1.500 = 0,0867`. Lợi nhuận cao hơn dòng tiền hoạt động; dồn tích dương lớn gợi ý lợi nhuận chưa thành tiền.
4. `M = −4,84 + 1,557 + 0,606 + 0,420 + 1,160 + 0,123 − 0,179 + 0,406 − 0,366 ≈ −1,11`.
5. `X1 = 250/1.500 = 0,1667`; `X2 = 0,2533`; `X3 = 0,14`; `X4 = 1,1429`; `Z'' = 1,093 + 0,826 + 0,941 + 1,2 = 4,06`, vùng an toàn (trên 2,6).
6. Dồn tích: CFO/TTS đầu năm `= 20/1.200 = 1,7%` nhỏ hơn ROA `= 150/1.200 = 12,5%`, nên trượt. Thanh khoản: `700/450 = 1,556` thấp hơn `500/300 = 1,667`, nên trượt.
7. `(10.971,8/156.116,1)/(4.352,1/138.855,1) = 0,07028/0,03134 = 2,242`.
8. Phải thu `10.971,8/4.352,1 − 1 = +152,1%`; doanh thu `+12,4%`. M hiện `−1,575`; cần giảm 0,205; nên DSRI ngưỡng `= 2,242 − 0,205/0,92 ≈ 2,02`.
9. Ví dụ: giao hàng cuối năm (xem ngày giao); kéo dài điều khoản thanh toán (xem hợp đồng); đổi cơ cấu khách hàng (xem báo cáo bộ phận).
10. Năm 2025 có 73.824,2 tỷ VND công trình hoàn thành chuyển vào TSCĐ hữu hình. Phần tài sản ngoài tài sản ngắn hạn (mã 100, đã gồm đầu tư ngắn hạn) và TSCĐ hữu hình: `1 − (103.659,4 + 133.420,8)/257.899,2 = 8,1%` năm 2025 so với `1 − (86.674,3 + 67.244,2)/224.489,7 = 31,4%` năm 2024, tỷ lệ `0,081/0,314 ≈ 0,257`; sụt vì dở dang chuyển sang TSCĐ; coi mã 240 là PP&E và mã 250 là "chứng khoán" thì AQI `≈ 1,00`.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty thép N năm 2025: doanh thu 156.116 tỷ, phải thu ngắn hạn 15.042 tỷ (tổng phải thu). Năm 2024: doanh thu 138.855 tỷ, phải thu khách hàng 4.352 tỷ. Tính DSRI và kết luận có gắn cờ không. (Bảy chỉ số còn lại trùng bảng HPG.)"

Phát hiện: (a) hai năm dùng hai định nghĩa phải thu; (b) không biết "phải thu khác" gồm gì; (c) thiếu dự phòng; (d) chưa biết cùng phạm vi hợp nhất không.

`Đáp án` Dùng nhầm định nghĩa cho DSRI `= (15.042/156.116)/(4.352/138.855) = 3,07`, quá cao và vô nghĩa. Nhất quán theo phải thu khách hàng cho 2,24, theo tổng phải thu cho 1,75; M là −1,57 và −2,03, một cách trên ngưỡng −1,78 một cách dưới. Chọn một định nghĩa, ghi rõ, và báo cáo cả hai khi kết luận phụ thuộc.

## Sai ở đâu

Một học viên viết: "M-score của HPG FY2025 là −1,67, cao hơn −1,78, nên Hòa Phát thổi phồng lợi nhuận. Z'' 2,5 là vùng xám nên sắp có vấn đề tài chính. F-score nên mua. DSRI 2,24 chứng tỏ phải thu ảo. AQI tôi tính từ tài sản ngắn hạn cộng đầu tư ngắn hạn cộng TSCĐ."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. Vượt ngưỡng không phải bằng chứng; ngưỡng không phân biệt thao túng với thay đổi kinh doanh.
2. Bỏ qua việc kết quả phụ thuộc định nghĩa phải thu (tổng phải thu cho M −2,03); cộng đầu tư ngắn hạn hai lần vào AQI (đã nằm trong tài sản ngắn hạn) nên M −1,67 sai.
3. Bỏ qua dòng tiền cao hơn lợi nhuận; phải thu dồn vào vài khách hàng cần giải thích, chưa là kết luận.
4. Z'' vùng xám là chưa phân biệt, không phải "sắp có vấn đề"; vùng của biến thể thị trường mới nổi chưa rõ.
5. "F-score cao nên mua" là khuyến nghị cá nhân hóa (nghiên cứu trên cổ phiếu giá trị Mỹ 1976–1996).
6. "Phải thu ảo" là kết luận về động cơ không có bằng chứng.

</details>

## Kiểm tra chuyển bài

1. Doanh thu 500 và 600; phải thu 50 và 90 (năm t−1 và t). Tính DSRI.
2. Lợi nhuận 80, CFO 30, tổng tài sản cuối năm 400. Tính TATA và nêu ý nghĩa.
3. Nêu hai việc phải làm trước khi viết "công ty bị cờ M-score" vào một báo cáo nghiên cứu.

<details>
<summary>Mở sau khi tự làm</summary>

Đạt khi đúng cả ba: câu 1 `(90/600)/(50/500) = 0,15/0,10 = 1,5`. Câu 2 `(80 − 30)/400 = 0,125`; cần xem phải thu, tồn kho, chi phí trả trước. Câu 3: in từng thành phần, tìm hiệu ứng cơ học, mở thuyết minh và dòng tiền, kiểm định nghĩa nhất quán, ghi nguồn và nhãn.

</details>

## Ranh giới an toàn

- Không phải khuyến nghị mua/bán/nắm giữ hay cáo buộc; Hòa Phát chỉ là dữ liệu thực hành (báo cáo FY2025 có ý kiến kiểm toán không ngoại trừ).

## Điều tôi vẫn chưa hiểu

- Mã VAS nào tương ứng đúng với "phải thu", "chứng khoán", "khấu hao" của mô hình gốc, và ngưỡng nào hợp thị trường tôi quan tâm?

## Nguồn Internet đã mở

Truy cập `2026-11-01` và `2026-11-02`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Piotroski (2000), Selected Paper 84, Univ. of Chicago](https://www.chicagobooth.edu/~/media/FE874EE65F624AAEBD0166B1974FD74D.pdf) | Gốc; Hoa Kỳ 1976–1996; cổ phiếu có tỷ lệ sổ sách/thị giá cao | Định nghĩa chín tín hiệu F-score, phạm vi mẫu |
| [Wikipedia — Beneish M-score](https://en.wikipedia.org/wiki/Beneish_M-score) | Thứ cấp; trang có thông báo thiếu trích dẫn | Tám chỉ số, hệ số, ngưỡng −1,78 (chưa đối chiếu bài gốc) |
| [Wikipedia — Altman Z-score](https://en.wikipedia.org/wiki/Altman_Z-score) | Thứ cấp | Công thức Z'' và các vùng (chưa đối chiếu bài gốc) |
| [BCTC hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) | FY2025 và cột năm trước; VND; VAS; đã đọc trang in 4–10, 26–27, 29–30 | Mọi số HPG, thuyết minh 7 và 12, ý kiến kiểm toán |
| [Báo cáo thường niên 2023 của Hòa Phát](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) | Tóm tắt chỉ số FY2023, tỷ VND | Tổng tài sản cuối FY2023 (187.783 tỷ) dùng cho ROA FY2024 |

Đã mở thêm (02/11/2026): [Altman (2000), bản sao](https://moodle2.units.it/pluginfile.php/322514/mod_resource/content/0/Zscores.pdf); tóm tắt Beneish (1999) trên [CFA Institute](https://rpc.cfainstitute.org/research/financial-analysts-journal/1999/the-detection-of-earnings-manipulation); tóm tắt [VNU](https://js.vnu.edu.vn/EAB/article/view/1287) và [Accounting and Taxation 2018](https://ideas.repec.org/a/ibf/acttax/v10y2018i1p39-49.html); thuyết minh 23 của BCTC HPG. `CHƯA_BIẾT` Beneish (1999) và Altman (1968) toàn văn.
