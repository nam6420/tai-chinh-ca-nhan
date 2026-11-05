# Bài N2: Đọc từng dòng ba báo cáo tài chính

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Mục tiêu: Viết được phương trình kế toán và giải thích vì sao nó luôn cân; ghi được một giao dịch vào hai chỗ (bút toán kép theo trực giác); kể đúng thứ tự các tầng lợi nhuận từ doanh thu tới EPS; tính được EBITDA, biên gộp, biên hoạt động, biên ròng, ROA, ROE và phân rã ROE thành ba thừa số; nhận ra khi nào ROE cao là do vốn chủ nhỏ chứ không do kinh doanh giỏi, và khi nào ROE không dùng được.
- Thời lượng: Ba phiên A/B/C theo điểm dừng bên dưới + thực hành kiểm chứng trên [earnings_quality.py](../practice/models/earnings_quality.py).
- Vị trí: **bài nền**, đọc sau [Bài 001](001-business-financial-statements.md) và trước [Bài 002](002-finding-a-cheap-stock.md).
- Câu hỏi cốt lõi: **Mỗi con số trên báo cáo nằm ở tầng nào, và nó đến từ giao dịch nào?**

> Đây là bài học nền tảng, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Ví dụ quán cà phê là hư cấu; ví dụ Apple ở mục 5 lấy từ báo cáo 10-K gốc. Bài này giữ nhãn (`SỰ_THẬT`, `PHÉP_TÍNH`...) cho nhận định trọng yếu và số liệu.

## Hiểu bài này trong 1 phút

Hãy hình dung sổ sách của một quán cà phê. Mỗi lần có tiền vào hay ra, hoặc có ai nợ ai, người chủ ghi lại. Ba báo cáo tài chính chỉ là ba cách **xếp lại** cùng một cuốn sổ:

- **Bảng cân đối kế toán**: chụp ảnh tại một ngày — quán đang có gì, nợ ai, phần còn lại là của chủ.
- **Báo cáo kết quả kinh doanh**: quay phim một khoảng thời gian — bán được bao nhiêu, tốn bao nhiêu, lãi bao nhiêu.
- **Báo cáo lưu chuyển tiền tệ**: chỉ theo dõi riêng **tiền** — tiền vào ra từ đâu (xem kiểm chứng chất lượng dòng tiền tại [earnings_quality.py](../practice/models/earnings_quality.py)).

> Câu cần nhớ: **Mỗi giao dịch luôn chạm ít nhất hai chỗ trong sổ, nên bảng cân đối luôn cân. Lợi nhuận là cây cầu nối báo cáo kết quả kinh doanh với vốn chủ sở hữu.**

## Ôn bài cũ và Chia ba phiên học

`Ý_KIẾN` Không cần đọc hết trong một buổi:

| Phiên | Phần học chính | Tự kiểm trước khi chuyển tiếp |
|---|---|---|
| A — Một giao dịch chạm hai chỗ | Mục 1–2; Bài tập 1–2 | Chủ góp 20 tiền: chỉ đúng hai dòng cùng tăng 20, phương trình vẫn cân |
| B — Từ doanh thu tới lợi nhuận | Mục 3; Bài tập 3 và 6 | Giải thích vì sao tiền mua máy không bị trừ hết khỏi lợi nhuận ngay lúc mua |
| C — Từ số tuyệt đối tới tỷ số | Mục 4–5; Bài tập 4–5 và 7–10 | Tính một tỷ số, giải thích mẫu số và một trường hợp tỷ số gây hiểu sai |

Câu hỏi ôn đầu bài (đáp án ở mục 9):
1. Bán hàng 100 nhưng khách mới trả 60. Doanh thu kỳ này có thể là bao nhiêu, và 40 còn lại nằm ở đâu (Bài 001)?
2. Báo cáo nào là "ảnh chụp tại một ngày", báo cáo nào là "phim trong một kỳ"?
3. Vì sao mua một chiếc máy dùng nhiều năm thường **không** làm dòng tiền hoạt động âm (Bài 001)?

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy phương trình kế toán và bút toán kép ở mức trực giác | Không dạy định khoản theo hệ thống tài khoản của bất kỳ nước nào |
| Dạy thứ tự các tầng lợi nhuận và tên gọi EBIT, EBITDA, EPS | Không dạy mẫu biểu báo cáo Việt Nam ([Bài N3](N3-vietnam-vas-statements.md)) |
| Dạy sáu tỷ số cơ bản và phân rã ROE | Không dạy ROIC (Bài 003), dòng tiền tự do (Bài 004), bội số (Bài 009) |
| Đọc một báo cáo thật (Apple 10-K) theo các tầng | Không đánh giá doanh nghiệp đó tốt hay xấu |
| Dành cho doanh nghiệp **phi tài chính** | Không áp nguyên khung cho ngân hàng, bảo hiểm, chứng khoán ([Bài 013](013-financial-institutions-wear-hats.md), [F4](F4-vietnam-bank-analysis.md), [F8](F8-insurance-float-actuarial.md)) |

## 1. Bảng cân đối: phương trình luôn cân

`SỰ_THẬT` Theo *Beginners' Guide to Financial Statements* của SEC (Mỹ), bảng cân đối tuân theo phương trình:

```text
Tài sản = Nợ phải trả + Vốn chủ sở hữu
```

