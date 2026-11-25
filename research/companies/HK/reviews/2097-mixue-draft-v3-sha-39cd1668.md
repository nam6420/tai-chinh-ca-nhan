# BẢN NHÁP - CHƯA KIỂM DUYỆT: MIXUE Group, đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (2097.HK)

- Chốt dữ liệu lúc: `2026-11-25 09:05 +07` (bản v3; nguồn HKEXnews đã được mở lại và đối chiếu trong hai lượt kiểm nguồn cùng ngày, 08:21–08:27 và 08:42–08:50 +07)
- Quốc gia / thị trường / sở giao dịch: Trung Quốc đại lục (hoạt động chính), niêm yết cổ phiếu H tại Sở Giao dịch Hồng Kông (HKEX) mã `2097` từ 2025-03-03
- Chuẩn kế toán: IFRS Accounting Standards; kiểm toán Ernst & Young (Hong Kong)
- Tiền tệ / đơn vị báo cáo: RMB; số gốc tính theo RMB nghìn, bài này làm tròn sang RMB triệu hoặc tỷ
- Phạm vi: đọc báo cáo tài chính để hiểu công ty. **Chưa định giá** (chưa lấy giá cổ phiếu để tính bội số, chưa có giá trị nội tại). Đây chưa phải nghiên cứu doanh nghiệp đầy đủ.
- Dữ liệu gốc: `data/raw/mixue-financials-2026-11-25.json`; PDF gốc và mã băm tại `data/raw/mixue-hkex/`
- Phép tính: `data/processed/mixue-financial-calculations-2026-11-25.md`
- Kiểm nguồn: lượt 1 (v1) `KHÔNG_ĐẠT` (`reviews/2097-mixue-fact-check-v1.md`); lượt 2 (v2) `KHÔNG_ĐẠT` (`reviews/2097-mixue-fact-check-v2.md`); bản v3 này `ĐANG_CHỜ` kiểm lại
- Phản biện rủi ro: lượt 1 (v1) `KHÔNG_ĐẠT` (`reviews/2097-mixue-bear-review-v1.md`); lượt 2 (v2) `KHÔNG_ĐẠT` (`reviews/2097-mixue-bear-review-v2.md`); bản v3 này `ĐANG_CHỜ` kiểm lại
- Lịch sử: v1 (SHA-256 `a682acf7…`) và v2 (`ddcbc7c1…`) được lưu nguyên vẹn trong `research/companies/HK/reviews/`. Bản v3 này đã sửa các phát hiện của bốn biên bản, nhưng **chưa được hai agent kiểm duyệt đọc lại**.

> Không phải lời khuyên mua, bán hay nắm giữ. Các điều kiện, kịch bản và chỉ báo dưới đây là công cụ học tập để theo dõi dữ kiện, không phải hướng dẫn quản lý một vị thế.

## Tóm tắt bài học

1. **Mixue gần như là nhà cung ứng chuỗi cung ứng cho các chủ cửa hàng nhượng quyền, không phải chuỗi tự bán lẻ.** 93,7% doanh thu 2025 đến từ bán hàng hóa cho cửa hàng, 4,0% từ bán thiết bị, chỉ 2,4% từ phí dịch vụ nhượng quyền. `SỰ_THẬT` [S4, thuyết minh 3]. Doanh thu của công ty xấp xỉ **số cửa hàng × giá trị hàng mỗi cửa hàng mua**, không phải doanh số bán cốc nước. `SUY_LUẬN`
2. **Bốn năm FY2022–FY2025 tăng trưởng rất mạnh, nhưng năm gốc là năm đáy:** doanh thu 13,6 → 33,6 tỷ RMB (CAGR ba kỳ 35,2%); lợi nhuận năm 2,0 → 5,9 tỷ RMB (CAGR ba kỳ 43,3%, nhưng lấy gốc 2021 thì chỉ 32,7% vì 2022 là năm lợi nhuận chỉ +5,3%). `PHÉP_TÍNH`
3. **Bảng cân đối ít nợ, nhiều tiền:** vay ngân hàng 28,2 triệu RMB; tiền, tiền gửi và tài sản tài chính 19,99 tỷ RMB cuối 2025; nợ phải trả / tổng tài sản 19,6%. `SỰ_THẬT` [S4]. Phần lớn tiền nằm ở sản phẩm quản lý tài sản (8,9 tỷ) và tiền gửi có kỳ hạn, và có lỗ tỷ giá trên tiền gửi ngoại tệ (79,5 triệu RMB năm 2025; 153,8 triệu RMB trong H1 2026). `SỰ_THẬT` [S4, S7]
4. **H1 2026 là kỳ có tín hiệu xấu nhất trong dữ liệu:** doanh thu +2,3%, lợi nhuận −14,7%, biên gộp thấp hơn 1,2 điểm %, trong khi tổng số cửa hàng tăng 20,7%. `SỰ_THẬT` + `PHÉP_TÍNH` [S7]. Doanh thu hàng hóa bán cho chủ cửa hàng tính trên mỗi cửa hàng giảm khoảng 15–17% tùy cách chia mẫu số `PHÉP_TÍNH`; nguyên nhân (nền cao do trợ giá năm 2025, bão hòa, chiết khấu, đổi cơ cấu sản phẩm, hợp nhất FULU) **chưa được nguồn nào xác nhận** `CHƯA_BIẾT`.
5. **Sụt lợi nhuận H1 2026: chi phí là yếu tố lớn nhất, nhưng biên gộp cũng góp khoảng một phần ba.** Lợi nhuận trước thuế giảm 492,6 triệu RMB. Phân rã tuyệt đối: chi phí bán hàng + quản lý tăng 381,7 triệu (≈ 77,5%), lợi nhuận gộp giảm 76,7 triệu (≈ 15,6%). Phân rã theo hiệu ứng: biên gộp lùi 1,2 điểm % làm mất ≈ 184,6 triệu (≈ 37%), trong khi doanh thu tăng cộng ≈ 107,9 triệu. Cả hai cách đều đúng; cách thứ hai cho thấy biên gộp không thể coi là không quan trọng. `PHÉP_TÍNH` [S7]

## Mô hình kinh doanh (theo báo cáo)

- Ba thương hiệu: MIXUE (trà, nước ép, kem; giá lõi RMB 2–8), Lucky Cup (cà phê; RMB 2–11 cuối 2025), FULU Fresh Beer (bia tươi; mua lại, hoàn tất 2025-12-01). Giá điển hình khoảng 1 USD (≈ RMB 6) mỗi món. `SỰ_THẬT` [S4]
- Mô hình chủ yếu là nhượng quyền: chủ cửa hàng sở hữu và chịu kết quả cửa hàng, mua nguyên liệu và thiết bị từ Mixue. Công ty tự sản xuất 100% nguyên liệu lõi: cuối 2025 có 5 cơ sở sản xuất và 28 kho; đến 30/6/2026 là 6 cơ sở và 31 kho. `SỰ_THẬT` [S4, S7]
- Khách hàng thường **trả trước** khi nhận hàng và thiết bị. `SỰ_THẬT` [S4, thuyết minh 3]. Nợ hợp đồng chỉ 485,1 triệu RMB cuối 2025 (≈ 1,4% doanh thu, ≈ 5,3 ngày doanh thu) `PHÉP_TÍNH`, nên đòn bẩy vốn lưu động từ trả trước **không lớn**; phải trả người bán (2.212,5 triệu RMB) mới là khoản lớn hơn. `SỰ_THẬT` [S4]
- Không có khách hàng nào chiếm từ 10% doanh thu trong FY2024–FY2025 [S4, thuyết minh 2], FY2023 [S2], H1 2025–H1 2026 [S7]; khách hàng lớn nhất dưới 1% doanh thu 2025 [S5]. FY2022: `CHƯA_BIẾT`.
- Doanh thu theo địa lý: đến FY2023 cáo bạch tách; doanh thu ngoài đại lục là 50,1 triệu RMB (2021, 0,5%), 540,6 triệu (2022, 4,0%), 1.486,9 triệu (2023, 7,3%), và 9 tháng đầu 2024 là 952,4 triệu so với 1.171,3 triệu cùng kỳ 2023 (giảm). `SỰ_THẬT` [S1]. Từ FY2024, báo cáo chỉ nói "phần lớn từ đại lục", không tách số. `SỰ_THẬT` [S4, thuyết minh 2]

