# BẢN NHÁP - CHƯA KIỂM DUYỆT: MIXUE Group, câu chuyện doanh nghiệp, dòng tiền và triển vọng 3 năm (2097.HK)

- Chốt dữ liệu lúc: `2026-11-25 10:00 +07` (báo cáo công ty: HKEXnews, mở lại tệp PDF đã lưu và đối chiếu mã băm SHA-256; giá cổ phiếu: nguồn thứ cấp 23–24/11/2026)
- Quốc gia / thị trường / sở giao dịch: Trung Quốc đại lục (hoạt động chính), niêm yết cổ phiếu H tại HKEX mã `2097` từ 2025-03-03
- Chuẩn kế toán: IFRS Accounting Standards; kiểm toán Ernst & Young (Hong Kong)
- Tiền tệ / đơn vị báo cáo: RMB; số gốc tính theo RMB nghìn, bài này làm tròn sang RMB triệu hoặc tỷ
- Phạm vi: (1) kể lại mô hình kinh doanh, nguồn thu, dòng tiền vào–ra và đầu tư; (2) đánh giá khả năng bão hòa, vị trí giá và tăng trưởng 3 năm theo kịch bản, dùng khung các bài 011, 012, 014, N6. **Không định giá nội tại và không đưa khuyến nghị mua, bán, nắm giữ.**
- Tài liệu liên quan: nghiên cứu nền `research/companies/HK/2097-mixue-financial-statements-2026-11-25.md` (bản v4); dữ liệu gốc `data/raw/mixue-financials-2026-11-25.json`; PDF và mã băm `data/raw/mixue-hkex/`; phép tính `data/processed/mixue-financial-calculations-2026-11-25.md` và `data/processed/mixue-outlook-scenarios-2026-11-25.md`
- Kiểm nguồn: `ĐANG_CHỜ` (số công ty đã qua ba lượt kiểm ở bản v4 nhưng bản này là tài liệu mới, chưa kiểm)
- Phản biện rủi ro: `ĐANG_CHỜ`
- Điều kiện kế thừa: số doanh nghiệp lấy từ bản v4, bản đó cũng chưa bỏ nhãn nháp. Các số mới trong bản này là dòng tiền đầu tư và tài chính 2025 và H1 2026, giá cổ phiếu, vốn hóa, FCF LTM, định giá ngược và ba kịch bản.

> Không phải lời khuyên mua, bán hay nắm giữ. Các kịch bản là khung theo dõi, không gắn xác suất, không phải dự báo.

## Tóm tắt bài học

