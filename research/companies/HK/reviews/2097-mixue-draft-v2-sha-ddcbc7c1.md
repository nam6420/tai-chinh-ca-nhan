# BẢN NHÁP - CHƯA KIỂM DUYỆT: MIXUE Group, đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (2097.HK)

- Chốt dữ liệu lúc: `2026-11-25 08:35 +07` (bản v2; nguồn HKEXnews đã được mở lại và đối chiếu trong lượt kiểm nguồn 08:21–08:27 +07 cùng ngày)
- Quốc gia / thị trường / sở giao dịch: Trung Quốc đại lục (hoạt động chính), niêm yết cổ phiếu H tại Sở Giao dịch Hồng Kông (HKEX) mã `2097` từ 2025-03-03
- Chuẩn kế toán: IFRS Accounting Standards; kiểm toán Ernst & Young (Hong Kong)
- Tiền tệ / đơn vị báo cáo: RMB; số gốc tính theo RMB nghìn, bài này làm tròn sang RMB triệu hoặc tỷ
- Phạm vi: đọc báo cáo tài chính để hiểu công ty. **Chưa định giá** (chưa lấy giá cổ phiếu để tính bội số, chưa có giá trị nội tại). Đây chưa phải nghiên cứu doanh nghiệp đầy đủ.
- Dữ liệu gốc: `data/raw/mixue-financials-2026-11-25.json`; PDF gốc và mã băm tại `data/raw/mixue-hkex/`
- Phép tính: `data/processed/mixue-financial-calculations-2026-11-25.md`
- Kiểm nguồn: lượt 1 (bản v1) `KHÔNG_ĐẠT`, biên bản `research/companies/HK/reviews/2097-mixue-fact-check-v1.md`; bản v2 này `ĐANG_CHỜ` kiểm lại
- Phản biện rủi ro: lượt 1 (bản v1) `KHÔNG_ĐẠT`, biên bản `research/companies/HK/reviews/2097-mixue-bear-review-v1.md`; bản v2 này `ĐANG_CHỜ` kiểm lại
- Lịch sử: v1 (SHA-256 `a682acf7…`) được lưu nguyên vẹn tại `research/companies/HK/reviews/2097-mixue-draft-v1-sha-a682acf7.md`. Bản v2 này đã sửa các phát hiện của hai biên bản, nhưng **chưa được hai agent kiểm duyệt đọc lại**.

> Không phải lời khuyên mua, bán hay nắm giữ. Các điều kiện, kịch bản và chỉ báo dưới đây là công cụ học tập để theo dõi dữ kiện, không phải hướng dẫn quản lý một vị thế.

## Tóm tắt bài học

1. **Mixue gần như là nhà cung ứng chuỗi cung ứng cho các chủ cửa hàng nhượng quyền, không phải chuỗi tự bán lẻ.** 93,7% doanh thu 2025 đến từ bán hàng hóa cho cửa hàng, 4,0% từ bán thiết bị, chỉ 2,4% từ phí dịch vụ nhượng quyền. `SỰ_THẬT` [S4, thuyết minh 3]. Doanh thu của công ty xấp xỉ **số cửa hàng × giá trị hàng mỗi cửa hàng mua**, không phải doanh số bán cốc nước. `SUY_LUẬN`
2. **Bốn năm FY2022–FY2025 tăng trưởng rất mạnh, nhưng năm gốc là năm đáy:** doanh thu 13,6 → 33,6 tỷ RMB (CAGR ba kỳ 35,2%); lợi nhuận năm 2,0 → 5,9 tỷ RMB (CAGR ba kỳ 43,3%, nhưng lấy gốc 2021 thì chỉ 32,7% vì 2022 là năm lợi nhuận chỉ +5,3%). `PHÉP_TÍNH`
3. **Bảng cân đối ít nợ, nhiều tiền:** vay ngân hàng 28,2 triệu RMB; tiền, tiền gửi và tài sản tài chính 19,99 tỷ RMB cuối 2025; nợ phải trả / tổng tài sản 19,6%. `SỰ_THẬT` [S4]. Phần lớn tiền nằm ở sản phẩm quản lý tài sản (8,9 tỷ) và tiền gửi có kỳ hạn, và có lỗ tỷ giá trên tiền gửi ngoại tệ (79,5 triệu RMB năm 2025; 153,8 triệu RMB trong H1 2026). `SỰ_THẬT` [S4, S7]
4. **H1 2026 là kỳ có tín hiệu xấu nhất trong dữ liệu:** doanh thu +2,3%, lợi nhuận −14,7%, biên gộp thấp hơn 1,2 điểm %, trong khi tổng số cửa hàng tăng 20,7%. `SỰ_THẬT` + `PHÉP_TÍNH` [S7]. Doanh thu hàng hóa bán cho chủ cửa hàng tính trên mỗi cửa hàng giảm khoảng 15–17% tùy cách chia mẫu số `PHÉP_TÍNH`; nguyên nhân (nền cao do trợ giá năm 2025, bão hòa, chiết khấu, đổi cơ cấu sản phẩm, hợp nhất FULU) **chưa được nguồn nào xác nhận** `CHƯA_BIẾT`.
5. **Sụt lợi nhuận H1 2026 chủ yếu đến từ chi phí, không phải từ biên gộp:** lợi nhuận trước thuế giảm 492,6 triệu RMB, trong đó chi phí bán hàng + quản lý tăng thêm 381,7 triệu RMB (≈ 77,5%), lợi nhuận gộp giảm 76,7 triệu (≈ 15,6%). `PHÉP_TÍNH` [S7]

