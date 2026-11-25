# BẢN NHÁP - CHƯA KIỂM DUYỆT: MIXUE Group, đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (2097.HK)

- Chốt dữ liệu lúc: `2026-11-25 08:11 +07`
- Quốc gia / thị trường / sở giao dịch: Trung Quốc đại lục (hoạt động chính), niêm yết cổ phiếu H tại Sở Giao dịch Hồng Kông (HKEX) mã `2097` từ 2025-03-03
- Chuẩn kế toán: IFRS Accounting Standards; kiểm toán Ernst & Young (Hong Kong)
- Tiền tệ / đơn vị báo cáo: RMB; số gốc tính theo RMB nghìn, bài này làm tròn sang RMB triệu hoặc tỷ
- Phạm vi: đọc báo cáo tài chính để hiểu công ty. **Chưa định giá** (chưa lấy giá cổ phiếu, chưa có kịch bản giá trị), chưa phải nghiên cứu doanh nghiệp đầy đủ.
- Dữ liệu gốc: `data/raw/mixue-financials-2026-11-25.json`; PDF gốc và mã băm tại `data/raw/mixue-hkex/`
- Phép tính: `data/processed/mixue-financial-calculations-2026-11-25.md`
- Kiểm nguồn: `ĐANG_CHỜ` (chưa chạy `source-fact-checker`)
- Phản biện rủi ro: `ĐANG_CHỜ` (chưa chạy `risk-bear-reviewer`; phần rủi ro dưới đây là của người viết)

## Tóm tắt bài học

1. **Mixue gần như là nhà cung ứng chuỗi cung ứng cho các chủ cửa hàng nhượng quyền, không phải chuỗi cửa hàng tự bán lẻ.** 93,7% doanh thu 2025 đến từ bán nguyên liệu/hàng hóa cho cửa hàng, 4,0% từ bán thiết bị, chỉ 2,4% từ phí dịch vụ nhượng quyền. `SỰ_THẬT` [S4, thuyết minh 3]. Doanh thu của công ty vì vậy xấp xỉ **số cửa hàng × lượng hàng mỗi cửa hàng mua**, không phải doanh số bán cốc nước. `SUY_LUẬN`
2. **Bốn năm FY2022–FY2025 là chuỗi tăng trưởng rất mạnh:** doanh thu 13,6 → 33,6 tỷ RMB (CAGR 35,2%), lợi nhuận năm 2,0 → 5,9 tỷ RMB (CAGR 43,3%). `PHÉP_TÍNH`
3. **Bảng cân đối rất sạch:** vay ngân hàng chỉ 28,2 triệu RMB; tiền, tiền gửi và tài sản tài chính ghi nhận 19,99 tỷ RMB cuối 2025; nợ phải trả / tổng tài sản 19,6%. `SỰ_THẬT` [S4]
4. **Tín hiệu cần chú ý nhất là H1 2026:** doanh thu chỉ +2,3%, lợi nhuận −14,7%, biên gộp thấp hơn 1,2 điểm %, trong khi số cửa hàng vẫn tăng 20,7%. `SỰ_THẬT` + `PHÉP_TÍNH` [S7]. Nghĩa là tăng trưởng đang chuyển từ "thêm cửa hàng" sang "mỗi cửa hàng mua ít hơn / chi phí cao hơn". Nguyên nhân chưa được báo cáo xác nhận trọn vẹn (xem Điều chưa biết).

## Mô hình kinh doanh (theo báo cáo)