## Bối cảnh ngành, vĩ mô và so sánh toàn cầu

Phần này lấy từ các báo cáo gốc của đối thủ và nguồn thứ cấp **do bên phản biện mở**; tôi chưa tự mở lại các nguồn ghi "bên phản biện". Nguồn thứ cấp chỉ dùng cho bối cảnh, một số bài có lỗi số, nên không làm bằng chứng cho số liệu chính. Nhãn: `Ý_KIẾN` / `CHƯA_XÁC_MINH` trừ khi ghi khác.

- **Trợ giá giao hàng.** Công ty tự mô tả 2025 là năm nền tảng giao hàng tăng trợ giá đồ uống pha chế, đẩy đơn sang kênh trực tuyến `SỰ_THẬT` (lời công ty, [S4]). Theo báo cáo gốc do bên phản biện mở: Meituan có lãi ở Q2 2026 nhưng **cả H1 2026 vẫn lỗ hoạt động** (≈ −3.778,6 triệu RMB), nên Q1 2026 lỗ nặng và trợ giá chỉ hạ nhiệt **từ Q2 2026**, không phải "từ đầu 2026"; Guming nói doanh số mỗi cửa hàng "broadly stable", bị bù trừ một phần bởi việc các nền tảng giao hàng giảm trợ giá; Luckin (6-K ngày 2026-11-03) nói doanh số cùng cửa hàng Q3 2026 −11,1%, chủ yếu do nền so sánh cao vì trợ giá năm trước. Hệ quả logic: **việc trợ giá giảm chính là cơ chế của giả thuyết "nền cao"**, không phải bằng chứng ngược với nó. Và vì Luckin nêu Q3 2025 là kỳ trợ giá cao, trong khi doanh thu H2 2025 của Mixue tăng +32,0%, nền so sánh của H2 2026 có thể **khó hơn** nền H1.
- **So sánh ngang hàng bằng số gốc (bên phản biện mở; điều phối viên chưa tự mở).** Guming H1 2026: doanh thu +31,9% so với số cửa hàng +28,4% (doanh thu/cửa hàng ≈ +2,7%), biên gộp 33,4% so với 31,5%, chi phí bán hàng 5,05% so với 5,51% doanh thu, chi phí quản lý 2,79% so với 3,27%; lợi nhuận kỳ −3,6% chỉ vì H1 2025 có khoản lãi giá trị hợp lý 556,9 triệu RMB; mở mới 1.318 so với 1.570. Auntea Jenny: 13.155 cửa hàng so với 9.436 (+39,4%). Nguồn thứ cấp: Chagee doanh số cùng cửa hàng −16,1% ở Q2 2026 (Inside Retail), Nayuki doanh thu −13,1% (Caixin) `CHƯA_XÁC_MINH`. **Cách đọc có thể nhất quán với dữ liệu** (`SUY_LUẬN`): sụt doanh số mỗi cửa hàng là hiện tượng mang tính ngành (nền trợ giá), còn điều **riêng của Mixue** nằm ở **biên và cấu trúc chi phí** (biên gộp −1,2 điểm %, chi phí bán hàng + quản lý +2,4 điểm % doanh thu, trong khi Guming cải thiện cả hai). Chú ý: doanh thu hàng hóa của Mixue là doanh thu bán buôn cho chủ cửa hàng, còn GMV của Guming là doanh số bán lẻ, nên hai thước đo không cùng loại. Giả thuyết "đặc thù Mixue" về doanh thu mỗi cửa hàng và giả thuyết "nền trợ giá chung" đều chưa được chứng minh, giữ cả hai mở.
- **Thị trường (nguồn thứ cấp, không phải khuyến nghị).** Cổ phiếu giảm khoảng 57% từ đầu 2026 đến 2026-11-09 (Nikkei qua KrASIA, 2026-11-17); trang tổng hợp Investing.com (trễ, có thể sai) ghi đóng cửa HK$ 176,60 ngày 9/11 và HK$ 155,70 ngày 24/11 (≈ −11,8%, thấp hơn giá IPO HK$ 202,5 khoảng 23%). Bên phản biện không tìm thấy công bố trọng yếu nào của công ty trong giai đoạn đó, nên nguyên nhân `CHƯA_BIẾT`. Giá thị trường phản ánh kỳ vọng, không phải bằng chứng về hoạt động kinh doanh.
- **Quy định nhượng quyền.** Tòa án nhân dân tối cao công bố 7 án điển hình về nhượng quyền ngày 2026-08-12 (Tân Hoa Xã): hướng dẫn tư pháp, không phải quy tắc mới riêng cho trà sữa. Dự thảo thông báo giám sát nhượng quyền của Bộ Thương mại cùng các cơ quan là của **tháng 6/2023**, không phải 2026. Bên phản biện không tìm thấy xử phạt hay thu hồi nào năm 2026 đối với Mixue. `CHƯA_XÁC_MINH`
- **Tin giai thoại sau H1 2026** (chủ nhượng quyền kể nhiều quán Mixue gần nhau, giá nguyên liệu tăng, Lucky Cup có thể giảm cửa hàng ròng) chỉ có trong báo chí thứ cấp, phần lớn không nêu nguồn; **không dùng**.

## Lịch sử và chất lượng tài chính

### Kết quả kinh doanh (RMB triệu)

| | 2021 (cơ sở) | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|
| Doanh thu | 10.351,0 | 13.575,6 | 20.302,5 | 24.828,9 | 33.559,9 | 14.874,8 | 15.215,8 |
| Tăng trưởng doanh thu | n/a | 31,2% | 49,6% | 22,3% | 35,2% | +39,3% | +2,3% |
| Lợi nhuận gộp | 3.243,9 | 3.846,8 | 5.999,0 | 8.060,2 | 10.451,8 | 4.706,4 | 4.629,7 |
| Biên gộp | 31,3% | 28,3% | 29,5% | 32,5% | 31,1% | 31,6% | 30,4% |
| Lợi nhuận năm | 1.911,9 | 2.013,1 | 3.186,6 | 4.454,2 | 5.927,1 | 2.718,2 | 2.319,3 |
| Biên ròng | 18,5% | 14,8% | 15,7% | 17,9% | 17,7% | 18,3% | 15,2% |
| EPS cơ bản (RMB) | 5,32 | 5,55 | 8,71 | 12,32 | 15,65 | 7,23 | 6,05 |