## Mô hình kinh doanh (theo báo cáo)

- Ba thương hiệu: MIXUE (trà, nước ép, kem; giá lõi RMB 2–8), Lucky Cup (cà phê; RMB 2–11 cuối 2025), FULU Fresh Beer (bia tươi; mua lại, hoàn tất 2025-12-01). Giá điển hình khoảng 1 USD (≈ RMB 6) mỗi món. `SỰ_THẬT` [S4]
- Mô hình chủ yếu là nhượng quyền: chủ cửa hàng sở hữu và chịu kết quả cửa hàng, mua nguyên liệu và thiết bị từ Mixue. Công ty tự sản xuất 100% nguyên liệu lõi: cuối 2025 có 5 cơ sở sản xuất và 28 kho; đến 30/6/2026 là 6 cơ sở và 31 kho. `SỰ_THẬT` [S4, S7]
- Khách hàng thường **trả trước** khi nhận hàng và thiết bị. `SỰ_THẬT` [S4, thuyết minh 3]. Nợ hợp đồng chỉ 485,1 triệu RMB cuối 2025 (≈ 1,4% doanh thu, ≈ 5,3 ngày doanh thu) `PHÉP_TÍNH`, nên đòn bẩy vốn lưu động từ trả trước **không lớn**; phải trả người bán (2.212,5 triệu RMB) mới là khoản lớn hơn. `SỰ_THẬT` [S4]
- Không có khách hàng nào chiếm từ 10% doanh thu trong FY2024–FY2025 [S4, thuyết minh 2], FY2023 [S2], H1 2025–H1 2026 [S7]; khách hàng lớn nhất dưới 1% doanh thu 2025 [S5]. FY2022: `CHƯA_BIẾT`.
- Doanh thu theo địa lý: đến FY2023 cáo bạch tách; doanh thu ngoài đại lục là 50,1 triệu RMB (2021, 0,5%), 540,6 triệu (2022, 4,0%), 1.486,9 triệu (2023, 7,3%), và 9 tháng đầu 2024 là 952,4 triệu so với 1.171,3 triệu cùng kỳ 2023 (giảm). `SỰ_THẬT` [S1]. Từ FY2024, báo cáo chỉ nói "phần lớn từ đại lục", không tách số. `SỰ_THẬT` [S4, thuyết minh 2]

## Bối cảnh ngành, vĩ mô và so sánh toàn cầu

Phần này **chủ yếu dựa vào nguồn thứ cấp** do bên phản biện mở trong lượt kiểm duyệt (người viết chưa tự mở lại); chỉ dùng cho bối cảnh, một số bài có lỗi số, nên không dùng làm bằng chứng cho kết luận số liệu. `Ý_KIẾN` / `CHƯA_XÁC_MINH`

- **Trợ giá giao hàng:** công ty tự mô tả năm 2025 là năm nền tảng giao hàng tăng trợ giá đồ uống pha chế, đẩy đơn sang kênh trực tuyến và nâng kỳ vọng "đáng tiền" của khách `SỰ_THẬT` (lời công ty, [S4]). Nguồn thứ cấp cho biết trợ giá hạ nhiệt từ đầu 2026: cơ quan chống độc quyền vào cuộc ngành giao hàng (Caixin, 2026-01-10); Meituan có lãi trở lại ở Q2 2026 (The Standard, 2026-08-28). Nếu đúng, trợ giá đang giảm là **bằng chứng ngược** với việc coi trợ giá kéo dài là nguyên nhân duy nhất của H1 2026.
- **Đối thủ không đồng hướng** (nguồn thứ cấp): Guming và Auntea Jenny vẫn tăng doanh thu mạnh; Chagee doanh số cùng cửa hàng giảm hai chữ số nhiều quý (−16,1% ở Q2 2026, Inside Retail 2026-09-01); Nayuki giảm. Nên vấn đề của Mixue có thể mang tính đặc thù (bão hòa ở thành phố hạng ba trở xuống, chi phí nâng chất lượng, nước ngoài), chưa chứng minh được.
- **Thị trường:** theo nguồn thứ cấp, cổ phiếu chạm dưới giá IPO (HK$ 201,2 so với HK$ 202,5) ngày 2026-07-10 và giảm khoảng 57% từ đầu 2026 đến 2026-11-09 (Nikkei qua KrASIA, 2026-11-17); số này chưa được xác minh với nguồn gốc. Đây chỉ là bối cảnh để người học hiểu vì sao công ty đang được chú ý, không phải tín hiệu mua hay bán.
- **Lưu hành cổ phiếu H:** nguồn thứ cấp nêu kế hoạch chuyển 22,8 triệu cổ phiếu chưa niêm yết (≈ 6,01%) thành cổ phiếu H nộp CSRC ngày 2026-04-30; tiến độ `CHƯA_BIẾT`.

