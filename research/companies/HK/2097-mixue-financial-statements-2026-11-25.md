# MIXUE Group, đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (2097.HK)

- Chốt dữ liệu lúc: `2026-11-25 15:00 UTC+7`
- Quốc gia / thị trường / sở giao dịch: Trung Quốc đại lục (hoạt động chính), niêm yết cổ phiếu H tại Sở Giao dịch Hồng Kông (HKEX) mã `2097` từ 2025-03-03
- Chuẩn kế toán: IFRS Accounting Standards; kiểm toán Ernst & Young (Hong Kong)
- Tiền tệ / đơn vị báo cáo: RMB; số gốc tính theo RMB nghìn, bài này làm tròn sang RMB triệu hoặc tỷ
- Phạm vi: đọc báo cáo tài chính để hiểu công ty. **Chưa định giá** (chưa lấy giá cổ phiếu để tính bội số, chưa có giá trị nội tại). Đây chưa phải nghiên cứu doanh nghiệp đầy đủ.
- Dữ liệu gốc: `data/raw/mixue-financials-2026-11-25.json`; PDF gốc và mã băm tại `data/raw/mixue-hkex/`
- Phép tính: `data/processed/mixue-financial-calculations-2026-11-25.md`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Phiên bản v6. Bản v4 bổ sung lưu chuyển tiền tệ H1 2026. Bản hiện hành đối chiếu thêm cơ cấu tiền, cam kết vốn, giao dịch FULU, thưởng cổ phiếu và giới hạn suy luận từ chi phí nhân sự. Các biên bản v1–v3 được lưu trong [thư mục kiểm duyệt](reviews/).

> Không phải lời khuyên mua, bán hay nắm giữ. Các điều kiện, kịch bản và chỉ báo dưới đây là công cụ học tập để theo dõi dữ kiện, không phải hướng dẫn quản lý một vị thế.

## Tóm tắt bài học

1. **Mixue gần như là nhà cung ứng chuỗi cung ứng cho các chủ cửa hàng nhượng quyền, không phải chuỗi tự bán lẻ.** 93,7% doanh thu 2025 đến từ bán hàng hóa cho cửa hàng, 4,0% từ bán thiết bị, chỉ 2,4% từ phí dịch vụ nhượng quyền. `SỰ_THẬT` [S4, thuyết minh 3]. Doanh thu của công ty xấp xỉ **số cửa hàng × giá trị hàng mỗi cửa hàng mua**, không phải doanh số bán cốc nước. `SUY_LUẬN`
2. **Bốn năm FY2022–FY2025 tăng trưởng rất mạnh, nhưng năm gốc là năm đáy:** doanh thu 13,6 → 33,6 tỷ RMB (CAGR ba kỳ 35,2%); lợi nhuận năm 2,0 → 5,9 tỷ RMB (CAGR ba kỳ 43,3%, nhưng lấy gốc 2021 thì chỉ 32,7% vì 2022 là năm lợi nhuận chỉ +5,3%). `PHÉP_TÍNH`
3. **Bảng cân đối ít nợ, nhiều tiền:** vay ngân hàng 28,2 triệu RMB; tiền, tiền gửi và tài sản tài chính 19,99 tỷ RMB cuối 2025; nợ phải trả / tổng tài sản 19,6%. `SỰ_THẬT` [S4]. Phần lớn tiền nằm ở sản phẩm quản lý tài sản (8,9 tỷ) và tiền gửi có kỳ hạn, và có lỗ tỷ giá trên tiền gửi ngoại tệ (79,5 triệu RMB năm 2025; 153,8 triệu RMB trong H1 2026). `SỰ_THẬT` [S4, S7]
4. **H1 2026 là kỳ có tín hiệu xấu nhất trong dữ liệu:** doanh thu +2,3%, lợi nhuận −14,7%, biên gộp thấp hơn 1,2 điểm %, trong khi tổng số cửa hàng tăng 20,7%. `SỰ_THẬT` + `PHÉP_TÍNH` [S7]. Doanh thu hàng hóa bán cho chủ cửa hàng tính trên mỗi cửa hàng giảm khoảng 15–17% tùy cách chia mẫu số `PHÉP_TÍNH`; nguyên nhân (nền cao do trợ giá năm 2025, bão hòa, chiết khấu, đổi cơ cấu sản phẩm, hợp nhất FULU) **chưa được nguồn nào xác nhận** `CHƯA_BIẾT`.
5. **Sụt lợi nhuận H1 2026: chi phí là yếu tố lớn nhất, nhưng biên gộp cũng góp khoảng một phần ba.** Lợi nhuận trước thuế giảm 492,6 triệu RMB. Phân rã tuyệt đối: chi phí bán hàng + quản lý tăng 381,7 triệu (≈ 77,5%), lợi nhuận gộp giảm 76,7 triệu (≈ 15,6%). Phân rã theo hiệu ứng: biên gộp lùi 1,2 điểm % làm mất ≈ 184,6 triệu (≈ 37%), trong khi doanh thu tăng cộng ≈ 107,9 triệu. Cả hai cách đều đúng; cách thứ hai cho thấy biên gộp không thể coi là không quan trọng. `PHÉP_TÍNH` [S7]
6. **Dòng tiền H1 2026 xác nhận tín hiệu xấu:** dòng tiền thuần từ hoạt động kinh doanh (OCF) giảm 37,4% còn 2.049,8 triệu RMB (H1 2025: 3.275,4), OCF/lợi nhuận 0,88 (H1 2025: 1,20). `SỰ_THẬT` + `PHÉP_TÍNH` [S13, báo cáo giữa kỳ 2026 đầy đủ]. Báo cáo lưu chuyển tiền tệ này **có sẵn** từ 2026-09-23; phiên bản trước của tài liệu này nói sai là chưa có.