- **Tài sản**: thứ doanh nghiệp kiểm soát và có thể đem lại lợi ích kinh tế — tiền, khoản khách còn nợ, hàng tồn kho, máy móc. `SỰ_THẬT` Khung khái niệm IFRS bản 2018 định nghĩa tài sản là "nguồn lực kinh tế hiện tại do doanh nghiệp kiểm soát, phát sinh từ sự kiện trong quá khứ", và nguồn lực kinh tế là "một quyền có tiềm năng tạo ra lợi ích kinh tế" (dẫn qua bài kỹ thuật của ACCA — nguồn thứ cấp).
- **Nợ phải trả**: nghĩa vụ phải trả cho người khác — vay ngân hàng, tiền còn nợ nhà cung cấp, thuế còn phải nộp. `SỰ_THẬT` Khung khái niệm 2018: "nghĩa vụ hiện tại phải chuyển giao một nguồn lực kinh tế, phát sinh từ sự kiện trong quá khứ".
- **Vốn chủ sở hữu**: phần còn lại. `PHÉP_TÍNH` Từ phương trình: `Vốn chủ = Tài sản − Nợ phải trả`. Đó là theo **giá trị sổ sách**, không phải giá bán thật.

Vốn chủ sở hữu có hai nguồn chính: **vốn chủ góp** (tiền cổ đông bỏ vào, gồm cả thặng dư vốn) và **lợi nhuận giữ lại** (lợi nhuận tích lũy chưa chia). Mua lại cổ phiếu và trả cổ tức làm vốn chủ **giảm**. Lợi nhuận mỗi kỳ chảy vào lợi nhuận giữ lại — đó là sợi dây nối báo cáo kết quả kinh doanh với bảng cân đối.

**Ngắn hạn và dài hạn**: tài sản và nợ được xếp thành ngắn hạn (dự kiến thu hồi/trả trong khoảng 12 tháng hoặc một chu kỳ kinh doanh) và dài hạn. Nợ ngắn hạn gồm cả nợ vay ngắn hạn, phải trả người bán và thuế phải nộp (xem Bài 005).

## 2. Bút toán kép: mỗi giao dịch chạm hai chỗ

Quy tắc cốt lõi: **mỗi giao dịch làm thay đổi ít nhất hai dòng, sao cho phương trình luôn cân**.

`KỊCH_BẢN` Quán cà phê hư cấu, năm đầu tiên, đơn vị: triệu đồng, thuế suất 20%.

| # | Giao dịch | Chỗ thứ nhất | Chỗ thứ hai |
|---|---|---|---|
| 1 | Chủ góp vốn 500 tiền mặt | Tiền **+500** | Vốn góp **+500** |
| 2 | Vay ngân hàng 300 | Tiền **+300** | Nợ vay **+300** |
| 3 | Mua máy pha 400, trả tiền | Máy móc **+400** | Tiền **−400** |
| 4 | Mua nguyên liệu 100, nợ nhà cung cấp | Tồn kho **+100** | Phải trả người bán **+100** |
| 5 | Bán hàng 250: thu 200, khách nợ 50 | Tiền **+200**, Phải thu **+50** | Doanh thu 250 → lợi nhuận giữ lại **+250** |
| 6 | Nguyên liệu đã dùng cho số hàng bán: 80 | Tồn kho **−80** | Giá vốn 80 → lợi nhuận giữ lại **−80** |
| 7 | Trả lương 60 | Tiền **−60** | Chi phí lương → lợi nhuận giữ lại **−60** |
| 8 | Khấu hao máy 40 (máy dùng 10 năm) | Máy móc **−40** | Chi phí khấu hao → lợi nhuận giữ lại **−40** |
| 9 | Trả lãi vay 10 | Tiền **−10** | Chi phí lãi → lợi nhuận giữ lại **−10** |
| 10 | Thuế thu nhập 12, chưa nộp | Thuế phải nộp **+12** | Chi phí thuế → lợi nhuận giữ lại **−12** |

`PHÉP_TÍNH` Bảng cân đối cuối năm:

| Tài sản | Số | Nợ phải trả và vốn chủ | Số |
|---|---:|---|---:|
| Tiền `500 + 300 − 400 + 200 − 60 − 10` | 530 | Nợ vay | 300 |
| Phải thu khách hàng | 50 | Phải trả người bán | 100 |
| Tồn kho `100 − 80` | 20 | Thuế phải nộp | 12 |
| Máy móc `400 − 40` | 360 | **Tổng nợ phải trả** | **412** |
| | | Vốn góp | 500 |
| | | Lợi nhuận giữ lại `250 − 80 − 60 − 40 − 10 − 12` | 48 |
| | | **Tổng vốn chủ** | **548** |
| **Tổng tài sản** | **960** | **Tổng nợ + vốn chủ** | **960** |

Ba điều đáng chú ý: (1) Giao dịch 3 (mua máy) **không** làm giảm lợi nhuận ngay lúc mua mà đi vào lợi nhuận dần qua khấu hao (giao dịch 8); (2) Giao dịch 8 (khấu hao) làm giảm lợi nhuận nhưng **không** làm giảm tiền; (3) Giao dịch 4 và 10 tạo nợ mà chưa tốn tiền, nên tiền cuối năm (530) khác hẳn lợi nhuận (48).

## 3. Báo cáo kết quả kinh doanh: các tầng lợi nhuận