Nguồn: [S1] cho 2021–2023, [S4]/[S5] cho 2024–2025, [S7] cho H1. `SỰ_THẬT` (số) / `PHÉP_TÍNH` (tỷ lệ). 2021–2025 là số kiểm toán; H1 chưa kiểm toán.

Đọc bảng này:

- **2022 là năm trũng về biên:** biên gộp hàng hóa giảm từ 31,4% (2021) xuống 27,8% (2022), chủ yếu do (i) giá mua một số nguyên liệu biến động và (ii) công ty giảm giá trung bình 15% cho 69 mặt hàng vật tư và thiết bị bán cho chủ cửa hàng để giảm tác động của COVID-19; nhóm hàng này chiếm 23,1% doanh thu 2022. `SỰ_THẬT` [S1]. Quyết định đầu 2022 miễn một năm phí nhượng quyền cho các chủ cửa hàng hiện hữu chỉ làm giảm một phần mức tăng của doanh thu dịch vụ nhượng quyền (vẫn tăng 40,6%, nhanh hơn doanh thu chung +31,2%); biên gộp dịch vụ nhượng quyền thậm chí tăng từ 71,5% lên 78,2%. `SỰ_THẬT` [S1]. Chi phí bán hàng cũng tăng từ 3,9% lên 5,7% doanh thu. `PHÉP_TÍNH`
- **2023–2024 là giai đoạn mở rộng biên:** biên gộp 29,5% → 32,5%, lợi nhuận +58,3% rồi +39,8%. Đà lợi nhuận chậm dần từ trước H1 2026: so với cùng kỳ năm trước, lợi nhuận H1 2025 +44,1%, H2 2025 +25,0%, H1 2026 −14,7% `PHÉP_TÍNH` [S4, S6, S7]. Biên gộp H2 2025 ≈ 30,7% (từ doanh thu và lợi nhuận gộp cả năm trừ H1), nên phần lớn mức giảm so với H1 2025 (31,6%) đã xảy ra từ H2 2025; so với kỳ liền trước, H1 2026 chỉ thêm −0,3 điểm %. `PHÉP_TÍNH`
- **2025: doanh thu +35,2% nhưng biên gộp lùi về 31,1%.** Công ty giải thích biên gộp hàng hóa và thiết bị giảm từ 31,2% xuống 29,9% do thay đổi cơ cấu doanh thu và giá một số nguyên liệu tăng; biên gộp dịch vụ nhượng quyền tăng từ 80,4% lên 82,6%. `SỰ_THẬT` [S4]
- **Thuế suất hiệu dụng giảm dần** 25,3% → 24,3% → 23,3% → 23,3% → 21,5% (2021–2025). `PHÉP_TÍNH`. Nếu 2025 giữ thuế suất 2024 (23,3%), lợi nhuận 2025 sẽ ≈ 5.788 triệu RMB thay vì 5.927 triệu (chênh ≈ 139 triệu, 2,4%) và tăng trưởng ≈ +29,9% thay vì +33,1%. `PHÉP_TÍNH`. Công ty nêu một số công ty con hưởng thuế 15% (ưu đãi miền Tây, Cảng thương mại tự do Hải Nam) và miễn thuế sơ chế nông sản [S7, thuyết minh thuế]; thời hạn và độ ổn định của các ưu đãi này `CHƯA_BIẾT`.
- Chi phí quản lý chỉ 3,0–3,7% doanh thu suốt 2021–2025; chi phí bán hàng ổn định quanh 6% từ 2023. Vì vậy **trong 2023–2025** biên ròng chủ yếu bị biên gộp chi phối `SUY_LUẬN`. **Điều này không còn đúng ở H1 2026** (xem cầu nối bên dưới).

### Cơ cấu doanh thu

| RMB triệu | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|
| Bán hàng hóa | 12.551,0 | 19.160,2 | 23.452,5 | 31.439,5 | 13.843,2 | 14.264,9 |
| Bán thiết bị | 748,4 | 736,5 | 756,4 | 1.326,6 | 651,5 | 532,7 |
| Dịch vụ nhượng quyền | 276,1 | 405,7 | 620,0 | 793,9 | 380,1 | 418,2 |
| Phí NQ / doanh thu | 2,0% | 2,0% | 2,5% | 2,4% | 2,6% | 2,7% |

Nguồn: [S1], [S4], [S7]. `SỰ_THẬT`. Bán thiết bị gần như đi ngang 2022–2024 (≈ 0,74–0,76 tỷ) rồi tăng 75,4% (+570,2 triệu) năm 2025. Công ty đồng thời triển khai máy rót đồ uống thông minh (trên 13.000 cửa hàng MIXUE cuối 2025, trên 18.000 tại 30/6/2026) [S4, S7]. **Nguồn không xác nhận mối liên hệ** giữa hai việc này; hơn nữa doanh thu thiết bị H1 2026 giảm 18,2% trong khi số cửa hàng có máy rót vẫn tăng, nên giả thuyết "máy rót kéo doanh thu thiết bị" bị yếu đi. `SUY_LUẬN`

### Bảng cân đối và dòng tiền (RMB triệu)

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Tổng tài sản | 7.316,4 | 9.945,4 | 14.593,6 | 19.783,3 | 30.793,6 |
| Tổng vốn chủ sở hữu | 5.542,7 | 7.479,3 | 10.595,5 | 15.060,8 | 24.768,8 |
| Tiền, tiền gửi có kỳ hạn và tiền bị hạn chế (*) | 2.737,7 | 2.829,3 | 6.037,5 | 7.617,9 | 11.054,9 |
| Tài sản tài chính ghi nhận qua lãi lỗ (FVTPL) | 900,2 | 1.865,7 | 746,0 | 3.491,6 | 8.935,1 |
| Hàng tồn kho | 1.251,9 | 1.541,2 | 2.231,7 | 2.215,4 | 3.673,0 |
| Dòng tiền thuần từ HĐKD (OCF) | 1.692,4 | 2.430,6 | 3.793,9 | 6.008,7 | 6.039,0 |
| Mua tài sản cố định hữu hình (capex PPE) | 944,5 | 997,3 | 1.685,3 | 1.438,6 | 685,1 |
| FCF đơn giản (OCF − capex PPE) | 747,9 | 1.433,3 | 2.108,6 | 4.570,1 | 5.353,9 |
| OCF / lợi nhuận năm | 0,89 | 1,21 | 1,19 | 1,35 | 1,02 |

(*) Cuối 2025: tiền và tương đương tiền 7.429,1 triệu; tiền gửi có kỳ hạn và tiền bị hạn chế 3.625,8 triệu. `SỰ_THẬT` [S4]. Nguồn: [S5] (tóm tắt, OCF 2024–2025), [S1] (OCF 2021–2023, capex; capex PPE 944,523; 997,293; 1.685,292 triệu), [S4]. `SỰ_THẬT` / `PHÉP_TÍNH`. Capex trên chỉ gồm tài sản cố định hữu hình; năm 2022 công ty còn trả 253,9 triệu RMB cho quyền sử dụng đất (tổng capex 2022 gồm cả hạng mục này ≈ 1.260,0 triệu). `SỰ_THẬT` [S1]

