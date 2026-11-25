# BẢN NHÁP - CHƯA KIỂM DUYỆT: MIXUE Group, câu chuyện doanh nghiệp, dòng tiền và triển vọng 3 năm (2097.HK)

- Chốt dữ liệu lúc: `2026-11-25 10:00 +07` (báo cáo công ty: HKEXnews, tệp PDF đã lưu và đối chiếu mã băm SHA-256; giá cổ phiếu: giá **đóng cửa 24/11/2026** từ nguồn thứ cấp; phiên 25/11 chưa đóng khi chốt)
- Quốc gia / thị trường / sở giao dịch: Trung Quốc đại lục (hoạt động chính), niêm yết cổ phiếu H tại HKEX mã `2097` từ 2025-03-03
- Chuẩn kế toán: IFRS Accounting Standards; kiểm toán Ernst & Young (Hong Kong)
- Tiền tệ / đơn vị báo cáo: RMB; số gốc tính theo RMB nghìn, bài này làm tròn sang RMB triệu hoặc tỷ
- Phạm vi: (1) kể lại mô hình kinh doanh, nguồn thu, dòng tiền vào–ra và đầu tư; (2) đánh giá khả năng bão hòa, vị trí giá so với các mốc tham chiếu và tăng trưởng 3 năm theo kịch bản, dùng khung các bài 011, 012, 014, N6. **Không định giá nội tại, không kết luận cổ phiếu rẻ hay đắt, không đưa khuyến nghị mua, bán, nắm giữ.**
- Tài liệu liên quan: nghiên cứu nền `research/companies/HK/2097-mixue-financial-statements-2026-11-25.md` (bản v4); dữ liệu gốc `data/raw/mixue-financials-2026-11-25.json`; PDF và mã băm `data/raw/mixue-hkex/`; phép tính `data/processed/mixue-financial-calculations-2026-11-25.md` và `data/processed/mixue-outlook-scenarios-2026-11-25.md` (bản v2)
- Kiểm nguồn: lượt 1 (v1, `92b496ae…`) `ĐẠT` có điều kiện, 0 lỗi nghiêm trọng (`reviews/2097-mixue-outlook-fact-check-v1.md`); bản v2 này `ĐANG_CHỜ` kiểm lại
- Phản biện rủi ro: lượt 1 (v1, `92b496ae…`) `KHÔNG_ĐẠT`, 1 lỗi CAO và 7 điểm TRUNG_BÌNH (`reviews/2097-mixue-outlook-bear-review-v1.md`); bản v2 này `ĐANG_CHỜ` kiểm lại
- Lịch sử: v1 (`92b496ae…`) được lưu nguyên vẹn tại `reviews/2097-mixue-outlook-draft-v1-sha-92b496ae.md`. Bản v2 này sửa các phát hiện của hai biên bản (bảng đối chiếu ở cuối), **chưa được hai agent kiểm duyệt đọc lại**; không được bỏ nhãn nháp.

> Không phải lời khuyên mua, bán hay nắm giữ. Các kịch bản là khung theo dõi, không gắn xác suất, không phải dự báo.

## Tóm tắt bài học

1. **Mixue là nhà cung ứng chuỗi cung ứng, không phải chuỗi tự bán lẻ.** 93,7% doanh thu 2025 là bán hàng hóa cho cửa hàng, 4,0% bán thiết bị, 2,4% phí dịch vụ nhượng quyền. `SỰ_THẬT` [S4]. Doanh thu xấp xỉ **số quán × lượng hàng mỗi quán nhập**. `SUY_LUẬN`
2. **Tiền không bị đốt vào mở rộng; nó nằm trong "két".** Năm 2025 OCF là 6.039,0 triệu, capex tài sản cố định chỉ 685,1 triệu, trong khi mua ròng sản phẩm quản lý tài sản (FVTPL) khoảng 5.332,6 triệu. `SỰ_THẬT` + `PHÉP_TÍNH` [S5]. Cuối H1 2026 tiền, tiền gửi và FVTPL đạt 21.640,7 triệu, nợ vay bằng 0. `SỰ_THẬT` [S7]
3. **H1 2026 là điểm ngoặt.** Doanh thu +2,3%, lợi nhuận −14,7%, OCF −37,4%, trong khi số quán +20,7%; doanh thu hàng hóa mỗi quán giảm khoảng 15–17% (tùy mẫu số). `SỰ_THẬT` + `PHÉP_TÍNH` [S7, S13]. Nguyên nhân `CHƯA_BIẾT`; hai giả thuyết (nền trợ giá ngành; đặc thù Mixue) được giữ cả hai, và bằng chứng ngoài (mục "Bằng chứng trái chiều") **làm giả thuyết "ngành" yếu hơn bản v1 đã trình bày**.
4. **"Chết" nên tách thành ba lớp** (thanh khoản; mạng lưới chủ quán; giá trị với cổ đông). Với lớp **thanh khoản**, rủi ro cạn tiền trong 3 năm thấp: tiền ròng khoảng 20 tỷ RMB, nợ vay 0, OCF LTM khoảng 4,8 tỷ. `PHÉP_TÍNH`. Hai lớp còn lại **không** được bảo đảm bởi bảng cân đối và có kịch bản đuôi ở mục kịch bản.
5. **Vị trí giá so với các mốc tham chiếu.** Giá đóng cửa 24/11/2026 là HK$155,70, thấp hơn giá IPO HK$202,5 khoảng 23% và thấp hơn đỉnh 52 tuần HK$464 khoảng 66%; đó là mốc neo, không phải bằng chứng về mức hợp lý. `SỰ_THẬT` (giá, nguồn thứ cấp) + `PHÉP_TÍNH`. Câu hỏi quan trọng hơn là **lợi nhuận bình thường hóa nằm ở đâu**; EV/lợi nhuận LTM chỉ 5,5 lần nhưng phụ thuộc vào việc coi tiền mặt có giá trị đầy đủ.
6. **Định giá ngược chịu ảnh hưởng mạnh của chiết khấu tiền mặt và WACC.** Với EV ≈ 30,2 tỷ RMB và FCF LTM ≈ 3,9–4,0 tỷ, g hàm ý nằm khoảng −4,6% đến −0,7% mỗi năm (chiết khấu tiền 0%, WACC 8–12%); nếu thị trường chiết khấu tiền mặt từ khoảng 10–15% thì ở WACC 12% g hàm ý đã về 0, và ở WACC 10% g đảo dấu khi chiết khấu từ khoảng 41–47%. `PHÉP_TÍNH` có nhiều giả định. Không kết luận cổ phiếu rẻ hay đắt.
7. **Tăng trưởng 3 năm (2025 → 2028), kịch bản dựng từ số quán × doanh thu mỗi quán × biên:** doanh thu từ −1,6% (bất lợi) qua +5,3% (cơ sở) đến +11,8% (thuận lợi) mỗi năm; lợi nhuận từ −11,2% qua −1,1% đến +9,3% mỗi năm; kịch bản đuôi −11,7% doanh thu và −29,5% lợi nhuận mỗi năm. `KỊCH_BẢN`. Ở kịch bản cơ sở lợi nhuận **không tăng**.