## Mô hình kinh doanh (theo báo cáo)

- Ba thương hiệu: MIXUE (trà, nước ép, kem; giá lõi RMB 2–8), Lucky Cup (cà phê; RMB 2–11 cuối 2025), FULU Fresh Beer (bia tươi; mua lại, hoàn tất 2025-12-01). Giá điển hình khoảng 1 USD (≈ RMB 6) mỗi món. `SỰ_THẬT` [S4]
- Mô hình chủ yếu là nhượng quyền: chủ cửa hàng sở hữu và chịu kết quả cửa hàng, mua nguyên liệu và thiết bị từ Mixue. Công ty tự sản xuất 100% nguyên liệu lõi: cuối 2025 có 5 cơ sở sản xuất và 28 kho; đến 30/6/2026 là 6 cơ sở và 31 kho. `SỰ_THẬT` [S4, S7]
- Khách hàng thường **trả trước** khi nhận hàng và thiết bị. `SỰ_THẬT` [S4, thuyết minh 3]. Nợ hợp đồng chỉ 485,1 triệu RMB cuối 2025 (≈ 1,4% doanh thu, ≈ 5,3 ngày doanh thu) `PHÉP_TÍNH`, nên đòn bẩy vốn lưu động từ trả trước **không lớn**; phải trả người bán (2.212,5 triệu RMB) mới là khoản lớn hơn. `SỰ_THẬT` [S4]
- Không có khách hàng nào chiếm từ 10% doanh thu trong FY2024–FY2025 [S4, thuyết minh 2], FY2023 [S2], H1 2025–H1 2026 [S7]; khách hàng lớn nhất dưới 1% doanh thu 2025 [S5]. FY2022: `CHƯA_BIẾT`.
- Doanh thu theo địa lý: đến FY2023 cáo bạch tách; doanh thu ngoài đại lục là 50,1 triệu RMB (2021, 0,5%), 540,6 triệu (2022, 4,0%), 1.486,9 triệu (2023, 7,3%), và 9 tháng đầu 2024 là 952,4 triệu so với 1.171,3 triệu cùng kỳ 2023 (giảm). `SỰ_THẬT` [S1]. Từ FY2024, báo cáo chỉ nói "phần lớn từ đại lục", không tách số. `SỰ_THẬT` [S4, thuyết minh 2]

## Bối cảnh ngành, vĩ mô và so sánh toàn cầu