- **OCF vượt lợi nhuận bốn năm liên tiếp (2022–2025)**, nhưng 2025 chỉ còn 1,02 lần: hàng tồn kho tăng 65,8% (so với giá vốn +37,8%) làm dòng tiền hao 1,55 tỷ RMB, và OCF 2025 gần như đi ngang (6.039,0 so với 6.008,7) dù lợi nhuận tăng 33,1%. `PHÉP_TÍNH` [S5]
- **Tồn kho đo theo ba cách cho kết quả khác nhau:** (a) số cuối kỳ tăng 65,8% so với giá vốn cả năm +37,8%; (b) ngày tồn kho bình quân đầu–cuối năm giảm từ 48,4 (2024) xuống 46,5 (2025); (c) ngày tồn kho theo số cuối kỳ tăng từ 48,2 lên 58,0. `PHÉP_TÍNH`. Tồn kho tiếp tục tăng sang 3.828,2 triệu RMB tại 30/6/2026 (+4,2% so với cuối 2025) trong khi doanh thu H1 gần như đi ngang. `SỰ_THẬT` [S7]. Nguyên nhân (mua trước Tết 2026, giá nguyên liệu, dự trữ khi nâng chất lượng, hay hàng bán chậm) `CHƯA_BIẾT`; trích lập giảm giá hàng tồn kho 2025 là 97,2 triệu (so với 37,0 triệu 2024) `SỰ_THẬT` [S5]; H1 2026 là 21,0 triệu so với 32,5 triệu cùng kỳ 2025 (giảm, bằng chứng trái chiều với lo ngại hàng tồn). `SỰ_THẬT` [S7, thuyết minh 5]
- Thu từ phát hành cổ phiếu 2025 là 3.665,1 triệu RMB. Thu nhập lãi và sản phẩm quản lý tài sản 2025 là 330,0 triệu RMB, khoảng 4,4% lợi nhuận trước thuế. `PHÉP_TÍNH`
- Capex PPE giảm mạnh từ 1,44 tỷ (2024) xuống 0,69 tỷ (2025); cam kết vốn còn 301,8 triệu và công ty nói sẽ tiếp tục đầu tư năng lực sản xuất (cơ sở Vân Nam bắt đầu hoạt động 5/2026). `SỰ_THẬT` [S4, S7]
- ROE bình quân (lợi nhuận công ty mẹ / vốn chủ sở hữu gồm cổ đông thiểu số bình quân) giảm từ 34,6% (2024) xuống 29,6% (2025) do vốn chủ sở hữu tăng vọt sau IPO; nếu chỉ chia cho vốn công ty mẹ, 2025 là ≈ 29,9%. `PHÉP_TÍNH`

### Mạng lưới cửa hàng

| | 2021 | 2022 | 2023 | 2024 | 2025 | 30/6/2025 | 30/6/2026 |
|---|---|---|---|---|---|---|---|
| Tổng số cửa hàng | 20.001 | 28.983 | 37.565 | 46.479 | 59.823 | 53.014 | 63.987 |
| Trung Quốc đại lục | 19.731 (*) | 27.188 (*) | 33.234 | 41.584 | 55.356 | 48.281 | 59.609 |
| Ngoài đại lục | 270 | 1.795 | 4.331 | 4.895 | 4.467 | 4.733 | 4.378 |
| Cửa hàng NQ mở mới (kỳ) | n/a | n/a | 9.894 | 10.555 | 14.496 | 7.721 | 5.455 |
| Cửa hàng NQ đóng (kỳ) | n/a | n/a | 1.307 | 1.609 | 2.527 | 1.187 | 1.289 |
| Tỷ lệ đóng / số cửa hàng NQ đầu kỳ | n/a | n/a | 4,5% | 4,3% | 5,4% | 2,6% | 2,2% |
| Chủ nhượng quyền (cuối kỳ) | n/a | n/a | 16.784 | 20.976 | 27.450 | 23.404 | 29.775 |

(*) Số đại lục 2021–2022 là số suy ra (tổng trừ ngoài đại lục); tổng 20.001 / 28.983 và ngoài đại lục 270 / 1.795 lấy từ [S1, trang 333], bên kiểm nguồn đã đối chiếu. Nguồn: [S1], [S2], [S4], [S6], [S7]. `SỰ_THẬT`. Điểm cần đọc:

(a) Tỷ lệ đóng cửa hàng năm 2025 tăng (4,3% → 5,4%; con số 2025 chưa tách riêng cửa hàng FULU mua lại), **nhưng trong H1 2026 tỷ lệ đóng thấp hơn H1 2025** (2,2% so với 2,6%) và chủ nhượng quyền tăng 27,2% so với cùng kỳ; điều thật sự giảm là **số cửa hàng mở mới** (−29,3%). `PHÉP_TÍNH`
(b) Hơn 58% cửa hàng đại lục ở thành phố hạng ba trở xuống. `SỰ_THẬT` [S4]
(c) Mạng lưới nước ngoài **thu hẹp** từ 4.895 (2024) xuống 4.467 (2025, −8,7%) rồi 4.378 (30/6/2026, −2,0% so với cuối 2025): đà thu hẹp chậm lại nhưng chưa đảo chiều (Indonesia và Việt Nam giảm), trái với câu chuyện "ra toàn cầu" `PHÉP_TÍNH`; đồng thời công ty nói đã vào Kazakhstan, Mỹ, Mexico, Kyrgyzstan, Brazil. `SỰ_THẬT` [S4, S7]
(d) Số cửa hàng tự vận hành tăng từ 17 lên 38 (cuối 2025), chủ yếu do mua FULU. `SỰ_THẬT` [S4]

### H1 2026: cầu nối lợi nhuận và độ chắc chắn của suy luận

| | H1 2025 | H1 2026 | Thay đổi |
|---|---|---|---|
| Doanh thu | 14.874,8 | 15.215,8 | +2,3% |
| Bán hàng hóa | 13.843,2 | 14.264,9 | +3,0% |
| Bán thiết bị | 651,5 | 532,7 | −18,2% |
| Lợi nhuận gộp | 4.706,4 | 4.629,7 | −76,7 triệu (−1,6%) |
| Chi phí bán hàng | 913,7 | 1.122,9 | +209,3 triệu (+22,9%); 6,1% → 7,4% doanh thu |
| Chi phí quản lý | 437,7 | 610,0 | +172,4 triệu (+39,4%); 2,9% → 4,0% doanh thu |
| Lỗ chênh lệch tỷ giá (thuyết minh 5; nằm trong "thu nhập và lãi khác, ròng") | 42,2 | 153,8 | +111,6 triệu; mức 153,8 triệu ≈ 5,2% lợi nhuận trước thuế H1 2026. Thu nhập khác ròng cả khoản giảm chỉ 31,1 triệu (158,6 → 127,5) vì được bù một phần bởi trợ cấp chính phủ và lãi giá trị hợp lý |
| Lợi nhuận trước thuế | 3.468,3 | 2.975,7 | −492,6 triệu (−14,2%) |
| Thuế suất hiệu dụng | 21,6% | 22,1% | tăng nhẹ, không giải thích mức giảm |
| Lợi nhuận kỳ | 2.718,2 | 2.319,3 | −14,7% |
| Tồn kho (cuối kỳ so với cuối 2025) | n/a | 3.828,2 | +4,2% so với 3.673,0 |
| Nhân viên (cuối kỳ so với cuối 2025) | n/a | 10.374 | +14,0% so với 9.102 |
| Chủ nhượng quyền | 23.404 | 29.775 | +27,2% |