## Mô hình kinh doanh

- Ba thương hiệu: MIXUE (trà, nước ép, kem; giá lõi RMB 2–8), Lucky Cup (cà phê), FULU Fresh Beer (bia tươi; mua lại, hoàn tất 2025-12-01). `SỰ_THẬT` [S4]
- Chủ quán sở hữu và chịu kết quả cửa hàng, mua nguyên liệu và thiết bị từ Mixue. Công ty tự sản xuất 100% nguyên liệu lõi: 5 cơ sở và 28 kho (cuối 2025), 6 cơ sở và 31 kho (30/6/2026). `SỰ_THẬT` [S4, S7]
- Nợ hợp đồng (tiền chủ quán trả trước) chỉ 485,1 triệu cuối 2025 (khoảng 5,3 ngày doanh thu), nên không phải nguồn vốn lớn. `PHÉP_TÍNH`
- Mạng lưới: 20.001 quán (2021) → 59.823 (2025) → 63.987 (30/6/2026). Hơn 58% quán đại lục ở thành phố hạng ba trở xuống. Chủ nhượng quyền 27.450 (2025), 29.775 (30/6/2026). `SỰ_THẬT` [S1, S4, S7]
- Không khách hàng nào chiếm từ 10% doanh thu trong các kỳ có công bố. `SỰ_THẬT` [S4, S7]

Ẩn dụ giải thích (không phải so sánh số liệu): giống một nhà bán sỉ kiểu Costco của ngành trà; công ty kiếm tiền nhờ quy mô mua, sản xuất và logistics rồi chia lại biên cho chủ quán. `Ý_KIẾN`

## Bối cảnh ngành, vĩ mô và so sánh toàn cầu

Kế thừa từ bản v4 (mục "Bối cảnh ngành"). Điểm chính phục vụ triển vọng:
- Năm 2025 nền tảng giao hàng trợ giá rất mạnh, đẩy đơn đồ uống pha chế (lời công ty, [S4]). Luckin (6-K 2026-11-03, SEC, đã được bên kiểm nguồn mở lại): doanh số cùng cửa hàng tự vận hành Q3 2026 −11,1% (so với +14,3% cùng kỳ năm trước), nguyên nhân do nền so sánh cao vì trợ giá. `SỰ_THẬT` [T5, 6-K]
- Nayuki −13,1% doanh thu; Chagee sụt hai chữ số; Guming và Auntea Jenny doanh thu mỗi quán xấp xỉ phẳng (báo cáo gốc do bên kiểm duyệt mở ở bản v4, tôi chưa tự mở lại). `CHƯA_XÁC_MINH`
- Nikkei Asia / KrASIA (thứ cấp, tháng 11/2026): quán đầu tiên tại Hồng Kông đóng đầu tháng 10; làn sóng đóng quán từ Hồng Kông đến Đông Nam Á; cổ phiếu giảm 57% từ đầu 2026 đến 9/11. `CHƯA_XÁC_MINH`

## Lịch sử và chất lượng tài chính

### Kết quả kinh doanh (RMB triệu)

| | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|
| Doanh thu | 13.575,6 | 20.302,5 | 24.828,9 | 33.559,9 | 14.874,8 | 15.215,8 |
| Tăng trưởng | 31,2% | 49,6% | 22,3% | 35,2% | +39,3% | +2,3% |
| Biên gộp | 28,3% | 29,5% | 32,5% | 31,1% | 31,6% | 30,4% |
| Lợi nhuận | 2.013,1 | 3.186,6 | 4.454,2 | 5.927,1 | 2.718,2 | 2.319,3 |
| Biên ròng | 14,8% | 15,7% | 17,9% | 17,7% | 18,3% | 15,2% |

Nguồn [S1, S4, S6, S7]. `SỰ_THẬT` / `PHÉP_TÍNH`. Biên H2 2025 = (5.927,1 − 2.718,2) / 18.685,1 = 17,2% `PHÉP_TÍNH`. Giải thích năm 2022 (giảm giá 15% cho 69 mặt hàng để hỗ trợ chủ quán qua COVID) và các nhận xét biên khác ở bản v4.

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
| Gửi ròng tiền kỳ hạn > 3 tháng | +2.929,9 | +232,8 | +755,0 | +3.972,0 |
| Dòng tiền đầu tư thuần | −7.019,0 | −6.364,1 | −2.741,8 | −3.384,5 |
| Dòng tiền tài chính thuần | −277,4 | +3.505,4 | +3.578,1 | −51,8 |
| Thu phát hành cổ phiếu | 0 | 3.665,1 | 3.665,1 | 0 |

Nguồn [S5 trang in 114–116; S13 trang in 51–53; trang in, không phải chỉ số trang PDF]. `SỰ_THẬT`; các dòng ròng là `PHÉP_TÍNH` (xem tệp phép tính).

Điều đọc ra:
- **Mô hình ít vốn:** capex hữu hình chỉ 10,8% dòng tiền đầu tư 2025; phần lớn dòng tiền đầu tư (87,5%) là chuyển tiền sang FVTPL và tiền gửi kỳ hạn. `PHÉP_TÍNH`
- **H1 2026 đảo chiều:** thu hồi ròng 908 triệu FVTPL nhưng gửi ròng 3.972 triệu tiền kỳ hạn; tiền và tương đương tiền giảm từ 7.429,1 xuống 6.027,9 triệu. `SỰ_THẬT` [S13]
- Mua FULU hợp nhất chỉ tốn ròng 13,7 triệu tiền mặt (FULU nắm 271,9 triệu tiền). Góp vốn công ty liên kết 109,0 triệu (đối tượng `CHƯA_BIẾT`: thuyết minh 19 chỉ nêu "không trọng yếu riêng lẻ"). `SỰ_THẬT` [S5]
- Thu nhập lãi và quản lý tài sản 2025 là 330,0 triệu, khoảng 4,4% lợi nhuận trước thuế; lỗ tỷ giá 79,5 triệu (2025) và 153,8 triệu (H1 2026). `SỰ_THẬT` [S4, S7]
- OCF H1 2026 giảm 1.225,6 triệu. Phải trả người bán đảo chiều là nguyên nhân lớn nhất (−378,7 so với +739,4, chênh −1.118,1), nhưng tồn kho bù lại +632,8 (−176,1 so với −808,9) và lợi nhuận trước thuế giảm 492,6. OCF/lợi nhuận 0,88 (H1 2025: 1,20). `SỰ_THẬT` + `PHÉP_TÍNH` [S13]
- Vốn lưu động H1 2026: phải trả người bán 1.859,9 (cuối 2025: 2.212,5, −16%); tồn kho 3.828,2 (+4,2% trong khi doanh thu gần phẳng); nợ hợp đồng 594,0. `SỰ_THẬT` [S13, bảng cân đối]