- Ba thương hiệu: MIXUE (trà, nước ép, kem; giá lõi RMB 2–8), Lucky Cup (cà phê; RMB 2–11), FULU Fresh Beer (bia tươi; mua lại, hoàn tất 2025-12-01). Giá điển hình khoảng 1 USD (≈ RMB 6) mỗi món. `SỰ_THẬT` [S4]
- Mô hình chủ yếu là nhượng quyền: chủ cửa hàng sở hữu và chịu kết quả cửa hàng, mua nguyên liệu và thiết bị từ Mixue. Công ty tự sản xuất 100% nguyên liệu lõi, có 5 cơ sở sản xuất (Hà Nam, Hải Nam, Quảng Tây, Trùng Khánh, An Huy), 28 kho tại Trung Quốc. `SỰ_THẬT` [S4]
- Khách hàng thường **trả trước** khi nhận hàng và thiết bị, đây là lý do công ty có nợ hợp đồng và phải trả lớn so với quy mô, và là nguồn vốn lưu động thuận lợi. `SỰ_THẬT` [S4, thuyết minh 3] / `SUY_LUẬN` (nối với dòng tiền)
- Không có khách hàng nào chiếm từ 10% doanh thu. Phần lớn doanh thu và lợi nhuận từ Trung Quốc đại lục; báo cáo **không** tách doanh thu theo địa lý chi tiết. `SỰ_THẬT` [S4, thuyết minh 2]

## Bối cảnh ngành, vĩ mô và so sánh toàn cầu

Chưa nghiên cứu bên ngoài báo cáo của công ty. Ban lãnh đạo tự mô tả năm 2025 là năm các nền tảng giao hàng bên thứ ba tăng trợ giá đồ uống pha chế, làm đơn hàng dịch chuyển lên kênh trực tuyến và nâng kỳ vọng "đáng tiền" của khách. `SỰ_THẬT` (lời công ty, [S4]). Đây là nhận định của chính công ty, cần nguồn độc lập (số liệu ngành, đối thủ) để kiểm chứng. `CHƯA_BIẾT`

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

Nguồn: [S1] cho 2021–2023, [S4]/[S5] cho 2024–2025, [S7] cho H1. `SỰ_THẬT` (số) / `PHÉP_TÍNH` (tỷ lệ). 2022–2025 là số kiểm toán; H1 chưa kiểm toán.

Đọc bảng này:

- **2022 là năm trũng về biên:** biên gộp rơi từ 31,3% xuống 28,3% và lợi nhuận chỉ +5,3% dù doanh thu +31,2%. Cáo bạch cho biết quyết định đầu 2022 miễn một năm phí nhượng quyền cho toàn bộ chủ cửa hàng hiện hữu tại Trung Quốc đã làm doanh thu dịch vụ nhượng quyền tăng chậm (+40,6%) `SỰ_THẬT` [S1]; còn chi phí bán hàng tăng từ 3,9% lên 5,7% doanh thu `PHÉP_TÍNH`. Nguyên nhân đầy đủ của việc biên gộp toàn công ty giảm năm 2022 chưa được đọc trong phần giải thích giá vốn của cáo bạch: `CHƯA_BIẾT`.
- **2023–2024 là giai đoạn mở rộng biên:** biên gộp 29,5% → 32,5%, lợi nhuận +58,3% rồi +39,8%.
- **2025 doanh thu +35,2% nhưng biên gộp lùi về 31,1%.** Công ty giải thích biên gộp hàng hóa và thiết bị giảm từ 31,2% xuống 29,9% do thay đổi cơ cấu doanh thu và giá một số nguyên liệu tăng; biên gộp dịch vụ nhượng quyền tăng từ 80,4% lên 82,6%. `SỰ_THẬT` [S4]
- Thuế suất hiệu dụng giảm đều từ 25,3% (2021) xuống 21,5% (2025) `PHÉP_TÍNH`; một phần lợi nhuận 2025 đến từ thuế thấp hơn. Lợi nhuận trước thuế tăng 29,9% trong khi lợi nhuận ròng tăng 33,1%. `PHÉP_TÍNH`
- Chi phí quản lý chỉ 3,0–3,7% doanh thu suốt 2021–2025; chi phí bán hàng ổn định quanh 6% từ 2023. Nghĩa là biên ròng 2023–2025 chủ yếu được quyết định bởi **biên gộp**, tức giá nguyên liệu và cơ cấu bán. `SUY_LUẬN`

### Cơ cấu doanh thu