Nguồn: [S7]; tỷ lệ và hiệu là `PHÉP_TÍNH`. **Về chi phí:** công ty nói chi phí quản lý tăng chủ yếu do nhân sự, nhưng lương và tiền công trong thuyết minh chi phí chỉ tăng từ 760,7 lên 851,7 triệu (+91,0 triệu) `SỰ_THẬT` [S7, thuyết minh 5]; bên phản biện tính tổng chi phí nhân sự kể cả cổ phiếu thưởng tăng ≈ 102 triệu (chưa tự kiểm). Nhân sự vì vậy chỉ giải thích khoảng một phần tư mức tăng 381,7 triệu của chi phí bán hàng + quản lý; phần còn lại (marketing, IP, hỗ trợ vận hành, có thể cả thay đổi phân loại chi phí giữa các dòng) `CHƯA_BIẾT`. Mức tuyệt đối của chi phí bán hàng H1 2026 (1.122,9) gần bằng H2 2025 (≈ 1.123,2) và chi phí quản lý (610,0) thấp hơn H2 2025 (≈ 643,8) `PHÉP_TÍNH`: chi phí đã bước lên từ H2 2025 rồi đi ngang, chứ chưa chắc còn leo; mức +23%/+39% là so với nền H1 2025 thấp, và tính mùa vụ chưa kiểm. Gọi chúng là "chi phí tăng, thành phần chưa rõ", không phải "chi phí cố định".

**Lời giải thích của công ty:** giá vốn tăng nhanh hơn doanh thu do đầu tư nâng chất lượng sản phẩm theo hướng nguyên liệu thật; chi phí bán hàng tăng do marketing và nhân sự phục vụ phát triển IP và hỗ trợ vận hành cửa hàng; chi phí quản lý tăng do nhân sự. `SỰ_THẬT` [S7].

**Về suy luận "giá trị hàng mỗi cửa hàng giảm":** doanh thu hàng hóa +3,0% so với số cửa hàng +23,5% (đại lục cuối kỳ), +20,7% (tổng cuối kỳ), +24,4% (cửa hàng nhượng quyền bình quân đầu–cuối kỳ) cho doanh thu hàng hóa trên mỗi cửa hàng giảm khoảng 16,5%, 14,6% và 17,2% tương ứng. `PHÉP_TÍNH`. Đây là **giá trị** (lượng × giá × cơ cấu), không phải "lượng hàng"; công ty đã đổi cơ cấu/chất lượng sản phẩm. Phép chia còn bị nhiễu bởi: 1.354 cửa hàng FULU mua tháng 12/2025 (có trong mẫu số H1 2026 nhưng không có ở H1 2025); doanh thu bán cho cửa hàng nước ngoài; cửa hàng mới mở chưa trưởng thành; công ty không công bố doanh số cùng cửa hàng. Các ước tính ngoài (môi giới, một số bài phân tích) đều chia từ cùng số tổng hợp nên **không phải bằng chứng cấp cửa hàng**. Hướng suy luận (đang giảm đáng kể) nhất quán giữa các cách chia, nhưng mức độ có thể còn lệch vì thời điểm nhập hàng của chủ cửa hàng (mua trước hay dùng sau) chưa được nêu trong báo cáo. `SUY_LUẬN`

## Ban lãnh đạo, quản trị và phân bổ vốn

- **Lãnh đạo.** Zhang Hongfu (đồng sáng lập) chuyển từ Tổng giám đốc sang đồng chủ tịch; Zhang Yuan (35 tuổi, vào tập đoàn tháng 2/2023 làm giám đốc tài chính) làm Tổng giám đốc; cả hai có hiệu lực 2026-03-24, tức **trong** H1 2026 (sau khi FY2025 kết thúc). `SỰ_THẬT` [S5]. Không có bằng chứng về quan hệ nhân quả giữa việc đổi lãnh đạo và kết quả H1; người thay giám đốc tài chính `CHƯA_BIẾT`.
- **Cổ đông.** Báo cáo ghi **từng** nhà sáng lập, Zhang Hongchao (chủ tịch) và Zhang Hongfu (đồng chủ tịch), là chủ sở hữu hưởng lợi của 100.098.196 cổ phiếu chưa niêm yết (26,37% vốn) và 53.899.028 cổ phiếu H (14,20%), tức ≈ 40,57% vốn cổ phần **mỗi người**, cộng 971.993 cổ phiếu chưa niêm yết và 647.994 cổ phiếu H (≈ 0,43%) qua nền tảng sở hữu của nhân viên do từng người kiểm soát. `SỰ_THẬT` [S5, phần quyền lợi cổ phần]. Báo cáo không nêu số tổng chung của hai người. Nếu đây là hai lô riêng biệt thì tổng ≈ 81–82% vốn (`PHÉP_TÍNH` dưới giả định này; khả thi về số học vì 2 × 100,1 triệu ≤ 228,7 triệu cổ phiếu chưa niêm yết); nếu là một lô khai chung thì ≈ 40,57%. Tổng chung và thỏa thuận hành động phối hợp: `CHƯA_BIẾT`, cần mở mục "Substantial Shareholders" của cáo bạch.
- **Giao dịch bên liên quan: mua FULU.** FULU (Fulujia) trước khi mua do bà Tian Haixia, vợ của ông Zhang Hongfu (một cổ đông kiểm soát), nắm khoảng 60,05%. Công ty mua 51% bằng 285,6 triệu RMB tiền mặt, hoàn tất 2025-12-01, và giao dịch được công bố là giao dịch liên kết. `SỰ_THẬT` [S5, báo cáo HĐQT và thuyết minh 40–41]. Lợi thế thương mại ghi nhận 91,9 triệu RMB. Giá có công bằng hay không cần ý kiến độc lập và báo cáo thẩm định: `CHƯA_BIẾT`.
- **Quản trị.** Chủ tịch ủy ban kiểm toán, ông Huang Sidney Xuande (giám đốc độc lập), có tiểu sử trong S5 nêu quan hệ công việc hiện tại với JD.com và việc từng là giám đốc tài chính của JD.com đến 9/2020 (theo bên kiểm nguồn đọc từ S5). Không có bằng chứng sai phạm; đây chỉ là điểm cần xem phần đánh giá tính độc lập và giao dịch bên liên quan của báo cáo thường niên (chưa đọc). `CHƯA_BIẾT`
- **Nhân sự.** Nhân viên 7.025 → 9.102 (cuối 2025) → 10.374 (30/6/2026); chi phí nhân sự 2025 là 2,07 tỷ RMB (từ 1,45 tỷ). `SỰ_THẬT` [S4, S7]. Nguồn thứ cấp nhắc kế hoạch cổ phiếu thưởng cho nhân viên (H Share Award Scheme); chưa mở: `CHƯA_BIẾT`.
- **Phân bổ vốn.** Tiền IPO ròng ≈ HK$ 3,8 tỷ, đã dùng ≈ HK$ 1,35 tỷ (≈ 35,5%) đến cuối 2025 [S5, theo bên kiểm nguồn]. Góp vốn 109,0 triệu RMB vào công ty liên kết (đối tượng chưa rõ, thuyết minh chỉ ghi gộp). Không đề xuất cổ tức thường niên FY2025 [S4].
- **Cổ tức đặc biệt H1 2026.** Hội đồng quản trị đề xuất ngày 2026-08-27 cổ tức đặc biệt RMB 2,65 mỗi cổ phiếu, ≈ 1.006,0 triệu RMB (379.618.800 × 2,65 `PHÉP_TÍNH`; ≈ 43% lợi nhuận H1 2026 và ≈ 27% khoản thu từ phát hành cổ phiếu 2025), dự kiến trả khoảng 2026-11-06 [S7 trang 16, thuyết minh 7; thông báo HKEXnews 2026-08-27; thông báo họp cổ đông bất thường 2026-09-11, cả hai đã lưu]. Theo bản sao thông báo HKEX trên Eastmoney (chưa phải HKEXnews gốc), nghị quyết được thông qua ngày 2026-09-30 với 99,999446% phiếu thuận; chỉ **hai cổ đông hoặc người đại diện** hiện diện, nắm 90,30% quyền biểu quyết. `CHƯA_XÁC_MINH`. Việc đã trả chưa xác minh. Cách đọc có hai chiều: (a) sức khỏe tài chính tốt và công ty ưu tiên hoàn vốn; (b) ít cơ hội tái đầu tư trong bối cảnh tăng trưởng chậm, và một phần đáng kể chảy tới nhóm cổ đông kiểm soát (số tiền cụ thể `CHƯA_BIẾT` cho đến khi rõ cơ cấu sở hữu). Cả hai chiều chưa được chứng minh.