### Điểm ngoặt H1 2026

Doanh thu +2,3%, lợi nhuận −14,7%, số quán +20,7%. Lợi nhuận trước thuế giảm 492,6 triệu: chi phí bán hàng và quản lý tăng 381,7 triệu (≈ 77,5% mức giảm), lợi nhuận gộp giảm 76,7 triệu. Mở mới H1 2026 là 5.455 (−29,3%); đóng 1.289; mở mới ròng 4.166. Mạng lưới nước ngoài thu hẹp 4.895 → 4.378. Doanh thu hàng hóa mỗi quán so với cùng kỳ: −14,6% (quán cuối kỳ, tổng), −16,5% (đại lục), −17,2% (bình quân nhượng quyền); doanh thu mỗi quán bình quân của cả tập đoàn: −17,8%. `PHÉP_TÍNH`. Chi tiết và phần rà soát ở bản v4.

## Ban lãnh đạo, quản trị và phân bổ vốn

Kế thừa từ bản v4:
- Hai nhà sáng lập nắm ≈ 81% vốn qua thỏa thuận hành động phối hợp. `SỰ_THẬT` [S14]
- Mua FULU (2025-10-01 ký, 2025-12-01 hoàn tất): giao dịch bên liên quan, ≈ 80% FULU thuộc người nhà một cổ đông kiểm soát; giá công bằng hay không `CHƯA_BIẾT`. `SỰ_THẬT` [S5]
- Cổ tức đặc biệt RMB 2,65 mỗi cổ phiếu (≈ 1.006 triệu, khoảng 43% lợi nhuận H1 2026) **đã được đại hội cổ đông thông qua ngày 30/9/2026 và dự kiến chi trả ngày 6/11/2026; việc đã chi trả `CHƯA_XÁC_MINH`**. Khoảng 816 triệu về hai nhà sáng lập theo tỷ lệ sở hữu. `SỰ_THẬT` [S10, S11] (phần "đã chi trả" là `CHƯA_XÁC_MINH`)
- Quyền thưởng cổ phiếu 12.023.300 (≈ 3,17%) giá mua HK$18,47 so với giá thị trường HK$184,70 khi cấp. `SỰ_THẬT` [S15]

## Triển vọng 3 năm: bão hòa hay tiếp tục tăng

### "Chết" gồm ba lớp

| Lớp | Câu hỏi | Bằng chứng hiện có | Đánh giá |
|---|---|---|---|
| 1. Thanh khoản | Công ty có cạn tiền không? | Tiền ròng ≈ 20,6 tỷ RMB, nợ vay 0, nợ ngắn hạn 5,35 tỷ, OCF LTM ≈ 4,8 tỷ `SỰ_THẬT` + `PHÉP_TÍNH` | Rủi ro thấp trong 3 năm `SUY_LUẬN` |
| 2. Mạng lưới chủ quán | Chủ quán còn lãi để mở và giữ quán không? | Số quán đóng tuyệt đối tăng (1.187 → 1.289 trong H1; 2.527 cả năm 2025); doanh thu mỗi quán −15% đến −18%; kinh tế đơn vị quán `CHƯA_BIẾT` | **Rủi ro thật**; kịch bản đuôi mục dưới |
| 3. Giá trị với cổ đông | Tiền mặt có đến được cổ đông không? | Sở hữu ≈ 81% tập trung; giao dịch FULU bên liên quan; cổ tức đặc biệt chảy theo tỷ lệ sở hữu; chưa đọc đủ báo cáo (cam kết vốn, kiện tụng, bảo lãnh) `CHƯA_BIẾT` | Không loại trừ; xem chiết khấu tiền mặt ở mục định giá ngược |

Báo cáo thường niên 2025 (254 trang) và phần lớn báo cáo giữa kỳ chưa đọc toàn văn, nên các khoản cam kết vốn, kiện tụng và bảo lãnh chưa được rà. `CHƯA_BIẾT`

### Cơ chế bão hòa (bài 014 và N6; đây là phép so sánh, không phải ngành thâm dụng tài sản cố định)

- Bài 014 mô tả chu kỳ vốn năm pha. **Phép so sánh:** ở Mixue "nhà đầu tư" là hơn 29.000 chủ quán nhượng quyền. Mở mới H1 2026 giảm 29,3% là một dấu hiệu có thể gợi pha bùng nổ đầu tư đang hạ nhiệt; liệu đã chuyển sang dư cung hay chưa `CHƯA_BIẾT`. `SUY_LUẬN`
- Doanh thu hàng hóa mỗi quán giảm khoảng 15–18% `PHÉP_TÍNH` (mẫu số nhiễu: FULU, cửa hàng mới, hàng bán nước ngoài). Theo bài N6, định phí không giảm theo doanh số nên lãi giảm nhanh hơn doanh số. Minh họa **hư cấu** (số tự đặt, không phải số của Mixue): doanh số quán −10% làm lãi quán từ 15,0 xuống 10,0 (−33%). Đại lượng này **không đồng nhất** với doanh thu hàng hóa mỗi quán của Mixue, vì đó là doanh thu Mixue bán cho quán, chịu ảnh hưởng của tồn kho tại quán, cơ cấu thương hiệu và giá bán buôn. `KỊCH_BẢN`
- Kinh tế đơn vị thật của quán và doanh số cùng cửa hàng `CHƯA_BIẾT` (công ty không công bố).

### Vị trí giá so với các mốc tham chiếu

| Chỉ báo | Giá trị | Nguồn |
|---|---|---|
| Giá đóng cửa 24/11/2026 | HK$ 155,70 | Investing.com, StockAnalysis (thứ cấp) |
| Giá đóng cửa 23/11/2026 | HK$ 158,20 | Investing.com, StockAnalysis (Google Finance không mở được) |
| Giá đóng cửa 16/11/2026 | HK$ 170,1 (24/11 thấp hơn ≈ 8,5%) | BNext (thứ cấp); nguyên nhân giảm tuần cuối `CHƯA_BIẾT` |
| Biên 52 tuần | 154,50–464,00 (154,50 là đáy trong ngày 24/11) | Investing.com, StockAnalysis |
| Giá IPO; đỉnh trong ngày 6/2025 | HK$ 202,5; HK$ 618,5 | KrASIA/Nikkei |
| Vốn hóa | ≈ 59,1 tỷ HKD ≈ 50,8 tỷ RMB (tỷ giá PBoC 0,85954 cho cổ tức; 50,3 tỷ nếu 0,851) | `PHÉP_TÍNH` |
| Tiền ròng giả định (sau cổ tức 1,0 tỷ; số dư 30/6/2026) | ≈ 20,6 tỷ RMB | `PHÉP_TÍNH` |
| EV | ≈ 30,2 tỷ RMB (29,2 nếu cổ tức chưa trả; 29,7 và 28,7 theo 0,851) | `PHÉP_TÍNH` |
| P/E LTM (lợi nhuận gồm cổ đông thiểu số) | ≈ 9,2 lần (Google Finance: 9,30; Investing.com tự mâu thuẫn 9,1x và 11,1x) | `PHÉP_TÍNH` |
| EV / lợi nhuận LTM | ≈ 5,5 lần | `PHÉP_TÍNH` |