## Lịch sử và chất lượng tài chính

### Kết quả kinh doanh (RMB triệu)

| | 2021 (cơ sở) | 2022 | 2023 | 2024 | 2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|
| Doanh thu | 10.351,0 | 13.575,6 | 20.302,5 | 24.828,9 | 33.559,9 | 14.874,8 | 15.215,8 |
| Tăng trưởng doanh thu | n/a | 31,2% | 49,6% | 22,3% | 35,2% | n/a | +2,3% |
| Lợi nhuận gộp | 3.243,9 | 3.846,8 | 5.999,0 | 8.060,2 | 10.451,8 | 4.706,4 | 4.629,7 |
| Biên gộp | 31,3% | 28,3% | 29,5% | 32,5% | 31,1% | 31,6% | 30,4% |
| Lợi nhuận năm | 1.911,9 | 2.013,1 | 3.186,6 | 4.454,2 | 5.927,1 | 2.718,2 | 2.319,3 |
| Biên ròng | 18,5% | 14,8% | 15,7% | 17,9% | 17,7% | 18,3% | 15,2% |
| EPS cơ bản (RMB) | 5,32 | 5,55 | 8,71 | 12,32 | 15,65 | 7,23 | 6,05 |

Nguồn: [S1] cho 2021–2023, [S4]/[S5] cho 2024–2025, [S7] cho H1. `SỰ_THẬT` (số) / `PHÉP_TÍNH` (tỷ lệ). 2021–2025 là số kiểm toán; H1 chưa kiểm toán.

Đọc bảng này:

- **2022 là năm trũng về biên:** biên gộp hàng hóa giảm từ 31,4% (2021) xuống 27,8% (2022), chủ yếu do (i) giá mua một số nguyên liệu biến động và (ii) công ty giảm giá trung bình 15% cho 69 mặt hàng vật tư và thiết bị bán cho chủ cửa hàng để giảm tác động của COVID-19; nhóm hàng này chiếm 23,1% doanh thu 2022. `SỰ_THẬT` [S1]. Quyết định đầu 2022 miễn một năm phí nhượng quyền cho các chủ cửa hàng hiện hữu chỉ làm giảm một phần mức tăng của doanh thu dịch vụ nhượng quyền (vẫn tăng 40,6%, nhanh hơn doanh thu chung +31,2%); biên gộp dịch vụ nhượng quyền thậm chí tăng từ 71,5% lên 78,2%. `SỰ_THẬT` [S1]. Chi phí bán hàng cũng tăng từ 3,9% lên 5,7% doanh thu. `PHÉP_TÍNH`
- **2023–2024 là giai đoạn mở rộng biên:** biên gộp 29,5% → 32,5%, lợi nhuận +58,3% rồi +39,8%.
- **2025: doanh thu +35,2% nhưng biên gộp lùi về 31,1%.** Công ty giải thích biên gộp hàng hóa và thiết bị giảm từ 31,2% xuống 29,9% do thay đổi cơ cấu doanh thu và giá một số nguyên liệu tăng; biên gộp dịch vụ nhượng quyền tăng từ 80,4% lên 82,6%. `SỰ_THẬT` [S4]
- **Thuế suất hiệu dụng giảm dần** 25,3% → 24,3% → 23,3% → 23,3% → 21,5% (2021–2025). `PHÉP_TÍNH`. Nếu 2025 giữ thuế suất 2024 (23,3%), lợi nhuận 2025 sẽ ≈ 5.788 triệu RMB thay vì 5.927 triệu (chênh ≈ 139 triệu, 2,3%) và tăng trưởng ≈ +29,9% thay vì +33,1%. `PHÉP_TÍNH`. Công ty nêu một số công ty con hưởng thuế 15% (ưu đãi miền Tây, Cảng thương mại tự do Hải Nam) và miễn thuế sơ chế nông sản [S7, thuyết minh thuế]; thời hạn và độ ổn định của các ưu đãi này `CHƯA_BIẾT`.
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
- **Tồn kho đo theo ba cách cho kết quả khác nhau:** (a) số cuối kỳ tăng 65,8% so với giá vốn cả năm +37,8%; (b) ngày tồn kho bình quân đầu–cuối năm giảm từ 48,4 (2024) xuống 46,5 (2025); (c) ngày tồn kho theo số cuối kỳ tăng từ 48,2 lên 58,0. `PHÉP_TÍNH`. Tồn kho tiếp tục tăng sang 3.828,2 triệu RMB tại 30/6/2026 (+4,2% so với cuối 2025) trong khi doanh thu H1 gần như đi ngang. `SỰ_THẬT` [S7]. Nguyên nhân (mua trước Tết 2026, giá nguyên liệu, dự trữ khi nâng chất lượng, hay hàng bán chậm) `CHƯA_BIẾT`; trích lập giảm giá hàng tồn kho 2025 là 97,2 triệu (so với 37,0 triệu 2024). `SỰ_THẬT` [S5]
- Thu từ phát hành cổ phiếu 2025 là 3.665,1 triệu RMB. Thu nhập lãi và sản phẩm quản lý tài sản 2025 là 330,0 triệu RMB, khoảng 4,4% lợi nhuận trước thuế. `PHÉP_TÍNH`
- Capex PPE giảm mạnh từ 1,44 tỷ (2024) xuống 0,69 tỷ (2025); cam kết vốn còn 301,8 triệu và công ty nói sẽ tiếp tục đầu tư năng lực sản xuất (cơ sở Vân Nam bắt đầu hoạt động 5/2026). `SỰ_THẬT` [S4, S7]
- ROE bình quân (lợi nhuận công ty mẹ / vốn chủ sở hữu gồm cổ đông thiểu số bình quân) giảm từ 34,6% (2024) xuống 29,6% (2025) do vốn chủ sở hữu tăng vọt sau IPO; nếu chỉ chia cho vốn công ty mẹ, 2025 là ≈ 29,9%. `PHÉP_TÍNH`