## Các kịch bản (kịch bản vận hành, chưa định giá)

Chưa có giá trị nội tại hay khoảng giá, nên "Khoảng giá trị" là `CHƯA_BIẾT`. Các kịch bản là khung theo dõi, **không** gắn xác suất. Các ngưỡng dưới đây là `Ý_KIẾN` làm tròn từ mức hiện tại để có điểm so sánh, không phải điểm gãy đã được chứng minh; cách suy ra: mở mới 5.000 ≈ 8,4% số cửa hàng nhượng quyền đầu kỳ (H1 2026: 9,1%; H1 2025: 16,6%); chi phí bán hàng + quản lý 11% ≈ mức H1 2026 (11,4%; H1 2025: 9,1%); biên gộp 30% ≈ số tròn gần H1 2026 (30,4%), và năm 2022–2023 biên 28,3–29,5% vẫn đi cùng lợi nhuận tăng nên 30% không tự nó là điểm gãy.

| Kịch bản | Giả định chính (đo được) | Chỉ báo kiểm tra, mốc | Điều gì phải đúng |
|---|---|---|---|
| Bất lợi | Doanh thu hàng hóa/cửa hàng tiếp tục giảm ở H2 2026; mở mới dưới 5.000 cửa hàng/nửa năm; chi phí bán hàng + quản lý ≥ 12% doanh thu | Kết quả H2 2026 (FY2026, khoảng tháng 3/2027; lịch `CHƯA_BIẾT`); số chủ nhượng quyền tăng chậm hơn số cửa hàng | Nền trợ giá khó hơn ở H2 2026 và/hoặc vấn đề biên-chi phí đặc thù Mixue kéo dài |
| Cơ sở | Doanh thu hàng hóa/cửa hàng ổn định quanh mức H1 2026; mở mới 5.000–7.000; chi phí bán hàng + quản lý 10–12% doanh thu; biên gộp 30–31% | Doanh thu H2 2026 so với H2 2025 (nền +32,0%) không xấu hơn H1 (+2,3%); tồn kho/giá vốn ngừng tăng; OCF/lợi nhuận ≥ 1 | Nền so sánh H2 không khó hơn đáng kể. **Lưu ý:** Luckin nêu Q3 2025 là kỳ trợ giá cao, nên giả định này có thể lạc quan |
| Thuận lợi | Doanh thu/cửa hàng phục hồi về mức 2025; chi phí bán hàng + quản lý dưới 10%; biên gộp ≥ 31% | Doanh thu/cửa hàng, tỷ lệ chi phí, mở mới phục hồi | Chi phí IP và nhân sự hiện tại là đầu tư có hoàn vốn |

`KỊCH_BẢN`: giả định có điều kiện, không phải dự báo, không phải khuyến nghị.

## Rủi ro và bằng chứng trái chiều

**Rủi ro (xếp theo độ trọng yếu của người viết, `Ý_KIẾN`):**

1. **Tăng trưởng đã mất đà:** H1 2026 doanh thu +2,3%, lợi nhuận −14,7% sau FY2025 +35,2% và +33,1%; đà lợi nhuận đã chậm từ H2 2025. `SỰ_THẬT` + `PHÉP_TÍNH` [S4, S6, S7]
2. **Chi phí tăng nhanh hơn doanh thu, thành phần chưa rõ:** chi phí bán hàng +22,9%, quản lý +39,4% so với cùng kỳ, nhân viên +14,0% trong sáu tháng; nhân sự chỉ giải thích một phần. `SỰ_THẬT` [S7]
3. **Phụ thuộc sức khỏe chủ cửa hàng nhượng quyền.** Doanh thu của Mixue là doanh thu bán cho chủ cửa hàng. Phí dịch vụ nhượng quyền cố định (không có phần biến đổi) và chỉ 2,7% doanh thu H1 2026 `SỰ_THẬT` [S7]; do đó nó phản ánh số cửa hàng chứ không phản ánh sức khỏe chủ cửa hàng `SUY_LUẬN`. Dữ liệu doanh số bán lẻ độc lập `CHƯA_BIẾT`.
4. **Tồn kho tăng nhanh:** nguyên nhân `CHƯA_BIẾT` (xem phần Tồn kho).
5. **Biên gộp:** biên gộp hàng hóa và thiết bị giảm 1,3 điểm % năm 2025 [S4]; biên toàn công ty thấp hơn 1,2 điểm % so với H1 2025 (nhưng chỉ −0,3 điểm % so với H2 2025) do công ty chủ động nâng chất lượng nguyên liệu [S7]. `SỰ_THẬT` + `PHÉP_TÍNH`
6. **Mạng lưới nước ngoài thu hẹp nhưng chậm lại:** 4.895 → 4.467 → 4.378. `SỰ_THẬT`
7. **Tỷ giá trên tiền gửi ngoại tệ:** lỗ 79,5 triệu RMB (2025) và 153,8 triệu (H1 2026), nhưng ròng trong "thu nhập khác" chỉ giảm 31,1 triệu. `SỰ_THẬT` [S4, S7]
8. **Quản trị: giao dịch bên liên quan và tập trung sở hữu.** Mua FULU từ người nhà cổ đông kiểm soát; hai nhà sáng lập nắm tỷ lệ lớn vốn cổ phần; chỉ hai cổ đông hiện diện ở đại hội cổ đông bất thường (bản sao). `SỰ_THẬT` [S5] / `CHƯA_XÁC_MINH`
9. **An toàn thực phẩm và uy tín qua hành vi chủ cửa hàng** (rủi ro cấu trúc của mô hình nhượng quyền). Nguồn thứ cấp: vụ chanh cũ ở Hồ Bắc tháng 3/2025, 8.727 khiếu nại trên Black Cat đến 2/2025 (≈ 70% liên quan an toàn thực phẩm), 16 cửa hàng nhượng quyền bị Hội người tiêu dùng Bắc Kinh nêu năm 2024 (The Standard, 2025-03-17). Bên phản biện không tìm thấy xử phạt riêng đối với Mixue năm 2026. `CHƯA_XÁC_MINH`
10. **Ưu đãi thuế** có thể không kéo dài (xem phần thuế suất).

**Bằng chứng trái chiều với lập luận bất lợi** (khiến kết luận "tăng trưởng đang gãy" kém chắc):