1. **Mixue là nhà cung ứng chuỗi cung ứng, không phải chuỗi tự bán lẻ.** 93,7% doanh thu 2025 là bán hàng hóa cho cửa hàng, 4,0% bán thiết bị, 2,4% phí dịch vụ nhượng quyền. `SỰ_THẬT` [S4]. Doanh thu xấp xỉ **số quán × lượng hàng mỗi quán nhập**. `SUY_LUẬN`
2. **Tiền không bị đốt vào mở rộng; nó nằm trong "két".** Năm 2025 OCF là 6.039,0 triệu, capex tài sản cố định chỉ 685,1 triệu, trong khi mua ròng sản phẩm quản lý tài sản (FVTPL) khoảng 5.332,6 triệu. `SỰ_THẬT` + `PHÉP_TÍNH` [S5]. Cuối H1 2026 tiền, tiền gửi và FVTPL đạt 21.640,7 triệu, nợ vay bằng 0. `SỰ_THẬT` [S7]
3. **H1 2026 là điểm ngoặt.** Doanh thu +2,3%, lợi nhuận −14,7%, OCF −37,4%, trong khi số quán +20,7%; doanh thu hàng hóa mỗi quán giảm khoảng 15–17% (tùy mẫu số). `SỰ_THẬT` + `PHÉP_TÍNH` [S7, S13]. Nguyên nhân `CHƯA_BIẾT`; hai giả thuyết (nền trợ giá ngành; đặc thù Mixue) được giữ cả hai.
4. **"Chết" trong 3 năm: gần như không. "Bão hòa": rủi ro thật.** Bảng cân đối không thể cạn thanh khoản trong 3 năm dưới mọi kịch bản dưới đây `SUY_LUẬN`; điểm yếu nằm ở sức khỏe chủ quán và quản trị. Đường đi khả dĩ nhất là chuyển từ tăng trưởng nhờ mở quán sang trưởng thành.
5. **Giá đã rời đỉnh.** Giá khoảng HK$155,70 (24/11/2026), thấp hơn giá IPO HK$202,5 và khoảng −66% so với đỉnh 52 tuần HK$464 (đỉnh trong ngày tháng 6/2025 theo KrASIA là HK$618,5). `SỰ_THẬT` (giá, nguồn thứ cấp) + `PHÉP_TÍNH`. Câu hỏi còn lại là **đỉnh của lợi nhuận** có phải năm 2025 không.
6. **Giá hiện tại hàm ý dòng tiền giảm dần.** Với EV ≈ 29,7 tỷ RMB và FCF LTM ≈ 3,75–4,0 tỷ, tăng trưởng vĩnh viễn hàm ý là khoảng −0,6% đến −4,8% mỗi năm tùy WACC 8–12%. `PHÉP_TÍNH` có nhiều giả định (mục "Định giá ngược"); không kết luận cổ phiếu rẻ hay đắt.
7. **Tăng trưởng 3 năm (2025 → 2028), kịch bản:** doanh thu −1,3% / +4,0% / +9,3% mỗi năm; lợi nhuận −12,1% / −0,4% / +7,9% mỗi năm (bất lợi / cơ sở / thuận lợi). `KỊCH_BẢN`. Ở kịch bản cơ sở lợi nhuận **không tăng**.

## Mô hình kinh doanh

- Ba thương hiệu: MIXUE (trà, nước ép, kem; giá lõi RMB 2–8), Lucky Cup (cà phê), FULU Fresh Beer (bia tươi; mua lại, hoàn tất 2025-12-01). `SỰ_THẬT` [S4]
- Chủ quán sở hữu và chịu kết quả cửa hàng, mua nguyên liệu và thiết bị từ Mixue. Công ty tự sản xuất 100% nguyên liệu lõi: 5 cơ sở và 28 kho (cuối 2025), 6 cơ sở và 31 kho (30/6/2026). `SỰ_THẬT` [S4, S7]
- Nợ hợp đồng (tiền chủ quán trả trước) chỉ 485,1 triệu cuối 2025 (khoảng 5,3 ngày doanh thu), nên không phải nguồn vốn lớn. `PHÉP_TÍNH`
- Mạng lưới: 20.001 quán (2021) → 59.823 (2025) → 63.987 (30/6/2026). Hơn 58% quán đại lục ở thành phố hạng ba trở xuống. Chủ nhượng quyền 27.450 (2025), 29.775 (30/6/2026). `SỰ_THẬT` [S1, S4, S7]
- Không khách hàng nào chiếm từ 10% doanh thu trong các kỳ có công bố. `SỰ_THẬT` [S4, S7]

**So sánh với Costco của ngành trà (ẩn dụ giải thích, không phải so sánh số liệu):** công ty kiếm tiền nhờ quy mô mua, sản xuất và logistics, rồi chia lại biên cho chủ quán. `Ý_KIẾN`

## Bối cảnh ngành, vĩ mô và so sánh toàn cầu