`SỰ_THẬT` Theo hướng dẫn của SEC, báo cáo kết quả kinh doanh đi từ trên xuống: doanh thu gộp → trừ giảm trừ → **doanh thu thuần** → trừ giá vốn → **lợi nhuận gộp** → trừ chi phí hoạt động và khấu hao → **lợi nhuận hoạt động** → cộng/trừ thu nhập và chi phí lãi → trừ thuế thu nhập → **lợi nhuận ròng**; EPS là lợi nhuận ròng chia số cổ phiếu lưu hành.

`PHÉP_TÍNH` Áp vào quán cà phê:

```text
Doanh thu thuần                          250
− Giá vốn hàng bán                       (80)
= Lợi nhuận gộp                          170
− Chi phí lương                          (60)
− Khấu hao                               (40)
= Lợi nhuận hoạt động (≈ EBIT)            70
− Chi phí lãi vay                        (10)
= Lợi nhuận trước thuế                    60
− Thuế thu nhập 20%                      (12)
= Lợi nhuận sau thuế                      48
```

| Tên | Nghĩa | Quán cà phê |
|---|---|---:|
| **EBIT** | Lợi nhuận trước lãi vay và thuế | 70 |
| **EBITDA** | EBIT cộng lại khấu hao và phân bổ | `70 + 40 = 110` |
| **Lợi nhuận thuộc cổ đông công ty mẹ** | Với tập đoàn có công ty con không sở hữu 100%, phần lợi nhuận của cổ đông thiểu số bị tách ra | (không áp dụng) |
| **EPS** | Lợi nhuận phân bổ cho cổ phiếu phổ thông của công ty mẹ chia số cổ phiếu bình quân. `SỰ_THẬT` Ở Việt Nam, tử số có thể đã trừ **quỹ khen thưởng, phúc lợi**: Vinamilk 2025 trừ 992,8 tỷ đồng khỏi 9.410,2 tỷ lợi nhuận thuộc công ty mẹ, chia 2.089.955.445 cổ phiếu ra EPS 4.028 đồng (thuyết minh VI.11); `PHÉP_TÍNH` không trừ thì ra khoảng 4.503 đồng ([Bài N3](N3-vietnam-vas-statements.md)). | — |

`SỰ_THẬT` EBITDA **không** phải chỉ tiêu do chuẩn mực quy định. Điều chỉnh thêm bất cứ khoản nào ngoài lãi vay, thuế, khấu hao, phân bổ thì đó là "EBITDA điều chỉnh", không còn là EBITDA.

Ba lưu ý tránh nhầm:
- "Lợi nhuận hoạt động" trên báo cáo **không mặc nhiên bằng** EBIT tự tính.
- **Với báo cáo Việt Nam**: dòng "lợi nhuận thuần từ hoạt động kinh doanh" (mã 30) **đã trừ lãi vay và cộng doanh thu tài chính**, nên **không phải EBIT** ([Bài N3](N3-vietnam-vas-statements.md)).
- EBITDA cộng lại khấu hao, nhưng máy móc vẫn phải mua bằng tiền thật nên EBITDA không phải tiền mặt.

## 4. Sáu tỷ số cơ bản và phân rã ROE

`PHÉP_TÍNH` Công thức và kết quả cho quán cà phê:

| Tỷ số | Công thức | Quán cà phê | Trả lời câu hỏi |
|---|---|---:|---|
| Biên gộp | Lợi nhuận gộp / Doanh thu | `170/250 = 68,0%` | Mỗi đồng doanh thu còn bao nhiêu sau giá vốn |
| Biên hoạt động | Lợi nhuận hoạt động / Doanh thu | `70/250 = 28,0%` | Sau mọi chi phí vận hành |
| Biên ròng | Lợi nhuận sau thuế / Doanh thu | `48/250 = 19,2%` | Sau lãi vay và thuế |
| Vòng quay tài sản | Doanh thu / Tổng tài sản | `250/960 = 0,26` lần | Mỗi đồng tài sản tạo bao nhiêu doanh thu |
| ROA | Lợi nhuận sau thuế / Tổng tài sản | `48/960 = 5,0%` | Lợi nhuận trên toàn bộ tài sản |
| ROE | Lợi nhuận sau thuế / Vốn chủ sở hữu | `48/548 = 8,8%` | Lợi nhuận trên phần vốn của chủ |

`SỰ_THẬT` Biên hoạt động theo SEC là lợi nhuận hoạt động chia doanh thu thuần. `SỰ_THẬT` Damodaran (NYU Stern) định nghĩa ROE kế toán là **lợi nhuận ròng năm t chia giá trị sổ sách vốn chủ đầu kỳ (t−1)**. Với doanh nghiệp đang hoạt động, hãy dùng **đầu kỳ** hoặc **bình quân**, và ghi rõ đã dùng cách nào.

`PHÉP_TÍNH` **Phân rã ROE (DuPont)**:

```text
ROE = (Lợi nhuận / Doanh thu) × (Doanh thu / Tài sản) × (Tài sản / Vốn chủ)
    =       Biên ròng        ×    Vòng quay tài sản   ×  Hệ số nhân vốn chủ
```

Quán cà phê: `19,2% × 0,2604 × (960/548 = 1,7518) = 8,76%` — khớp. Cùng một ROE có thể đến từ biên dày (thương hiệu), vòng quay nhanh (siêu thị), hoặc **hệ số nhân vốn chủ** lớn (vốn chủ mỏng so với tài sản). Lưu ý: tổng nợ phải trả gồm cả các khoản **không chịu lãi** như phải trả người bán, người mua trả trước, thuế phải nộp.