- Tỷ lệ đóng cửa hàng H1 2026 thấp hơn H1 2025 (2,2% so với 2,6%), chủ nhượng quyền +27,2%. `PHÉP_TÍNH`
- Sụt doanh số mỗi cửa hàng có vẻ là hiện tượng ngành (Luckin −11,1% cùng cửa hàng; Guming doanh thu/cửa hàng chỉ ≈ +2,7% dù mở rộng nhanh), nên không chắc là lỗi riêng của Mixue. `CHƯA_XÁC_MINH`
- Trích lập giảm giá hàng tồn kho H1 2026 giảm (21,0 so với 32,5 triệu). `SỰ_THẬT` [S7]
- Điểm chuyển ở doanh thu xảy ra đột ngột: +39,3% (H1 2025) → +32,0% (H2 2025) → +2,3% (H1 2026); H2 2026 chưa có dữ liệu. `PHÉP_TÍNH`
- Tỷ lệ đóng cửa hàng của Mixue (≈ 2,2% mỗi nửa năm) thấp hơn Guming (3,84%) và Auntea Jenny (≈ 4,9%) theo số của bên phản biện. `CHƯA_XÁC_MINH`

**Bằng chứng ủng hộ lập luận bất lợi:** (a) biên gộp và tỷ lệ chi phí của Mixue xấu đi trong khi Guming cải thiện cả hai (số gốc do bên phản biện mở); (b) các ước tính ngoài về doanh thu hàng hóa/cửa hàng giảm 15–17% (không độc lập về dữ liệu vì đều chia từ số tổng của công ty); (c) nền H2 2025 có thể khó hơn.

**Thanh khoản (không phản bác luận điểm tăng trưởng, chỉ giảm rủi ro tài chính):** tiền, tiền gửi, tiền hạn chế và sản phẩm quản lý tài sản đạt 21.640,7 triệu RMB ở 30/6/2026 (+8,3% so với 19.990,0 triệu cuối 2025, "chủ yếu nhờ dòng tiền thuần từ hoạt động kinh doanh" theo công ty), vay ngân hàng bằng 0, tỷ lệ nợ/tài sản 17,7% `SỰ_THẬT` [S7]; mức tăng 1.650,7 triệu ≈ 71% lợi nhuận H1 (chỉ báo thô, đã gồm lỗ tỷ giá, biến động sản phẩm quản lý tài sản và chưa trừ cổ tức 1.006 triệu). `PHÉP_TÍNH`

## Điều kiện làm luận điểm mất hiệu lực

Luận điểm cần kiểm tra: "Mixue tiếp tục tăng trưởng nhờ mở rộng mạng lưới và lợi thế chuỗi cung ứng". Các chỉ báo dưới đây là `Ý_KIẾN` của người viết, làm tròn từ mức hiện tại; không phải ngưỡng do công ty công bố và không phải khuyến nghị. Nên theo dõi theo **xu hướng nhiều kỳ** hơn là một ngưỡng cứng:

1. Doanh thu hàng hóa / cửa hàng nhượng quyền bình quân giảm ở hai nửa năm liên tiếp (H1 2026 đã giảm; H2 2026 chưa biết, và nền H2 2025 cao).
2. Số cửa hàng nhượng quyền mở mới mỗi nửa năm dưới ≈ 8% số đầu kỳ (≈ 5.000) trong khi số chủ nhượng quyền ngừng tăng.
3. Chi phí bán hàng + quản lý trên doanh thu ≈ 11% hoặc cao hơn không giảm lại sau hai kỳ liên tiếp. **Chỉ báo này đã thỏa ở H1 2026 (11,4%)**, nên điều cần theo dõi là xu hướng, không phải mức.
4. Biên gộp tiếp tục giảm so với kỳ liền trước (H2 2025 ≈ 30,7%; H1 2026 30,4%) mà chi phí không giảm.
5. Tồn kho / giá vốn (theo số cuối kỳ) tăng tiếp, hoặc trích lập giảm giá hàng tồn kho tăng mạnh trở lại, hoặc OCF/lợi nhuận dưới 1 khi có báo cáo lưu chuyển tiền tệ (H1 2026: tiền tăng 8,3% là dấu hiệu ngược chiều, nhưng chưa phải báo cáo dòng tiền).
6. Bằng chứng mới về an toàn thực phẩm, quy định nhượng quyền hoặc giao dịch bên liên quan làm tăng số cửa hàng đóng hoặc làm giảm niềm tin vào quản trị.

## Điều chưa biết và lần kiểm tra tiếp theo

- **Vì sao giá trị hàng mỗi cửa hàng giảm trong H1 2026?** Nền cao do trợ giá, đổi cơ cấu sản phẩm, bão hòa, chiết khấu, FULU, hay mẫu số? Cần doanh số cùng cửa hàng chính thức (công ty không công bố), thuyết minh hợp nhất FULU, họp báo, dữ liệu độc lập. Giữ cả hai giả thuyết (nền trợ giá chung; biên-chi phí đặc thù Mixue).
- Báo cáo lưu chuyển tiền tệ H1 2026: thông báo kết quả không có; chỉ có số dư tiền và tài sản tài chính. Chờ báo cáo giữa kỳ đầy đủ.
- Thành phần chi phí bán hàng + quản lý tăng thêm 381,7 triệu (ngoài nhân sự) và có thay đổi phân loại hay không.
- Cơ cấu sở hữu tổng của hai nhà sáng lập; thỏa thuận hành động phối hợp; giá mua FULU có công bằng không; giao dịch bên liên quan khác; đối tượng góp vốn 109,0 triệu RMB.
- Cổ tức đặc biệt đã trả chưa; bản HKEXnews gốc của kết quả biểu quyết 2026-09-30.
- Giá cổ phiếu hiện tại và bội số; so sánh với đối thủ bằng báo cáo gốc của từng công ty (Chagee, Nayuki chưa mở được nguồn gốc).
- Doanh thu theo thương hiệu và theo địa lý từ FY2024: báo cáo không tách `CHƯA_BIẾT`.
- Chưa đọc toàn văn S3 và S5 (254 trang), chưa đọc chương rủi ro và Business của cáo bạch.

## Sổ nguồn

