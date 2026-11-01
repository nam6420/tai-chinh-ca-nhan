# BẢN NHÁP - CHƯA KIỂM DUYỆT: Bài Q1 — Chất lượng lợi nhuận có công cụ (Beneish, Altman, Piotroski)

- Ngày viết: `2026-11-01`. Bài mới của Đợt 3; chưa có biên bản kiểm nguồn hay phản biện.
- Chốt dữ liệu lúc: `2026-11-01 (Asia/Ho_Chi_Minh)`
- Nguồn số HPG: báo cáo tài chính hợp nhất kiểm toán FY2025, mở ngày `2026-11-01`. Nguồn phương pháp ở bảng cuối bài; **hệ số Beneish và Altman lấy từ nguồn thứ cấp**, bài gốc bị chặn sau tường phí.
- Mục tiêu: Tính ba điểm sàng lọc (M-score, Z'' và F-score) từ báo cáo tài chính; đọc từng thành phần thay vì chỉ nhìn tổng điểm; phân biệt tín hiệu thật với hiệu ứng cơ học do đổi quy mô hay định nghĩa; viết kết luận không vượt quá bằng chứng.
- Bài trước liên quan: 004, 005, 007. Học tiếp Q3.
- Thời lượng: 3 phiên (A: mục 1–3; B: mục 4–6; C: bài tập).
- Tệp thực hành: [earnings_quality.py](../practice/models/earnings_quality.py) và [hpg_fy2025_statements.csv](../practice/models/hpg_fy2025_statements.csv); kiểm bằng `python3 -m unittest discover tests`.
- Kiểm nguồn: `CHƯA`
- Phản biện rủi ro: `CHƯA`
- Câu hỏi cốt lõi: **Báo cáo này có chỗ nào bất thường đáng đào sâu, và mỗi bất thường đó có lời giải thích đời thường nào không?**

## Hiểu bài này trong 1 phút

Bác sĩ đo huyết áp không kết luận bạn bị bệnh; con số cao chỉ nói "cần khám thêm". Ba điểm số trong bài này cũng vậy. Chúng biến một đống số kế toán thành vài chỉ số so sánh năm nay với năm trước, rồi đối chiếu với một ngưỡng rút ra từ dữ liệu quá khứ. Điểm cao là **lý do để mở thuyết minh và đọc kỹ**, không phải bằng chứng gian lận, càng không phải lệnh bán. Bài dạy cách tính, đọc từng thành phần và viết kết luận khiêm tốn.

## Ôn bài cũ hoặc kiểm tra đầu vào

1. 004: lợi nhuận kế toán cao hơn dòng tiền hoạt động nhiều năm liền gợi ý gì?
2. 007: kể một cờ đỏ trong thuyết minh liên quan phải thu.

<details>
<summary>Mở sau khi tự làm</summary>

(1) phần lớn lợi nhuận chưa thành tiền; cần xem nguyên nhân; (2) phải thu tăng nhanh hơn doanh thu, dồn vào ít khách hàng hoặc bên liên quan.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Dạy tính và đọc M-score, Z'' và F-score trên báo cáo kiểm toán FY2025 của Hòa Phát (HPG), kèm thuyết minh | Không kết luận công ty nào gian lận hay sắp phá sản; không khuyến nghị mua/bán/nắm giữ |
| Cho thấy điểm vượt ngưỡng vẫn có thể có lời giải thích vô hại; dạy bài "bẩn" | Không kiểm độ chính xác của ba mô hình tại Việt Nam; chưa dạy kiểm tra tuần tự nhiều kỳ |

## 1. Ba công cụ, ba câu hỏi khác nhau

| Công cụ | Câu hỏi | Dữ liệu cần | Kết quả |
|---|---|---|---|
| Beneish M-score | Năm nay báo cáo có giống mẫu của những công ty từng bị phát hiện thổi phồng lợi nhuận không? | Hai năm báo cáo | Một số liên tục; điểm cao hơn ngưỡng là cờ |
| Altman Z (dạng Z'') | Công ty có giống những công ty từng phá sản không? | Một năm báo cáo | Một số liên tục, ba vùng |
| Piotroski F-score | Nền tảng tài chính của công ty đang mạnh lên hay yếu đi? | Hai năm báo cáo | Số nguyên 0–9 |