- `SỰ_THẬT` Mixue cho biết các nền tảng giao hàng tăng trợ giá đồ uống pha chế trong năm 2025. Luckin ghi nhận doanh số cùng cửa hàng tự vận hành quý 3/2026 giảm **11,1%** và nêu nền so sánh do trợ giá. Yum China công bố doanh số cùng cửa hàng quý 3 giảm **3%**. Đây là dữ liệu ở cấp bán lẻ, còn doanh thu hàng hóa của Mixue là bán buôn. [Mixue FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf) · [Luckin Q3 2026](https://www.sec.gov/Archives/edgar/data/1767582/000110465926121665/tm2628441d1_ex99-1.htm) · [Yum China Q3 2026](https://ir.yumchina.com/news-releases/news-release-details/yum-china-reports-third-quarter-2026-results)
- `SỰ_THẬT` Guming H1 2026 tăng doanh thu **31,9%**, số cửa hàng cuối kỳ **28,4%**, và biên gộp **33,4%** so với **31,5%**. `PHÉP_TÍNH` Giá trị giao dịch bán lẻ bình quân mỗi cửa hàng tăng khoảng **3,4%** (1.417,5 / 1.370,5 − 1). Guming cũng nêu tác động của giảm trợ giá. [Guming H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0826/2026082601151.pdf)
- `SUY_LUẬN` Nền cao do trợ giá và các yếu tố riêng của Mixue có thể cùng tác động. Khác biệt về phân khúc, cấp đo và thời kỳ giới hạn khả năng so sánh. Mixue nêu nâng chất lượng nguyên liệu, đầu tư tiếp thị và nhân sự trong giải trình kết quả. Mức đóng góp của từng nguyên nhân vào doanh thu hàng hóa trên mỗi cửa hàng là `CHƯA_BIẾT`. [Mixue H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0923/2026092300280.pdf)

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

- **OCF vượt lợi nhuận bốn năm liên tiếp (2022–2025)**, nhưng 2025 chỉ còn 1,02 lần: hàng tồn kho cuối kỳ tăng 65,8% (so với giá vốn +37,8%) và biến động tồn kho trên báo cáo lưu chuyển tiền làm giảm dòng tiền khoảng 1,55 tỷ RMB, và OCF 2025 gần như đi ngang (6.039,0 so với 6.008,7) dù lợi nhuận tăng 33,1%. `PHÉP_TÍNH` [S5]
- **Tồn kho đo theo ba cách cho kết quả khác nhau:** (a) số cuối kỳ tăng 65,8% so với giá vốn cả năm +37,8%; (b) ngày tồn kho bình quân đầu–cuối năm giảm từ 48,4 (2024) xuống 46,5 (2025); (c) ngày tồn kho theo số cuối kỳ tăng từ 48,2 lên 58,0. `PHÉP_TÍNH`. Tồn kho tiếp tục tăng sang 3.828,2 triệu RMB tại 30/6/2026 (+4,2% so với cuối 2025) trong khi doanh thu H1 gần như đi ngang. `SỰ_THẬT` [S7]. Nguyên nhân (mua trước Tết 2026, giá nguyên liệu, dự trữ khi nâng chất lượng, hay hàng bán chậm) `CHƯA_BIẾT`; trích lập giảm giá hàng tồn kho 2025 là 97,2 triệu (so với 37,0 triệu 2024) `SỰ_THẬT` [S5]; H1 2026 là 21,0 triệu so với 32,5 triệu cùng kỳ 2025 (giảm, bằng chứng trái chiều với lo ngại hàng tồn). `SỰ_THẬT` [S7, thuyết minh 5]
- **H1 2026 (báo cáo giữa kỳ đầy đủ [S13], chưa kiểm toán):** OCF 2.049,8 triệu so với 3.275,4 triệu cùng kỳ 2025 (−37,4%); OCF/lợi nhuận 0,88 so với 1,20. Nguyên nhân chính trong dòng tiền: phải trả người bán −378,7 triệu so với +739,4 triệu; tăng tồn kho −176,1 triệu so với −808,9 triệu (hàng tồn tăng ít hơn nhưng vẫn tăng); thuế đã trả 621,9 so với 567,6 triệu; mua tài sản cố định hữu hình 289,4 so với 305,8 triệu. `SỰ_THẬT` [S13]; OCF/lợi nhuận `PHÉP_TÍNH`.
- Thu từ phát hành cổ phiếu 2025 là 3.665,1 triệu RMB. Thu nhập lãi và sản phẩm quản lý tài sản 2025 là 330,0 triệu RMB, khoảng 4,4% lợi nhuận trước thuế. `PHÉP_TÍNH`
- Capex PPE giảm mạnh từ 1,44 tỷ (2024) xuống 0,69 tỷ (2025); cam kết vốn còn 301,8 triệu và công ty nói sẽ tiếp tục đầu tư năng lực sản xuất (cơ sở Vân Nam bắt đầu hoạt động 5/2026). `SỰ_THẬT` [S4, S7]
- ROE của cổ đông công ty mẹ (lợi nhuận thuộc cổ đông công ty mẹ chia vốn chủ sở hữu thuộc cổ đông công ty mẹ bình quân đầu–cuối năm) giảm từ 34,8% năm 2024 xuống 29,9% năm 2025. Vốn chủ sở hữu sau IPO tăng nhanh hơn lợi nhuận. `PHÉP_TÍNH`

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
(c) Mạng lưới nước ngoài **thu hẹp** từ 4.895 (cuối 2024) xuống 4.733 (30/6/2025, −3,3%), 4.467 (cuối 2025, −5,6% trong nửa năm) rồi 4.378 (30/6/2026, −2,0%); so cùng kỳ 30/6/2025 là −7,5%. Nửa năm gần nhất thu hẹp ít hơn nửa năm trước, nhưng chưa đủ để gọi là xu hướng (Indonesia và Việt Nam giảm), trái với câu chuyện "ra toàn cầu" `PHÉP_TÍNH`; đồng thời công ty nói đã vào Kazakhstan, Mỹ, Mexico, Kyrgyzstan, Brazil. `SỰ_THẬT` [S4, S7]
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

Nguồn: [S7]; tỷ lệ và hiệu là `PHÉP_TÍNH`. **Về chi phí:** công ty nói chi phí quản lý tăng chủ yếu do nhân sự. Tổng chi phí nhân sự toàn tập đoàn (gồm cả giá vốn và nghiên cứu phát triển) tăng từ 897,8 lên 1.000,1 triệu RMB (+102,3 triệu), trong đó lương và tiền công +91,0 triệu (760,7 → 851,7) `SỰ_THẬT` [S7, trang 5 và thuyết minh 5]. Tỷ số **102,3 / 381,7 ≈ 27%** so sánh hai khoản khác phạm vi `PHÉP_TÍNH`. Chi phí nhân sự toàn tập đoàn là tổng biến động của nhiều bộ phận và có thể gồm các khoản bù trừ. Đóng góp của nhân sự vào chi phí bán hàng và quản lý, cũng như khả năng kiểm chứng định lượng lời giải thích của công ty, là `CHƯA_BIẾT` cho đến khi có phân tách theo chức năng. **Tỷ lệ bán hàng + quản lý trên doanh thu** là 9,1% (H1 2025), 9,5% (H2 2025) và 11,4% (H1 2026) `PHÉP_TÍNH`; mức tuyệt đối của chi phí bán hàng H1 2026 (1.122,9) gần bằng H2 2025 (≈ 1.123,2) và chi phí quản lý (610,0) thấp hơn H2 2025 (≈ 643,9), nhưng H2 là nửa năm có doanh thu cao hơn (18.685,1 so với 15.215,8), FULU chỉ được hợp nhất một tháng trong H2 2025 so với sáu tháng ở H1 2026, và thời điểm ghi nhận chi phí có thể khác giữa hai kỳ. Vì vậy **không thể kết luận chi phí "đã đi ngang"**: so với H2 2025 tỷ lệ vẫn tăng khoảng 1,9 điểm %. Cách gọi đúng là "chi phí tăng, thành phần và tính bền chưa rõ". `SUY_LUẬN`

**Lời giải thích của công ty:** giá vốn tăng nhanh hơn doanh thu do đầu tư nâng chất lượng sản phẩm theo hướng nguyên liệu thật; chi phí bán hàng tăng do marketing và nhân sự phục vụ phát triển IP và hỗ trợ vận hành cửa hàng; chi phí quản lý tăng do nhân sự. `SỰ_THẬT` [S7].

**Về suy luận "giá trị hàng mỗi cửa hàng giảm":** doanh thu hàng hóa +3,0% so với số cửa hàng +23,5% (đại lục cuối kỳ), +20,7% (tổng cuối kỳ), +24,4% (cửa hàng nhượng quyền bình quân đầu–cuối kỳ) cho doanh thu hàng hóa trên mỗi cửa hàng giảm khoảng 16,5%, 14,6% và 17,2% tương ứng. `PHÉP_TÍNH`. Đây là **giá trị** (lượng × giá × cơ cấu), không phải "lượng hàng"; công ty đã đổi cơ cấu/chất lượng sản phẩm. Phép chia còn bị nhiễu bởi: 1.354 cửa hàng FULU mua tháng 12/2025 (có trong mẫu số H1 2026 nhưng không có ở H1 2025); doanh thu bán cho cửa hàng nước ngoài; cửa hàng mới mở chưa trưởng thành; công ty không công bố doanh số cùng cửa hàng. Các ước tính ngoài (môi giới, một số bài phân tích) đều chia từ cùng số tổng hợp nên **không phải bằng chứng cấp cửa hàng**. Hướng suy luận (đang giảm đáng kể) nhất quán giữa các cách chia, nhưng mức độ có thể còn lệch vì thời điểm nhập hàng của chủ cửa hàng (mua trước hay dùng sau) chưa được nêu trong báo cáo. `SUY_LUẬN`

## Ban lãnh đạo, quản trị và phân bổ vốn

- **Lãnh đạo.** Zhang Hongfu (đồng sáng lập) chuyển từ Tổng giám đốc sang đồng chủ tịch; Zhang Yuan (35 tuổi, vào tập đoàn tháng 2/2023 làm giám đốc tài chính) làm Tổng giám đốc; cả hai có hiệu lực 2026-03-24, tức **trong** H1 2026 (sau khi FY2025 kết thúc). Cùng ngày bà Cui Haijing từ chức chủ tịch ban kiểm soát và được bổ nhiệm "Head of Finance" phụ trách quản lý tài chính tập đoàn. `SỰ_THẬT` [S5, S17]. Không có bằng chứng về quan hệ nhân quả giữa việc đổi lãnh đạo và kết quả H1.
- **Cổ đông kiểm soát.** Hai nhà sáng lập, Zhang Hongchao (chủ tịch) và Zhang Hongfu (đồng chủ tịch), **ký thỏa thuận hành động phối hợp** từ tháng 9/2022 trong họp hội đồng quản trị và đại hội cổ đông, và không có ý định chấm dứt sau niêm yết. `SỰ_THẬT` [S14, cáo bạch, mục Concert Party Agreement]. Mỗi người là chủ sở hữu hưởng lợi **riêng** của 100.098.196 cổ phiếu chưa niêm yết và 53.899.028 cổ phiếu H = 153.997.224 cổ phiếu (40,84% vốn lúc IPO; ≈ 40,57% trên 379.618.800 cổ phiếu hiện nay), cộng 971.993 cổ phiếu chưa niêm yết và 647.994 cổ phiếu H qua nền tảng nhân viên do từng người kiểm soát. `SỰ_THẬT` [S14, mục Substantial Shareholders; S5]. Tổng hai người ≈ **81,1%** vốn (trực tiếp) hoặc ≈ 82,0% (gồm hai nền tảng) `PHÉP_TÍNH` trên 379.618.800; nhóm "core connected persons" (hai người, hai nền tảng, một giám sát viên và một giám đốc điều hành) giữ 315.044.663 cổ phiếu (83,55% lúc IPO) không tính vào cổ phiếu tự do chuyển nhượng. `SỰ_THẬT` [S14]. Hệ quả: cổ phiếu ngoài nhóm nội bộ ít; việc cổ đông nhỏ có tiếng nói trong các nghị quyết thường rất hạn chế `SUY_LUẬN`.
- **Giao dịch bên liên quan FULU.** Mixue ký ngày 30/9/2025, công bố 1/10 và hoàn tất giao dịch ngày 1/12/2025. Mixue góp **285,6 triệu RMB** để nắm 51% vốn sau góp và ký mua thêm 2% từ Zhao Jie với giá **11,2 triệu RMB**. Vợ của một cổ đông kiểm soát nắm 60,05% vốn trước giao dịch và kiểm soát pháp nhân nắm thêm 20,41%. Phần góp vốn được miễn phê duyệt bởi cổ đông độc lập theo quy tắc niêm yết. Hai khoản giá dựa trên định giá trước góp vốn **274,4 triệu RMB**, trong khoảng thẩm định độc lập **244,7–276,6 triệu**. Thuyết minh hợp nhất ghi dòng tiền ra ròng **13,725 triệu RMB** cho phần **285,6 − 271,875** triệu, gồm tiền nhận khi hợp nhất. Khoản ròng này có phạm vi riêng với giao dịch mua thêm 2%. `SỰ_THẬT` [S5, thuyết minh 40–41; S18]. `SUY_LUẬN` Khoảng định giá độc lập là bằng chứng để đánh giá giá mua, với các giả định tiền, nợ, quyền kiểm soát và thanh khoản nêu trong phụ lục công bố.
- **Quản trị.** Chủ tịch ủy ban kiểm toán, ông Huang Sidney Xuande (giám đốc độc lập), hiện là cố vấn cấp cao của JD.com và từng là giám đốc tài chính JD.com đến 9/2020 (theo S5 trang 33–34, bên kiểm nguồn đọc). Không có bằng chứng sai phạm; điểm cần xem là phần đánh giá tính độc lập và giao dịch bên liên quan của báo cáo thường niên (chưa đọc). `CHƯA_BIẾT`
- **Nhân sự và thưởng cổ phiếu.** Nhân viên tăng từ 7.025 cuối 2024 lên 9.102 cuối 2025 và 10.374 tại 30/6/2026. Ngày 28/9/2026, công ty cấp **12.023.300 quyền** cho 1.234 người, tương ứng cổ phiếu H mới, giá phải trả **18,47 HKD/cổ phiếu**, so với giá đóng cửa **184,70 HKD** khi cấp. Quyền xác lập theo đợt, đợt đầu sau ít nhất 12 tháng, và đợt cấp này không có điều kiện hiệu suất. `SỰ_THẬT` [S4, S7, S15]. Nếu toàn bộ được phát hành, tỷ lệ sở hữu hiện hữu giảm tương đối **3,07%** = 12.023.300 / (379.618.800 + 12.023.300) `PHÉP_TÍNH`. Báo cáo tháng 10 ghi nhận số cổ phiếu phát hành vẫn là **379.618.800** [S19].
- **Phân bổ vốn.** Tiền IPO ròng ≈ HK$ 3,8 tỷ, đã dùng ≈ HK$ 1,35 tỷ (≈ 35,5%) đến cuối 2025 [S5, theo bên kiểm nguồn]. Góp vốn 109,0 triệu RMB vào công ty liên kết (đối tượng `CHƯA_BIẾT`). Không đề xuất cổ tức thường niên FY2025 [S4].
- **Cổ tức đặc biệt H1 2026.** Hội đồng quản trị đề xuất ngày 2026-08-27 cổ tức đặc biệt RMB 2,65 mỗi cổ phiếu, ≈ 1.006,0 triệu RMB (379.618.800 × 2,65 `PHÉP_TÍNH`; ≈ 43% lợi nhuận H1 2026 và ≈ 27% khoản thu từ phát hành cổ phiếu 2025), dự kiến trả khoảng 2026-11-06 [S7 trang 16; S10, thông báo 2026-08-27; S12, thông báo họp 2026-09-11; cả ba đã lưu]. Đại hội cổ đông bất thường ngày 2026-09-30 thông qua với 342.789.315 phiếu thuận (99,999446%), 1.000 chống, 900 trắng; hai cổ đông hoặc người đại diện hiện diện nắm 342.791.215 cổ phiếu (90,30% quyền biểu quyết); ngày giao dịch không hưởng quyền 2026-10-05, ngày ghi nhận 2026-10-12, 3,08304 HKD mỗi cổ phiếu H. `SỰ_THẬT` [S11, S20]. Quyền hưởng theo số cổ phiếu trực tiếp của hai nhà sáng lập ước ≈ 816,2 triệu RMB (307.994.448 × 2,65, ≈ 81% tổng, trước thuế; ≈ 408,1 triệu mỗi người) `PHÉP_TÍNH`. Cổ tức chia đều theo cổ phiếu nên việc phần lớn chảy tới người kiểm soát là hệ quả của tỷ lệ sở hữu, không tự nó là chuyển giá trị khỏi cổ đông nhỏ; nhưng nghị quyết do chính người kiểm soát biểu quyết, nên 99,999% không chứng minh sự đồng thuận của cổ đông không kiểm soát. Việc ít cổ đông dự trực tiếp là bình thường (đại hội thường niên 2026-06-26 có 14 người, 94,21%), nên không coi là dấu hiệu bất thường. **Citi đã phát hành thông báo cuối cùng cho chương trình chứng chỉ lưu ký Mỹ ngày 6/11**, ghi mức 3,08304 HKD trên cổ phiếu cơ sở và lịch chi chứng chỉ ngày 23/11 [S21]. Đây là bằng chứng bổ sung về phân phối qua chương trình lưu ký. Số tiền đã tất toán cho toàn bộ cổ phiếu H và cổ phiếu chưa niêm yết là `CHƯA_BIẾT`. Cách đọc có hai chiều: (a) công ty ưu tiên hoàn vốn với tiền mặt 21,6 tỷ RMB, tiền IPO mới dùng ≈ 35,5% và tăng trưởng chậm, tức không thiếu tiền nhưng cũng không thấy dùng hết cho đầu tư; (b) dòng tiền tới nhóm kiểm soát. Cả hai chiều chưa được chứng minh.

## Kịch bản vận hành

| `KỊCH_BẢN` | Điều cần quan sát |
|---|---|
| Bất lợi | Doanh thu trên mỗi cửa hàng tiếp tục giảm, số mở ròng chậm lại và chi phí doanh thu cao hơn. Kiểm tra xem dòng tiền kinh doanh có tiếp tục giảm nhanh hơn lợi nhuận. |
| Cơ sở | Doanh thu trên mỗi cửa hàng giảm chậm dần, chi phí và dòng tiền cải thiện từng bước. Kiểm tra báo cáo FY2026 và FY2027. |
| Thuận lợi | Doanh thu trên mỗi cửa hàng phục hồi và biên lợi nhuận tăng. Kiểm tra số quán mở/đóng và nguyên nhân biến động chi phí. |

[Báo cáo triển vọng 2026–2028](2097-mixue-story-and-3y-outlook-2026-11-25.md#kịch-bản-hoạt-động-20262028) trình bày giả định định lượng và bảng ngưỡng thống nhất. Doanh thu trên mỗi cửa hàng dùng để mô tả doanh thu hợp nhất của Mixue chia số quán bình quân. Theo dõi riêng doanh thu hàng hóa trên mỗi cửa hàng trong phần chất lượng tài chính.

## Rủi ro và bằng chứng trái chiều

**Rủi ro (xếp theo độ trọng yếu của người viết, `Ý_KIẾN`):**

1. **Tăng trưởng đã mất đà:** H1 2026 doanh thu +2,3%, lợi nhuận −14,7% sau FY2025 +35,2% và +33,1%; đà lợi nhuận đã chậm từ H2 2025. `SỰ_THẬT` + `PHÉP_TÍNH` [S4, S6, S7]
2. **Chất lượng dòng tiền giảm:** OCF H1 2026 −37,4%, OCF/lợi nhuận 0,88 (H1 2025: 1,20), phần lớn do phải trả người bán đảo chiều (−378,7 so với +739,4 triệu). `SỰ_THẬT` + `PHÉP_TÍNH` [S13]
3. **Chi phí tăng nhanh hơn doanh thu, thành phần chưa rõ:** chi phí bán hàng +22,9%, quản lý +39,4%, nhân viên +14,0% trong sáu tháng; chưa có dữ liệu tách chi phí nhân sự theo chức năng. `SỰ_THẬT` + `PHÉP_TÍNH` [S7]
4. **Phụ thuộc sức khỏe chủ cửa hàng nhượng quyền.** Doanh thu của Mixue là doanh thu bán cho chủ cửa hàng. Doanh thu dịch vụ nhượng quyền chiếm 2,7% doanh thu H1 2026 `SỰ_THẬT` [S7]. Kết quả của chủ quán cần dữ liệu bán ra và chi phí ở cấp cửa hàng `SUY_LUẬN`. Dữ liệu doanh số bán lẻ độc lập `CHƯA_BIẾT`.
5. **Tồn kho tăng nhanh:** nguyên nhân `CHƯA_BIẾT` (xem phần Tồn kho); H1 2026 tăng thêm 4,2% nhưng trích lập giảm giá hàng tồn kho thấp hơn.
6. **Biên gộp:** biên gộp hàng hóa và thiết bị giảm 1,3 điểm % năm 2025 [S4]; biên toàn công ty thấp hơn 1,2 điểm % so với H1 2025 (nhưng chỉ −0,3 điểm % so với H2 2025) theo giải trình của công ty, mức đầu tư nâng chất lượng nguyên liệu góp phần đẩy giá vốn [S7]. `SỰ_THẬT` + `PHÉP_TÍNH`
7. **Mạng lưới nước ngoài thu hẹp:** −3,3%, −5,6%, −2,0% theo từng nửa năm (4.895 → 4.378). `PHÉP_TÍNH`
8. **Tỷ giá trên tiền gửi ngoại tệ:** lỗ 79,5 triệu RMB (2025) và 153,8 triệu (H1 2026), nhưng ròng trong "thu nhập khác" chỉ giảm 31,1 triệu. `SỰ_THẬT` [S4, S7]
9. **Quản trị: tập trung sở hữu và giao dịch bên liên quan.** Hai nhà sáng lập có thỏa thuận hành động phối hợp và nắm ≈ 81% vốn; công ty đầu tư vào FULU, doanh nghiệp do người nhà một cổ đông kiểm soát nắm ≈ 80% trước giao dịch (giá dựa trên khoảng thẩm định đã công bố, kết quả kinh tế sau mua là `CHƯA_BIẾT`). `SỰ_THẬT` [S5, S14]
10. **An toàn thực phẩm và uy tín của mạng lưới nhượng quyền.** Mức tuân thủ có thể khác theo cửa hàng. Tần suất sự cố đã xác minh và tác động tài chính đối với Mixue là `CHƯA_BIẾT`. `SUY_LUẬN`
11. **Ưu đãi thuế** có thể không kéo dài (xem phần thuế suất).
12. **Thưởng cổ phiếu và lưu hành cổ phiếu H:** quyền thưởng ≈ 3,17% số cổ phiếu hiện có; kế hoạch chuyển 22,8 triệu cổ phiếu chưa niêm yết (6,01%) thành cổ phiếu H có thể làm đổi tính thanh khoản; tác động đến giá `CHƯA_BIẾT`.

**Bằng chứng trái chiều với lập luận bất lợi** (khiến kết luận "tăng trưởng đang gãy" kém chắc):

- Tỷ lệ đóng cửa hàng H1 2026 thấp hơn H1 2025 (2,2% so với 2,6%), chủ nhượng quyền +27,2%. `PHÉP_TÍNH`
- Số cửa hàng mở mới thấp có thể phản ánh tiêu chuẩn mở quán chặt hơn, nhu cầu mở mới yếu đi hoặc cả hai. Đóng góp của từng yếu tố là `CHƯA_BIẾT`.
- Phạm vi hợp nhất FULU, tuổi cửa hàng và nền trợ giá 2025 có thể ảnh hưởng đến tỷ số doanh thu của Mixue trên mỗi cửa hàng. Dữ liệu Luckin và Yum China cho thấy áp lực ở một số chuỗi, với thước đo bán lẻ khác Mixue. `SUY_LUẬN`
- Trích lập giảm giá hàng tồn kho H1 2026 giảm (21,0 so với 32,5 triệu). `SỰ_THẬT` [S7]
- Điểm chuyển ở doanh thu xảy ra đột ngột: +39,3% (H1 2025) → +32,0% (H2 2025) → +2,3% (H1 2026); H2 2026 chưa có dữ liệu. `PHÉP_TÍNH`

**Bằng chứng ủng hộ lập luận bất lợi:** (a) biên gộp và tỷ lệ chi phí của Mixue xấu đi trong khi Guming cải thiện cả hai. Doanh thu Guming trên số quán cuối kỳ tăng khoảng 2,7% = 1,319 / 1,284 − 1, một phép chia xấp xỉ; (b) các ước tính ngoài về doanh thu hàng hóa/cửa hàng giảm 15–17% (không độc lập về dữ liệu vì đều chia từ số tổng của công ty); (c) nền H2 2025 có thể khó hơn; (d) OCF giảm mạnh hơn lợi nhuận.

**Thanh khoản.** `SỰ_THẬT` Tại 30/6/2026, tiền và tương đương tiền **6.027,9 triệu RMB**, tiền gửi đáo hạn trong một năm **5.798,7 triệu**, sau một năm **1.716,6 triệu**, tiền bị hạn chế **11,5 triệu**, tài sản tài chính ghi nhận theo giá trị hợp lý qua lãi lỗ **8.096,1 triệu**, vay ngân hàng **0** và nợ thuê **227,8 triệu**. Phần thảo luận của quản lý công bố **21.640,7 triệu** khi chỉ cộng sản phẩm quản lý tài sản trong nhóm tài sản tài chính. Tổng theo toàn bộ dòng tài sản tài chính trên bảng cân đối là **21.650,7 triệu**, chênh xấp xỉ **10,0 triệu** `PHÉP_TÍNH`. Thuyết minh 16–17 ghi cam kết mua tài sản cố định **204,5 triệu** và không có nợ tiềm tàng đáng kể tại ngày báo cáo. [S13, trang 8, 46–47, 66 và 69]. Số dư, cấu phần và nghĩa vụ phát sinh sau 30/6 là `CHƯA_BIẾT` ngoài khoản cổ tức đã công bố.

## Điều kiện làm luận điểm mất hiệu lực

Luận điểm cần kiểm tra: "Mixue tiếp tục tăng trưởng nhờ mở rộng mạng lưới và lợi thế chuỗi cung ứng". Các chỉ báo dưới đây là `Ý_KIẾN` của người viết, làm tròn từ mức hiện tại; không phải ngưỡng do công ty công bố và không phải khuyến nghị. Nên theo dõi theo **xu hướng nhiều kỳ**, so cùng nửa năm với nhau (có mùa vụ), hơn là một ngưỡng cứng:

1. Doanh thu hàng hóa / cửa hàng nhượng quyền bình quân giảm ở hai nửa năm liên tiếp (H1 2026 đã giảm; H2 2026 chưa biết, và nền H2 2025 cao).
2. Số cửa hàng nhượng quyền mở mới mỗi nửa năm dưới khoảng 8% số đầu kỳ và số chủ nhượng quyền ngừng tăng. Khi cùng xảy ra, đối chiếu số quán đóng và tiêu chuẩn mở mới để tìm nguyên nhân.
3. Chi phí bán hàng + quản lý trên doanh thu từ khoảng 11% trở lên kéo dài qua hai nửa năm. H1 2026 đã vượt ngưỡng một kỳ (11,4%; H1 2025: 9,1%; H2 2025: 9,5%).
4. Biên gộp H2 2026 tiếp tục giảm so với H2 2025 (≈30,7%) và tỷ lệ chi phí không giảm.
5. OCF/lợi nhuận dưới 1: **đã thỏa ở H1 2026 (0,88)**; cần xem H2 2026 và FY2026 có quay về ≥ 1 không. Cùng với tồn kho / giá vốn theo số cuối kỳ tăng so cùng kỳ hoặc trích lập giảm giá hàng tồn kho tăng mạnh trở lại.
6. Bằng chứng mới về an toàn thực phẩm, quy định nhượng quyền hoặc giao dịch bên liên quan làm tăng số cửa hàng đóng hoặc làm giảm niềm tin vào quản trị.

## Điều chưa biết và lần kiểm tra tiếp theo

- **Vì sao giá trị hàng mỗi cửa hàng giảm trong H1 2026?** Nền cao do trợ giá, thương hiệu mới kéo trung bình, đổi cơ cấu sản phẩm, bão hòa, chiết khấu, FULU, hay mẫu số? Cần doanh số cùng cửa hàng chính thức (chưa thấy trong công bố đã kiểm), bản ghi cuộc họp kết quả, thuyết minh hợp nhất FULU và dữ liệu độc lập. Giữ cả hai giả thuyết (nền trợ giá chung; đặc thù Mixue).
- Thành phần chi phí bán hàng + quản lý tăng thêm 381,7 triệu (ngoài nhân sự), có thay đổi phân loại hay không, và tính bền của mức chi phí.
- Nguyên nhân phải trả người bán đảo chiều (−378,7 so với +739,4 triệu) và liệu OCF/lợi nhuận có quay về ≥ 1 ở H2 2026.
- Mức đóng góp của FULU sau hợp nhất, kết quả kiểm tra các giả định định giá và đối tượng góp vốn 109,0 triệu RMB là `CHƯA_BIẾT`. Theo dõi thuyết minh bên liên quan và báo cáo năm tiếp theo.
- Số tiền thực chi cổ tức đặc biệt trên toàn bộ hai loại cổ phiếu là `CHƯA_BIẾT`. Kiểm trong báo cáo lưu chuyển tiền và thuyết minh FY2026.
- Tỷ lệ thực hiện quyền thưởng và tiến độ chuyển đổi 22,8 triệu cổ phiếu sang cổ phiếu H là `CHƯA_BIẾT`. Theo dõi báo cáo biến động vốn hàng tháng và công bố của công ty.
- Dữ liệu cùng cửa hàng và kinh tế của bên nhận nhượng quyền là `CHƯA_BIẾT`. Kiểm tra cập nhật vận hành và công bố tài chính FY2026.
- Doanh thu theo thương hiệu và theo địa lý từ FY2024: báo cáo không tách `CHƯA_BIẾT`.
- Chưa đọc toàn văn S3, S5 (254 trang), S13 (86 trang), cáo bạch S14 (558 trang).

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
| S11 | Kết quả biểu quyết ĐHĐCĐ bất thường 2026-09-30 thông qua cổ tức đặc biệt | SỰ_THẬT | [HKEXnews, kết quả biểu quyết](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0930/2026093002215.pdf) | 2026-09-30 | n/a | 2026-11-25 | số cổ phiếu, % | 3 trang, `6f6805fe…`; đã lưu; bản sao Eastmoney khớp từng số |
| S12 | Thông báo họp cổ đông bất thường (một nghị quyết thường về cổ tức đặc biệt, họp 2026-09-30) | SỰ_THẬT | [HKEXnews, thông báo](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0911/2026091101193.pdf) | 2026-09-11 | n/a | 2026-11-25 | n/a | 2 trang, `ab600329…`; đã lưu |
| S13 | Báo cáo giữa kỳ 2026 đầy đủ: báo cáo lưu chuyển tiền tệ H1 2026 (OCF, tồn kho, phải trả, thuế, capex) | SỰ_THẬT | [HKEXnews, Interim Report 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0923/2026092300280.pdf) | 2026-09-23 | H1 2026, chưa kiểm toán | 2026-11-25 | RMB nghìn | 86 trang, `0e1ddcd2…`; đã lưu; đã đối chiếu các trang 8, 44, 46–54, 66, 69, 73 |
| S14 | Cáo bạch đầy đủ: thỏa thuận hành động phối hợp, sở hữu hai nhà sáng lập, nhóm kết nối cốt lõi | SỰ_THẬT | [HKEXnews, cáo bạch](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0221/2025022100009.pdf) | 2025-02-21 | tại IPO | 2026-11-25 | số cổ phiếu, % | 558 trang, `c9014020…`; đã lưu; mới đọc các mục sở hữu |
| S15 | Cấp 12.023.300 quyền thưởng cổ phiếu H (H Share Award Scheme) | SỰ_THẬT | [HKEXnews, thông báo](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0928/2026092801979.pdf) | 2026-09-28 | n/a | 2026-11-25 | số cổ phiếu, HK$ | 5 trang, `bcd2952b…`; đã lưu |
| S16 | Kế hoạch lưu hành toàn phần cổ phiếu H (22.823.988 cổ phiếu, ≈ 6,01%) | SỰ_THẬT | [HKEXnews, thông tin nội bộ](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0503/2026050300001.pdf) | 2026-05-03 | n/a | 2026-11-25 | số cổ phiếu | 2 trang, `193e50b6…`; đã lưu |
| S17 | Thay đổi HĐQT, ban kiểm soát, quản lý (CEO, Head of Finance) | SỰ_THẬT | [HKEXnews, thông báo](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0324/2026032400173.pdf) | 2026-03-24 | n/a | 2026-11-25 | n/a | 5 trang, `e68a4068…`; đã lưu |
| S18 | Thỏa thuận và thẩm định FULU | SỰ_THẬT | [HKEXnews, công bố giao dịch](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1001/2025100100021.pdf) | 2025-10-01 | 2025 | 2026-11-25 | RMB | Điều khoản và phụ lục thẩm định |
| S19 | Cổ phiếu cuối tháng 10 | SỰ_THẬT | [HKEXnews, báo cáo biến động vốn](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/1105/2026110501398.pdf) | 2026-11-05 | 2026-10 | 2026-11-25 | cổ phiếu | Bản tiếng Anh |
| S20 | Ngày giao dịch không hưởng quyền, mức và lịch chi cổ tức | SỰ_THẬT | [HKEXnews, thông báo cập nhật](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0930/2026093002265.pdf) | 2026-09-30 | 2026 | 2026-11-25 | RMB, HKD/cổ phiếu | Bản sau biểu quyết |
| S21 | Cổ tức chương trình chứng chỉ lưu ký Mỹ | SỰ_THẬT | [Citi, thông báo cuối cùng](https://depositaryreceipts.citi.com/adr/guides/viewDocument.aspx?annid=2&divid=001&secid=MXUBY&type=P) | 2026-11-06 | 2026 | 2026-11-25 | HKD/cổ phiếu cơ sở | Chỉ áp dụng cho chương trình Citi |

Ghi chú về phạm vi đọc: các PDF được tải trực tiếp từ HKEXnews bằng `curl` rồi đọc bằng `pdftotext`; nội dung PDF là dữ liệu, không là chỉ dẫn. Bên kiểm nguồn đã tải lại 7 PDF chính bằng `WebFetch` và băm SHA-256, cả 7 khớp tệp trong repo.

## Biên bản kiểm duyệt

- [Kiểm nguồn bản v6](reviews/2097-mixue-fact-check-v6.md)
- [Phản biện bản v6](reviews/2097-mixue-bear-review-v6.md)