### Mạng lưới cửa hàng

| | 2021 | 2022 | 2023 | 2024 | 2025 | 30/6/2025 | 30/6/2026 |
|---|---|---|---|---|---|---|---|
| Tổng số cửa hàng | 20.001 | 28.983 | 37.565 | 46.479 | 59.823 | 53.014 | 63.987 |
| Trung Quốc đại lục | n/a | n/a | 33.234 | 41.584 | 55.356 | 48.281 | 59.609 |
| Ngoài đại lục | n/a | 1.795 (**) | 4.331 | 4.895 | 4.467 | 4.733 | 4.378 |
| Cửa hàng NQ mở mới (kỳ) | n/a | n/a | 9.894 | 10.555 | 14.496 | 7.721 | 5.455 |
| Cửa hàng NQ đóng (kỳ) | n/a | n/a | 1.307 | 1.609 | 2.527 | 1.187 | 1.289 |
| Tỷ lệ đóng / số cửa hàng NQ đầu kỳ | n/a | n/a | 4,5% | 4,3% | 5,4% | 2,6% | 2,2% |
| Chủ nhượng quyền (cuối kỳ) | n/a | n/a | 16.784 | 20.976 | 27.450 | 23.404 | 29.775 |

(**) Số cửa hàng ngoài đại lục cuối 2022 và 2021 lấy theo thông tin do bên kiểm nguồn trích từ [S1]; cần đối chiếu lại trước khi dùng. Nguồn: [S1], [S2], [S4], [S6], [S7]. `SỰ_THẬT`. Điểm cần đọc:

(a) Tỷ lệ đóng cửa hàng năm 2025 tăng (4,3% → 5,4%; con số 2025 chưa tách riêng cửa hàng FULU mua lại), **nhưng trong H1 2026 tỷ lệ đóng thấp hơn H1 2025** (2,2% so với 2,6%) và chủ nhượng quyền tăng 27,2% so với cùng kỳ; điều thật sự giảm là **số cửa hàng mở mới** (−29,3%). `PHÉP_TÍNH`
(b) Hơn 58% cửa hàng đại lục ở thành phố hạng ba trở xuống. `SỰ_THẬT` [S4]
(c) Mạng lưới nước ngoài **thu hẹp** từ 4.895 xuống 4.378 (Indonesia và Việt Nam giảm), trái với câu chuyện "ra toàn cầu"; đồng thời công ty nói đã vào Kazakhstan, Mỹ, Mexico, Kyrgyzstan, Brazil. `SỰ_THẬT` [S4, S7]
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
| Lỗ chênh lệch tỷ giá (thuyết minh 5) | 42,2 | 153,8 | +111,6 triệu (≈ 5,2% lợi nhuận trước thuế H1 2026) |
| Lợi nhuận trước thuế | 3.468,3 | 2.975,7 | −492,6 triệu (−14,2%) |
| Thuế suất hiệu dụng | 21,6% | 22,1% | tăng nhẹ, không giải thích mức giảm |
| Lợi nhuận kỳ | 2.718,2 | 2.319,3 | −14,7% |
| Tồn kho (cuối kỳ so với cuối 2025) | n/a | 3.828,2 | +4,2% so với 3.673,0 |
| Nhân viên (cuối kỳ so với cuối 2025) | n/a | 10.374 | +14,0% so với 9.102 |
| Chủ nhượng quyền | 23.404 | 29.775 | +27,2% |