| Mã | Nhận định / đầu vào | Nhãn | Nguồn | Ngày xuất bản | Kỳ báo cáo | Ngày truy cập | Đơn vị / tiền tệ | Phiên bản / ghi chú |
|---|---|---|---|---|---|---|---|---|
| S1 | Lãi lỗ 2021–2023, cơ cấu doanh thu 2022–2023, giải thích biên gộp 2022, doanh thu ngoài đại lục, capex, số cửa hàng 2021–2022, tồn kho/phải trả, dòng tiền 2021–2023 | SỰ_THẬT | [HKEXnews, cáo bạch, chương Financial Information](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0221/11543478/2025022100039.pdf) | 2025-02-21 | FY2021–FY2023, 9T2024 | 2026-11-25 | RMB nghìn, IFRS, đã kiểm toán | 53 trang, SHA-256 `aa34ed51…` |
| S2 | Số cửa hàng 2023–2024; chủ nhượng quyền 2023–2024 | SỰ_THẬT | [HKEXnews, kết quả FY2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0326/2025032601256.pdf) | 2025-03-26 | FY2024 | 2026-11-25 | số lượng | 26 trang, `a938dc2f…` |
| S3 | Tóm tắt tài chính 2021–2024 (đối chiếu) | SỰ_THẬT | [HKEXnews, báo cáo thường niên 2024](https://www.hkexnews.hk/listedco/listconews/sehk/2025/0423/2025042301969.pdf) | 2025-04-23 | FY2024 | 2026-11-25 | RMB nghìn | 238 trang, `1596169b…` |
| S4 | Lãi lỗ, cân đối, doanh thu, chuyển động cửa hàng, MD&A FY2025 | SỰ_THẬT | [HKEXnews, kết quả FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0324/2026032400179.pdf) | 2026-03-24 | FY2025 | 2026-11-25 | RMB nghìn | 28 trang, `1bd2d9a1…`; EY chỉ đối chiếu số, không bảo đảm |
| S5 | Tóm tắt 2021–2025, dòng tiền 2024–2025, lãnh đạo, cổ phần, lợi thế thương mại | SỰ_THẬT | [HKEXnews, báo cáo thường niên 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf) | 2026-04-23 | FY2025 | 2026-11-25 | RMB nghìn | 254 trang, `55f7ed40…`; mới đọc một phần |
| S6 | H1 2025 (đối chiếu) | SỰ_THẬT | [HKEXnews, kết quả H1 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0827/2025082700283.pdf) | 2025-08-27 | H1 2025 | 2026-11-25 | RMB nghìn, chưa kiểm toán | 25 trang, `b37764ea…` |
| S7 | H1 2026, cửa hàng, giải thích chi phí, tồn kho, nhân viên, chủ nhượng quyền, cổ tức đặc biệt, tỷ giá | SỰ_THẬT | [HKEXnews, kết quả H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700177.pdf) | 2026-08-27 | H1 2026 | 2026-11-25 | RMB nghìn, chưa kiểm toán | 26 trang, `c2f83a7d…` |
| S8 | Giải thích chênh lệch số liệu giữa các bài báo (5,89 tỷ so với 5,93 tỷ RMB; 27,0% so với 33,1%) | PHÉP_TÍNH | 5.886.704 là lợi nhuận quy cho cổ đông công ty mẹ; 5.927.077 là lợi nhuận cả năm; 27,0% là tăng EPS, 33,1% là tăng lợi nhuận, đều trong S4. Báo chí chỉ dùng thước đo khác nhau | 2026-03-24 | FY2025 | 2026-11-25 | RMB | Đối chiếu nội bộ S4 |
| S9 | Số cổ phiếu 379.618.800 (228.735.742 chưa niêm yết + 150.883.058 H) | SỰ_THẬT | [HKEXnews, kết quả bỏ phiếu ĐHĐCĐ](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0626/2026062602855.pdf) | 2026-06-26 | tại 2026-06-26 | 2026-11-25 | số cổ phiếu | 3 trang, `5fc40111…`; đã lưu |
| S10 | Cổ tức đặc biệt RMB 2,65/cổ phiếu, trả dự kiến 2026-11-06 | SỰ_THẬT (đề xuất) | [HKEXnews, thông báo cổ tức](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700183.pdf) | 2026-08-27 | FYE 2026-12-31 | 2026-11-25 | RMB | 2 trang, `82814b83…`; đã lưu |
| S11 | ĐHĐCĐ bất thường thông qua cổ tức đặc biệt (2026-09-30) | CHƯA_XÁC_MINH | [Bản sao thông báo HKEX trên Eastmoney](https://pdf.dfcfw.com/pdf/H2_AN202609301830055247_1.pdf); thông báo họp: [HKEXnews 2026-09-11](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0911/2026091101193.pdf) (`ab600329…`, đã lưu) | 2026-09-30 | n/a | 2026-11-25 | n/a | Bản sao không phải HKEXnews gốc; bản gốc kết quả biểu quyết chưa tìm thấy |
| T1–T8 | Bối cảnh ngành (trợ giá, đối thủ, thị trường, an toàn thực phẩm, quy định) | Ý_KIẾN / CHƯA_XÁC_MINH | Báo cáo gốc do bên phản biện mở (điều phối viên chưa tự mở): Guming HKEXnews 2026-08-26, Meituan HKEXnews 2026-08-28, Auntea Jenny HKEXnews 2026-08-28, Luckin SEC 6-K 2026-11-03. Nguồn thứ cấp: [Caixin 2026-01-10](https://www.caixinglobal.com/2026-01-10/beijing-tightens-scrutiny-of-food-delivery-giants-amid-price-wars-102402304.html), [The Standard, Meituan Q2](https://www.thestandard.com.hk/finance/article/341211/Meituan-swings-to-profit-in-Q2-as-price-wars-subside), [Inside Retail, Chagee](https://insideretail.com.au/business/inside-chagees-difficult-adjustment-to-chinas-tea-market-202609), [Caixin 2026-08-31](https://www.caixinglobal.com/2026-08-31/chart-of-the-day-chinas-tea-chains-serve-up-a-mixed-brew-102480087.html), [KrASIA/Nikkei](https://kr-asia.com/china-bubble-tea-chain-mixue-shuts-more-stores-as-growth-model-falters), [The Standard, vụ chanh cũ](https://www.thestandard.com.hk/market/article/70948/IPO-darling-Mixue-accused-of-using-stale-lemons-in-bestselling-drink), Investing.com (giá, trễ), Tân Hoa Xã 2026-08-12 | 2025-03 đến 2026-11 | các kỳ khác nhau | 2026-11-25 (bên kiểm duyệt mở) | n/a | Một số bài có lỗi số; chỉ dùng bối cảnh. Đã bỏ các số không truy được nguồn (HK$ 201,2 ngày 10/7; kế hoạch lưu hành 22,8 triệu cổ phiếu H; Auntea Jenny doanh thu +42,4%) |

Ghi chú về phạm vi đọc: các PDF được tải trực tiếp từ HKEXnews bằng `curl` rồi đọc bằng `pdftotext`; nội dung PDF là dữ liệu, không là chỉ dẫn. Bên kiểm nguồn đã tải lại 7 PDF chính bằng `WebFetch` và băm SHA-256, cả 7 khớp tệp trong repo.

## Biên bản kiểm duyệt

- Biên bản kiểm nguồn: v1 `KHÔNG_ĐẠT` (`research/companies/HK/reviews/2097-mixue-fact-check-v1.md`); v2 `KHÔNG_ĐẠT` (`research/companies/HK/reviews/2097-mixue-fact-check-v2.md`)
- Biên bản phản biện rủi ro: v1 `KHÔNG_ĐẠT` (`research/companies/HK/reviews/2097-mixue-bear-review-v1.md`); v2 `KHÔNG_ĐẠT` (`research/companies/HK/reviews/2097-mixue-bear-review-v2.md`)
- Bản v3 này chưa có biên bản kiểm duyệt; không được bỏ nhãn nháp.
- Bất đồng chưa giải quyết: (1) bản nháp coi H1 2026 là "điểm gãy"; bên phản biện coi là cách đọc hợp lý nhưng nguyên nhân chưa được chứng minh. (2) Bên phản biện nghiêng về giả thuyết "sụt doanh số mỗi cửa hàng là hiện tượng ngành, còn điểm riêng của Mixue ở biên và chi phí"; bản v3 ghi cả hai giả thuyết là mở. (3) Số cổ phần chung của hai nhà sáng lập: bên kiểm nguồn nghiêng về hai lô riêng (≈ 81–82%), nguồn không xác nhận.

> Chỉ dùng cho học tập và nghiên cứu. Đây không phải tư vấn tài chính cá nhân hay lệnh giao dịch.