- Giá phiên 25/11 hiển thị khoảng HK$161 khi chốt, chưa đóng cửa nên không dùng. Tiền ròng dùng số dư 30/6/2026, chưa cộng dòng tiền tháng 7–11 (chưa công bố).
- Giá đã giảm khoảng 66% từ đỉnh 52 tuần và khoảng 23% dưới giá IPO (155,70 / 202,5 − 1 = −23,1%). Các mốc 464 và 618,5 là điểm neo tâm lý; −66% không chứng minh gì về mức hợp lý. `PHÉP_TÍNH`
- **Lợi nhuận 2025 có phải đỉnh?** Bài 014 mục "bẫy P/E ngược" nói P/E thấp ở đỉnh lợi nhuận dễ gây hiểu lầm. Mixue không phải cổ phiếu chu kỳ thuần; phép so sánh có điều kiện và chỉ đáng tin nếu lợi nhuận bình thường hóa thấp hơn lợi nhuận 2025. Bằng chứng ủng hộ: biên ròng 17,7% (2025) → 15,2% (H1 2026), doanh thu mỗi quán −15% đến −18%. Bằng chứng yếu hơn: thuế suất hiệu dụng 21,5% (2025, từ 23,3%) chỉ giải thích khoảng 139 triệu (2,4%) mức tăng 2025, và thuế suất H1 2026 (22,1%) chỉ đóng góp khoảng 0,5 điểm % vào mức giảm lợi nhuận; thuế không phải nguyên nhân chính của đỉnh. `SUY_LUẬN`
- Nếu lợi nhuận 2028 chỉ còn 4,15 tỷ (kịch bản bất lợi) thì cùng vốn hóa tương ứng P/E ≈ 12,2 lần. `PHÉP_TÍNH`

### Định giá ngược (bài 011)

Giả định: `EV = FCF0 × (1 + g) / (WACC − g)`; FCF0 là FCF LTM: **3.989,7 triệu (thô)** hoặc **3.871,4 triệu (đã trừ lãi nhận LTM 150,8 triệu × (1 − 21,5%), theo bài 011)**. FCF thô gồm lãi nhận được, nên cộng cả tiền vào cầu nối sẽ tính tiền hai lần; vì vậy hai biến thể cùng được nêu. WACC 8–12% là giả định minh họa, **chưa dựng theo bài 010** (`CHƯA_BIẾT`). EV = vốn hóa − tiền ròng × (1 − chiết khấu); "chiết khấu tiền" là cách đo giá mà thị trường áp cho tiền mặt (quản trị, thuế khấu trừ, tiền bị hạn chế, pháp nhân giữ tiền), mức thực tế `CHƯA_BIẾT`.

g hàm ý (% mỗi năm), tỷ giá 0,85954, cổ tức đã trừ:

| Chiết khấu tiền | EV (tỷ RMB) | FCF0 3.989,7: WACC 8 / 10 / 12% | FCF0 3.871,4: WACC 8 / 10 / 12% |
|---|---|---|---|
| 0% | 30,2 | −4,6 / −2,8 / −1,1 | −4,3 / −2,5 / −0,7 |
| 10% | 32,2 | −3,9 / −2,1 / −0,3 | −3,6 / −1,8 / 0,0 |
| 30% | 36,4 | −2,7 / −0,9 / +0,9 | −2,4 / −0,6 / +1,2 |
| 50% | 40,5 | −1,7 / +0,1 / +2,0 | −1,4 / +0,4 / +2,2 |

Ngưỡng chiết khấu tiền để g hàm ý bằng 0: ≈ 88–95% (WACC 8%), ≈ 41–47% (WACC 10%), ≈ 10–15% (WACC 12%).

Cách đọc: kết luận "giá hàm ý dòng tiền giảm" **vững ở WACC 8–10% khi chiết khấu tiền dưới khoảng 40%** và **mong manh ở WACC 12%**. Đây là `PHÉP_TÍNH` nhạy; không nói cổ phiếu rẻ hay đắt, và tài liệu này **không** kết luận rằng kỳ vọng của thị trường bi quan hơn hay lạc quan hơn thực tế. Các điều có thể làm kết quả đổi hướng:
1. Chiết khấu tiền mặt vì quản trị (sở hữu tập trung, giao dịch bên liên quan, cổ tức chảy về người kiểm soát) và các điều chưa biết: thuế khấu trừ, tiền bị hạn chế (bảng cân đối H1 2026 chỉ cho tổng 21.650,8, lệch 10,1 so với 21.640,7), cơ cấu tiền theo đồng tiền và pháp nhân.
2. FCF0 chưa chuẩn hóa: vốn lưu động LTM hao (phải trả người bán và tồn kho); nếu FCF chuẩn hóa cao hơn thì g hàm ý còn âm hơn.
3. Lợi nhuận bình thường hóa `CHƯA_BIẾT`.
4. Dòng tiền ra khả dĩ chưa thấy trong FCF0 (hỗ trợ chủ quán, máy cà phê, quỹ hỗ trợ; xem mục "Bằng chứng trái chiều").

### Bốn kịch bản 2025 → 2028 dựng từ số quán × doanh thu mỗi quán × biên (`KỊCH_BẢN`, không gắn xác suất)

Công thức: `quán cuối năm = đầu năm + mở mới ròng`; `doanh thu = quán bình quân × doanh thu mỗi quán (RPS)`; `lợi nhuận = doanh thu × biên ròng`. Gốc 2025: quán bình quân 53.151, RPS 0,6314 triệu RMB, doanh thu 33,56 tỷ, lợi nhuận 5,93 tỷ. Chi tiết và script ở `data/processed/mixue-outlook-scenarios-2026-11-25.md` mục 5.

| | Đuôi: vòng phản hồi chủ quán | Bất lợi | Cơ sở | Thuận lợi |
|---|---|---|---|---|
| Mở mới ròng 2026 / 2027 / 2028 (quán) | +6.000 / −3.000 / −6.000 | +7.000 / +2.000 / −1.000 | +8.000 / +5.000 / +3.500 | +9.000 / +6.500 / +5.500 |
| Thay đổi doanh thu mỗi quán | −20% / −15% / −10% | −17% / −8% / −3% | −15% / −2% / 0% | −12% / +5% / +3% |
| Tăng doanh thu 2026 / 2027 / 2028 | −5,4% / −13,0% / −16,3% | −1,1% / −1,5% / −2,3% | +2,1% / +8,0% / +6,0% | +6,5% / +17,7% / +11,6% |
| Doanh thu 2028 | 23,1 tỷ | 32,0 tỷ | 39,2 tỷ | 46,9 tỷ |
| **CAGR doanh thu** | **−11,7%** | **−1,6%** | **+5,3%** | **+11,8%** |
| Biên ròng giả định | 9,0% | 13,0% | 14,6% | 16,5% |
| Lợi nhuận 2028 | 2,08 tỷ | 4,15 tỷ | 5,73 tỷ | 7,74 tỷ |
| **CAGR lợi nhuận** | **−29,5%** | **−11,2%** | **−1,1%** | **+9,3%** |
| P/E nếu vốn hóa 50,8 tỷ RMB giữ nguyên (*) | 24,4 | 12,2 | 8,9 | 6,6 |