Kế thừa từ bản v4 (mục "Bối cảnh ngành"). Điểm chính phục vụ triển vọng:
- Năm 2025 nền tảng giao hàng trợ giá rất mạnh, đẩy đơn đồ uống pha chế; Luckin (6-K 2026-11-03) nói doanh số cùng cửa hàng tự vận hành Q3 2026 −11,1% chủ yếu do nền so sánh cao. Nayuki −13,1% doanh thu; Chagee sụt hai chữ số; Guming và Auntea Jenny doanh thu mỗi quán xấp xỉ phẳng. Báo cáo gốc do bên kiểm duyệt mở ở bản v4, tôi chưa tự mở lại; `CHƯA_XÁC_MINH` trong tài liệu này.
- Nikkei Asia / KrASIA (thứ cấp, tháng 11/2026): quán đầu tiên của Mixue tại Hồng Kông đóng cửa đầu tháng 10; làn sóng đóng quán từ Hồng Kông đến Đông Nam Á; cổ phiếu giảm 57% từ đầu 2026 đến 9/11. `CHƯA_XÁC_MINH`
- Macquarie khởi đầu độ phủ ở mức Underperform và kỳ vọng mạng lưới tăng chậm hơn (thứ cấp). Giá mục tiêu của các nhà phân tích trên các trang tổng hợp lệch nhau và không đồng ngày; không dùng làm bằng chứng. `Ý_KIẾN`

## Lịch sử và chất lượng tài chính

### Kết quả kinh doanh (RMB triệu)

| | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|
| Doanh thu | 13.575,6 | 20.302,5 | 24.828,9 | 33.559,9 | 14.874,8 | 15.215,8 |
| Tăng trưởng | 31,2% | 49,6% | 22,3% | 35,2% | +39,3% | +2,3% |
| Biên gộp | 28,3% | 29,5% | 32,5% | 31,1% | 31,6% | 30,4% |
| Lợi nhuận | 2.013,1 | 3.186,6 | 4.454,2 | 5.927,1 | 2.718,2 | 2.319,3 |
| Biên ròng | 14,8% | 15,7% | 17,9% | 17,7% | 18,3% | 15,2% |

Nguồn [S1, S4, S6, S7]. `SỰ_THẬT` / `PHÉP_TÍNH`. Giải thích năm 2022 (giảm giá 15% cho 69 mặt hàng để hỗ trợ chủ quán qua COVID) và các nhận xét biên khác ở bản v4.

### 100 đồng doanh thu đi đâu (FY2025)

| Khoản | Tỷ lệ doanh thu |
|---|---|
| Giá vốn | ≈ 68,9% |
| Chi phí bán hàng | 6,1% |
| Chi phí quản lý | 3,2% |
| Thuế thu nhập (1.623,1 triệu) | 4,8% |
| Lợi nhuận năm | 17,7% |

Các khoản còn lại (nghiên cứu phát triển, thu nhập khác ròng, lãi) cộng ròng khoảng +0,7 điểm %. `PHÉP_TÍNH` [S4]

### Dòng tiền: tiền vào, tiền ra và đầu tư

| RMB triệu | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|
| OCF | 6.008,7 | 6.039,0 | 3.275,4 | 2.049,8 |
| Mua tài sản cố định hữu hình | −1.438,6 | −685,1 | −305,8 | −289,4 |
| Mua ròng FVTPL (+ là mua) | +2.700,4 | +5.332,6 | +1.581,3 | −908,0 |
| Gửi ròng tiền kỳ hạn > 3 tháng | +2.930,0 | +232,8 | +755,0 | +3.972,0 |
| Dòng tiền đầu tư thuần | −7.019,0 | −6.364,1 | −2.741,8 | −3.384,5 |
| Dòng tiền tài chính thuần | −277,4 | +3.505,4 | +3.578,1 | −51,8 |
| Thu phát hành cổ phiếu | 0 | 3.665,1 | 3.665,1 | 0 |

Nguồn [S5 trang 115–116; S13 trang 51–53]. `SỰ_THẬT`; các dòng ròng là `PHÉP_TÍNH` (xem tệp phép tính).

