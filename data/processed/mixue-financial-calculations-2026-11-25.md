# Phép tính tài chính MIXUE Group (2097.HK), FY2021–FY2025 và H1 2026

- Chốt dữ liệu lúc: `2026-11-25 15:00 UTC+7`
- Đầu vào: `data/raw/mixue-financials-2026-11-25.json` (số gốc, đơn vị RMB nghìn). Bản này chỉ chứa số chuyển đổi/tính lại, không thay thế dữ liệu gốc.
- Chuẩn kế toán: IFRS. Tiền tệ: RMB. `bình quân` = (cuối kỳ + đầu kỳ) / 2.
- Tất cả nhãn: `PHÉP_TÍNH`. Làm tròn 1 chữ số thập phân. Tái lập bằng script ở cuối tệp.

## Công thức

| Chỉ số | Công thức |
|---|---|
| Tăng trưởng doanh thu | Doanh thu(t) / Doanh thu(t−1) − 1 |
| Biên lợi nhuận gộp | Lợi nhuận gộp / Doanh thu |
| Biên lợi nhuận ròng | Lợi nhuận năm (gồm cổ đông thiểu số) / Doanh thu |
| Tỷ lệ chi phí bán hàng, quản lý | Chi phí bán hàng và phân phối (hoặc quản lý) / Doanh thu |
| Biên lợi nhuận trước thuế | Lợi nhuận trước thuế / Doanh thu |
| Thuế suất hiệu dụng | Thuế thu nhập / Lợi nhuận trước thuế |
| ROE dùng tổng vốn, tham chiếu lịch sử | Lợi nhuận quy cho chủ sở hữu công ty mẹ / bình quân Tổng vốn chủ sở hữu (gồm cổ đông thiểu số, nên ROE hơi thấp so với định nghĩa chỉ tính vốn công ty mẹ) |
| OCF / Lợi nhuận | Dòng tiền thuần từ hoạt động kinh doanh / Lợi nhuận năm |
| FCF đơn giản | Dòng tiền thuần từ hoạt động kinh doanh − tiền mua tài sản cố định hữu hình (capex PPE). Chưa trừ tiền thuê, mua tài sản vô hình |
| Số ngày tồn kho | bình quân Hàng tồn kho / Giá vốn × 365 |
| Nợ phải trả / Tổng tài sản | Tổng nợ phải trả / Tổng tài sản |
| CAGR | (Cuối / Đầu)^(1/số năm) − 1 |

## Kết quả (FY2021 là năm cơ sở; "4 năm gần đây" = FY2022–FY2025)

| Năm | Doanh thu (RMB triệu) | Tăng DT | Biên gộp | Lợi nhuận năm (RMB triệu) | Biên ròng | CP bán hàng/DT | CP quản lý/DT | Thuế suất hiệu dụng | ROE dùng tổng vốn | OCF/LN | FCF đơn giản (RMB triệu) | Ngày tồn kho | Nợ/TS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 10.351,0 | n/a | 31,3% | 1.911,9 | 18,5% | 3,9% | 3,6% | 25,3% | n/a | 0,89 | 747,9 | n/a | 24,2% |
| 2022 | 13.575,6 | 31,2% | 28,3% | 2.013,1 | 14,8% | 5,7% | 3,7% | 24,3% | 30,7% | 1,21 | 1.433,3 | 52,4 | 24,8% |
| 2023 | 20.302,5 | 49,6% | 29,5% | 3.186,6 | 15,7% | 6,5% | 3,0% | 23,3% | 34,7% | 1,19 | 2.108,6 | 48,1 | 27,4% |
| 2024 | 24.828,9 | 22,3% | 32,5% | 4.454,2 | 17,9% | 6,4% | 3,0% | 23,3% | 34,6% | 1,35 | 4.570,1 | 48,4 | 23,9% |
| 2025 | 33.559,9 | 35,2% | 31,1% | 5.927,1 | 17,7% | 6,1% | 3,2% | 21,5% | 29,6% | 1,02 | 5.353,9 | 46,5 | 19,6% |