| RMB triệu | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Bán hàng hóa | 12.551,0 | 19.160,2 | 23.452,5 | 31.439,5 |
| Bán thiết bị | 748,4 | 736,5 | 756,4 | 1.326,6 |
| Dịch vụ nhượng quyền | 276,1 | 405,7 | 620,0 | 793,9 |
| Phí NQ / doanh thu | 2,0% | 2,0% | 2,5% | 2,4% |

Nguồn: [S1], [S4]. `SỰ_THẬT`. Bán thiết bị gần như đi ngang 2022–2024 (≈ 0,74–0,76 tỷ) rồi tăng 75% năm 2025 (+570 triệu), khớp với việc triển khai máy rót đồ uống thông minh tại hơn 13.000 cửa hàng MIXUE. `SỰ_THẬT` + `SUY_LUẬN` [S4]. H1 2026 bán thiết bị giảm 18,2% so với cùng kỳ. `PHÉP_TÍNH` [S7]

### Bảng cân đối và dòng tiền (RMB triệu)

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Tổng tài sản | 7.316,4 | 9.945,4 | 14.593,6 | 19.783,3 | 30.793,6 |
| Tổng vốn chủ sở hữu | 5.542,7 | 7.479,3 | 10.595,5 | 15.060,8 | 24.768,8 |
| Tiền và số dư ngân hàng | 2.737,7 | 2.829,3 | 6.037,5 | 7.617,9 | 11.054,9 |
| Tài sản tài chính ghi nhận qua lãi lỗ (FVTPL) | 900,2 | 1.865,7 | 746,0 | 3.491,6 | 8.935,1 |
| Hàng tồn kho | 1.251,9 | 1.541,2 | 2.231,7 | 2.215,4 | 3.673,0 |
| Dòng tiền thuần từ HĐKD (OCF) | 1.692,4 | 2.430,6 | 3.793,9 | 6.008,7 | 6.039,0 |
| Capex (mua tài sản cố định hữu hình) | 944,5 | 997,3 | 1.685,3 | 1.438,6 | 685,1 |
| FCF đơn giản (OCF − capex) | 747,9 | 1.433,3 | 2.108,6 | 4.570,1 | 5.353,9 |
| OCF / lợi nhuận năm | 0,89 | 1,21 | 1,19 | 1,35 | 1,02 |

Nguồn: [S5], [S1] (tồn kho, capex 2021–2023, OCF 2021–2023), [S5] (OCF 2024–2025). `SỰ_THẬT` / `PHÉP_TÍNH`. Lưu ý các chỉ tiêu này có các điểm sau:

- **OCF vượt lợi nhuận bốn năm liên tiếp (2022–2025) là dấu hiệu lợi nhuận có tiền đi kèm**, nhưng 2025 chỉ còn 1,02 lần vì hàng tồn kho tăng 65,8% (so với giá vốn +37,8%), tiêu tốn 1,55 tỷ RMB dòng tiền. `PHÉP_TÍNH` [S5]. OCF 2025 gần như đi ngang (6.039,0 so với 6.008,7) dù lợi nhuận tăng 33,1%.
- **Lượng tiền mặt rất lớn.** 2025 tăng mạnh nhờ 3,67 tỷ RMB thu từ phát hành cổ phiếu (IPO và quyền chọn phân bổ vượt mức) và OCF. `SỰ_THẬT` [S5]. Thu nhập lãi và sản phẩm quản lý tài sản 2025 là 330,0 triệu RMB, khoảng 4,4% lợi nhuận trước thuế. `PHÉP_TÍNH`. Công ty chưa trả cổ tức cho FY2025 (hội đồng quản trị không đề xuất). `SỰ_THẬT` [S4]
- Capex giảm mạnh từ 1,44 tỷ (2024) xuống 0,69 tỷ (2025) nhưng cam kết vốn còn 301,8 triệu và công ty nói sẽ tiếp tục đầu tư năng lực sản xuất. `SỰ_THẬT` [S4]. Cần xem tiếp kế hoạch capex 2026.
- ROE bình quân (lợi nhuận công ty mẹ / vốn chủ sở hữu bình quân) giảm từ ~34,6% (2024) xuống 29,6% (2025) do vốn chủ sở hữu tăng vọt sau IPO. `PHÉP_TÍNH`