Điều đọc ra:
- **Mô hình ít vốn:** capex hữu hình chỉ 10,8% dòng tiền đầu tư 2025; phần còn lại phần lớn là chuyển tiền từ tiền mặt sang tiền gửi kỳ hạn và sản phẩm tài chính. `PHÉP_TÍNH`
- **H1 2026 đảo chiều:** thu hồi ròng 908 triệu FVTPL nhưng gửi ròng 3.972 triệu tiền kỳ hạn; tiền và tương đương tiền giảm từ 7.429,1 xuống 6.027,9 triệu. `SỰ_THẬT` [S13]
- Mua FULU hợp nhất chỉ tốn ròng 13,7 triệu tiền mặt (FULU nắm 271,9 triệu tiền). Góp vốn công ty liên kết 109,0 triệu (đối tượng `CHƯA_BIẾT`). `SỰ_THẬT` [S5]
- Thu nhập lãi và quản lý tài sản 2025 là 330,0 triệu, khoảng 4,4% lợi nhuận trước thuế; lỗ tỷ giá 79,5 triệu (2025) và 153,8 triệu (H1 2026). `SỰ_THẬT` [S4, S7]
- OCF H1 2026 giảm chủ yếu do biến động phải trả người bán (−378,7 so với +739,4 triệu); OCF/lợi nhuận 0,88 (H1 2025: 1,20). `SỰ_THẬT` [S13]

### Điểm ngoặt H1 2026

Doanh thu +2,3%, lợi nhuận −14,7%, số quán +20,7%. Lợi nhuận trước thuế giảm 492,6 triệu: chi phí bán hàng và quản lý tăng 381,7 triệu (≈ 77,5% mức giảm), lợi nhuận gộp giảm 76,7 triệu. Mở mới H1 2026 5.455 (−29,3%). Mạng lưới nước ngoài thu hẹp 4.895 → 4.378. Chi tiết và phần rà soát ở bản v4.

## Ban lãnh đạo, quản trị và phân bổ vốn

Kế thừa từ bản v4:
- Hai nhà sáng lập nắm ≈ 81% vốn qua thỏa thuận hành động phối hợp. `SỰ_THẬT` [S14]
- Mua FULU (2025-10-01 ký, 2025-12-01 hoàn tất): giao dịch bên liên quan, ≈ 80% FULU thuộc người nhà một cổ đông kiểm soát; giá công bằng hay không `CHƯA_BIẾT`. `SỰ_THẬT` [S5]
- Cổ tức đặc biệt RMB 2,65 mỗi cổ phiếu (≈ 1.006 triệu, khoảng 43% lợi nhuận H1 2026), thông qua 2026-09-30; khoảng 816 triệu về hai nhà sáng lập; đã chi trả ngày 6/11 `CHƯA_XÁC_MINH`. `SỰ_THẬT` [S10, S11]
- Quyền thưởng cổ phiếu 12.023.300 (≈ 3,17%) giá mua HK$18,47 so với giá thị trường HK$184,70 khi cấp. `SỰ_THẬT` [S15]

## Triển vọng 3 năm: bão hòa hay tiếp tục tăng

### Cơ chế bão hòa (bài 014 và N6)

- Bài 014 mô tả chu kỳ vốn năm pha; ở Mixue "nhà đầu tư" là hơn 29.000 chủ quán. Số mở mới giảm 29,3% là dấu hiệu pha bùng nổ đầu tư đang hạ nhiệt; liệu đã chuyển sang dư cung hay chưa `CHƯA_BIẾT`.
- Doanh thu hàng hóa mỗi quán giảm 15–17% `PHÉP_TÍNH` (mẫu số nhiễu: FULU, cửa hàng mới, hàng bán nước ngoài). Với định phí không giảm theo doanh số (bài N6), lãi chủ quán giảm nhanh hơn doanh số. Minh họa **hư cấu**: doanh số −15% khiến lãi quán từ 15,0 xuống 7,5 (−50%). `KỊCH_BẢN`
- Doanh thu của Mixue chỉ bền khi chủ quán còn lãi; dữ liệu kinh tế đơn vị cấp quán và doanh số cùng cửa hàng `CHƯA_BIẾT` (công ty không công bố).
- Đóng quán: tỷ lệ đóng so với số quán nhượng quyền đầu kỳ là 4,5% (2023), 4,3% (2024), 5,4% (2025), 2,2% (H1 2026, so với 2,6% H1 2025). Chủ nhượng quyền vẫn +27,2% so với cùng kỳ. Đây là bằng chứng trái chiều với luận điểm gãy. `PHÉP_TÍNH` [S2, S4, S7]