- CAGR doanh thu 2022→2025 (3 kỳ tăng trưởng, tức 4 năm dữ liệu 2022–2025): 35,2%. CAGR lợi nhuận năm: 43,3%. CAGR doanh thu 2021→2025: 34,2%.
- Tăng trưởng lợi nhuận năm: 2022 +5,3%; 2023 +58,3%; 2024 +39,8%; 2025 +33,1%.
- 2025: hàng tồn kho +65,8% so với giá vốn +37,8% (3.673,0 / 2.215,4 − 1; 23.108,2 / 16.768,7 − 1).
- 2025: thu nhập lãi tiền gửi (219,1) + thu nhập sản phẩm quản lý tài sản (110,9) = 330,0 triệu RMB = 4,4% lợi nhuận trước thuế (7.550,2).
- Cơ cấu doanh thu 2025: bán hàng hóa 93,7%; bán thiết bị 4,0%; dịch vụ nhượng quyền 2,4%.

## Động lực mạng lưới cửa hàng (cửa hàng nhượng quyền)

| Năm | Đầu kỳ | Mở mới | Đóng | Mua lại (FULU) | Cuối kỳ | Tỷ lệ đóng / số đầu kỳ | Doanh thu / cửa hàng NQ bình quân (RMB triệu) |
|---|---|---|---|---|---|---|---|
| 2023 | 28.929 | 9.894 | 1.307 | 0 | 37.516 | 4,5% | 0,611 |
| 2024 | 37.516 | 10.555 | 1.609 | 0 | 46.462 | 4,3% | 0,591 |
| 2025 | 46.462 | 14.496 | 2.527 | 1.354 | 59.785 | 5,4% | 0,632 |

Lưu ý: "Doanh thu / cửa hàng bình quân" chia **tổng doanh thu tập đoàn** cho bình quân cửa hàng nhượng quyền đầu và cuối năm; nó đo doanh thu của Mixue trên mỗi cửa hàng (chủ yếu là hàng cung ứng), không phải doanh thu bán lẻ của cửa hàng. Đây là xấp xỉ thô vì tử số gồm cả doanh thu thiết bị và dịch vụ, mẫu số bỏ qua thời điểm mở/đóng trong năm và cửa hàng ngoài mạng nhượng quyền.

## H1 2026 so với H1 2025 (chưa kiểm toán)

| Chỉ tiêu | H1 2025 | H1 2026 | Thay đổi |
|---|---|---|---|
| Doanh thu (RMB triệu) | 14.874,8 | 15.215,8 | +2,3% |
| Lợi nhuận gộp (RMB triệu) | 4.706,4 | 4.629,7 | −1,6% |
| Biên gộp | 31,6% | 30,4% | −1,2 điểm % |
| Lợi nhuận kỳ (RMB triệu) | 2.718,2 | 2.319,3 | −14,7% |
| Biên ròng | 18,3% | 15,2% | −3,0 điểm % |
| Bán hàng hóa (RMB triệu) | 13.843,2 | 14.264,9 | +3,0% |
| Bán thiết bị (RMB triệu) | 651,5 | 532,7 | −18,2% |
| Chi phí bán hàng / DT | 6,1% | 7,4% | +1,3 điểm % (số công ty nêu) |
| Chi phí quản lý / DT | 2,9% | 4,0% | +1,1 điểm % (số công ty nêu) |
| Cửa hàng Trung Quốc đại lục (cuối kỳ) | 48.281 | 59.609 | +23,5% |
| Tổng số cửa hàng (cuối kỳ) | 53.014 | 63.987 | +20,7% |
| Cửa hàng NQ mở mới trong kỳ | 7.721 | 5.455 | −29,3% |
| Cửa hàng NQ đóng trong kỳ | 1.187 | 1.289 | +8,6% |

## Tái lập