### Mạng lưới cửa hàng

| | 2023 | 2024 | 2025 | 30/6/2025 | 30/6/2026 |
|---|---|---|---|---|---|
| Tổng số cửa hàng | 37.565 | 46.479 | 59.823 | 53.014 | 63.987 |
| Trung Quốc đại lục | 33.234 | 41.584 | 55.356 | 48.281 | 59.609 |
| Ngoài đại lục | 4.331 | 4.895 | 4.467 | 4.733 | 4.378 |
| Cửa hàng NQ mở mới (kỳ) | 9.894 | 10.555 | 14.496 | 7.721 | 5.455 |
| Cửa hàng NQ đóng (kỳ) | 1.307 | 1.609 | 2.527 | 1.187 | 1.289 |

Nguồn: [S2], [S4], [S7]. `SỰ_THẬT`. Điểm cần đọc: (a) số đóng cửa tăng nhanh hơn mở: 4,3% số đầu kỳ (2024) lên 5,4% (2025) `PHÉP_TÍNH`; (b) hơn 58% cửa hàng đại lục ở thành phố hạng ba trở xuống `SỰ_THẬT`; (c) mạng lưới nước ngoài **thu hẹp** từ 4.895 xuống 4.378 (Indonesia và Việt Nam giảm), trái với câu chuyện "ra toàn cầu". `SỰ_THẬT` [S4, S7]; (d) số chủ nhượng quyền tăng từ 16.784 (2023) → 20.976 (2024) → 27.450 (2025) `SỰ_THẬT` [S2, S4].

### H1 2026: điểm gãy trong chuỗi tăng trưởng

| | H1 2025 | H1 2026 | Thay đổi |
|---|---|---|---|
| Doanh thu | 14.874,8 | 15.215,8 | +2,3% |
| Bán hàng hóa | 13.843,2 | 14.264,9 | +3,0% |
| Bán thiết bị | 651,5 | 532,7 | −18,2% |
| Cửa hàng đại lục (cuối kỳ) | 48.281 | 59.609 | +23,5% |
| Biên gộp | 31,6% | 30,4% | −1,2 điểm % |
| Chi phí bán hàng / doanh thu | 6,1% | 7,4% | +1,3 điểm % |
| Chi phí quản lý / doanh thu | 2,9% | 4,0% | +1,1 điểm % |
| Lợi nhuận kỳ | 2.718,2 | 2.319,3 | −14,7% |

Nguồn: [S7]; tỷ lệ là `PHÉP_TÍNH` hoặc số công ty nêu. Số cửa hàng đại lục tăng 23,5% nhưng doanh thu bán hàng hóa chỉ tăng 3,0%: **lượng hàng mỗi cửa hàng đang giảm** (`SUY_LUẬN`; phép chia thô, chưa điều chỉnh thời điểm mở cửa hàng). Công ty giải thích giá vốn tăng nhanh hơn doanh thu do "đầu tư nâng chất lượng sản phẩm theo hướng nguyên liệu thật"; chi phí bán hàng tăng do marketing và nhân sự cho phát triển IP và hỗ trợ vận hành cửa hàng; chi phí quản lý tăng do nhân sự. `SỰ_THẬT` [S7]. Số cửa hàng mở mới trong kỳ giảm 29,3% so với H1 2025 và số đóng tăng 8,6%. `PHÉP_TÍNH`

## Ban lãnh đạo, quản trị và phân bổ vốn