(*) Cột này chỉ là thước đo so sánh với giá hiện tại; nó không phải dự báo giá và không phải giả định rằng thị trường giữ vốn hóa.

Cơ sở của giả định:
- Biên ròng cơ sở 14,6% = mức đang chạy: biên H1 2026 là 15,2%, H1 thường cao hơn cả năm ≈ 0,6 điểm % (2025: 18,3% so với 17,7%). Biên bất lợi 13,0% trừ thêm ≈ 1,6 điểm % (chi phí bán hàng + quản lý thêm 1 điểm % và biên gộp thấp hơn 1 điểm %, sau thuế 22%); biên thuận lợi 16,5% giữa mức đang chạy và mức 2025; biên đuôi 9,0% là giả định `Ý_KIẾN`. Các biên là làm tròn từ dữ liệu, không phải ngưỡng công ty công bố.
- Năm 2026 đã biết một nửa (H1 doanh thu +2,3%): cơ sở hàm ý H2 gần +2%, bất lợi H2 ≈ −4%, thuận lợi H2 ≈ +10% so với nền H2 2025 đã +32,0%.
- Mở mới ròng cơ sở thấp hơn nhiều so với 13.344 ròng của 2025 (H1 2026 đã +4.166 ròng).
- **Đuôi: vòng phản hồi chủ quán** mô hình hóa chuỗi doanh thu mỗi quán giảm → lãi quán giảm → đóng quán → mở mới giảm; **không phải dự đoán**. Hai đuôi khác **chưa mô hình hóa số**: (a) sự cố an toàn thực phẩm hoặc quy định làm một năm doanh thu giảm thêm và biên giảm (quy mô và xác suất `CHƯA_BIẾT`); (b) chiết khấu tiền mặt vì quản trị, xử lý ở bảng độ nhạy trên.
- Nếu kỳ vọng "tăng 20–30% như 2022–2025", dữ liệu hiện tại không ủng hộ ngay cả ở kịch bản thuận lợi.

Điều gì phải đúng:
- **Bất lợi:** doanh thu mỗi quán còn giảm mạnh năm 2026 (< −16%) và giảm tiếp 2027; mở mới ròng dưới 3.000 trong 2027; chi phí bán hàng + quản lý từ 11% doanh thu trở lên; OCF/lợi nhuận dưới 1.
- **Cơ sở:** doanh thu mỗi quán cả năm 2026 giảm khoảng 13–17% rồi ổn định; mở mới ròng 5.000 (2027) và 3.500 (2028); biên gộp 30–31%; chi phí bán hàng + quản lý 10–11% doanh thu; OCF/lợi nhuận về từ 1 trở lên.
- **Thuận lợi:** doanh thu mỗi quán hồi phục từ 2027; mở mới ròng 6.500 và 5.500; chi phí dưới 10% doanh thu; biên gộp từ 31%.
- **Đuôi:** lãi chủ quán sụt đủ để quán đóng nhanh hơn mở; doanh thu mỗi quán giảm hai chữ số liên tiếp.

## Rủi ro và bằng chứng trái chiều

Kế thừa danh mục rủi ro 12 mục ở bản v4. Bổ sung cho triển vọng 3 năm:
1. **Vòng phản hồi chủ quán:** doanh số mỗi quán giảm làm lãi quán giảm nhanh hơn (đòn bẩy vận hành), dẫn đến đóng quán và mở mới ít hơn. `SUY_LUẬN` (mô hình hóa ở kịch bản đuôi)
2. **Đỉnh lợi nhuận:** năm 2025 có thể là đỉnh; mức bình thường hóa `CHƯA_BIẾT`. `SUY_LUẬN`
3. **Quản trị làm giảm giá trị của tiền mặt trong mắt thị trường:** sở hữu 81%, giao dịch FULU, cổ tức đặc biệt. `SUY_LUẬN`
4. **Định giá ngược nhạy với WACC, chiết khấu tiền và FCF0** (mục trên).

Bằng chứng trái chiều với luận điểm "bão hòa" (ủng hộ hướng tích cực):
- Tỷ lệ đóng quán H1 2026 (2,2%) thấp hơn H1 2025 (2,6%); chủ nhượng quyền +27,2%. `PHÉP_TÍNH`. **Nhưng** số đóng tuyệt đối tăng (1.187 → 1.289, +8,6%; cả năm 2025 là 2.527, +57,1%), mẫu số tăng +28,7%, và chủ nhượng quyền là chỉ báo trễ, nên bằng chứng này chưa đủ mạnh.
- Mở mới thấp có thể là chủ ý (lời ban lãnh đạo, thứ cấp). `CHƯA_XÁC_MINH`
- Có dấu hiệu H2 2026 tốt hơn H1: Guming nói tỷ trọng đơn giao hàng giảm giúp doanh số quán và lợi nhuận hồi phục từ 6/2026 (tóm tắt tự động, độ tin cậy thấp); Luckin cho biết doanh số cùng cửa hàng cải thiện từng tháng từ tháng 7 đến 9 (6-K). `CHƯA_XÁC_MINH`

Bằng chứng trái chiều **với** giả thuyết "do nền trợ giá ngành" và các rủi ro bị v1 bỏ sót (nguồn thứ cấp, chưa kiểm chứng trừ khi ghi khác):