### Vì sao "chết" trong 3 năm là khó xảy ra

Tiền, tiền gửi và FVTPL 21,64 tỷ RMB, nợ vay 0, OCF LTM ≈ 4,81 tỷ, capex LTM ≈ 0,71 tỷ. `SỰ_THẬT` + `PHÉP_TÍNH` [S7, S13]. Rủi ro sống còn nằm ở niềm tin hệ sinh thái chủ quán, an toàn thực phẩm và quản trị, không ở thanh khoản. Không có bằng chứng về rủi ro thanh khoản trong dữ liệu đã đọc.

### Vị trí giá và "đỉnh"

| Chỉ báo | Giá trị | Nguồn |
|---|---|---|
| Giá đóng cửa 24/11/2026 | HK$ 155,70 | Investing.com (thứ cấp) |
| Biên 52 tuần | 154,50–464,00 | Investing.com (thứ cấp) |
| Giá IPO | HK$ 202,5 | KrASIA |
| Đỉnh trong ngày 6/2025 | HK$ 618,5 | KrASIA |
| Vốn hóa | ≈ 59,1 tỷ HKD ≈ 50,3 tỷ RMB | `PHÉP_TÍNH` |
| Tiền ròng giả định (sau cổ tức 1,0 tỷ) | ≈ 20,6 tỷ RMB | `PHÉP_TÍNH` |
| EV | ≈ 29,7 tỷ RMB | `PHÉP_TÍNH` |
| P/E LTM | ≈ 9,1 lần (Google Finance: 9,30) | `PHÉP_TÍNH` |

- Giá đã giảm khoảng 66% từ đỉnh 52 tuần và khoảng 23% dưới giá IPO (155,70 / 202,5 − 1 = −23,1%). `PHÉP_TÍNH`
- Bài 014 mục "bẫy P/E ngược" cảnh báo P/E thấp ở đỉnh lợi nhuận là dễ gây hiểu lầm. Mixue không phải cổ phiếu chu kỳ thuần nhưng lợi nhuận 2025 được hỗ trợ bởi nền trợ giá, nên áp dụng được lập luận tương tự. Nếu lợi nhuận 2028 chỉ còn 4,0 tỷ thì cùng vốn hóa tương ứng P/E ≈ 12,5. `SUY_LUẬN`

### Định giá ngược (bài 011)

Giả định: `EV = FCF0 × (1 + g) / (WACC − g)`; EV = 29,7 tỷ RMB; FCF0 = 4,0 tỷ (thô) hoặc 3,75 tỷ (trừ lãi nhận ước 0,25 tỷ). WACC 8–12% là giả định minh họa, **chưa dựng theo bài 010**.

| WACC | g hàm ý (FCF0 4,0) | g hàm ý (FCF0 3,75) |
|---|---|---|
| 8% | −4,8% | −4,1% |
| 10% | −3,1% | −2,3% |
| 12% | −1,3% | −0,6% |

Cách đọc: với các giả định này, giá đã hàm ý dòng tiền giảm dần. Đây là `PHÉP_TÍNH` nhạy; không nói cổ phiếu rẻ. Ba lý do thị trường có thể hợp lý hoặc mô hình quá bi quan:
1. Thị trường có thể chiết khấu tiền mặt vì quản trị (sở hữu tập trung, giao dịch bên liên quan, cổ tức chảy về người kiểm soát). Một phần 21,6 tỷ là tiền kỳ hạn và tiền bị hạn chế.
2. Lợi nhuận bình thường hóa `CHƯA_BIẾT`.
3. Đà bán có thể còn quán tính sau giai đoạn định giá cao (đỉnh HK$618,5).

### Ba kịch bản tăng trưởng 2025 → 2028 (`KỊCH_BẢN`, không gắn xác suất)