`SUY_LUẬN` Mỗi công cụ trả lời một câu hỏi, nên ba kết quả có thể không đi cùng nhau. Một công ty thổi phồng lợi nhuận vẫn có thể có Z'' "an toàn" (ví dụ hư cấu ở mục 3 cho đúng kết quả này), và công ty có F-score cao vẫn có thể bị cờ ở M-score. Đừng gộp ba điểm thành một "điểm uy tín".

## 2. Cách tính

### 2.1 Beneish M-score

`SỰ_THẬT` (thứ cấp) Trang [Wikipedia — Beneish M-score](https://en.wikipedia.org/wiki/Beneish_M-score) (mở 01/11/2026) ghi tám chỉ số so năm `t` với năm `t−1`: DSRI (phải thu trên doanh thu), GMI (biên gộp), AQI (chất lượng tài sản), SGI (tăng doanh thu), DEPI (khấu hao), SGAI (chi phí bán hàng và quản lý trên doanh thu), LVGI (đòn bẩy) và TATA (tổng dồn tích trên tổng tài sản). Công thức trang nêu: `M = −4,84 + 0,92·DSRI + 0,528·GMI + 0,404·AQI + 0,892·SGI + 0,115·DEPI − 0,172·SGAI + 4,679·TATA − 0,327·LVGI`, ngưỡng −1,78 (trên ngưỡng: khả năng thổi phồng cao). Trang này dẫn bài gốc của Beneish (1999, *Financial Analysts Journal*), nhưng trang chính thức của tạp chí chỉ cho hội viên, và tôi chưa đối chiếu từng hệ số với bài gốc. `CHƯA_BIẾT` hệ số và ngưỡng có khớp bài gốc không, và các nguồn khác có dùng ngưỡng khác không.

Định nghĩa từng chỉ số (cùng trang Wikipedia):

| Chỉ số | Công thức | Đọc thế nào |
|---|---|---|
| DSRI | `(Phải thu_t/Doanh thu_t) ÷ (Phải thu_{t−1}/Doanh thu_{t−1})` | >1: phải thu tăng nhanh hơn doanh thu |
| GMI | `Biên gộp_{t−1} ÷ Biên gộp_t` | >1: biên gộp xấu đi |
| AQI | `[1 − (TSNH+TSCĐ+Chứng khoán)/TTS]_t ÷ [cùng biểu thức]_{t−1}` | >1: tỷ trọng "tài sản khác" tăng |
| SGI | `Doanh thu_t ÷ Doanh thu_{t−1}` | Tăng trưởng cao tạo áp lực duy trì |
| DEPI | `[KH/(TSCĐ+KH)]_{t−1} ÷ [KH/(TSCĐ+KH)]_t` | >1: tỷ lệ khấu hao giảm |
| SGAI | `(CPBH+QLDN)/Doanh thu` của `t` ÷ của `t−1` | >1: chi phí tăng nhanh hơn doanh thu |
| LVGI | `[(Nợ ngắn hạn+Vay dài hạn)/TTS]_t ÷ [cùng]_{t−1}` | >1: đòn bẩy tăng |
| TATA | `(Lợi nhuận − Dòng tiền hoạt động)/TTS_t` | Dương: lợi nhuận nhiều hơn tiền |

`PHÉP_TÍNH` Mỗi hàm trong [earnings_quality.py](../practice/models/earnings_quality.py) tính một chỉ số; `beneish()` trả cả tám chỉ số và M; `beneish_contributions()` trả hệ số × giá trị từng biến, để thấy biến nào đẩy điểm lên.

### 2.2 Altman Z''

`SỰ_THẬT` (thứ cấp) [Wikipedia — Altman Z-score](https://en.wikipedia.org/wiki/Altman_Z-score) (mở 01/11/2026) ghi dạng cho doanh nghiệp không sản xuất và thị trường mới nổi: `Z'' = 6,56·X1 + 3,26·X2 + 6,72·X3 + 1,05·X4`, với `X1 = (TSNH − Nợ ngắn hạn)/TTS`, `X2 = Lợi nhuận giữ lại/TTS`, `X3 = EBIT/TTS`, `X4 = Vốn chủ sổ sách/Tổng nợ`; an toàn trên 2,6, xám 1,1–2,6, nguy cơ dưới 1,1. Trang dẫn Altman (1968) và Altman (2000); tôi chưa mở hai bài gốc. Bản 1968 trên trang dùng giá trị thị trường của vốn chủ và hệ số khác. `CHƯA_BIẾT` độ chính xác của Z'' với doanh nghiệp Việt Nam.

### 2.3 Piotroski F-score

`SỰ_THẬT` Bài gốc [Piotroski (2000), *Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers*](https://www.chicagobooth.edu/~/media/FE874EE65F624AAEBD0166B1974FD74D.pdf) (Univ. of Chicago Selected Paper 84; mở 01/11/2026) định nghĩa chín tín hiệu nhị phân, mỗi tín hiệu 1 điểm, F_SCORE từ 0 đến 9 (mục 2.3). Bốn tín hiệu lợi nhuận: ROA dương, CFO dương, ROA tăng so với năm trước, và CFO lớn hơn ROA (tín hiệu dồn tích). Ba tín hiệu đòn bẩy và thanh khoản: tỷ lệ nợ dài hạn trên tổng tài sản bình quân giảm, tỷ số thanh toán hiện hành tăng, và không phát hành cổ phiếu phổ thông. Hai tín hiệu hiệu quả: biên gộp tăng và vòng quay tài sản tăng. ROA và CFO chia cho tổng tài sản **đầu năm**. Bài tóm tắt rằng chiến lược chọn công ty mạnh trong nhóm có hệ số giá trị sổ sách/thị giá cao tăng lợi suất trung bình ít nhất 7,5% mỗi năm (bản PDF hiển thị phân số; tôi đọc là 7½), và mua-bán chênh lệch tạo 23% mỗi năm giai đoạn 1976–1996. Tác giả giới hạn phạm vi ở các công ty có tỷ lệ giá trị sổ sách trên giá trị thị trường cao (value stocks).

`SUY_LUẬN` Kết quả của Piotroski là lợi suất cổ phiếu Mỹ trong một thời kỳ, không phải bằng chứng cho Việt Nam. Bài này chỉ dùng F-score như chín câu hỏi về xu hướng, không như tín hiệu mua.

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

`PHÉP_TÍNH` DSRI `= (330/1.300)/(150/1.000) = 1,692`; GMI `= 1,147` (biên gộp từ 30% xuống 26,2%); AQI `= 1,04`; SGI `= 1,3`; DEPI `= 1,072`; SGAI `= 1,038`; LVGI `= 1,12`; TATA `= (150 − 20)/1.500 = 0,0867`. **M ≈ −1,11**, cao hơn ngưỡng −1,78 nên bị cờ. Biến đẩy mạnh nhất là DSRI (đóng góp `0,92 × 1,692 ≈ 1,56`) và TATA (`4,679 × 0,0867 ≈ 0,41`): lợi nhuận tăng gần gấp đôi trong khi tiền hoạt động rơi từ 90 xuống 20 và phải thu tăng hơn gấp đôi.

`PHÉP_TÍNH` Cùng số năm t: `X1 = 0,167`, `X2 = 0,253`, `X3 = 210/1.500 = 0,14` (EBIT giả định 210), `X4 = 1,143`; Z'' `≈ 4,06`, vùng an toàn. F-score `= 5`, trượt bốn tín hiệu (dồn tích, biên gộp, đòn bẩy, thanh toán hiện hành). Công ty này không có nguy cơ vỡ nợ gần mà chất lượng lợi nhuận vẫn đáng ngờ: đúng bài học mục 1.

## Ví dụ từ nguồn thật

Ca thực hành: tập đoàn Hòa Phát (HPG), báo cáo tài chính hợp nhất FY2025 kiểm toán bởi Deloitte, [tải từ trang công ty](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf). Đơn vị gốc VND, quy đổi sang tỷ VND. Ca này **không** nghi ngờ HPG gian lận; chọn nó vì có đủ số liệu hai năm và vì kết quả sàng lọc cho ví dụ rõ về hiệu ứng cơ học.

`SỰ_THẬT` Ý kiến kiểm toán (trang in 4): kiểm toán viên nêu ý kiến chấp nhận toàn phần với báo cáo FY2025; báo cáo FY2024 do một công ty kiểm toán độc lập khác kiểm toán, cũng chấp nhận toàn phần theo văn bản này. Số chính (tỷ VND; 2025 / 2024): doanh thu thuần 156.116,1 / 138.855,1; phải thu khách hàng (mã 131) 10.971,8 / 4.352,1; tài sản cố định hữu hình 133.420,8 / 67.244,2; tổng tài sản 257.899,2 / 224.489,7; lợi nhuận sau thuế 15.514,9 / 12.020,0; dòng tiền hoạt động 17.365,9 / 6.608,3. Đủ 20 chỉ tiêu trong [hpg_fy2025_statements.csv](../practice/models/hpg_fy2025_statements.csv); cột năm trước là cột "năm trước" của báo cáo FY2025.

`PHÉP_TÍNH` Tám chỉ số và M-score của HPG năm 2025:

| Chỉ số | Giá trị | Đóng góp vào M (hệ số × giá trị) |
|---|---:|---:|
| DSRI | 2,242 | +2,063 |
| GMI | 0,849 | +0,448 |
| AQI | 0,023 | +0,009 |
| SGI | 1,124 | +1,003 |
| DEPI | 1,565 | +0,180 |
| SGAI | 0,932 | −0,160 |
| LVGI | 1,035 | −0,339 |
| TATA | −0,007 | −0,034 |
| **M** | **−1,669** | (hằng số −4,84) |

M `= −1,669` cao hơn ngưỡng −1,78 một khoảng **0,11**, tức công cụ gắn cờ. Hai điều cần đọc kỹ trước khi nói thêm.

**Một: DSRI một mình quyết định.** Phải thu khách hàng tăng 152,1% (4.352,1 lên 10.971,8) trong khi doanh thu tăng 12,4%. Nếu DSRI bằng 1, M sẽ là −2,81; muốn M đúng bằng −1,78 thì DSRI chỉ cần 2,12 (gần như bằng giá trị thật 2,24). Điểm sát ngưỡng như vậy rất mong manh: đổi định nghĩa "phải thu" là đổi kết luận. Nếu thay phải thu khách hàng (mã 131) bằng tổng phải thu ngắn hạn (mã 130: 15.042,3 và 7.647,8), DSRI chỉ còn 1,749 và M về −2,12, dưới ngưỡng. Mô hình gốc không nói chọn mã nào cho kế toán Việt Nam; `CHƯA_BIẾT`.

**Hai: AQI và DEPI là hiệu ứng cơ học.** Thuyết minh số 12 (trang in 29) cho thấy trong năm 2025 có 73.824,2 tỷ VND chi phí xây dựng cơ bản **hoàn thành** được chuyển sang tài sản cố định hữu hình (nguyên giá tăng từ 108.146,6 lên 182.308,7 tỷ). Bảng cân đối cho thấy tài sản cố định hữu hình tăng 98,4% trong khi chi phí xây dựng dở dang giảm từ 63.655,9 xuống 10.721,1 tỷ. AQI thấp (0,023) vì năm trước tài sản dở dang nằm ngoài ba nhóm "tài sản tốt" của công thức, nay đã vào nhóm TSCĐ; DEPI cao (1,565) vì TSCĐ nhân đôi trong khi khấu hao chỉ tăng 22%; nhiều khả năng vì công trình mới chỉ chạy một phần năm (`SUY_LUẬN`, thời điểm đưa vào khai thác `CHƯA_BIẾT`). Đó là đổi quy mô, không có dấu hiệu rằng khấu hao bị chỉnh. `SUY_LUẬN` Đóng góp của hai biến này vào M là nhỏ (0,009 và 0,180), nhưng ví dụ cho thấy mọi chỉ số "so hai năm" đều nhiễm biến động quy mô.

`SỰ_THẬT` Thuyết minh số 7 (trang in 26) liệt kê khách hàng lớn: Marcegaglia Carbon Steel 1.837,3 tỷ (đầu năm 482,4); Công ty CP Thép Minh Phú – Hải Dương 1.641,2 (đầu năm không có tên); Công ty CP Thép Minh Phú 679,3 (không có tên); Công ty CP Kim Khí Nam Hưng 592,6 (60,7); Công ty CP Tập đoàn Hoa Sen 617,3 (218,6); các khách hàng khác 5.604,1 (3.590,4). `PHÉP_TÍNH` Năm khách hàng được nêu tên chiếm `5.367,7/10.971,8 = 48,9%` phải thu cuối năm, so với 17,5% đầu năm theo cách tính cùng năm tên (`761,7/4.352,1`; các ô trống đầu năm coi là dưới ngưỡng liệt kê hoặc không có số dư, chưa xác nhận). Phải thu đang dồn vào vài khách hàng thép. Nguyên nhân (điều khoản tín dụng, thời điểm giao hàng cuối năm, xuất khẩu, hay bên liên quan) báo cáo không nêu: `CHƯA_BIẾT`, cần xem thuyết minh bên liên quan và điều khoản thanh toán.

`SỰ_THẬT` Báo cáo lưu chuyển tiền tệ (trang in 9): dòng tiền hoạt động 17.365,9 tỷ, cao hơn lợi nhuận sau thuế 15.514,9 tỷ, dù các khoản phải thu thay đổi −8.743,1 tỷ và hàng tồn kho −7.241,8 tỷ, vì các khoản phải trả thay đổi +11.393,2 tỷ (phải trả người bán ngắn hạn tăng từ 14.046,8 lên 21.183,4 tỷ). `PHÉP_TÍNH` TATA `= (15.514,9 − 17.365,9)/257.899,2 = −0,0072`: lợi nhuận được dòng tiền hỗ trợ. `SUY_LUẬN` Tiền đến nhờ nhà cung cấp là một cách tài trợ vốn lưu động; bền hay không phụ thuộc điều khoản thương mại, nguồn đã mở không nêu.

**Altman Z'' và F-score của HPG.** `PHÉP_TÍNH` `X1 = 0,0367`, `X2 = 51.037,9/257.899,2 = 0,1979` (lợi nhuận chưa phân phối, mã 421), `X3 = (18.040,6 + 3.114,9)/257.899,2 = 0,0820` (EBIT xấp xỉ bằng lợi nhuận trước thuế cộng lãi vay), `X4 = 131.220,0/126.679,2 = 1,0358`; Z'' `≈ 2,525`, **vùng xám** sát cận trên 2,6. F-score `= 7/9`: trượt hai tín hiệu, vòng quay tài sản (0,739 xuống 0,695) và thanh toán hiện hành (1,152 xuống 1,101); đạt bảy tín hiệu còn lại, trong đó biên gộp tăng 13,3% lên 15,7% và tỷ lệ vay dài hạn trên tài sản bình quân giảm 13,1% xuống 11,4%. `CHƯA_BIẾT` ROA năm 2024 dùng tổng tài sản cuối 2023 là 187.783 tỷ từ báo cáo thường niên 2023, còn cột FY2024 có thể đã trình bày lại; tín hiệu "ROA tăng" kém chắc hơn các tín hiệu còn lại.

**Kết luận được phép viết.** `Ý_KIẾN` "M-score FY2025 của HPG là −1,67, cao hơn ngưỡng −1,78 khoảng 0,11 chủ yếu do phải thu khách hàng tăng nhanh hơn doanh thu; thuyết minh cho thấy phải thu dồn vào năm khách hàng thép, và dòng tiền hoạt động vẫn cao hơn lợi nhuận. Các chỉ số AQI và DEPI bị nhiễu bởi việc chuyển công trình hoàn thành vào TSCĐ. Cần đọc thêm điều khoản bán hàng và thuyết minh bên liên quan trước khi nói gì thêm." Không được viết: "HPG thổi phồng lợi nhuận."

## 4. Hiệu ứng cơ học và định nghĩa

Trước khi tin một chỉ số, kiểm ba loại nhiễu: (1) quy mô thay đổi (công trình hoàn thành, mua bán công ty) làm AQI, DEPI, LVGI, SGI nhảy cơ học, như HPG ở trên; (2) định nghĩa khoản mục (phải thu khách hàng hay tổng phải thu; khấu hao trong báo cáo lưu chuyển tiền tệ có gồm phân bổ lợi thế thương mại và chi phí thuê đất), trong đó nhất quán giữa hai năm quan trọng hơn chọn đúng mã; (3) chuẩn kế toán: công thức xây trên số liệu Mỹ, nhiều khoản của VAS không có chỗ tương ứng chuẩn. `CHƯA_BIẾT` bảng quy đổi chuẩn.

## 5. Giới hạn của Z'' và F-score

Z'' đổi mạnh khi công ty vừa chia cổ phiếu thưởng hay lỗ lớn (X2); EBIT xấp xỉ ở đây còn gồm thu nhập tài chính. F-score cho biết tiến hay lùi, không cho biết mức: công ty rất yếu bớt tệ cũng có điểm cao. Ngưỡng nhị phân trên đại lượng liên tục làm 2,5 và 2,7 khác vùng nhưng gần như cùng mức rủi ro.

## 6. Quy trình đọc: từ cờ tới câu hỏi

1. In từng thành phần, không chỉ tổng; tìm biến đóng góp lớn nhất và hỏi có giải thích cơ học (quy mô, định nghĩa) không.
2. Mở thuyết minh liên quan (phải thu theo khách hàng, bên liên quan, ghi nhận doanh thu, dự phòng) và đối chiếu dòng tiền: tiền đến từ khách hàng, nhà cung cấp hay vay.
3. Nhìn nhiều kỳ: một năm bất thường khác ba năm cùng hướng. Bài này làm một năm; `CHƯA_BIẾT` chuỗi M-score HPG nhiều năm.
4. Viết kết luận bằng nhãn đúng mức: `SỰ_THẬT` cho số và thuyết minh đã mở, `PHÉP_TÍNH` cho điểm, `CHƯA_BIẾT` cho nguyên nhân chưa có nguồn.

## Bài tập — làm trước khi mở đáp án

1. Mỗi công cụ (M-score, Z'', F-score) trả lời câu hỏi nào, và vì sao điểm của chúng có thể mâu thuẫn?
2. Cờ Đỏ: tính DSRI từ bảng ở mục 3.
3. Cờ Đỏ: tính TATA và nói điều nó gợi ý.
4. Cờ Đỏ: biết DSRI 1,6923; GMI 1,1471; AQI 1,04; SGI 1,3; DEPI 1,0718; SGAI 1,0385; LVGI 1,12; TATA 0,0867; tính M.
5. Cờ Đỏ: tính Z'' năm t và cho biết vùng.
6. Cờ Đỏ: hai tín hiệu Piotroski nào trượt trong nhóm dồn tích và thanh khoản? Giải thích.
7. HPG: tính DSRI từ doanh thu thuần và phải thu khách hàng (mã 131) của hai năm.
8. HPG: phải thu tăng bao nhiêu phần trăm, doanh thu tăng bao nhiêu? DSRI cần bằng bao nhiêu để M đạt −1,78?
9. (Chuyển giao) Nêu ba lời giải thích không liên quan thao túng cho việc phải thu tăng nhanh hơn doanh thu và với mỗi lời giải thích, nêu tài liệu cần mở để kiểm.
10. (Chuyển giao) Dùng thuyết minh số 12 của HPG giải thích vì sao AQI chỉ bằng 0,023 và vì sao đó không phải dấu hiệu thao túng.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. M-score: giống mẫu thổi phồng lợi nhuận; Z'': giống mẫu phá sản; F-score: nền tảng đang mạnh hay yếu đi. Mâu thuẫn vì đo ba đối tượng khác nhau (mục 1).
2. `(330/1.300)/(150/1.000) = 0,2538/0,15 = 1,692`.
3. `(150 − 20)/1.500 = 0,0867`. Lợi nhuận cao hơn dòng tiền hoạt động; dồn tích dương lớn gợi ý lợi nhuận chưa thành tiền.
4. `−4,84 + 0,92×1,6923 + 0,528×1,1471 + 0,404×1,04 + 0,892×1,3 + 0,115×1,0718 − 0,172×1,0385 + 4,679×0,0867 − 0,327×1,12` `= −4,84 + 1,557 + 0,606 + 0,420 + 1,160 + 0,123 − 0,179 + 0,406 − 0,366 ≈ −1,11`.
5. `X1 = 250/1.500 = 0,1667`; `X2 = 0,2533`; `X3 = 0,14`; `X4 = 1,1429`; `Z'' = 1,093 + 0,826 + 0,941 + 1,2 = 4,06`, vùng an toàn (trên 2,6).
6. Dồn tích: CFO/TTS đầu năm `= 20/1.200 = 1,7%` nhỏ hơn ROA `= 150/1.200 = 12,5%`, nên trượt. Thanh khoản: `700/450 = 1,556` thấp hơn `500/300 = 1,667`, nên trượt.
7. `(10.971,8/156.116,1)/(4.352,1/138.855,1) = 0,07028/0,03134 = 2,242`.
8. Phải thu `10.971,8/4.352,1 − 1 = +152,1%`; doanh thu `+12,4%`. M hiện `−1,669`; cần giảm 0,111; mỗi điểm DSRI đóng góp 0,92 nên DSRI ngưỡng `= 2,242 − 0,111/0,92 ≈ 2,12`.
9. Ví dụ: (a) khách hàng lớn nhận hàng cuối năm → xem chính sách bán hàng và ngày giao; (b) kéo dài điều khoản thanh toán để tăng doanh số xuất khẩu → xem thuyết minh phải thu theo khách hàng và hợp đồng; (c) cơ cấu bán đổi từ bán lẻ sang bán cho khách hàng lớn → xem báo cáo bộ phận. Chấp nhận lời giải thích khác nếu kèm tài liệu kiểm cụ thể.
10. Năm 2025 có 73.824,2 tỷ VND công trình xây dựng hoàn thành chuyển vào TSCĐ hữu hình. Tổng `TSNH + TSCĐ + chứng khoán` năm 2025 chiếm 99,5% tổng tài sản, nên phần "tài sản khác" (mẫu của AQI) còn 0,5%, so với 23,0% năm trước khi dở dang chưa chuyển. Tỷ lệ sụt mạnh vì phân loại thay đổi, không vì tài sản xấu đi.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty thép N năm 2025: doanh thu 156.116 tỷ, phải thu ngắn hạn 15.042 tỷ (tổng các khoản phải thu). Năm 2024: doanh thu 138.855 tỷ, phải thu khách hàng 4.352 tỷ. Tính DSRI và kết luận có gắn cờ hay không."

Phát hiện: (a) hai năm dùng hai định nghĩa phải thu khác nhau (tổng và chỉ khách hàng); (b) không biết khoản "phải thu ngắn hạn khác" gồm gì; (c) thiếu dự phòng nợ khó đòi; (d) chưa biết cùng phạm vi hợp nhất không.

`Đáp án` Dùng nhầm định nghĩa cho DSRI `= (15.042/156.116)/(4.352/138.855) = 3,07`, quá cao và vô nghĩa. Nhất quán theo phải thu khách hàng cho 2,24, nhất quán theo tổng phải thu cho 1,75; hai cách cho M khác nhau (−1,67 và −2,12), một cách trên ngưỡng một cách dưới. Phải chọn một định nghĩa, ghi rõ, và báo cáo cả hai khi kết luận phụ thuộc.

## Sai ở đâu

Một học viên viết: "M-score của HPG FY2025 là −1,67, cao hơn −1,78, nên Hòa Phát thổi phồng lợi nhuận. Z'' 2,5 là vùng xám nên sắp có vấn đề tài chính. F-score 7 nên mua. Chuỗi DSRI 2,24 chứng tỏ phải thu ảo."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. Vượt ngưỡng 0,11 không phải bằng chứng; ngưỡng không phân biệt thao túng với thay đổi kinh doanh.
2. Bỏ qua việc kết quả phụ thuộc định nghĩa phải thu (tổng phải thu cho M −2,12).
3. Bỏ qua dòng tiền cao hơn lợi nhuận; phải thu dồn vào vài khách hàng thép cần giải thích, chưa phải kết luận.
4. Z'' vùng xám là vùng chưa phân biệt, không phải "sắp có vấn đề".
5. "F-score 7 nên mua" là khuyến nghị cá nhân hóa; F-score nghiên cứu trên value stocks Mỹ 1976–1996.
6. "Phải thu ảo" là kết luận về động cơ không có bằng chứng.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Doanh thu 500 và 600; phải thu 50 và 90 (năm t−1 và t). Tính DSRI.
2. Lợi nhuận 80, CFO 30, tổng tài sản cuối năm 400. Tính TATA và nêu ý nghĩa.
3. Nêu hai việc phải làm trước khi viết "công ty bị cờ M-score" vào một báo cáo nghiên cứu.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `(90/600)/(50/500) = 0,15/0,10 = 1,5`. Câu 2 `(80 − 30)/400 = 0,125`; lợi nhuận hơn tiền nhiều, cần xem phải thu, tồn kho, chi phí trả trước. Câu 3: in từng thành phần và tìm hiệu ứng cơ học; mở thuyết minh và dòng tiền; kiểm định nghĩa khoản mục nhất quán giữa hai năm; ghi nguồn và nhãn.

</details>

## Lỗi thường gặp

- Coi điểm vượt ngưỡng là bằng chứng gian lận, hoặc điểm dưới ngưỡng là chứng chỉ sạch.
- Đổi định nghĩa khoản mục giữa hai năm; quên hiệu ứng cơ học khi quy mô đổi.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ và không phải cáo buộc. Hòa Phát chỉ là dữ liệu thực hành; báo cáo FY2025 của công ty có ý kiến kiểm toán chấp nhận toàn phần.
- Hệ số Beneish và Altman chưa đối chiếu với bài gốc; ngưỡng có thể khác giữa các nguồn.

## Điều tôi vẫn chưa hiểu

- Mã khoản mục VAS nào tương ứng đúng với "phải thu", "tài sản cố định", "khấu hao" của mô hình gốc?
- Chuỗi điểm nhiều năm của một công ty nói gì mà một năm không nói?

## Nguồn Internet đã mở

Truy cập `2026-11-01`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Piotroski (2000), Selected Paper 84, Univ. of Chicago](https://www.chicagobooth.edu/~/media/FE874EE65F624AAEBD0166B1974FD74D.pdf) | Gốc; Hoa Kỳ 1976–1996; cổ phiếu có tỷ lệ sổ sách/thị giá cao | Định nghĩa chín tín hiệu F-score, phạm vi mẫu |
| [Wikipedia — Beneish M-score](https://en.wikipedia.org/wiki/Beneish_M-score) | Thứ cấp; trang có thông báo thiếu trích dẫn | Tám chỉ số, hệ số, ngưỡng −1,78 (chưa đối chiếu bài gốc) |
| [Wikipedia — Altman Z-score](https://en.wikipedia.org/wiki/Altman_Z-score) | Thứ cấp | Công thức Z'' và các vùng (chưa đối chiếu bài gốc) |
| [BCTC hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) | FY2025 và cột năm trước; VND; VAS; đã đọc trang in 4–10, 26–27, 29–30 | Mọi số HPG, thuyết minh 7 và 12, ý kiến kiểm toán |
| [Báo cáo thường niên 2023 của Hòa Phát](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) | Tóm tắt chỉ số FY2023, tỷ VND | Tổng tài sản cuối FY2023 (187.783 tỷ) dùng cho ROA FY2024 |

`CHƯA_BIẾT` Bài gốc Beneish (1999) và Altman (1968, 2000): bản chính bị chặn (HTTP 403 hoặc lỗi máy chủ), chưa có nguồn gốc mở được. Cần đối chiếu hệ số, định nghĩa chỉ số và ngưỡng với bài gốc trước khi bỏ nhãn nháp.