| Nội dung | Chi tiết | Nhãn / nguồn |
|---|---|---|
| Đối thủ cùng phân khúc vẫn tăng mạnh | Doanh thu H1 2026: Guming (GoodMe) +32%, Auntea Jenny +42%, so với Mixue +2,3% | `CHƯA_XÁC_MINH` [T11, KrASIA/Nikkei; do bên phản biện đọc] |
| Luckin tăng biên khi trợ giá rút | Cùng 6-K: biên hoạt động GAAP +3,8 điểm % lên 15,4%; biên cấp quán tự vận hành +5,8 điểm % lên 23,3%; doanh thu +17,0%. Mixue ngược lại: biên ròng −3,1 điểm %, chi phí bán hàng +22,9%, quản lý +39,4%. Vì vậy "nền trợ giá" không giải thích được sụt biên riêng của Mixue | `CHƯA_XÁC_MINH` [6-K; bên phản biện đọc, bên kiểm nguồn mới xác nhận −11,1% và +14,3%] |
| Lucky Cup co lại | Báo cáo ngành: dừng mở quán huyện/xã từ đầu 2026, tổng quán về ≈ 8.000 từ trên 10.000, đóng ≈ 2.000 quán đuôi | `CHƯA_XÁC_MINH` [T14, CBNData, thứ cấp] |
| Mật độ quán và phí nền tảng | Chủ quán nói quán mới mở cách 400–900 m dù bán kính bảo hộ danh nghĩa 300 m; hoa hồng nền tảng giao hàng ≈ 30% | `CHƯA_XÁC_MINH` [T15, Jiemian, Sina; lời một chủ quán, ẩn danh] |
| Dòng tiền ra chưa thấy trong FCF0 | Máy cà phê trả trước 33.000 RMB (phải nộp thêm 37.000 nếu dưới 40 ly mỗi ngày); Mixue bị báo bỏ ≈ 500 triệu RMB cho máy miễn phí và quỹ hỗ trợ ≈ 1 tỷ RMB | `CHƯA_XÁC_MINH` [T14, T15] |
| An toàn thực phẩm | Đến 29/3/2026: 11.216 khiếu nại tích lũy, 30 ngày gần nhất hơn 70% liên quan an toàn thực phẩm; 6/2025 cơ quan y tế Hồng Kông báo mẫu kem có coliform vượt giới hạn (chưa mở nguồn gốc) | `CHƯA_XÁC_MINH` [T16, Sohu / Trường Giang Thương báo] |
| Quy định | Bản thảo SAMR (6/2026) về trợ giá giao hàng, lấy ý kiến đến 17/7/2026; có thể hỗ trợ (giảm trợ giá cạnh tranh) hoặc làm xấu thêm | `CHƯA_XÁC_MINH` [T17, China Briefing] |
| Nhà phân tích bất đồng | Macquarie Underperform (khởi đầu độ phủ 2025-09-05, mục tiêu HK$279; hiện Sell HK$180, duy trì 31/8/2026); JPMorgan Underweight HK$190; Deutsche Bank Hold HK$203; Jefferies hạ xuống Hold HK$252; CLSA Outperform HK$324; đồng thuận Mua 10, Giữ 7, Bán 4. Chỉ để thấy mức bất đồng, không làm bằng chứng | `Ý_KIẾN` [T12, Investing.com; các mục tiêu không đồng ngày] |
| Tỷ lệ cơ sở | Chuỗi trà đại chúng niêm yết từng giảm mạnh kéo dài: Nayuki ≈ HK$17,1 (6/2021) → ≈ HK$0,68 (10/2026) | `CHƯA_XÁC_MINH` [Digrin, chưa mở nguồn]; chỉ là manh mối |

## Điều kiện làm luận điểm mất hiệu lực

Luận điểm cần kiểm: "Mixue chuyển sang giai đoạn trưởng thành, ổn định (kịch bản cơ sở)." Ba nhóm dưới đây dùng **cùng đơn vị với kịch bản** (thay đổi doanh thu mỗi quán bình quân so với năm trước). Mỗi điều kiện có một con số, một nguồn, một hành động (bài 012). Các ngưỡng là `Ý_KIẾN` làm tròn từ kịch bản.

| Chỉ báo | Vùng cơ sở | Vùng bất lợi / đuôi | Vùng thuận lợi | Nguồn kiểm | Hành động |
|---|---|---|---|---|---|
| Doanh thu mỗi quán bình quân, cả năm 2026 so với 2025 | −13% đến −17% | dưới −17% (đuôi: dưới −20%) | trên −13% | Kết quả FY2026 (khoảng 3/2027, `CHƯA_BIẾT`) | Chọn lại kịch bản |
| Doanh thu mỗi quán bình quân, 2027 so với 2026 | −5% đến +2% | dưới −8% (đuôi: dưới −15%) | trên +3% | Kết quả FY2027 | Chọn lại kịch bản |
| Mở mới ròng cả năm | 2026: ≈ 8.000; 2027: ≈ 5.000 | 2026: dưới 7.000; 2027: dưới 2.000; âm hai năm liên tiếp là đuôi | 2026: trên 9.000 | Kết quả giữa kỳ và cuối năm | Tách "chủ động" khỏi "bị động" bằng số chủ nhượng quyền |
| Chi phí bán hàng + quản lý / doanh thu (so cùng nửa năm: H1 2025 là 9,1%, H1 2026 là 11,4%) | 10–11% | trên 11% | dưới 10% | Kết quả | Hạ biên ròng giả định |
| OCF / lợi nhuận | từ 1 | dưới 1 | trên 1,1 | Báo cáo lưu chuyển tiền tệ | Xem lại chất lượng lợi nhuận |
| Biên gộp | 30–31% | dưới 30% hai kỳ liên tiếp | trên 31% | Kết quả | Hạ chuỗi tăng trưởng |

**Hai chỉ báo đã nằm ngoài vùng cơ sở ngay ở H1 2026:** chi phí bán hàng + quản lý 11,4% (trên 11%) và OCF/lợi nhuận 0,88 (dưới 1). Nghĩa là kịch bản cơ sở **đang lạc quan** ở hai chỉ báo này và phụ thuộc vào việc chúng cải thiện ở H2 2026.

Điều kiện bác bỏ cho các nhận định khác:
- **Bác bỏ "bão hòa" (luận điểm đối lập):** doanh thu mỗi quán bình quân so với cùng kỳ từ 0% trở lên ở hai nửa năm liên tiếp (H2 2026 và H1 2027) **và** mở mới ròng từ 5.000 mỗi nửa năm.
- **Bác bỏ "khó chết" (lớp 1, thanh khoản):** tiền ròng (tiền + tiền kỳ hạn + FVTPL − nợ vay) giảm quá 25% trong hai kỳ liên tiếp mà không do cổ tức đã thông báo; hoặc OCF âm; hoặc xuất hiện giao dịch bên liên quan lớn mới.
- Bằng chứng mới về an toàn thực phẩm, quy định nhượng quyền hoặc giao dịch bên liên quan làm tăng số quán đóng hoặc giảm niềm tin vào quản trị: kích hoạt rà lại kịch bản đuôi.

## Điều chưa biết và lần kiểm tra tiếp theo