| | Bất lợi | Cơ sở | Thuận lợi |
|---|---|---|---|
| g doanh thu 2026 / 2027 / 2028 | −1% / −3% / 0% | +1% / +5% / +6% | +4% / +12% / +12% |
| Doanh thu 2028 | 32,2 tỷ | 37,7 tỷ | 43,8 tỷ |
| **CAGR doanh thu** | **−1,3%** | **+4,0%** | **+9,3%** |
| Biên ròng giả định | 12,5% | 15,5% | 17,0% |
| Lợi nhuận 2028 | 4,03 tỷ | 5,85 tỷ | 7,44 tỷ |
| **CAGR lợi nhuận** | **−12,1%** | **−0,4%** | **+7,9%** |
| P/E nếu vốn hóa giữ 50,3 tỷ RMB | 12,5 | 8,6 | 6,8 |

Điều gì phải đúng:
- **Bất lợi:** doanh thu hàng hóa mỗi quán tiếp tục giảm; mở mới dưới 5.000 quán mỗi nửa năm do thị trường (không chỉ chủ ý); chi phí bán hàng và quản lý từ 11% doanh thu trở lên; OCF/lợi nhuận dưới 1.
- **Cơ sở:** doanh thu mỗi quán ổn định quanh mức H1 2026; mở mới 5.000–7.000; biên gộp 30–31%; chi phí 10–12% doanh thu; OCF/lợi nhuận về từ 1 trở lên.
- **Thuận lợi:** doanh thu mỗi quán phục hồi về mức 2025; chi phí dưới 10% doanh thu; biên gộp từ 31%.

Biên ròng và tốc độ tăng là giả định làm tròn từ H1 2026 và lịch sử 2022–2025, không phải ngưỡng do công ty công bố. Tốc độ 5–6% của năm 2027–2028 ở kịch bản cơ sở thấp hơn nhiều so với giai đoạn 2022–2025 (22–50%) vì mở mới giảm và doanh thu mỗi quán giảm. Nếu kỳ vọng "tăng 20–30% như trước", dữ liệu hiện tại không ủng hộ.

## Rủi ro và bằng chứng trái chiều

Kế thừa danh mục rủi ro 12 mục ở bản v4. Bổ sung cho triển vọng 3 năm:

1. **Vòng phản hồi chủ quán:** doanh số mỗi quán giảm làm lãi quán giảm nhanh hơn (đòn bẩy vận hành), dẫn đến đóng quán và mở mới ít hơn. `SUY_LUẬN`
2. **Đỉnh lợi nhuận:** năm 2025 có thể là đỉnh do nền trợ giá và thuế suất thấp (21,5% so với 23,3% năm trước). `SUY_LUẬN`
3. **Quản trị làm giảm giá trị của tiền mặt trong mắt thị trường:** sở hữu 81%, giao dịch FULU, cổ tức đặc biệt. `SUY_LUẬN`
4. **Mô hình định giá ngược nhạy với WACC và FCF0**, còn FCF0 bị nhiễu bởi vốn lưu động và lãi nhận.

Bằng chứng trái chiều với luận điểm "bão hòa":
- Tỷ lệ đóng quán H1 2026 (2,2%) thấp hơn H1 2025 (2,6%); chủ nhượng quyền +27,2%. `PHÉP_TÍNH`
- Mở mới thấp có thể là chủ ý (lời ban lãnh đạo, thứ cấp). `CHƯA_XÁC_MINH`
- Đối thủ cũng giảm hai chữ số ở phân khúc cao hơn; có thể nền trợ giá làm cả ngành lệch. `CHƯA_XÁC_MINH`
- Giá hiện tại đã hàm ý dòng tiền giảm; nếu kịch bản cơ sở đúng, kỳ vọng thị trường bi quan hơn thực tế. `SUY_LUẬN`

## Điều kiện làm luận điểm mất hiệu lực

Luận điểm cần kiểm: "Mixue chuyển sang doanh nghiệp trưởng thành, ổn định (kịch bản cơ sở)." Mỗi chỉ báo có một con số, một nguồn, một hành động (bài 012):