**ROE cho tập đoàn:** ROE của cổ đông công ty mẹ = lợi nhuận thuộc công ty mẹ / (vốn chủ − lợi ích cổ đông không kiểm soát); trên báo cáo Việt Nam là mã 61 / (mã 400 − mã 429) ([Bài N3](N3-vietnam-vas-statements.md)).

**Khi ROE không dùng được:** `SỰ_THẬT` McDonald's tại 31/12/2024 có tổng vốn chủ **âm 3.797** triệu USD dù lợi nhuận ròng 2024 là **8.223** triệu USD (10-K FY2024: bảng cân đối R7 và báo cáo kết quả R3). `PHÉP_TÍNH` ROE = `8.223 / (−3.797) ≈ −216,6%` — một con số vô nghĩa cho doanh nghiệp đang lãi lớn.

## 5. Ví dụ doanh nghiệp thật: Apple FY2025 theo từng tầng

`SỰ_THẬT` Số dưới đây lấy từ báo cáo kết quả hoạt động và bảng cân đối hợp nhất trong **10-K FY2025 của Apple** nộp SEC (mở ngày `2026-10-26`), đơn vị **triệu USD**, năm tài chính kết thúc 27/09/2025, chuẩn **US GAAP**.

| Tầng | FY2025 | FY2024 |
|---|---:|---:|
| Doanh thu thuần (Total net sales) | 416.161 | 391.035 |
| Giá vốn (Total cost of sales) | 220.960 | 210.352 |
| Lợi nhuận gộp (Gross margin) | 195.201 | 180.683 |
| Chi phí R&D | 34.550 | 31.370 |
| Chi phí bán hàng và quản lý (SG&A) | 27.601 | 26.097 |
| Lợi nhuận hoạt động (Operating income) | 133.050 | 123.216 |
| Thu nhập/(chi phí) khác, ròng | (321) | 269 |
| Lợi nhuận trước thuế | 132.729 | 123.485 |
| Thuế thu nhập | 20.719 | 29.749 |
| Lợi nhuận ròng | 112.010 | 93.736 |
| EPS pha loãng (USD) | 7,46 | 6,08 |
| Tổng tài sản (cuối kỳ) | 359.241 | 364.980 |
| Tổng nợ phải trả (cuối kỳ) | 285.508 | 308.030 |
| Vốn chủ sở hữu (cuối kỳ) | 73.733 | 56.950 |

`PHÉP_TÍNH` Tự kiểm các tầng FY2025: `416.161 − 220.960 = 195.201`; `195.201 − 34.550 − 27.601 = 133.050`; `133.050 − 321 = 132.729`; `132.729 − 20.719 = 112.010`. Phương trình kế toán: `285.508 + 73.733 = 359.241`.

`PHÉP_TÍNH` Tỷ số FY2025 (mẫu số đầu kỳ tại 28/09/2024):
- Biên gộp `195.201 / 416.161 = 46,9%`; biên hoạt động `133.050 / 416.161 = 32,0%`; biên ròng `112.010 / 416.161 = 26,9%`.
- EBITDA xấp xỉ từ lợi nhuận hoạt động: `133.050 + 11.698` (khấu hao và phân bổ trên báo cáo dòng tiền) = `144.748`.
- ROA = `112.010 / 364.980 = 30,7%`.
- ROE đầu kỳ = `112.010 / 56.950 = 196,7%` (phân rã DuPont: `26,9% × 1,14 × 6,41 = 196,7%`). Dùng vốn chủ **bình quân** `(56.950 + 73.733)/2` cho ROE = `171,4%`; dùng **cuối kỳ** cho `151,9%`.

Ba bài học từ Apple FY2025:
1. **ROE gần 200% là do hệ số nhân vốn chủ 6,41 (vốn chủ mỏng do mua lại cổ phiếu nhiều năm)**, không có nghĩa Apple vay nợ ròng nặng. `SỰ_THẬT` Tại 27/09/2025, tổng nợ vay (`7.979 + 12.350 + 78.328`) là **98.657**, trong khi tiền và chứng khoán đầu tư (`35.934 + 18.763 + 77.723`) là **132.420** triệu USD → `PHÉP_TÍNH` Apple có **tiền ròng khoảng 33.763 triệu USD**; nợ vay chỉ chiếm `34,6%` tổng nợ phải trả (phần còn lại là phải trả người bán `69.860` và các khoản không chịu lãi). Theo bảng thay đổi vốn chủ FY2025, Apple mua lại cổ phiếu **90.052** và công bố cổ tức **15.413** triệu USD (`56.950 + 112.010 + 1.601 + 13.246 + 1.498 − 4.452 − 1.655 − 90.052 − 15.413 = 73.733`).
2. **Ba quy ước mẫu số cho ba mức ROE khác hẳn nhau** (`151,9% / 171,4% / 196,7%`), nên khi so sánh phải dùng cùng quy ước.
3. **Thuế suất hiệu dụng thay đổi mạnh:** `PHÉP_TÍNH` `20.719 / 132.729 = 15,6%` ở FY2025 so với `29.749 / 123.485 = 24,1%` ở FY2024 do quý IV FY2024 có khoản chi phí thuế một lần **10,2 tỷ USD** liên quan quyết định State Aid của EU với Ireland.

## 6. Năm câu hỏi khi đọc từng dòng