- Vì sao doanh thu hàng hóa mỗi quán giảm: nền trợ giá, thương hiệu mới kéo trung bình, đổi cơ cấu, bão hòa hay cạnh tranh. Cần doanh số cùng cửa hàng và bản ghi cuộc họp kết quả.
- Lợi nhuận bình thường hóa; liệu 2025 là đỉnh.
- WACC dựng theo bài 010 cho doanh nghiệp này (hiện là giả định 8–12%).
- Mức chiết khấu mà thị trường áp cho tiền mặt; số tiền bị hạn chế thực; cơ cấu tiền theo đồng tiền và pháp nhân; thuế khấu trừ khi chia cổ tức.
- Giá cổ phiếu từ nguồn sàn chính thức (HKEXnews hoặc báo giá của sở không mở được qua công cụ đọc); Google Finance không mở được; hai nguồn thứ cấp đã dùng có thể chung dữ liệu.
- Tỷ giá tham chiếu đúng ngày 24/11 (đang dùng PBoC trung bình 5 ngày đến 30/9: 0,85954).
- Cổ tức đặc biệt đã chi trả chưa.
- Giá công bằng của giao dịch FULU; đối tượng góp vốn 109,0 triệu.
- Chưa đọc toàn văn cáo bạch, báo cáo thường niên 2025 (254 trang) và phần lớn báo cáo giữa kỳ 2026 (86 trang); mới đọc báo cáo lưu chuyển tiền tệ, bảng cân đối, MD&A và các mục sở hữu.
- Báo cáo gốc đối thủ (Guming, Nayuki, Chagee, Auntea Jenny) chưa tự mở lại; Luckin đã được bên kiểm nguồn mở lại.
- Dòng tiền hỗ trợ chủ quán (máy cà phê, quỹ hỗ trợ) thực tế; số quán Lucky Cup từ công ty.

## Sổ nguồn