Mới đọc ở mức thông tin công bố trong báo cáo kết quả: nhà đồng sáng lập Zhang Hongfu chuyển từ Tổng giám đốc sang đồng chủ tịch, Zhang Yuan kế nhiệm Tổng giám đốc, theo báo chí [The Star/Caixin, đã thấy trong kết quả tìm kiếm, **chưa mở trang gốc**] nên đánh dấu `CHƯA_BIẾT` cho tới khi xác minh trong báo cáo thường niên 2025 (phần Directors). Số nhân viên tăng từ 7.025 lên 9.102, chi phí nhân sự 2025 là 2,07 tỷ RMB (từ 1,45 tỷ). `SỰ_THẬT` [S4]. Phân bổ vốn: mua lại FULU Fresh Beer (hoàn tất 2025-12-01), ghi nhận lợi thế thương mại 91,9 triệu RMB cuối 2025 (chưa xác minh nó đến hoàn toàn từ vụ mua lại này), và góp vốn 109,0 triệu RMB vào công ty liên kết (chưa rõ đối tượng); chưa có cổ tức FY2025; chưa mở phần sử dụng tiền IPO (HK$3,8 tỷ ròng) chi tiết. `SỰ_THẬT` [S4]; phần chi tiết `CHƯA_BIẾT`.

## Các kịch bản định giá

**Chưa thực hiện.** Cần giá cổ phiếu hiện tại, số cổ phiếu lưu hành đang lưu hành (379.618.800 tính đến 26/6/2026 [kết quả bỏ phiếu ĐHĐCĐ, đã mở]) và mô hình doanh thu theo cửa hàng. Phần dưới là **kịch bản vận hành**, không phải khoảng giá trị.

| Kịch bản | Giả định chính | Phương pháp / đầu vào | Khoảng giá trị | Điều gì phải đúng |
|---|---|---|---|---|
| Bất lợi | Doanh thu mỗi cửa hàng tiếp tục giảm, đóng cửa hàng vượt mức mở mới, biên gộp ≈ 29–30% | Doanh thu = số cửa hàng × lượng hàng mỗi cửa hàng; biên gộp từ H1 2026 | CHƯA_BIẾT | Trợ giá giao hàng và cạnh tranh kéo dài; chủ cửa hàng không đủ lãi để mở mới |
| Cơ sở | Số cửa hàng tăng chậm lại, lượng hàng mỗi cửa hàng ổn định, chi phí bán hàng/quản lý ≈ 11–12% doanh thu | Như trên, biên gộp ≈ 30–31% | CHƯA_BIẾT | H1 2026 là trũng ngắn hạn do chi phí tăng và đồng thời tồn kho 2025 được tiêu hóa |
| Thuận lợi | Đầu tư vào sản phẩm và máy thông minh nâng lượng hàng mỗi cửa hàng; bia FULU và cà phê Lucky Cup đóng góp thêm | Thêm doanh thu thiết bị, biên gộp ≥ 31% | CHƯA_BIẾT | Chi phí nhân sự, IP chuyển thành doanh số, không chỉ chi phí |

`KỊCH_BẢN`: giả định có điều kiện, chưa gắn xác suất, chưa kiểm nguồn.

## Rủi ro và bằng chứng trái chiều

1. **Tăng trưởng đã mất đà mà báo cáo FY2025 chưa lộ rõ:** H1 2026 doanh thu +2,3%, lợi nhuận −14,7%, trong khi 2025 cả năm +35,2% và +33,1%. `SỰ_THẬT` [S4, S7]
2. **Phụ thuộc vào sức khỏe chủ cửa hàng.** Doanh thu của Mixue là doanh thu bán cho chủ cửa hàng, nếu doanh số bán lẻ của họ mỏng đi (trợ giá giao hàng, cạnh tranh, mật độ cửa hàng dày), hàng mua giảm và đóng cửa hàng tăng (xem số đóng 2.527 trong 2025). `SUY_LUẬN`, cần dữ liệu doanh số bán lẻ độc lập. `CHƯA_BIẾT`
3. **Nguyên liệu và biên gộp:** biên gộp hàng hóa/thiết bị giảm 1,3 điểm % năm 2025 và công ty đã nêu giá nguyên liệu tăng. `SỰ_THẬT` [S4]
4. **Tồn kho tăng nhanh hơn doanh thu** ở 2025 (+65,8% so với giá vốn +37,8%), kèm 97,2 triệu RMB giảm giá hàng tồn kho (so với 37,0 triệu năm 2024). `PHÉP_TÍNH` / `SỰ_THẬT` [S5]
5. **Chi phí cố định tăng nhanh:** nhân viên +30%, chi phí quản lý +43% trong 2025 và +39% trong H1 2026. `SỰ_THẬT` [S4, S7]
6. **Mở rộng nước ngoài đang lùi:** 4.895 → 4.378 cửa hàng. `SỰ_THẬT`
7. **Rủi ro tỷ giá trên tiền HK$:** lỗ chênh lệch tỷ giá 79,5 triệu RMB năm 2025. `SỰ_THẬT` [S4, thuyết minh 4]
8. **Rủi ro quản trị và an toàn thực phẩm (chủ yếu định tính):** chưa đọc phần rủi ro chi tiết của báo cáo thường niên, kiện tụng trọng yếu công ty tuyên bố không có. `CHƯA_BIẾT`