Nguồn: [S7]; tỷ lệ và hiệu là `PHÉP_TÍNH`. Công ty giải thích: giá vốn tăng nhanh hơn doanh thu do đầu tư nâng chất lượng sản phẩm theo hướng nguyên liệu thật; chi phí bán hàng tăng do marketing và nhân sự phục vụ phát triển IP và hỗ trợ vận hành cửa hàng; chi phí quản lý tăng do nhân sự. `SỰ_THẬT` [S7].

**Về suy luận "giá trị hàng mỗi cửa hàng giảm":** doanh thu hàng hóa +3,0% so với số cửa hàng +23,5% (đại lục cuối kỳ), +20,7% (tổng cuối kỳ), +24,4% (cửa hàng nhượng quyền bình quân đầu–cuối kỳ) cho doanh thu hàng hóa trên mỗi cửa hàng giảm khoảng 16,5%, 14,6% và 17,2% tương ứng. `PHÉP_TÍNH`. Đây là **giá trị** (lượng × giá × cơ cấu), không phải "lượng hàng"; công ty đã đổi cơ cấu/chất lượng sản phẩm. Phép chia còn bị nhiễu bởi: 1.354 cửa hàng FULU mua tháng 12/2025 (có trong mẫu số H1 2026 nhưng không có ở H1 2025); doanh thu bán cho cửa hàng nước ngoài; cửa hàng mới mở chưa trưởng thành; công ty không công bố doanh số cùng cửa hàng. Các ước tính ngoài (môi giới, một số bài phân tích) đều chia từ cùng số tổng hợp nên **không phải bằng chứng cấp cửa hàng**. Tuy vậy hướng suy luận (đang giảm đáng kể) vững. `SUY_LUẬN`

## Ban lãnh đạo, quản trị và phân bổ vốn

- **Lãnh đạo:** Zhang Hongfu (đồng sáng lập) chuyển từ Tổng giám đốc sang đồng chủ tịch; Zhang Yuan (35 tuổi, vào tập đoàn tháng 2/2023 làm giám đốc tài chính) làm Tổng giám đốc, cả hai có hiệu lực 2026-03-24. `SỰ_THẬT` [S5]. Việc đổi Tổng giám đốc diễn ra ngay trước kỳ lợi nhuận đầu tiên giảm `PHÉP_TÍNH` (thứ tự thời gian); người thay giám đốc tài chính `CHƯA_BIẾT`.
- **Cổ đông:** hai nhà sáng lập Zhang Hongchao (chủ tịch) và Zhang Hongfu cùng khai quyền lợi trên cùng 100.098.196 cổ phiếu chưa niêm yết (26,37% vốn) và 53.899.028 cổ phiếu H (14,20%), tức khoảng 40,57% vốn cổ phần; cùng một lượng cổ phiếu được khai hai lần cho thấy sở hữu chung hoặc hành động phối hợp (văn bản thỏa thuận chưa đọc: `CHƯA_BIẾT` về mức độ pháp lý). `SỰ_THẬT` [S5, phần quyền lợi cổ phần]
- **Quản trị:** tiểu sử chủ tịch ủy ban kiểm toán trong S5 có nhắc JD.com (đối thủ trong giao hàng và là kênh bán đồ uống). Không có bằng chứng sai phạm; đây chỉ là câu hỏi độc lập cần xem phần đánh giá độc lập và giao dịch bên liên quan của báo cáo thường niên (chưa đọc). `CHƯA_BIẾT`
- **Nhân sự:** nhân viên 7.025 → 9.102 (cuối 2025) → 10.374 (30/6/2026); chi phí nhân sự 2025 là 2,07 tỷ RMB (từ 1,45 tỷ). `SỰ_THẬT` [S4, S7]
- **Phân bổ vốn:** mua FULU Fresh Beer (hoàn tất 2025-12-01), ghi nhận lợi thế thương mại 91,9 triệu RMB phân bổ cho đơn vị tạo tiền Fulujia [S5, thuyết minh 17] và góp vốn 109,0 triệu RMB vào công ty liên kết [S5, dòng tiền; đối tượng chưa rõ]. Tiền IPO ròng ≈ HK$ 3,8 tỷ, đã dùng ≈ HK$ 1,35 tỷ (≈ 35,5%) đến cuối 2025 theo S5 (do bên kiểm nguồn đọc).
- **Cổ tức:** không đề xuất cổ tức thường niên FY2025 [S4]. **Cổ tức đặc biệt H1 2026:** hội đồng quản trị đề xuất ngày 2026-08-27 cổ tức đặc biệt RMB 2,65 mỗi cổ phiếu, trả vào khoảng 2026-11-06, tổng ước tính ≈ RMB 1.006,0 triệu (≈ 43% lợi nhuận H1 2026), phụ thuộc phê duyệt của đại hội cổ đông bất thường [S7 trang 16, thuyết minh 7; 379.618.800 × 2,65 = 1.005,99 triệu `PHÉP_TÍNH`]. Theo bản sao thông báo HKEX trên Eastmoney, đại hội cổ đông bất thường ngày 2026-09-30 đã thông qua; **chưa mở bản gốc HKEXnews và chưa xác minh việc đã trả**. `CHƯA_XÁC_MINH`