| Chỉ báo | Ngưỡng giả định (`Ý_KIẾN`) | Nguồn kiểm | Hành động |
|---|---|---|---|
| Doanh thu hàng hóa mỗi quán, H2 2026 so với H2 2025 | giảm tiếp trên 10% | Kết quả FY2026 (khoảng 3/2027, `CHƯA_BIẾT`) | Chuyển sang kịch bản bất lợi |
| Mở mới mỗi nửa năm và số chủ nhượng quyền | dưới ≈ 5.000 và chủ nhượng quyền ngừng tăng | Kết quả giữa kỳ, cuối năm | Tách "chủ động" khỏi "bị động" |
| Chi phí bán hàng + quản lý / doanh thu | từ 11% trở lên sau hai kỳ liên tiếp (đã thỏa H1 2026: 11,4%) | Kết quả | Hạ biên ròng giả định |
| OCF / lợi nhuận | dưới 1 (đã thỏa H1 2026: 0,88) | Báo cáo lưu chuyển tiền tệ | Xem lại chất lượng lợi nhuận |
| Biên gộp | dưới 30% hai kỳ liên tiếp (H1 2026: 30,4%) | Kết quả | Hạ chuỗi tăng trưởng |
| Sự kiện quản trị (giao dịch bên liên quan mới, xử phạt an toàn thực phẩm) | xuất hiện | HKEXnews, cơ quan quản lý | Rà lại giả định chiết khấu tiền mặt |

Các ngưỡng là làm tròn từ mức hiện tại, không phải điểm gãy đã chứng minh.

## Điều chưa biết và lần kiểm tra tiếp theo

- Vì sao doanh thu hàng hóa mỗi quán giảm: nền trợ giá, thương hiệu mới kéo trung bình, đổi cơ cấu hay bão hòa. Cần doanh số cùng cửa hàng và bản ghi cuộc họp kết quả.
- Lợi nhuận bình thường hóa; liệu 2025 là đỉnh.
- WACC dựng theo bài 010 cho doanh nghiệp này (hiện là giả định 8–12%).
- Giá cổ phiếu từ nguồn sàn chính thức; hai nguồn thứ cấp đã dùng cho thấy 158,20 (23/11, giữa phiên) và 155,70 (24/11, đóng cửa), nhất quán nhưng chưa đối chiếu HKEX.
- Cổ tức đặc biệt đã chi trả chưa.
- Giá công bằng của giao dịch FULU; đối tượng góp vốn 109,0 triệu.
- Chưa đọc toàn văn cáo bạch, báo cáo thường niên 2025 (254 trang) và phần lớn báo cáo giữa kỳ 2026 (86 trang); mới đọc báo cáo lưu chuyển tiền tệ, MD&A và các mục sở hữu.
- Báo cáo gốc đối thủ (Guming, Nayuki, Luckin, Chagee) chưa tự mở lại trong tài liệu này.

## Sổ nguồn