Script: các phép chia ở bảng trên chỉ dùng số trong `data/raw/mixue-financials-2026-11-25.json`; chạy bằng `python3 -I` với các mảng `income_statement`, `balance_sheet`, `cash_flow`, `stores`, `interim`. Kiểm tra chéo đã chạy: lợi nhuận gộp = doanh thu − giá vốn; lợi nhuận năm = lợi nhuận trước thuế − thuế; tổng ba dòng doanh thu = doanh thu (2022–2025 và H1 2025–H1 2026); tài sản = nợ + vốn chủ sở hữu (2021–2025). Tất cả đều khớp.

## Bổ sung v4: dòng tiền H1 2026, tỷ lệ chi phí theo nửa năm, sở hữu

| Chỉ tiêu | Công thức | H1 2025 | H1 2026 |
|---|---|---|---|
| OCF (RMB triệu) | báo cáo lưu chuyển tiền tệ [S13] | 3.275,4 | 2.049,8 (−37,4%) |
| OCF / lợi nhuận kỳ | OCF / lợi nhuận | 1,20 (3.275,4 / 2.718,2) | 0,88 (2.049,8 / 2.319,3) |
| Chi phí bán hàng + quản lý / doanh thu | (bán hàng + quản lý) / doanh thu | 9,1% | 11,4% |

- Tỷ lệ chi phí H2 2025: (1.123,2 + 643,9) / 18.685,1 = 9,5% (H2 = cả năm trừ H1: bán hàng 2.036,9 − 913,7; quản lý 1.081,5 − 437,7; doanh thu 33.559,9 − 14.874,8).
- Phân rã lợi nhuận trước thuế H1 2026 (−492,6 triệu): hiệu ứng biên gộp (30,43% − 31,64%) × 15.215,8 = −184,6; hiệu ứng doanh thu (15.215,8 − 14.874,8) × 31,64% = +107,9; chi phí bán hàng + quản lý +381,7; hiệu ứng tỷ lệ chi phí ≈ −350,7.
- Sở hữu hai nhà sáng lập: mỗi người 153.997.224 / 379.618.800 = 40,57%; hai người 307.994.448 / 379.618.800 = 81,13%; gồm hai nền tảng nhân viên (2 × 1.619.987): 81,99%.
- Cổ tức đặc biệt tới hai nhà sáng lập (trực tiếp): 307.994.448 × 2,65 = 816,2 triệu RMB (81,1% của 1.006,0), trước thuế.
- Quyền thưởng: 12.023.300 / 379.618.800 = 3,167%.
- Mạng lưới nước ngoài theo nửa năm: 4.895 → 4.733 (−3,3%) → 4.467 (−5,6%) → 4.378 (−2,0%).


## Bổ sung v5

- ROE dùng riêng vốn và lợi nhuận của cổ đông công ty mẹ. 2024: 4.436,504 ÷ ((10.506,993 + 14.955,519) / 2) = **34,8%**. 2025: 5.886,704 ÷ ((14.955,519 + 24.449,037) / 2) = **29,9%**. [Báo cáo 2024](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0423/2025042301969.pdf) · [Báo cáo 2025](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf)
- H1 2026: 102,3 triệu là mức tăng chi phí nhân sự toàn tập đoàn. 102,3 / 381,7 ≈ 27% là tỷ số giữa hai khoản khác phạm vi. Tách mức tăng nhân sự theo chức năng cần thêm dữ liệu.
- Số cổ phiếu phát hành cuối tháng 10 là 379.618.800. Tỷ lệ giảm của phần sở hữu hiện hữu nếu phát hành toàn bộ 12.023.300 cổ phiếu thưởng = 12.023.300 / (379.618.800 + 12.023.300) ≈ **3,07%**. [Báo cáo biến động vốn](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/1105/2026110501398.pdf) · [Công bố thưởng](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0928/2026092801979.pdf)
- FY2025, số quán nhượng quyền mở ròng từ hoạt động = 14.496 − 2.527 = **11.969**. Thêm 1.354 quán FULU mua lại cho tăng **13.323** quán nhượng quyền. Tổng số quán tăng **13.344**, gồm thêm 21 quán tự vận hành.