## Các kịch bản (kịch bản vận hành, chưa định giá)

Chưa có giá trị nội tại hay khoảng giá, nên cột "Khoảng giá trị" là `CHƯA_BIẾT`. Các kịch bản dưới đây là khung theo dõi, **không** gắn xác suất.

| Kịch bản | Giả định chính (đo được) | Chỉ báo để kiểm tra, mốc | Điều gì phải đúng |
|---|---|---|---|
| Bất lợi | Doanh thu hàng hóa/cửa hàng tiếp tục giảm; mở mới dưới 5.000 cửa hàng/nửa năm; chi phí bán hàng + quản lý ≥ 11–12% doanh thu; biên gộp ≈ 29–30% | Báo cáo FY2026 (khoảng tháng 3/2027, `CHƯA_BIẾT` lịch), kết quả H2 2026; số chủ nhượng quyền tăng chậm hơn số cửa hàng | Nguyên nhân là bão hòa, chiết khấu hoặc đặc thù Mixue (không phải chỉ trợ giá, vì trợ giá đã hạ nhiệt theo nguồn thứ cấp) |
| Cơ sở | Doanh thu hàng hóa/cửa hàng ổn định ở mức thấp hơn H1 2025; chi phí bán hàng + quản lý ổn định ≈ 11% doanh thu; biên gộp ≈ 30–31%; tồn kho không tăng thêm | Tồn kho / giá vốn quay về 50 ngày hoặc thấp hơn; OCF/lợi nhuận ≥ 1; doanh thu H2 2026 tăng cao hơn H1 | Tồn kho cuối 2025 không thành khoản phải trích lập thêm. **Lưu ý:** theo so sánh với kỳ vọng thị trường (nguồn thứ cấp) kịch bản này có thể vẫn lạc quan, vì nó giả định H2 2026 ổn định trong khi H1 giảm 14,7% |
| Thuận lợi | Đầu tư vào sản phẩm và máy thông minh nâng doanh thu/cửa hàng; Lucky Cup và FULU đóng góp thêm; chi phí marketing chuyển thành doanh số | Doanh thu/cửa hàng quay về mức 2025; biên gộp ≥ 31%; mở mới phục hồi | Chi phí IP và nhân sự hiện tại là đầu tư có hoàn vốn, không phải chi phí thường xuyên |

`KỊCH_BẢN`: giả định có điều kiện, không phải dự báo, không phải khuyến nghị.

## Rủi ro và bằng chứng trái chiều

**Rủi ro (xếp theo độ trọng yếu của người viết, `Ý_KIẾN`):**

1. **Tăng trưởng đã mất đà:** H1 2026 doanh thu +2,3%, lợi nhuận −14,7% sau FY2025 +35,2% và +33,1%. `SỰ_THẬT` [S4, S7]
2. **Chi phí cố định tăng nhanh hơn doanh thu:** nhân viên +14,0% trong sáu tháng, chi phí quản lý +39% và chi phí bán hàng +23% so với cùng kỳ. `SỰ_THẬT` [S7]
3. **Phụ thuộc sức khỏe chủ cửa hàng nhượng quyền:** doanh thu của Mixue là doanh thu bán cho chủ cửa hàng; phí dịch vụ nhượng quyền cố định (không có phần biến đổi) và chỉ 2,7% doanh thu nên phản ánh số cửa hàng, không phản ánh sức khỏe chủ cửa hàng. `SỰ_THẬT` [S7, thuyết minh 3]. Dữ liệu doanh số bán lẻ độc lập `CHƯA_BIẾT`.
4. **Tồn kho tăng nhanh:** đã nêu ở trên; nguyên nhân `CHƯA_BIẾT`.
5. **Biên gộp:** hàng hóa và thiết bị giảm 1,3 điểm % năm 2025, biên gộp toàn công ty giảm thêm 1,2 điểm % ở H1 2026 do công ty chủ động nâng chất lượng nguyên liệu. `SỰ_THẬT` [S4, S7]
6. **Mở rộng nước ngoài đang lùi:** 4.895 → 4.378. `SỰ_THẬT`
7. **Tỷ giá trên tiền HK$/ngoại tệ:** lỗ 79,5 triệu RMB (2025) và 153,8 triệu (H1 2026). `SỰ_THẬT` [S4, S7]
8. **An toàn thực phẩm và uy tín thương hiệu qua hành vi của chủ cửa hàng** (rủi ro cấu trúc của mô hình nhượng quyền). Nguồn thứ cấp: vụ chanh cũ ở Hồ Bắc tháng 3/2025, 8.727 khiếu nại trên Black Cat (khoảng 70% liên quan an toàn thực phẩm) đến 2/2025, 16 cửa hàng nhượng quyền bị Hội người tiêu dùng Bắc Kinh nêu năm 2024 (The Standard, 2025-03-17). Quy định nhượng quyền 2026 `CHƯA_BIẾT`. `CHƯA_XÁC_MINH`
9. **Ưu đãi thuế** có thể không kéo dài (xem phần thuế suất).