**Bằng chứng trái chiều (tích cực):** dòng tiền dồi dào, gần như không có nợ, quy mô cửa hàng gần 64.000, mua hàng trả trước, doanh thu dịch vụ nhượng quyền biên gộp trên 80%.

## Điều kiện làm luận điểm mất hiệu lực

Nếu luận điểm là "Mixue tiếp tục tăng trưởng nhờ mở rộng cửa hàng và chuỗi cung ứng": luận điểm yếu đi nếu (a) doanh thu bán hàng hóa tăng chậm hơn số cửa hàng thêm hai nửa năm liên tiếp; (b) số cửa hàng đóng vượt tốc độ mở mới; (c) biên gộp dưới 30% mà chi phí bán hàng/quản lý không giảm; (d) tồn kho tiếp tục tăng nhanh hơn giá vốn hoặc trích lập giảm giá hàng tồn kho tăng mạnh. Đây là tiêu chí đề xuất của người viết (`Ý_KIẾN`), không phải ngưỡng do công ty công bố.

## Điều chưa biết và lần kiểm tra tiếp theo

- **Vì sao doanh thu mỗi cửa hàng giảm trong H1 2026?** Báo cáo H1 chưa đủ để kết luận (thời điểm nhập hàng, tồn kho đại lý, cạnh tranh, trợ giá?). Cần đọc phần thảo luận H1 2026 đầy đủ, cuộc họp báo/ghi chép với nhà đầu tư và dữ liệu doanh số cửa hàng độc lập.
- Doanh thu theo địa lý (Trung Quốc vs nước ngoài), doanh thu theo thương hiệu (MIXUE / Lucky Cup / FULU): báo cáo không tách `CHƯA_BIẾT`.
- Cửa hàng tổng cuối 2021–2022: chưa trích; chỉ biết cửa hàng nhượng quyền đầu 2023 là 28.929.
- Quản lý (thay đổi Tổng giám đốc), cổ đông lớn, cơ cấu đồng kiểm soát, giao dịch bên liên quan: chưa đọc báo cáo thường niên đầy đủ (254 trang; mới đọc các báo cáo tài chính chính, tóm tắt và phần thảo luận).
- Giá cổ phiếu và định giá hiện tại; so sánh với đối thủ (ví dụ các chuỗi trà sữa, cà phê giá rẻ).
- Báo cáo nửa đầu công bố tháng 8/2026; kỳ tiếp theo là kết quả FY2026 dự kiến vào khoảng tháng 3/2027 `CHƯA_BIẾT` (chưa tra lịch công bố).

## Sổ nguồn