| Mã | Nhận định / đầu vào | Nhãn | Nguồn | Ngày xuất bản | Kỳ báo cáo | Ngày truy cập | Đơn vị / tiền tệ | Phiên bản / ghi chú |
|---|---|---|---|---|---|---|---|---|
| S1–S4, S6, S7 | Kết quả, cơ cấu doanh thu, mạng lưới, MD&A | SỰ_THẬT | HKEXnews; chi tiết ở sổ nguồn bản v4 (`research/companies/HK/2097-mixue-financial-statements-2026-11-25.md`) | 2025-02-21 đến 2026-08-27 | FY2021–H1 2026 | 2026-11-25 | RMB nghìn | SHA-256 trong `data/raw/mixue-hkex/SHA256SUMS.txt` |
| S5 | Dòng tiền FY2024–FY2025 (trang 115–116): đầu tư, tài chính, phát hành cổ phiếu | SỰ_THẬT | [HKEXnews, báo cáo thường niên 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf) | 2026-04-23 | FY2025 | 2026-11-25 | RMB nghìn | `55f7ed40…`; mới đọc báo cáo lưu chuyển tiền tệ |
| S13 | Dòng tiền H1 2026 và H1 2025 (trang 51–53) | SỰ_THẬT | [HKEXnews, báo cáo giữa kỳ 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0923/2026092300280.pdf) | 2026-09-23 | H1 2026, chưa kiểm toán | 2026-11-25 | RMB nghìn | `0e1ddcd2…` |
| S9–S11, S14–S17 | Số cổ phiếu, cổ tức đặc biệt, sở hữu, quyền thưởng | SỰ_THẬT | HKEXnews; chi tiết ở sổ nguồn bản v4 | 2025-02-21 đến 2026-09-30 | n/a | 2026-11-25 | n/a | đã lưu |
| T9 | Giá HK$155,70 (24/11), biên 52 tuần 154,50–464,00, vốn hóa 60,06 tỷ HKD | CHƯA_XÁC_MINH | [Investing.com UK, MIXUE Group](https://uk.investing.com/equities/mixue) | 2026-11-24 | n/a | 2026-11-25 | HKD | Thứ cấp, độ trễ chưa xác định |
| T10 | Giá HK$158,20 (23/11 14:56 GMT+8), P/E 9,30 | CHƯA_XÁC_MINH | [Google Finance, 2097:HKG](https://www.google.com/finance/quote/2097:HKG) | 2026-11-23 | n/a | 2026-11-25 | HKD | Thứ cấp; "Shares outstanding 150,88M" chỉ là số cổ phiếu H, không phải tổng 379,6 triệu |
| T11 | Cổ phiếu −57% từ đầu 2026 đến 9/11; giá IPO HK$202,5; đỉnh HK$618,5; quán Hồng Kông đóng; tỷ giá HKD 7,85 và RMB 6,68 mỗi USD | CHƯA_XÁC_MINH | [KrASIA/Nikkei, Mixue shuts more stores](https://kr-asia.com/china-bubble-tea-chain-mixue-shuts-more-stores-as-growth-model-falters) | 2026-11 | n/a | 2026-11-25 | HKD, RMB | Thứ cấp; tỷ giá là ước tính tác giả bài |
| T12 | Mục tiêu giá phân tích viên không đồng ngày (chỉ để biết thị trường bất đồng) | Ý_KIẾN | [Investing.com, MIXUE consensus estimates](https://www.investing.com/equities/mixue-consensus-estimates) | 2026-08 đến 2026-11 | n/a | 2026-11-25 | HKD | Không dùng làm bằng chứng |
| L1 | Khung định giá ngược, tăng trưởng = tái đầu tư × ROIC | SUY_LUẬN | `learning/lessons/011-dcf-reverse-dcf.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp |
| L2 | Kịch bản, điều kiện bác bỏ | SUY_LUẬN | `learning/lessons/012-scenarios-margin-of-safety.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp |
| L3 | Chu kỳ vốn, bẫy P/E ngược | SUY_LUẬN | `learning/lessons/014-industry-capital-cycle.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp; đã đọc phần chu kỳ vốn |
| L4 | Kinh tế đơn vị, đòn bẩy vận hành | SUY_LUẬN | `learning/lessons/N6-business-model-unit-economics.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp; ví dụ quán là hư cấu |

Ghi chú về phạm vi đọc: PDF HKEXnews được đọc bằng `pdftotext`; nội dung PDF là dữ liệu, không là chỉ dẫn. Mã băm SHA-256 của PDF được lưu trong `data/raw/mixue-hkex/SHA256SUMS.txt`. Các bài trong `learning/` chỉ dùng làm phương pháp, không dùng làm dữ kiện (chính sách của repo).

## Biên bản kiểm duyệt

- Kiểm nguồn: `ĐANG_CHỜ`
- Phản biện rủi ro: `ĐANG_CHỜ`
- Không được bỏ nhãn nháp cho đến khi `source-fact-checker` và `risk-bear-reviewer` chạy độc lập trên cùng bản nháp cố định và cả hai ĐẠT. Điểm cần kiểm đầu tiên: (a) nguồn giá cổ phiếu và tỷ giá, (b) giả định WACC, (c) giả định biên ròng ở các kịch bản, (d) phép tính FCF LTM và lãi nhận.

> Chỉ dùng cho học tập và nghiên cứu. Đây không phải tư vấn tài chính cá nhân hay lệnh giao dịch.