**Bằng chứng trái chiều với lập luận bất lợi** (tức khiến kết luận "tăng trưởng đang gãy" kém chắc):

- Tỷ lệ đóng cửa hàng H1 2026 thấp hơn H1 2025 (2,2% so với 2,6%); chủ nhượng quyền tăng 27,2%. `PHÉP_TÍNH`
- Trợ giá giao hàng đã hạ nhiệt từ 2026 (nguồn thứ cấp), nên nền cao của H1 2025 có thể chỉ là hiệu ứng một lần; Q3/H2 2026 chưa có dữ liệu. `CHƯA_BIẾT`
- Doanh thu nửa cuối 2025 tăng ≈ +32,0% so với nửa cuối 2024 `PHÉP_TÍNH` (từ doanh thu năm trừ H1), nghĩa là điểm chuyển xảy ra đột ngột ở H1 2026, không phải xu hướng dần; cần xem H2 2026.
- Tiền, tiền gửi và tài sản tài chính còn lớn; vay ngân hàng không đáng kể; có cổ tức đặc biệt. `SỰ_THẬT` [S4, S7]

**Bằng chứng ủng hộ lập luận bất lợi:** các ước tính ngoài về doanh thu hàng hóa/cửa hàng giảm 15–17% (đều chia từ cùng số công ty, nên không độc lập về dữ liệu); đối thủ như Guming và Auntea Jenny vẫn tăng (nguồn thứ cấp) nên vấn đề có thể đặc thù Mixue; cổ phiếu giảm sâu sau báo cáo (nguồn thứ cấp). `Ý_KIẾN` / `CHƯA_XÁC_MINH`

## Điều kiện làm luận điểm mất hiệu lực

Luận điểm cần kiểm tra: "Mixue tiếp tục tăng trưởng nhờ mở rộng mạng lưới và lợi thế chuỗi cung ứng". Đây là các chỉ báo đo được do người viết đề xuất (`Ý_KIẾN`), không phải ngưỡng do công ty công bố:

1. Doanh thu hàng hóa / cửa hàng nhượng quyền bình quân giảm ở hai nửa năm liên tiếp (H1 2026 đã giảm, H2 2026 chưa biết).
2. Số cửa hàng nhượng quyền mở mới thấp hơn 5.000 mỗi nửa năm trong khi chủ nhượng quyền ngừng tăng.
3. Chi phí bán hàng + quản lý trên doanh thu ≥ 11% (H1 2026: 11,4%; H1 2025: 9,0%) không giảm trở lại sau hai kỳ.
4. Biên gộp dưới 30% (H1 2026: 30,4%) cùng lúc với chi phí không giảm.
5. Tồn kho / giá vốn (theo số cuối kỳ) tăng tiếp hoặc trích lập giảm giá hàng tồn kho tăng mạnh; OCF/lợi nhuận dưới 1.
6. Bằng chứng thêm về vấn đề an toàn thực phẩm hoặc quy định nhượng quyền làm tăng số cửa hàng đóng.

## Điều chưa biết và lần kiểm tra tiếp theo