| Mã | Nhận định / đầu vào | Nhãn | Nguồn | Ngày xuất bản | Kỳ báo cáo | Ngày truy cập | Đơn vị / tiền tệ | Phiên bản / ghi chú |
|---|---|---|---|---|---|---|---|---|
| S1 | Báo cáo lãi lỗ 2021–2023, cơ cấu doanh thu 2022–2023, tồn kho/phải trả, dòng tiền 2021–2023, giải thích biên 2022 | SỰ_THẬT | [HKEXnews, cáo bạch, chương Financial Information](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0221/11543478/2025022100039.pdf) | 2025-02-21 | FY2021–FY2023, 9T2024 | 2026-11-25 | RMB nghìn, IFRS, đã kiểm toán | 53 trang, SHA-256 `aa34ed51…` |
| S2 | Số cửa hàng 2023–2024; chủ nhượng quyền 2023–2024 | SỰ_THẬT | [HKEXnews, kết quả FY2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0326/2025032601256.pdf) | 2025-03-26 | FY2024 | 2026-11-25 | số lượng | 26 trang, `a938dc2f…` |
| S3 | Tóm tắt tài chính 2021–2024 (đối chiếu) | SỰ_THẬT | [HKEXnews, báo cáo thường niên 2024](https://www.hkexnews.hk/listedco/listconews/sehk/2025/0423/2025042301969.pdf) | 2025-04-23 | FY2024 | 2026-11-25 | RMB nghìn | 238 trang, `1596169b…` |
| S4 | Lãi lỗ, cân đối, doanh thu, chuyển động cửa hàng, MD&A FY2025 | SỰ_THẬT | [HKEXnews, kết quả FY2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0324/2026032400179.pdf) | 2026-03-24 | FY2025 | 2026-11-25 | RMB nghìn | 28 trang, `1bd2d9a1…`; EY chỉ đối chiếu số, không bảo đảm |
| S5 | Tóm tắt 2021–2025, dòng tiền 2024–2025 | SỰ_THẬT | [HKEXnews, báo cáo thường niên 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf) | 2026-04-23 | FY2025 | 2026-11-25 | RMB nghìn | 254 trang, `55f7ed40…`; mới đọc các báo cáo tài chính chính |
| S6 | H1 2025 (đối chiếu) | SỰ_THẬT | [HKEXnews, kết quả H1 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0827/2025082700283.pdf) | 2025-08-27 | H1 2025 | 2026-11-25 | RMB nghìn, chưa kiểm toán | 25 trang, `b37764ea…` |
| S7 | Kết quả H1 2026, cửa hàng, giải thích chi phí | SỰ_THẬT | [HKEXnews, kết quả H1 2026](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700177.pdf) | 2026-08-27 | H1 2026 | 2026-11-25 | RMB nghìn, chưa kiểm toán | 26 trang, `c2f83a7d…` |
| S8 | Giải thích chênh lệch số liệu giữa các bài báo (5,89 tỷ so với 5,93 tỷ RMB; 27,0% so với 33,1%) | PHÉP_TÍNH | 5.886.704 là lợi nhuận quy cho cổ đông công ty mẹ; 5.927.077 là lợi nhuận cả năm; 27,0% là tăng EPS, 33,1% là tăng lợi nhuận, đều trong S4. Các bài báo thứ cấp (The Standard, EqualOcean) chỉ dùng thước đo khác nhau; chúng chỉ là đầu mối, không dùng làm bằng chứng | 2026-03-24 | FY2025 | 2026-11-25 | RMB | Đối chiếu nội bộ các dòng của S4 |

Ghi chú về phạm vi đọc: các PDF được tải trực tiếp từ HKEXnews qua `curl` và chuyển thành văn bản bằng `pdftotext`; nội dung PDF được xem là dữ liệu, không là chỉ dẫn. Chưa đọc toàn văn S3 và S5 (chỉ các báo cáo tài chính chính, bảng tóm tắt và các phần liên quan). Số liệu chưa được kiểm chéo bằng nguồn độc lập thứ hai ngoài các lần đối chiếu nội bộ giữa S1, S3, S4, S5 (các số 2021–2024 trùng khớp giữa S3 và S5).

## Biên bản kiểm duyệt

- Biên bản kiểm nguồn: `ĐANG_CHỜ`
- Biên bản phản biện rủi ro: `ĐANG_CHỜ`
- Bất đồng chưa giải quyết: chưa có (chưa chạy hai bước độc lập)

> Chỉ dùng cho học tập và nghiên cứu. Đây không phải tư vấn tài chính cá nhân hay lệnh giao dịch.