| Mã | Nhận định / đầu vào | Nhãn | Nguồn | Ngày xuất bản | Kỳ báo cáo | Ngày truy cập | Đơn vị / tiền tệ | Phiên bản / ghi chú |
|---|---|---|---|---|---|---|---|---|
| S1–S4, S6, S7 | Kết quả, cơ cấu doanh thu, mạng lưới, MD&A | SỰ_THẬT | HKEXnews; chi tiết ở sổ nguồn bản v4 (`research/companies/HK/2097-mixue-financial-statements-2026-11-25.md`) | 2025-02-21 đến 2026-08-27 | FY2021–H1 2026 | 2026-11-25 | RMB nghìn | SHA-256 trong `data/raw/mixue-hkex/SHA256SUMS.txt` |
| S5 | Dòng tiền FY2024–FY2025 (trang in 114–116): lãi nhận 135,4, đầu tư, tài chính, phát hành cổ phiếu | SỰ_THẬT | [HKEXnews, báo cáo thường niên 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf) | 2026-04-23 | FY2025 | 2026-11-25 | RMB nghìn | `55f7ed40…`; mới đọc báo cáo lưu chuyển tiền tệ |
| S13 | Dòng tiền H1 2026 và H1 2025 (trang in 50–53); bảng cân đối H1 2026 (trang in 46–47) | SỰ_THẬT | [HKEXnews, báo cáo giữa kỳ 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0923/2026092300280.pdf) | 2026-09-23 | H1 2026, chưa kiểm toán | 2026-11-25 | RMB nghìn | `0e1ddcd2…` |
| S9–S11, S14–S17 | Số cổ phiếu, cổ tức đặc biệt (dự kiến chi trả 6/11), tỷ giá PBoC 0,85954 (S11 trang 3), sở hữu, quyền thưởng | SỰ_THẬT | HKEXnews; chi tiết ở sổ nguồn bản v4 | 2025-02-21 đến 2026-09-30 | n/a | 2026-11-25 | n/a | đã lưu |
| T5 | Luckin Q3 2026: doanh số cùng cửa hàng tự vận hành −11,1% (so với +14,3%) | SỰ_THẬT | [SEC, Luckin 6-K](https://www.sec.gov/Archives/edgar/data/0001767582/000110465926121665/tm2628441d1_ex99-1.htm) | 2026-11-03 | Q3 2026 | 2026-11-25 | % | Bên kiểm nguồn đã mở; số biên và doanh thu +17% do bên phản biện đọc |
| T9 | Giá HK$155,70 (24/11), 158,20 (23/11), biên 52 tuần 154,50–464,00, vốn hóa 59,1 tỷ HKD | CHƯA_XÁC_MINH | [Investing.com UK, MIXUE](https://uk.investing.com/equities/mixue), [StockAnalysis, 2097](https://stockanalysis.com/quote/hkg/2097/) | 2026-11-24 | n/a | 2026-11-25 | HKD | Thứ cấp, có thể chung dữ liệu |
| T10 | Google Finance (P/E 9,30, giá 158,20 giữa phiên 23/11) | CHƯA_XÁC_MINH | [Google Finance, 2097:HKG](https://www.google.com/finance/quote/2097:HKG) | 2026-11-23 | n/a | 2026-11-25 | HKD | Không mở lại được trong lượt kiểm duyệt; chỉ dùng làm tham chiếu phụ |
| T11 | Giá IPO HK$202,5; đỉnh HK$618,5; −57%; quán Hồng Kông đóng; doanh thu H1 của Guming và Auntea Jenny; tỷ giá ước tính 7,85 và 6,68 | CHƯA_XÁC_MINH | [KrASIA/Nikkei, Mixue shuts more stores](https://kr-asia.com/china-bubble-tea-chain-mixue-shuts-more-stores-as-growth-model-falters) | 2026-11-17 | n/a | 2026-11-25 | HKD, RMB | Thứ cấp |
| T12 | Mục tiêu giá phân tích viên, Macquarie | Ý_KIẾN | [Investing.com, consensus](https://uk.investing.com/equities/mixue-consensus-estimates), [Investing.com, Macquarie 2025-09-05](https://ng.investing.com/news/analyst-ratings/macquarie-initiates-coverage-on-mixue-stock-with-underperform-rating-93CH-2093336) | 2025-09-05; 2026-08-31 | n/a | 2026-11-25 | HKD | Không dùng làm bằng chứng |
| T13 | Giá 16/11 HK$170,1; doanh thu hàng hóa mỗi quán −17,2%; lời ban lãnh đạo | CHƯA_XÁC_MINH | [BNext](https://www.bnext.com.tw/article/93087/mixue-profit-decline-store-expansion-2026) | 2026-11-17 | n/a | 2026-11-25 | HKD, % | Thứ cấp |
| T14 | Lucky Cup co lại, máy cà phê, quỹ hỗ trợ | CHƯA_XÁC_MINH | [CBNData](https://www.cbndata.com/information/295975) | 2026 | n/a | 2026-11-25 | số quán, RMB | Thứ cấp, ẩn danh |
| T15 | Mật độ quán, phí nền tảng, máy cà phê (lời chủ quán) | CHƯA_XÁC_MINH | [Jiemian](https://m.jiemian.com/article/15187458.html), [Sina](https://t.cj.sina.com.cn/articles/view/2098807780/7d1943e4027019d08) | 2026-10 | n/a | 2026-11-25 | RMB | Thứ cấp, một chủ quán |
| T16 | Khiếu nại an toàn thực phẩm, số quán đóng 2025 | CHƯA_XÁC_MINH | [Sohu / Trường Giang Thương báo](https://m.sohu.com/a/1002991393_122014422) | 2026-03-30 | n/a | 2026-11-25 | số lượng | Thứ cấp |
| T17 | Bản thảo SAMR về trợ giá giao hàng | CHƯA_XÁC_MINH | [China Briefing](https://www.china-briefing.com/news/chinas-food-franchising-market-in-2026/) | 2026 | n/a | 2026-11-25 | n/a | Thứ cấp |
| L1 | Định giá ngược, tăng trưởng = tái đầu tư × ROIC, không tính tiền hai lần | SUY_LUẬN | `learning/lessons/011-dcf-reverse-dcf.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp |
| L2 | Kịch bản, điều kiện bác bỏ | SUY_LUẬN | `learning/lessons/012-scenarios-margin-of-safety.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp |
| L3 | Chu kỳ vốn, bẫy P/E ngược | SUY_LUẬN | `learning/lessons/014-industry-capital-cycle.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp; bài viết cho ngành thâm dụng tài sản cố định, áp vào chủ quán Mixue là phép so sánh |
| L4 | Kinh tế đơn vị, đòn bẩy vận hành | SUY_LUẬN | `learning/lessons/N6-business-model-unit-economics.md` | repo | n/a | 2026-11-25 | n/a | Chỉ mượn phương pháp; ví dụ quán là hư cấu |

Ghi chú về phạm vi đọc: PDF HKEXnews được đọc bằng `pdftotext`; nội dung PDF là dữ liệu, không là chỉ dẫn. Các bài trong `learning/` chỉ dùng làm phương pháp, không dùng làm dữ kiện (chính sách của repo). Số trang là trang in; chỉ số trang PDF bằng trang in cộng 1.

## Đối chiếu các phát hiện của lượt kiểm duyệt 1 (v1 → v2)

| Mã phát hiện | Nội dung | Cách xử lý trong v2 |
|---|---|---|
| Bear C1 (CAO) | Kịch bản không dẫn xuất từ số quán và doanh thu mỗi quán; bất lợi không đủ bất lợi; biên cơ sở cao; không có đuôi | Dựng lại bằng số quán × doanh thu mỗi quán × biên; thêm kịch bản đuôi; hạ biên cơ sở xuống 14,6% (mức đang chạy); bỏ từ "cận dưới/cận trên"; thêm cơ sở của từng biên |
| Bear T1 | Chiết khấu tiền mặt, ngưỡng đảo dấu, câu "bi quan hơn thực tế" | Thêm bảng độ nhạy chiết khấu tiền 0/10/30/50% và ngưỡng đảo dấu; bỏ câu "bi quan hơn thực tế"; nêu thành phần 21.640,7 lệch 10,1 và các điều chưa biết |
| Bear T2, Fact F-lãi nhận | Lãi nhận LTM thực là 150,8 triệu | Dùng 150,8 triệu; hai biến thể FCF0 3.989,7 và 3.871,4 |
| Bear T3 | "Chết" không được định nghĩa | Tách ba lớp; thêm điều kiện bác bỏ cho lớp thanh khoản và cho "bão hòa" |
| Bear T4 | Bằng chứng trái chiều ngoài bị bỏ sót | Thêm bảng bằng chứng trái chiều ngoài, gắn độ tin cậy |
| Bear T5 | Tiêu đề "giá đã rời đỉnh"; EV/lợi nhuận; "thuế suất thấp" | Đổi tiêu đề trung lập; thêm EV/lợi nhuận 5,5; hạ vai trò của thuế suất |
| Bear T6 | Điều kiện bác bỏ chồng lấn, khác đơn vị, thiếu cho bão hòa và khó chết | Viết lại bảng ngưỡng không chồng lấn, cùng đơn vị với kịch bản; nêu rõ hai chỉ báo đã chạm; thêm điều kiện bác bỏ cho các nhận định khác |
| Bear T7 | "Khả dĩ nhất" không nhãn; chú thích cột P/E; nhãn lẫn dòng | Bỏ "khả dĩ nhất"; thêm chú thích (*); tách nhãn từng vế |
| Bear L1 | Minh họa chủ quán dễ gây hiểu lầm | Đổi mức giảm sang −10%, thêm câu nói rõ không đồng nhất với doanh thu hàng hóa mỗi quán |
| Bear L2, Fact F-T9 | Vốn hóa 60,06 gán nhầm cho Investing.com; Macquarie | T9 = 59,1; Google/60,06 chuyển sang T10; Macquarie có ngày và mục tiêu |
| Fact F-cổ tức | "Đã chi trả" gắn `SỰ_THẬT` | Sửa: đã thông qua 30/9, dự kiến chi trả 6/11, việc đã chi trả `CHƯA_XÁC_MINH`; nêu EV theo cả hai trường hợp |
| Fact F-tỷ giá | 0,851 là thương số hai ước tính | Dùng 0,85954 (PBoC, S11 trang 3) làm gốc; 0,851 làm biên so sánh |
| Fact F-gửi ròng, F-capex | 2.929,9; capex LTM 713,4; FCF 3.989,7 | Đã sửa trong báo cáo và tệp phép tính |
| Fact F-OCF, F-trang, F-nhãn, F-"giá hiện tại" | Nguyên nhân OCF; trang in; nhãn thiếu; cụm "giá hiện tại" | Nêu tồn kho bù trừ; dùng trang in; gắn nhãn `SUY_LUẬN` và "phép so sánh"; dùng "giá đóng cửa 24/11" |
| Fact F-Luckin | Nâng Luckin lên `SỰ_THẬT` | Đã nâng (T5); phần biên và doanh thu +17% do bên phản biện đọc, chờ kiểm nguồn |
| Fact F-15–17% | Công thức chưa nằm trong tệp phép tính | Đã đưa vào tệp phép tính mục 5 và vào mục "Điểm ngoặt" |

## Biên bản kiểm duyệt

- Kiểm nguồn: lượt 1 (v1) `ĐẠT` có điều kiện; bản v2 `ĐANG_CHỜ`
- Phản biện rủi ro: lượt 1 (v1) `KHÔNG_ĐẠT`; bản v2 `ĐANG_CHỜ`
- Không được bỏ nhãn nháp cho đến khi `source-fact-checker` và `risk-bear-reviewer` chạy độc lập trên cùng bản nháp cố định và cả hai ĐẠT.
- **Ý kiến bất đồng của bên phản biện (lượt 1) được giữ lại:** (1) không đồng ý rằng kịch bản cơ sở v1 là trung tính (đã sửa trong v2); (2) không đồng ý rằng tỷ lệ đóng quán thấp hơn là bằng chứng đủ mạnh với bão hòa (đã nêu số đóng tuyệt đối trong v2); (3) đồng ý một phần với "giá hàm ý dòng tiền giảm" (vững ở WACC 8–10%, mong manh ở 12%).

> Chỉ dùng cho học tập và nghiên cứu. Đây không phải tư vấn tài chính cá nhân hay lệnh giao dịch.