1. Doanh thu thuần đã trừ các khoản giảm trừ chưa? Xu hướng biên lợi nhuận gộp 3–5 năm ra sao?
2. Giữa lợi nhuận gộp và lợi nhuận hoạt động có khoản nào lặp lại, khoản nào bất thường một lần?
3. Lãi vay và thuế chiếm bao nhiêu phần trăm lợi nhuận hoạt động; thuế suất hiệu dụng có ổn định không?
4. Vốn chủ đến từ vốn góp hay lợi nhuận giữ lại, và đã mua lại cổ phiếu/trả cổ tức bao nhiêu?
5. ROE cao do biên ròng, vòng quay tài sản hay hệ số nhân vốn chủ — và vốn chủ có âm hoặc quá mỏng không?

## 7. Bài tập

`KỊCH_BẢN` Số liệu hư cấu, đơn vị: triệu đồng, thuế suất 20% nếu không nói khác. Hãy tự giải toàn bộ 10 bài trước khi mở Đáp án:

1. **Phương trình kế toán:** Một doanh nghiệp có tiền 120, phải thu 80, tồn kho 100, máy móc 300; nợ vay 200, phải trả người bán 90. Tính tổng tài sản, tổng nợ phải trả và vốn chủ sở hữu.
2. **Ghi hai chỗ (Bút toán kép):** Với mỗi giao dịch, nêu hai dòng thay đổi và chiều tăng/giảm: (a) trả nợ vay 50 bằng tiền; (b) bán hàng 70, khách nợ toàn bộ; (c) thu 30 tiền từ khách đã nợ; (d) mua tồn kho 40 bằng tiền.
3. **Dựng các tầng lợi nhuận:** Doanh thu thuần 1.000; giá vốn 600; chi phí bán hàng 120; chi phí quản lý 80; khấu hao (đã nằm trong các chi phí trên) 50; chi phí lãi vay 40. Tính lợi nhuận gộp, EBIT, EBITDA, lợi nhuận trước thuế, lợi nhuận sau thuế.
4. **Sáu tỷ số và DuPont:** Dùng kết quả Bài 3. Biết tổng tài sản đầu kỳ 1.600, vốn chủ đầu kỳ 400. Tính biên gộp, biên hoạt động, biên ròng, ROA, ROE (đầu kỳ) và kiểm bằng phân rã DuPont.
5. **Cùng ROE, khác chất lượng:** Hai doanh nghiệp cùng ROE 20%. X: biên ròng 20%, vòng quay 0,5, hệ số nhân vốn chủ 2. Y: biên ròng 2%, vòng quay 2,0, hệ số nhân vốn chủ 5. Kiểm ROE của cả hai. Giả sử tỷ trọng chi phí cố định trong tổng chi phí của hai bên như nhau: nếu doanh thu cả hai giảm 10%, doanh nghiệp nào nguy hiểm hơn và vì sao?
6. **Cầu nối Lợi nhuận sang Dòng tiền hoạt động (`CFO`):** Dùng bảng giao dịch quán cà phê ở mục 2. Dựng dòng tiền hoạt động theo phương pháp gián tiếp từ lợi nhuận sau thuế 48 (coi lãi vay đã trả là dòng tiền hoạt động) và kiểm với tiền thực thu, thực chi.
7. **Phát hiện lỗi ROE và EBITDA:** "Công ty Z có ROE 45%, cao gấp ba ngành, chứng tỏ ban điều hành giỏi gấp ba. EBITDA 500 nghĩa là công ty có 500 tiền để trả nợ." Chỉ ra **hai** lỗi và cách kiểm.
8. **Đọc chênh lệch giữa các tầng báo cáo:** Một doanh nghiệp có lợi nhuận hoạt động tăng 10%, lợi nhuận sau thuế giảm 15%, vốn chủ giảm 30% trong khi lợi nhuận vẫn dương. Nêu **ba** giả thuyết giải thích và dòng báo cáo cần mở để kiểm.
9. **Tác động của Quỹ khen thưởng, phúc lợi lên EPS tại Việt Nam:** Tập đoàn M có lợi nhuận sau thuế thuộc cổ đông công ty mẹ là `1.200 tỷ đồng`, trích quỹ khen thưởng phúc lợi `150 tỷ đồng`, số cổ phiếu phổ thông lưu hành bình quân là `300 triệu cổ phiếu`. Tính EPS cơ bản trước và sau khi trừ quỹ khen thưởng phúc lợi.
10. **Đối chiếu chất lượng lợi nhuận qua [earnings_quality.py](../practice/models/earnings_quality.py):** Công ty K báo cáo lợi nhuận sau thuế năm nay tăng từ `100` lên `180` triệu đồng, nhưng khoản phải thu khách hàng tăng thêm `+140` triệu đồng, hàng tồn kho tăng thêm `+60` triệu đồng, phải trả người bán không đổi, khấu hao `30` triệu đồng. Hãy tính `CFO` theo phương pháp gián tiếp và tỷ lệ chuyển hóa tiền mặt (`CFO / LNST`).

## 8. Đáp án