- **Vì sao giá trị hàng mỗi cửa hàng giảm trong H1 2026?** Nền cao do trợ giá, đổi cơ cấu sản phẩm, bão hòa, chiết khấu, FULU, hay mẫu số? Cần doanh số cùng cửa hàng chính thức (hiện công ty không công bố), thuyết minh hợp nhất FULU, họp báo, và dữ liệu độc lập.
- Dòng tiền và báo cáo lưu chuyển tiền tệ H1 2026: thông báo kết quả không có; chờ báo cáo giữa kỳ đầy đủ.
- Đối tượng góp vốn vào công ty liên kết (109,0 triệu RMB); giá mua FULU; giao dịch bên liên quan; thỏa thuận hành động phối hợp của hai nhà sáng lập.
- Giá cổ phiếu hiện tại và bội số; so sánh với đối thủ bằng nguồn gốc (báo cáo của từng công ty niêm yết).
- Cổ tức đặc biệt đã trả chưa; xác minh bằng bản gốc HKEXnews.
- Doanh thu theo thương hiệu (MIXUE / Lucky Cup / FULU) và theo địa lý từ FY2024: báo cáo không tách `CHƯA_BIẾT`.
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
| S9 | Số cổ phiếu 379.618.800 | SỰ_THẬT | [HKEXnews, kết quả bỏ phiếu ĐHĐCĐ](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0626/2026062602855.pdf) | 2026-06-26 | tại 2026-06-26 | 2026-11-25 | số cổ phiếu | Chưa lưu trong `data/raw` |
| S10 | Cổ tức đặc biệt RMB 2,65/cổ phiếu | SỰ_THẬT (đề xuất) | [HKEXnews, thông báo cổ tức](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700183.pdf) | 2026-08-27 | FYE 2026-12-31 | 2026-11-25 (bên kiểm nguồn mở) | RMB | Điều phối viên chưa tự mở; chưa lưu |
| S11 | ĐHĐCĐ bất thường thông qua cổ tức đặc biệt (2026-09-30) | CHƯA_XÁC_MINH | [Bản sao thông báo HKEX trên Eastmoney](https://pdf.dfcfw.com/pdf/H2_AN202609301830055247_1.pdf) | 2026-09-30 | n/a | 2026-11-25 (bên kiểm nguồn mở) | n/a | Không phải HKEXnews gốc |
| T1–T8 | Bối cảnh ngành (trợ giá, đối thủ, cổ phiếu, an toàn thực phẩm) | Ý_KIẾN / CHƯA_XÁC_MINH | Nguồn thứ cấp do bên phản biện mở: [Caixin 2026-01-10](https://www.caixinglobal.com/2026-01-10/beijing-tightens-scrutiny-of-food-delivery-giants-amid-price-wars-102402304.html), [The Standard, Meituan Q2](https://www.thestandard.com.hk/finance/article/341211/Meituan-swings-to-profit-in-Q2-as-price-wars-subside), [Inside Retail, Chagee](https://insideretail.com.au/business/inside-chagees-difficult-adjustment-to-chinas-tea-market-202609), [Caixin 2026-08-31](https://www.caixinglobal.com/2026-08-31/chart-of-the-day-chinas-tea-chains-serve-up-a-mixed-brew-102480087.html), [KrASIA/Nikkei](https://kr-asia.com/china-bubble-tea-chain-mixue-shuts-more-stores-as-growth-model-falters), [Huxiu](https://m.huxiu.com/article/4886802.html), [36Kr](https://eu.36kr.com/en/p/3966912256237060), [The Standard, vụ chanh cũ](https://www.thestandard.com.hk/market/article/70948/IPO-darling-Mixue-accused-of-using-stale-lemons-in-bestselling-drink) | 2025-03 đến 2026-11 | các kỳ khác nhau | 2026-11-25 (bên phản biện mở) | n/a | Người viết **chưa tự mở**; một số bài có lỗi số; chỉ dùng bối cảnh |

Ghi chú về phạm vi đọc: các PDF được tải trực tiếp từ HKEXnews bằng `curl` rồi đọc bằng `pdftotext`; nội dung PDF là dữ liệu, không là chỉ dẫn. Bên kiểm nguồn đã tải lại 7 PDF chính bằng `WebFetch` và băm SHA-256, cả 7 khớp tệp trong repo.

## Biên bản kiểm duyệt

- Biên bản kiểm nguồn (v1, `KHÔNG_ĐẠT`): `research/companies/HK/reviews/2097-mixue-fact-check-v1.md`
- Biên bản phản biện rủi ro (v1, `KHÔNG_ĐẠT`): `research/companies/HK/reviews/2097-mixue-bear-review-v1.md`
- Bản v2 này chưa có biên bản kiểm duyệt; không được bỏ nhãn nháp.
- Bất đồng chưa giải quyết: bản nháp coi H1 2026 là "điểm gãy" của chuỗi tăng trưởng; bên phản biện coi đó là cách đọc hợp lý nhưng nguyên nhân (trợ giá, bão hòa, chi phí tự chọn) chưa được chứng minh nên cần giữ cả ba giả thuyết mở. Bản v2 giữ cả ba giả thuyết mở và ghi rõ trợ giá có thể đã hạ nhiệt.

> Chỉ dùng cho học tập và nghiên cứu. Đây không phải tư vấn tài chính cá nhân hay lệnh giao dịch.