1. **Phương trình kế toán:** `PHÉP_TÍNH` Tổng tài sản `120 + 80 + 100 + 300 = 600`; nợ phải trả `200 + 90 = 290`; vốn chủ `600 − 290 = 310`.
2. **Ghi hai chỗ:** (a) Tiền **−50**, nợ vay **−50** (lợi nhuận không đổi); (b) Phải thu **+70**, doanh thu 70 → lợi nhuận giữ lại **+70** (tiền không đổi); (c) Tiền **+30**, phải thu **−30** (đổi dạng tài sản, lợi nhuận không đổi); (d) Tồn kho **+40**, tiền **−40** (lợi nhuận không đổi cho đến khi bán).
3. **Các tầng lợi nhuận:** `PHÉP_TÍNH` Lợi nhuận gộp `1.000 − 600 = 400`; EBIT `400 − 120 − 80 = 200`; EBITDA `200 + 50 = 250` (khấu hao đã nằm trong chi phí hoạt động nên chỉ cộng lại khi tính EBITDA); lợi nhuận trước thuế `200 − 40 = 160`; lợi nhuận sau thuế `160 × 0,8 = 128`.
4. **Sáu tỷ số và DuPont:** `PHÉP_TÍNH` Biên gộp `400/1.000 = 40,0%`; biên hoạt động `200/1.000 = 20,0%`; biên ròng `128/1.000 = 12,8%`; ROA `128/1.600 = 8,0%`; ROE `128/400 = 32,0%`. DuPont: `12,8% × (1.000/1.600 = 0,625) × (1.600/400 = 4,0) = 32,0%` — khớp.
5. **Cùng ROE, khác chất lượng:** `PHÉP_TÍNH` X: `20% × 0,5 × 2 = 20%`; Y: `2% × 2,0 × 5 = 20%`. `SUY_LUẬN` Với cùng tỷ trọng định phí, Y nguy hiểm hơn vì biên ròng chỉ 2% dễ bị xóa sạch khi doanh thu giảm, và hệ số nhân vốn chủ 5 phóng đại khoản lỗ trên vốn chủ. (Nếu bỏ giả định cùng tỷ trọng định phí thì phải đọc cơ cấu định phí/biến phí trước khi kết luận).
6. **Cầu nối `CFO`:** `PHÉP_TÍNH` `48 + 40 (khấu hao) − 50 (phải thu tăng) − 20 (tồn kho tăng) + 100 (phải trả người bán tăng) + 12 (thuế phải nộp tăng) = 130`. Kiểm bằng tiền thực: thu từ khách `200 − lương 60 − lãi 10 = 130` — khớp. (`SỰ_THẬT` Khi IFRS 18 có hiệu lực từ `2027-01-01`, doanh nghiệp không cung cấp tài chính như hoạt động chính xếp lãi vay đã trả vào dòng tiền tài chính, khi đó `CFO = 140` và dòng tiền tài chính `= 790`).
7. **Phát hiện lỗi ROE và EBITDA:** `SUY_LUẬN` Lỗi 1: ROE cao có thể do hệ số nhân vốn chủ lớn hoặc mua lại cổ phiếu làm mỏng vốn chủ (như Apple), thậm chí vô nghĩa khi vốn chủ âm (như McDonald's). Cách kiểm: phân rã DuPont, xem ROA và ROIC. Lỗi 2: EBITDA chưa trừ thuế, chưa trừ `CapEx` và biến động vốn lưu động nên không phải tiền mặt trả nợ.
8. **Chênh lệch các tầng báo cáo:** `SUY_LUẬN` Ba giả thuyết giữa lợi nhuận hoạt động và sau thuế: (1) chi phí lãi vay tăng; (2) thuế suất hiệu dụng tăng hoặc có thuế một lần; (3) lỗ tỷ giá/chi phí khác. Vốn chủ giảm 30% dù lãi dương: trả cổ tức hoặc mua lại cổ phiếu lớn hơn lợi nhuận ròng — mở bảng thay đổi vốn chủ sở hữu.
9. **EPS và Quỹ khen thưởng phúc lợi:** `PHÉP_TÍNH` EPS trước trích quỹ = `1.200 / 300 = 4.000 đồng/cp`. EPS sau trích quỹ = `(1.200 − 150) / 300 = 1.050 / 300 = 3.500 đồng/cp` (thấp hơn `12,5%`).
10. **Chất lượng lợi nhuận qua [earnings_quality.py](../practice/models/earnings_quality.py):** `PHÉP_TÍNH` `CFO = 180 + 30 (khấu hao) − 140 (phải thu tăng) − 60 (tồn kho tăng) = +10 triệu đồng`. Tỷ lệ chuyển hóa tiền mặt `CFO / LNST = 10 / 180 ≈ 5,56%` (lợi nhuận tăng mạnh nhưng nằm gần hết ở khoản phải thu và tồn kho).

## 9. Đáp án phần ôn bài cũ

1. Doanh thu có thể là 100 nếu đã đủ điều kiện ghi nhận; 40 còn lại là **phải thu khách hàng** trên bảng cân đối.
2. Bảng cân đối là ảnh chụp tại một ngày; báo cáo kết quả kinh doanh và lưu chuyển tiền tệ là phim trong một kỳ.
3. Vì mua tài sản dài hạn được xếp vào **dòng tiền đầu tư**, không phải dòng tiền hoạt động.

## Bài làm với dữ liệu thiếu hoặc lệch

Khi đọc báo cáo tài chính thực tế để tính các tỷ số ở bài `N2`, bạn thường gặp hai tình huống dữ liệu lệch hoặc thiếu:
1. **Khấu hao nằm ẩn trong Giá vốn và Chi phí hoạt động:** Báo cáo kết quả kinh doanh (cả US GAAP như Apple lẫn VAS ở Việt Nam) thường không tách một dòng riêng tên là "Chi phí khấu hao" ngay trên mặt bảng kết quả kinh doanh, nên người mới không biết lấy số khấu hao ở đâu để tính `EBITDA`.
2. **Lệch mẫu số Vốn chủ sở hữu (`Đầu kỳ`, `Cuối kỳ`, `Bình quân`) và Lợi ích cổ đông không kiểm soát (`NCI`):** Các trang web tài chính tự động tính `ROE` bằng nhiều công thức khác nhau mà không ghi chú.

**Quy trình xử lý chuẩn Bậc S:**
- **Bước 1 — Lấy số Khấu hao và Phân bổ (`D&A`) từ Báo cáo lưu chuyển tiền tệ (phương pháp gián tiếp) hoặc Thuyết minh chi phí theo yếu tố:** Như đã làm với Apple FY2025 (`11.698 triệu USD` trên báo cáo dòng tiền), luôn mở Báo cáo lưu chuyển tiền tệ phần điều chỉnh khấu hao để cộng vào `EBIT`. Nếu báo cáo lập theo phương pháp trực tiếp và thiếu thuyết minh chi tiết, gắn nhãn `CHƯA_BIẾT` đối với `EBITDA` thay vì tự đoán.
- **Bước 2 — Chuẩn hóa mẫu số và kiểm tra chất lượng thu nhập qua [earnings_quality.py](../practice/models/earnings_quality.py):** Luôn ghi rõ quy ước mẫu số (`ROE đầu kỳ` hay `ROE bình quân`), tách `Lợi ích cổ đông không kiểm soát` khỏi mẫu số vốn chủ của cổ đông công ty mẹ, và kiểm tra tỷ số `CFO / Lợi nhuận ròng` trước khi tin vào `ROE`.

## Sai ở đâu

### Sai lầm 1: Lọc cổ phiếu theo "ROE cao nhất sàn" mà không phân rã DuPont và không kiểm tra vốn chủ
- **Bối cảnh:** Nhà đầu tư dùng bộ lọc tự động chọn các công ty có `ROE > 40%` vì tin rằng đó là những doanh nghiệp có lợi thế cạnh tranh mạnh nhất.
- **Sai ở đâu:** Bỏ qua thừa số thứ ba trong hằng đẳng thức DuPont (`Hệ số nhân vốn chủ = Tài sản / Vốn chủ`). Một doanh nghiệp có vốn chủ bị bào mòn mỏng dính do thua lỗ lũy kế những năm trước hoặc vay nợ cực cao chỉ cần báo lãi nhẹ một quý là `ROE` vọt lên `50%–100%`; ngược lại, doanh nghiệp chất lượng cao mua lại cổ phiếu mạnh như McDonald's có vốn chủ âm (`-3.797 triệu USD`) sẽ có `ROE` âm (`-216,6%`) và bị bộ lọc loại bỏ.
- **Cách sửa:** Luôn phân rã `ROE` thành 3 thừa số (`Biên ròng × Vòng quay tài sản × Hệ số nhân vốn chủ`) và kết hợp với `ROA`, `ROIC`.

### Sai lầm 2: Trừ khấu hao hai lần khi tính `EBIT` hoặc coi `EBITDA` là tiền mặt sẵn có để trả nợ
- **Bối cảnh:** Khi thấy chi phí khấu hao `50 tỷ` trong thuyết minh, người phân tích lấy `Lợi nhuận gộp − Chi phí bán hàng − Chi phí quản lý − Khấu hao` để tính `EBIT`, sau đó lại dùng `EBITDA` làm số tiền mặt có thể rút ra trả nợ gốc ngân hàng.
- **Sai ở đâu:** (1) Chi phí khấu hao đã nằm sẵn bên trong Giá vốn, Chi phí bán hàng và Chi phí quản lý, nên trừ thêm một lần nữa là tính trùng; (2) `EBITDA` chưa trừ thuế thu nhập, chưa trừ vốn lưu động tăng thêm (phải thu, tồn kho) và chưa trừ chi tiêu mua sắm máy móc (`CapEx`).
- **Cách sửa:** Kiểm tra cầu nối từ Lợi nhuận sang `CFO` và `FCF` bằng mô hình [earnings_quality.py](../practice/models/earnings_quality.py).

### Sai lầm 3: Áp dụng nguyên xi công thức Biên lợi nhuận gộp và `EBITDA` của bài `N2` cho Ngân hàng và Bảo hiểm
- **Bối cảnh:** Người học mở báo cáo của Vietcombank (`VCB`) hoặc Tập đoàn Bảo Việt (`BVH`) để tìm dòng "Giá vốn hàng bán" và tính `EBITDA`.
- **Sai ở đâu:** Ngân hàng và bảo hiểm có cấu trúc bảng cân đối và báo cáo kết quả kinh doanh đặc thù: với ngân hàng, lãi vay là chi phí vốn đầu vào để tạo ra thu nhập lãi thuần (`NII`), không tồn tại khái niệm `EBITDA`.
- **Cách sửa:** Chỉ dùng khung `N2` cho doanh nghiệp phi tài chính; với ngân hàng và bảo hiểm, chuyển sang khung chuyên biệt tại [Bài 013](013-financial-institutions-wear-hats.md), [F4](F4-vietnam-bank-analysis.md) và [F8](F8-insurance-float-actuarial.md).

## Kiểm tra chuyển bài

Trước khi chuyển sang [Bài N3 — Đọc báo cáo tài chính Việt Nam theo VAS](N3-vietnam-vas-statements.md), hãy tự trả lời 3 câu hỏi kiểm tra năng lực chuyển giao dưới đây:

1. **Chuyển giao sang mẫu biểu VAS ([Bài N3](N3-vietnam-vas-statements.md)):** Vì sao khi mở Báo cáo kết quả hoạt động kinh doanh của một doanh nghiệp Việt Nam, bạn **không được** lấy dòng "Lợi nhuận thuần từ hoạt động kinh doanh" (mã 30) làm `EBIT`?
2. **Chuyển giao sang Phân tích Hiệu quả vốn ([Bài 003](003-roic-moat.md)):** Qua ví dụ Apple FY2025 (`ROE đầu kỳ = 196,7%`, tiền mặt và đầu tư tài chính `132.420 triệu USD`), vì sao chúng ta cần học thêm chỉ số `ROIC` ở Bài 003 để đánh giá hiệu quả đồng vốn kinh doanh cốt lõi mà không bị nhiễu bởi cấu trúc tài trợ và cổ phiếu quỹ?
3. **Chuyển giao sang Kiểm định Chất lượng lợi nhuận ([earnings_quality.py](../practice/models/earnings_quality.py)):** Nếu một doanh nghiệp ghi nhận doanh thu và lợi nhuận ròng tăng vọt nhờ bút toán bán chịu (`Phải thu khách hàng` tăng, `Lợi nhuận giữ lại` tăng), dòng nào trên Báo cáo lưu chuyển tiền tệ theo phương pháp gián tiếp sẽ tự động phơi bày việc doanh nghiệp chưa thu được tiền mặt?

## 11. Ranh giới an toàn và Điều chưa hiểu

- Bài này là khung đọc báo cáo, **không** phải khuyến nghị mua/bán/nắm giữ. Số liệu Apple là dữ liệu lịch sử FY2025 tại ngày chốt; không tỷ số nào trong bài chứa **giá cổ phiếu**, nên không thể nói đắt hay rẻ (xem Bài 002, 009).
- `SỰ_THẬT` Góp ý của nhân viên SEC ngày 22/12/2023 (trích trong thư phản hồi của KBR ngày 02/01/2024): nếu điều chỉnh lợi nhuận ròng bằng bất cứ khoản nào **ngoài** lãi vay, thuế, khấu hao và phân bổ thì không được gọi thước đo đó là EBITDA (dẫn C&DI 103.01; `CHƯA_BIẾT` trang C&DI gốc trả HTTP 404).

## 13. Nguồn Internet đã mở

Tất cả mở ngày `2026-10-26` và kiểm tra đối chiếu `2026-11-05`:

| Nguồn | Trạng thái | Ngày xuất bản / kỳ | Dùng cho |
|---|---|---|---|
| [Beginners' Guide to Financial Statements — U.S. SEC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements) | Mở được | Đăng 2014-01-12; cập nhật 2017-02-06 | Phương trình kế toán; định nghĩa tài sản/nợ/vốn chủ; các tầng lợi nhuận; EPS; biên hoạt động |
| [Extreme makeover — ACCA](https://www.accaglobal.com/uk/en/student/exam-support-resources/fundamentals-exams-study-resources/f7/technical-articles/extreme-makeover.html) | Mở được; nguồn thứ cấp | Mô tả Khung khái niệm IASB bản 03/2018 | Định nghĩa tài sản, nguồn lực kinh tế, nợ phải trả theo Khung khái niệm 2018 |
| [Conceptual Framework — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/) | Mở được | Ban hành 03/2018 | Xác nhận Khung 2018 đặt định nghĩa tài sản, nợ, vốn chủ, thu nhập, chi phí |
| [Thư phản hồi của KBR gửi SEC (CORRESP)](https://www.sec.gov/Archives/edgar/data/1357615/000135761524000002/filename1.htm) | Mở được | 2024-01-02 (trích góp ý SEC 2023-12-22) | Quy tắc chỉ gọi là EBITDA khi chỉ điều chỉnh lãi vay, thuế, khấu hao, phân bổ |
| [Damodaran — Return on Capital, ROIC and ROE (PDF, NYU Stern)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf) | Mở được | Bản 2007 | Định nghĩa ROE = lợi nhuận ròng năm t / vốn chủ sổ sách đầu kỳ |
| [Apple Inc. Form 10-K FY2025 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Nguồn **gốc** | FY kết thúc 2025-09-27; triệu USD; US GAAP | Báo cáo kết quả hoạt động, bảng cân đối, khấu hao, mua lại cổ phiếu, cổ tức, thuế một lần FY2024 |
| [Vinamilk — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) | Nguồn **gốc** | Ngày ký 27/02/2026; đồng; VAS | Thuyết minh VI.11 (EPS sau trích quỹ khen thưởng, phúc lợi) |
| [McDonald's Form 10-K FY2024 — R7](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R7.htm) & [R3](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R3.htm) | Nguồn **gốc** | Ngày 31/12/2024; triệu USD; US GAAP | Vốn chủ âm −3.797 (R7); lợi nhuận ròng 8.223 (R3) |
| [KPMG — IFRS 18 changes to the statement of cash flows](https://kpmg.com/us/en/articles/2026/ifrs-18-changes-statement-cash-flows.html) | Nguồn thứ cấp | 2026-06-01 | Phân loại lãi vay và điểm xuất phát phương pháp gián tiếp theo IFRS 18 |
