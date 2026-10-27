# Bài N2: Đọc từng dòng ba báo cáo tài chính

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 18:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Mục tiêu: Viết được phương trình kế toán và giải thích vì sao nó luôn cân; ghi được một giao dịch vào hai chỗ (bút toán kép theo trực giác); kể đúng thứ tự các tầng lợi nhuận từ doanh thu tới EPS; tính được EBITDA, biên gộp, biên hoạt động, biên ròng, ROA, ROE và phân rã ROE thành ba thừa số; nhận ra khi nào ROE cao là do vốn chủ nhỏ chứ không do kinh doanh giỏi, và khi nào ROE không dùng được.
- Thời lượng: Ba phiên A/B/C theo điểm dừng bên dưới; chưa đo thời gian học thực tế.
- Vị trí: **bài nền**, đọc sau [Bài 001](001-business-financial-statements.md) và trước [Bài 002](002-finding-a-cheap-stock.md) (theo thứ tự trong `learning/README.md`). Nếu đã học tới Bài 009, đọc bài này như bài ôn để lấp các định nghĩa mà các bài sau dùng nhưng chưa dạy (EBITDA, ROE, bút toán).
- Câu hỏi cốt lõi: **Mỗi con số trên báo cáo nằm ở tầng nào, và nó đến từ giao dịch nào?**

> Đây là bài học nền tảng, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Ví dụ quán cà phê là hư cấu; ví dụ Apple ở mục 5 lấy từ báo cáo 10-K gốc. Bài này giữ nhãn (`SỰ_THẬT`, `PHÉP_TÍNH`...) cho nhận định trọng yếu và số liệu; phần giảng giải thông thường không gắn nhãn.

## Hiểu bài này trong 1 phút

Hãy hình dung sổ sách của một quán cà phê. Mỗi lần có tiền vào hay ra, hoặc có ai nợ ai, người chủ ghi lại. Ba báo cáo tài chính chỉ là ba cách **xếp lại** cùng một cuốn sổ:

- **Bảng cân đối kế toán**: chụp ảnh tại một ngày — quán đang có gì, nợ ai, phần còn lại là của chủ.
- **Báo cáo kết quả kinh doanh**: quay phim một khoảng thời gian — bán được bao nhiêu, tốn bao nhiêu, lãi bao nhiêu.
- **Báo cáo lưu chuyển tiền tệ**: chỉ theo dõi riêng **tiền** — tiền vào ra từ đâu.

Bài 001 dạy ba báo cáo nối với nhau. Bài này dạy **từng dòng** trong mỗi báo cáo, để các bài sau (ROIC, nợ, bội số) không còn dùng thuật ngữ bạn chưa được định nghĩa.

> Câu cần nhớ: **Mỗi giao dịch luôn chạm ít nhất hai chỗ trong sổ, nên bảng cân đối luôn cân. Lợi nhuận là cây cầu nối báo cáo kết quả kinh doanh với vốn chủ sở hữu.**

## Ôn bài cũ (5 phút)

### Cách chia bài thành ba phiên

`Ý_KIẾN` Không cần đọc hết trong một buổi. Thời lượng ở đầu bài chỉ là dự kiến, chưa đo với người học.

| Phiên | Phần học chính | Tự kiểm trước khi chuyển tiếp |
|---|---|---|
| A — Một giao dịch chạm hai chỗ | Mục 1–2; Bài tập 1–2 | Chủ góp 20 tiền: chỉ đúng hai dòng cùng tăng 20, phương trình vẫn cân |
| B — Từ doanh thu tới lợi nhuận | Mục 3; Bài tập 3 và 6 | Giải thích vì sao tiền mua máy không bị trừ hết khỏi lợi nhuận ngay lúc mua |
| C — Từ số tuyệt đối tới tỷ số | Mục 4–5; Bài tập 4–5 và 7–8 | Tính một tỷ số, giải thích mẫu số và một trường hợp tỷ số gây hiểu sai |

Đáp án kiểm nhanh: A — tiền và vốn góp; B — tài sản dùng nhiều kỳ, chi phí được phân bổ qua khấu hao; C — dùng số trong bài tập và đối chiếu lời giải. Phải tự làm trước khi xem. Phân rã ROE và phần EBITDA theo SEC là phần đào sâu, có thể quay lại sau khi vững A/B.

Trả lời bằng lời của bạn, không nhìn tài liệu. Đáp án ở mục 9.

1. Bán hàng 100 nhưng khách mới trả 60. Doanh thu kỳ này có thể là bao nhiêu, và 40 còn lại nằm ở đâu (Bài 001)?
2. Báo cáo nào là "ảnh chụp tại một ngày", báo cáo nào là "phim trong một kỳ"?
3. Vì sao mua một chiếc máy dùng nhiều năm thường **không** làm dòng tiền hoạt động âm (Bài 001, mục "Lỗi thường gặp")?

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy phương trình kế toán và bút toán kép ở mức trực giác | Không dạy định khoản theo hệ thống tài khoản của bất kỳ nước nào |
| Dạy thứ tự các tầng lợi nhuận và tên gọi EBIT, EBITDA, EPS | Không dạy mẫu biểu báo cáo Việt Nam (Bài N3) |
| Dạy sáu tỷ số cơ bản và phân rã ROE | Không dạy ROIC (Bài 003), dòng tiền tự do (Bài 004), bội số (Bài 009) |
| Đọc một báo cáo thật (Apple 10-K) theo các tầng | Không đánh giá doanh nghiệp đó tốt hay xấu |
| Dành cho doanh nghiệp **phi tài chính** | Không áp nguyên khung cho ngân hàng, bảo hiểm, chứng khoán: với ngân hàng, lãi vay là giá vốn, "biên gộp" và EBITDA không dùng được, và hệ số tài sản/vốn chủ 10 lần trở lên là bình thường (Bài 013) |

## 1. Bảng cân đối: phương trình luôn cân

`SỰ_THẬT` Theo *Beginners' Guide to Financial Statements* của SEC (Mỹ), bảng cân đối tuân theo phương trình:

```text
Tài sản = Nợ phải trả + Vốn chủ sở hữu
```

- **Tài sản**: thứ doanh nghiệp kiểm soát và có thể đem lại lợi ích kinh tế — tiền, khoản khách còn nợ, hàng tồn kho, máy móc. `SỰ_THẬT` Khung khái niệm IFRS bản 2018 định nghĩa tài sản là "nguồn lực kinh tế hiện tại do doanh nghiệp kiểm soát, phát sinh từ sự kiện trong quá khứ", và nguồn lực kinh tế là "một quyền có tiềm năng tạo ra lợi ích kinh tế" (dẫn qua bài kỹ thuật của ACCA — nguồn thứ cấp).
- **Nợ phải trả**: nghĩa vụ phải trả cho người khác — vay ngân hàng, tiền còn nợ nhà cung cấp, thuế còn phải nộp. `SỰ_THẬT` Khung khái niệm 2018: "nghĩa vụ hiện tại phải chuyển giao một nguồn lực kinh tế, phát sinh từ sự kiện trong quá khứ" (cùng nguồn).
- **Vốn chủ sở hữu**: phần còn lại. `PHÉP_TÍNH` Từ phương trình: `Vốn chủ = Tài sản − Nợ phải trả`. SEC diễn đạt là phần sẽ còn lại nếu bán hết tài sản và trả hết nợ — với lưu ý của bài này: đó là theo **giá trị sổ sách**, không phải giá bán thật.

Vốn chủ sở hữu có hai nguồn chính: **vốn chủ góp** (tiền cổ đông bỏ vào, gồm cả thặng dư vốn) và **lợi nhuận giữ lại** (lợi nhuận tích lũy chưa chia). Mua lại cổ phiếu (giữ làm cổ phiếu quỹ hoặc hủy) và trả cổ tức làm vốn chủ **giảm**. Lợi nhuận mỗi kỳ chảy vào lợi nhuận giữ lại — đó là sợi dây nối báo cáo kết quả kinh doanh với bảng cân đối.

**Ngắn hạn và dài hạn**: tài sản và nợ thường được xếp thành ngắn hạn (dự kiến thu hồi/trả trong khoảng 12 tháng hoặc một chu kỳ kinh doanh) và dài hạn. Đây là lý do Bài 005 tách "nợ vay ngắn hạn" khỏi "nợ ngắn hạn" — nợ ngắn hạn còn gồm cả phải trả người bán và thuế phải nộp.

## 2. Bút toán kép: mỗi giao dịch chạm hai chỗ

Không cần học tên tài khoản. Chỉ cần một quy tắc: **mỗi giao dịch làm thay đổi ít nhất hai dòng, sao cho phương trình vẫn cân**.

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

Ba điều đáng chú ý:

1. Giao dịch 3 (mua máy) **không** làm giảm lợi nhuận: tiền biến thành máy. Chi phí của máy chỉ đi vào lợi nhuận dần qua khấu hao (giao dịch 8).
2. Giao dịch 8 (khấu hao) làm giảm lợi nhuận nhưng **không** làm giảm tiền — đúng "chi phí phi tiền mặt" của Bài 001.
3. Giao dịch 4 và 10 tạo nợ mà chưa tốn tiền. Đó là lý do tiền cuối năm (530) khác hẳn lợi nhuận (48).

## 3. Báo cáo kết quả kinh doanh: các tầng lợi nhuận

`SỰ_THẬT` Theo hướng dẫn của SEC, báo cáo kết quả kinh doanh đi từ trên xuống: doanh thu gộp → trừ hàng bán bị trả lại và giảm giá → **doanh thu thuần** → trừ giá vốn → **lợi nhuận gộp** → trừ chi phí hoạt động và khấu hao → **lợi nhuận hoạt động** → cộng/trừ thu nhập và chi phí lãi → trừ thuế thu nhập → **lợi nhuận ròng**; EPS là lợi nhuận ròng chia số cổ phiếu lưu hành. SEC cũng lưu ý các dòng này có thể được trình bày theo thứ tự khác nhau giữa các doanh nghiệp.

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

Bốn tên gọi bạn sẽ gặp mãi ở các bài sau:

| Tên | Nghĩa | Quán cà phê |
|---|---|---:|
| **EBIT** | Lợi nhuận trước lãi vay và thuế | 70 |
| **EBITDA** | EBIT cộng lại khấu hao và phân bổ | `70 + 40 = 110` |
| **Lợi nhuận thuộc cổ đông công ty mẹ** | Với tập đoàn có công ty con không sở hữu 100%, phần lợi nhuận của cổ đông thiểu số ở công ty con bị tách ra | (không áp dụng) |
| **EPS** | Lợi nhuận phân bổ cho cổ phiếu phổ thông của công ty mẹ chia số cổ phiếu bình quân; có bản cơ bản và pha loãng. `SỰ_THẬT` Ở Việt Nam, tử số có thể đã trừ phần trích **quỹ khen thưởng, phúc lợi**: Vinamilk 2025 trừ 992,8 tỷ đồng khỏi 9.410,2 tỷ lợi nhuận thuộc công ty mẹ, chia 2.089.955.445 cổ phiếu ra EPS 4.028 đồng (thuyết minh VI.11); `PHÉP_TÍNH` không trừ thì ra khoảng 4.503. `SUY_LUẬN` Mức trích khác nhau giữa doanh nghiệp — đọc thuyết minh EPS (Bài N3) | — |

`SỰ_THẬT` EBITDA **không** phải chỉ tiêu do chuẩn mực quy định. Điều chỉnh thêm bất cứ khoản nào ngoài lãi vay, thuế, khấu hao, phân bổ thì đó là "EBITDA điều chỉnh", không còn là EBITDA (nguồn ở hộp "Đọc thêm" cuối bài). Bài 007 và Bài 009 sẽ quay lại chuyện này.

Ba lưu ý tránh nhầm:

- "Lợi nhuận hoạt động" trên báo cáo của doanh nghiệp **không mặc nhiên bằng** EBIT bạn tự tính: tùy doanh nghiệp và chuẩn mực, thu nhập/chi phí khác có thể nằm trên hoặc dưới dòng này.
- **Với báo cáo Việt Nam**: dòng "lợi nhuận thuần từ hoạt động kinh doanh" (mã 30) **đã trừ lãi vay và cộng doanh thu tài chính**, nên **không phải EBIT**. EBIT xấp xỉ = lợi nhuận trước thuế + chi phí lãi vay — xem [Bài N3](N3-vietnam-vas-statements.md), mục 3.
- EBITDA cộng lại khấu hao, nhưng máy vẫn phải mua bằng tiền thật (giao dịch 3). Vì vậy EBITDA không phải tiền — Bài 005 sẽ có bài tập bắt bạn tìm đúng lỗi này.

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

`SỰ_THẬT` Biên hoạt động theo SEC là lợi nhuận hoạt động chia doanh thu thuần. `SỰ_THẬT` Damodaran (NYU Stern) định nghĩa ROE kế toán là **lợi nhuận ròng năm t chia giá trị sổ sách vốn chủ đầu kỳ (t−1)**, vì lợi nhuận năm nay được tạo ra từ vốn có lúc đầu năm — cùng quy ước "đầu kỳ" như ROIC ở Bài 003.

**Quy ước mẫu số.** Quán cà phê mới mở có vốn chủ đầu năm bằng 0, nên bảng trên buộc phải dùng số cuối năm. Với doanh nghiệp đang hoạt động, hãy dùng **đầu kỳ** (theo Damodaran) hoặc **bình quân**, và ghi rõ đã dùng cách nào. ROE "cuối kỳ", "đầu kỳ" và "bình quân" có thể khác nhau rất xa (xem mục 5).

`PHÉP_TÍNH` **Phân rã ROE (DuPont)** — một hằng đẳng thức, nhân ba phân số thì triệt tiêu mẫu và tử ở giữa:

```text
ROE = (Lợi nhuận / Doanh thu) × (Doanh thu / Tài sản) × (Tài sản / Vốn chủ)
    =       Biên ròng        ×    Vòng quay tài sản   ×  Hệ số nhân vốn chủ
```

Quán cà phê: `19,2% × 0,2604 × (960/548 = 1,7518) = 8,76%` — khớp (nhân bằng số đã làm tròn `0,26 × 1,75` sẽ ra 8,74%; chênh do làm tròn).

Giá trị của phân rã này: **cùng một ROE có thể đến từ ba nguồn rất khác nhau**. ROE cao vì biên dày (thương hiệu) khác với ROE cao vì quay vòng nhanh (siêu thị), và khác hẳn ROE cao vì **hệ số nhân vốn chủ** lớn — tức vốn chủ mỏng so với tài sản. Lưu ý: thừa số này chia cho **toàn bộ nợ phải trả**, gồm cả khoản **không chịu lãi** như phải trả người bán, người mua trả trước, thuế phải nộp. Hệ số lớn **chưa chắc** là vay nhiều — muốn biết nợ vay thật, mở dòng nợ vay và tiền (Bài 005). Thừa số thứ ba cũng là lý do Bài 003 dạy ROIC: ROIC loại ảnh hưởng của cách tài trợ, còn ROE thì không.

**ROE cho tập đoàn.** Nếu tập đoàn có công ty con không sở hữu 100%, vốn chủ trên báo cáo hợp nhất **đã gồm** lợi ích cổ đông không kiểm soát. ROE của cổ đông công ty mẹ = lợi nhuận thuộc công ty mẹ / (vốn chủ − lợi ích cổ đông không kiểm soát); trên báo cáo Việt Nam là mã 61 / (mã 400 − mã 429) (Bài N3).

**Khi ROE không dùng được.** `SỰ_THẬT` McDonald's tại 31/12/2024 có tổng vốn chủ **âm 3.797** triệu USD dù lợi nhuận ròng 2024 là **8.223** triệu USD (10-K FY2024: bảng cân đối R7 và báo cáo kết quả R3, xem mục 13). `PHÉP_TÍNH` ROE = `8.223 / (−3.797) ≈ −216,6%` — một con số vô nghĩa cho doanh nghiệp đang lãi lớn. ROE cũng mất nghĩa khi vốn chủ rất nhỏ hoặc doanh nghiệp lỗ. Lọc cổ phiếu theo "ROE cao nhất" sẽ kéo đúng những trường hợp này lên đầu.

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

`PHÉP_TÍNH` Tự kiểm các tầng FY2025: `416.161 − 220.960 = 195.201`; `195.201 − 34.550 − 27.601 = 133.050`; `133.050 − 321 = 132.729`; `132.729 − 20.719 = 112.010`. Phương trình kế toán: `285.508 + 73.733 = 359.241`. Tất cả khớp.

`PHÉP_TÍNH` Tỷ số FY2025 (mẫu số đầu kỳ = số tại 28/09/2024):

- Biên gộp `195.201 / 416.161 = 46,9%`; biên hoạt động `133.050 / 416.161 = 32,0%`; biên ròng `112.010 / 416.161 = 26,9%`.
- EBITDA **xấp xỉ**, tính từ lợi nhuận hoạt động (không phải EBIT tự dựng): `133.050 + 11.698` (khấu hao và phân bổ trên báo cáo dòng tiền) = `144.748`.
- ROA = `112.010 / 364.980 = 30,7%`.
- ROE = `112.010 / 56.950 = 196,7%`. Phân rã: biên ròng `26,9%` × vòng quay `416.161 / 364.980 = 1,14` × hệ số nhân vốn chủ `364.980 / 56.950 = 6,41` = `196,7%` (nhân số chưa làm tròn).
- Nếu dùng vốn chủ **bình quân** `(56.950 + 73.733)/2`: ROE = `171,4%`; dùng **cuối kỳ**: `151,9%`.

Bài học từ ví dụ này:

1. **ROE gần 200% không có nghĩa Apple kinh doanh "giỏi gấp 6 lần ROA"**. Hệ số nhân vốn chủ 6,41 cho thấy vốn chủ rất mỏng so với tài sản — nhưng **không** có nghĩa Apple vay nặng. `SỰ_THẬT` Tại 27/09/2025, nợ vay (thương phiếu 7.979 + nợ dài hạn đến hạn 12.350 + nợ dài hạn 78.328) là **98.657**, trong khi tiền và chứng khoán đầu tư (35.934 + 18.763 + 77.723) là **132.420** (triệu USD, 10-K). `PHÉP_TÍNH` Apple có **tiền ròng khoảng 33.763**; nợ vay chỉ chiếm `98.657 / 285.508 = 34,6%` tổng nợ phải trả — phần còn lại là phải trả người bán (69.860) và các khoản không chịu lãi khác.
   `SỰ_THẬT` Vì sao vốn chủ mỏng: theo **bảng thay đổi vốn chủ** FY2025, Apple mua lại cổ phiếu **90.052** và công bố cổ tức **15.413** (tiền thực chi trên báo cáo lưu chuyển tiền tệ là 90.711 và 15.421; `SUY_LUẬN` chênh lệch nhiều khả năng do thời điểm ghi nhận khác thời điểm chi tiền). `PHÉP_TÍNH` Cộng lại **105.465**, nhỏ hơn lợi nhuận ròng 112.010 (chênh 6.545). `SỰ_THẬT` Các khoản khác trong bảng thay đổi vốn chủ gồm thu nhập toàn diện khác 1.601, chi phí thù lao bằng cổ phiếu 13.246, phát hành cổ phiếu cho nhân viên 1.498, và cổ phiếu giữ lại để nộp thuế thay nhân viên (4.452 và 1.655). `PHÉP_TÍNH` `56.950 + 112.010 + 1.601 + 13.246 + 1.498 − 4.452 − 1.655 − 90.052 − 15.413 = 73.733`: vốn chủ FY2025 **tăng** 16.783. Tuy vậy, khoản lỗ lũy kế vẫn còn **−14.264** cuối kỳ (đầu kỳ −19.154). `SUY_LUẬN` Vốn chủ mỏng là kết quả **lũy kế nhiều năm** trả lại tiền cho cổ đông (mua lại cổ phiếu được ghi giảm vào lợi nhuận giữ lại), không phải do Apple thua lỗ; `CHƯA_BIẾT` số lũy kế các năm trước — phải mở thêm 10-K cũ. Muốn nhìn chất lượng kinh doanh, xem ROIC (Bài 003) và biên, không xem ROE đơn lẻ.
2. **Ba quy ước mẫu số cho ba con số ROE** (151,9% / 171,4% / 196,7%). Khi so sánh, phải dùng cùng quy ước.
3. **Thuế suất hiệu dụng thay đổi mạnh**: `PHÉP_TÍNH` `20.719 / 132.729 = 15,6%` ở FY2025 so với `29.749 / 123.485 = 24,1%` ở FY2024. `SỰ_THẬT` 10-K ghi quý IV FY2024 có một khoản chi phí thuế một lần **10,2 tỷ USD** (ròng) liên quan quyết định State Aid của EU với Ireland (Bài 004 sẽ quay lại). Vì vậy lợi nhuận ròng FY2024 (93.736) thấp hơn FY2023 (96.995) dù lợi nhuận hoạt động cao hơn (123.216 so với 114.301). Tầng "trước thuế" và "sau thuế" kể hai câu chuyện khác nhau.

## 6. Năm câu hỏi khi đọc từng dòng

1. Doanh thu thuần đã trừ giảm trừ (trả lại, chiết khấu) chưa? Lợi nhuận gộp chiếm bao nhiêu phần trăm doanh thu, xu hướng 3–5 năm?
2. Giữa lợi nhuận gộp và lợi nhuận hoạt động có những khoản nào; khoản nào lặp lại, khoản nào một lần?
3. Giữa lợi nhuận hoạt động và lợi nhuận sau thuế, lãi vay và thuế chiếm bao nhiêu; thuế suất hiệu dụng có ổn định không?
4. Bảng cân đối có cân không, vốn chủ đến từ vốn góp hay lợi nhuận giữ lại, và đã bị trả lại cho cổ đông bao nhiêu?
5. ROE cao do biên, do vòng quay hay do hệ số nhân vốn chủ — và vốn chủ có âm hoặc quá nhỏ không?

## 7. Bài tập (8 câu, 40 phút)

`KỊCH_BẢN` Số liệu hư cấu, đơn vị: triệu đồng, thuế suất 20% nếu không nói khác.

### Bài 1 (nhớ lại) — phương trình kế toán
Một doanh nghiệp có tiền 120, phải thu 80, tồn kho 100, máy móc 300; nợ vay 200, phải trả người bán 90. Tính tổng tài sản, tổng nợ phải trả và vốn chủ sở hữu.

### Bài 2 (nhớ lại) — ghi hai chỗ
Với mỗi giao dịch, nêu hai dòng thay đổi và chiều tăng/giảm: (a) trả nợ vay 50 bằng tiền; (b) bán hàng 70, khách nợ toàn bộ; (c) thu 30 tiền từ khách đã nợ; (d) mua tồn kho 40 bằng tiền.

### Bài 3 (vận dụng) — dựng các tầng lợi nhuận
Doanh thu thuần 1.000; giá vốn 600; chi phí bán hàng 120; chi phí quản lý 80; khấu hao (nằm trong các chi phí trên) 50; chi phí lãi vay 40. Tính lợi nhuận gộp, EBIT, EBITDA, lợi nhuận trước thuế, lợi nhuận sau thuế.

### Bài 4 (vận dụng) — sáu tỷ số
Dùng kết quả Bài 3. Biết tổng tài sản đầu kỳ 1.600, vốn chủ đầu kỳ 400. Tính biên gộp, biên hoạt động, biên ròng, ROA, ROE (đầu kỳ) và kiểm bằng phân rã DuPont.

### Bài 5 (vận dụng) — cùng ROE, khác chất lượng
Hai doanh nghiệp cùng ROE 20%. X: biên ròng 20%, vòng quay 0,5, hệ số nhân vốn chủ 2. Y: biên ròng 2%, vòng quay 2,0, hệ số nhân vốn chủ 5. Kiểm ROE của cả hai. Giả sử tỷ trọng chi phí cố định trong tổng chi phí của hai bên **như nhau**: nếu doanh thu cả hai giảm 10%, doanh nghiệp nào nguy hiểm hơn và vì sao?

### Bài 6 (vận dụng, câu cũ xen kẽ) — nối Bài 001
Dùng bảng giao dịch quán cà phê ở mục 2. Dựng dòng tiền hoạt động theo phương pháp gián tiếp, đi từ lợi nhuận sau thuế 48 (coi lãi vay đã trả là dòng tiền hoạt động). Kiểm với tiền thực thu, thực chi.

### Bài 7 (chuyển giao) — tìm lỗi
"Công ty Z có ROE 45%, cao gấp ba ngành, chứng tỏ ban điều hành giỏi gấp ba. EBITDA 500 nghĩa là công ty có 500 tiền để trả nợ." Chỉ ra **hai** lỗi và cách kiểm.

### Bài 8 (chuyển giao) — đọc một báo cáo mới
Một doanh nghiệp có: lợi nhuận hoạt động tăng 10%, lợi nhuận sau thuế giảm 15%, vốn chủ giảm 30% trong khi lợi nhuận vẫn dương. Nêu **ba** giả thuyết giải thích và dòng báo cáo cần mở để kiểm từng giả thuyết.

## 8. Đáp án

### Bài 1

`PHÉP_TÍNH` Tổng tài sản `120 + 80 + 100 + 300 = 600`; nợ phải trả `200 + 90 = 290`; vốn chủ `600 − 290 = 310`.
Câu này kiểm: bạn có coi vốn chủ là **phần còn lại**, không phải một con số độc lập.

### Bài 2

- (a) Tiền **−50**; nợ vay **−50**. Lợi nhuận không đổi.
- (b) Phải thu **+70**; doanh thu 70 → lợi nhuận giữ lại **+70**. Tiền không đổi.
- (c) Tiền **+30**; phải thu **−30**. Lợi nhuận không đổi — doanh thu đã ghi ở (b).
- (d) Tồn kho **+40**; tiền **−40**. Lợi nhuận không đổi — chỉ thành chi phí khi bán.

Câu này kiểm: bạn có phân biệt giao dịch **đổi dạng tài sản** (c, d), **vay/trả nợ** (a) với giao dịch **tạo lợi nhuận** (b).

### Bài 3

`PHÉP_TÍNH` Lợi nhuận gộp `1.000 − 600 = 400`; EBIT `400 − 120 − 80 = 200`; EBITDA `200 + 50 = 250`; lợi nhuận trước thuế `200 − 40 = 160`; lợi nhuận sau thuế `160 × 0,8 = 128`.
Câu này kiểm: khấu hao đã **nằm trong** chi phí bán hàng và quản lý, nên chỉ cộng lại khi tính EBITDA, không trừ thêm lần nữa khi tính EBIT.

### Bài 4

`PHÉP_TÍNH` Biên gộp `400/1.000 = 40,0%`; biên hoạt động `200/1.000 = 20,0%`; biên ròng `128/1.000 = 12,8%`; ROA `128/1.600 = 8,0%`; ROE `128/400 = 32,0%`.
`PHÉP_TÍNH` DuPont: `12,8% × (1.000/1.600 = 0,625) × (1.600/400 = 4,0) = 32,0%` — khớp.
Câu này kiểm: ROE gấp 4 lần ROA chính là hệ số nhân vốn chủ 4,0.

### Bài 5

`PHÉP_TÍNH` X: `20% × 0,5 × 2 = 20%`; Y: `2% × 2,0 × 5 = 20%`.
`SUY_LUẬN` Với giả định cùng tỷ trọng chi phí cố định, Y nguy hiểm hơn: biên ròng chỉ 2% nên phần chi phí cố định không giảm theo doanh thu dễ xóa sạch lợi nhuận, và hệ số nhân vốn chủ 5 nghĩa là nợ phải trả lớn so với vốn chủ — lỗ nhỏ trên tài sản thành lỗ lớn trên vốn chủ. X có biên dày và vốn chủ dày nên có đệm. `PHÉP_TÍNH` Nếu **bỏ** giả định đó, kết luận có thể đảo: X thâm dụng tài sản (vòng quay 0,5) có thể có chi phí gần như toàn cố định — doanh thu 100 → 90 với chi phí 80 giữ nguyên thì lợi nhuận 20 → 10, giảm 50%; còn Y toàn chi phí biến đổi thì lợi nhuận chỉ giảm 10%. Vì vậy phải đọc cơ cấu chi phí trước khi kết luận.
Câu này kiểm: bạn có đọc ROE qua ba thừa số thay vì một con số.

### Bài 6

`PHÉP_TÍNH` `48 + 40 (khấu hao) − 50 (phải thu tăng) − 20 (tồn kho tăng từ 0 lên 20) + 100 (phải trả người bán tăng) + 12 (thuế phải nộp tăng) = 130`.
`PHÉP_TÍNH` Kiểm bằng tiền thực: thu từ khách 200 − lương 60 − lãi 10 = 130. Khớp. Tiền mua máy 400 nằm ở dòng tiền đầu tư; góp vốn 500 và vay 300 nằm ở dòng tiền tài chính; tổng `130 − 400 + 800 = 530` đúng bằng tiền cuối năm.
Đọc thêm (không bắt buộc): `SỰ_THẬT` khi IFRS 18 có hiệu lực (kỳ bắt đầu từ `2027-01-01`), doanh nghiệp lập theo IFRS **không** cung cấp tài chính cho khách hàng như hoạt động kinh doanh chính phải xếp lãi vay đã trả vào dòng tiền tài chính, và phương pháp gián tiếp xuất phát từ **lợi nhuận hoạt động** (nguồn thứ cấp: KPMG, 01/06/2026). `PHÉP_TÍNH` Khi đó cầu nối là `70 + 40 − 50 − 20 + 100 = 140`, dòng tiền tài chính `800 − 10 = 790`; tổng vẫn `140 − 400 + 790 = 530`. Quán cà phê Việt Nam lập theo VAS thì vẫn để lãi vay đã trả trong dòng tiền hoạt động (Bài N3).
Câu này kiểm: bạn có nối được bút toán ở mục 2 với cây cầu lợi nhuận → tiền của Bài 001.

### Bài 7

`SUY_LUẬN` Lỗi 1: "ROE cao gấp ba ⇒ giỏi gấp ba" — ROE có thể cao vì hệ số nhân vốn chủ lớn hoặc vì vốn chủ bị thu nhỏ do trả lại tiền cho cổ đông nhiều năm (ví dụ Apple ở mục 5), thậm chí vô nghĩa nếu vốn chủ âm. Cách kiểm: phân rã DuPont, so ROA và ROIC. Lỗi 2: "EBITDA 500 = có 500 tiền trả nợ" — EBITDA chưa trừ thuế, chưa trừ chi tiêu vốn và chưa tính thay đổi vốn lưu động. Cách kiểm: mở báo cáo lưu chuyển tiền tệ, xem dòng tiền hoạt động trừ chi tiêu vốn (Bài 004).
Câu này kiểm mức "phát hiện lỗi": gọi đúng tên lỗi và nêu đúng báo cáo cần mở.

### Bài 8

`SUY_LUẬN` Ba giả thuyết: (1) **chi phí lãi vay tăng** (vay thêm hoặc lãi suất thả nổi tăng) — mở dòng chi phí lãi vay và thuyết minh nợ (Bài 005); (2) **thuế suất hiệu dụng tăng** hoặc có khoản thuế một lần — mở dòng thuế và thuyết minh thuế; (3) **chi phí/khoản lỗ khác** dưới dòng lợi nhuận hoạt động (lỗ tỷ giá, lỗ đầu tư) — mở dòng thu nhập/chi phí khác. Vốn chủ giảm 30% dù có lãi: doanh nghiệp đã trả cho cổ đông nhiều hơn lợi nhuận (cổ tức, mua lại cổ phiếu) hoặc ghi giảm thẳng vào vốn chủ (lỗ toàn diện khác như chênh lệch quy đổi tỷ giá; mua thêm phần của cổ đông không kiểm soát) — mở bảng thay đổi vốn chủ sở hữu (Bài 006).
Câu này kiểm: bạn có định vị được **tầng** nơi chênh lệch xảy ra.

## 9. Đáp án phần ôn bài cũ

1. Doanh thu có thể là 100 nếu đã đủ điều kiện ghi nhận; 40 còn lại là **phải thu khách hàng** trên bảng cân đối (Bài 001).
2. Bảng cân đối là ảnh chụp tại một ngày; báo cáo kết quả kinh doanh và báo cáo lưu chuyển tiền tệ là phim trong một kỳ.
3. Vì mua tài sản dài hạn thường được xếp vào **dòng tiền đầu tư**, không phải dòng tiền hoạt động.

## 10. Lỗi thường gặp

- Coi vốn chủ sở hữu là "tiền của chủ đang nằm trong két". Vốn chủ là phần còn lại theo sổ sách; tiền là một dòng tài sản riêng.
- Ghi mua máy móc thành chi phí ngay trong năm, rồi kết luận "năm nay lỗ".
- Trừ khấu hao hai lần (một lần trong chi phí hoạt động, một lần riêng) khi dựng các tầng lợi nhuận.
- Gọi "EBITDA điều chỉnh" là EBITDA, hoặc coi EBITDA là tiền.
- So ROE của hai doanh nghiệp mà không phân rã — bỏ sót hệ số nhân vốn chủ.
- Đọc hệ số nhân vốn chủ lớn thành "vay nhiều" — mẫu số gồm cả nợ không chịu lãi.
- Lọc cổ phiếu theo ROE cao nhất mà không xem vốn chủ có âm hoặc quá nhỏ không.
- Dùng biên gộp, EBITDA hay ROE theo khung này cho ngân hàng.
- Lấy "lợi nhuận thuần từ hoạt động kinh doanh" (mã 30) trên báo cáo Việt Nam làm EBIT.
- Tính ROE bằng vốn chủ cuối kỳ cho doanh nghiệp này và vốn chủ đầu kỳ cho doanh nghiệp kia.
- Dùng "lợi nhuận hoạt động" trên báo cáo như EBIT mà không đọc nó gồm những khoản nào.
- Quên rằng tập đoàn có cổ đông thiểu số: P/E và EPS phải dùng lợi nhuận **thuộc cổ đông công ty mẹ** (Bài 009).

## 11. Ranh giới an toàn

- Bài này là khung đọc báo cáo, **không** phải khuyến nghị mua/bán/nắm giữ.
- Số liệu Apple là ví dụ học tập tại ngày chốt; phải mở lại hồ sơ mới nhất trước khi dùng vào việc khác.
- Không kết luận chất lượng doanh nghiệp từ một tỷ số đơn lẻ (ROE cao, biên cao).
- Không tỷ số nào trong bài chứa **giá cổ phiếu**, nên không thể nói đắt hay rẻ (Bài 002, 009). Doanh nghiệp tốt chưa chắc là cổ phiếu đáng mua. Số Apple là dữ liệu lịch sử FY2025, không phải dự báo.

## 12. Điều tôi vẫn chưa hiểu

Câu hỏi mở để bạn tự trả lời bằng lời mình, dùng làm đầu vào cho Bài 003 và N3:

1. Nếu một doanh nghiệp liên tục mua lại cổ phiếu nhiều hơn lợi nhuận, vốn chủ có thể âm không? Khi đó ROE còn ý nghĩa gì?
2. Vì sao một khoản chi (ví dụ chi phí phát triển phần mềm) có thể được ghi thành tài sản ở doanh nghiệp này và thành chi phí ở doanh nghiệp khác (gợi ý: Bài 007)?
3. Hệ số nhân vốn chủ cao làm ROE tăng khi kinh doanh tốt. Nó làm gì khi kinh doanh xấu?
4. Một doanh nghiệp có hệ số nhân vốn chủ 6 nhưng tiền ròng dương — nợ phải trả của nó có thể là những khoản gì?

## Đọc thêm (không bắt buộc): EBITDA theo SEC

`SỰ_THẬT` Góp ý của nhân viên SEC ngày 22/12/2023, được trích lại trong thư phản hồi của KBR ngày 02/01/2024: nếu điều chỉnh lợi nhuận ròng bằng bất cứ khoản nào **ngoài** lãi vay, thuế, khấu hao và phân bổ thì không được gọi thước đo đó là EBITDA; thư dẫn Câu hỏi 103.01 trong bộ C&DI về thước đo non-GAAP. `CHƯA_BIẾT` Trang C&DI gốc trả HTTP 404 trong lượt này.

## 13. Nguồn Internet đã mở

Tất cả mở ngày `2026-10-26`; không dùng đoạn trích trên trang kết quả tìm kiếm làm bằng chứng.

| Nguồn | Trạng thái | Ngày xuất bản / kỳ | Dùng cho |
|---|---|---|---|
| [Beginners' Guide to Financial Statements — U.S. SEC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements) | Mở được | Đăng 2014-01-12; cập nhật 2017-02-06 | Phương trình kế toán; định nghĩa tài sản/nợ/vốn chủ; thứ tự các tầng báo cáo kết quả kinh doanh; EPS; biên hoạt động |
| [Extreme makeover — ACCA](https://www.accaglobal.com/uk/en/student/exam-support-resources/fundamentals-exams-study-resources/f7/technical-articles/extreme-makeover.html) | Mở được; **nguồn thứ cấp** | Không ghi ngày; mô tả Khung khái niệm IASB bản 03/2018 | Định nghĩa tài sản, nguồn lực kinh tế, nợ phải trả theo Khung khái niệm 2018 (trang IFRS Foundation chỉ nêu tên định nghĩa, không nêu câu chữ) |
| [Conceptual Framework — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/) | Mở được | Ban hành 03/2018 | Xác nhận Khung 2018 đặt định nghĩa tài sản, nợ, vốn chủ, thu nhập, chi phí |
| [Thư phản hồi của KBR gửi SEC (CORRESP)](https://www.sec.gov/Archives/edgar/data/1357615/000135761524000002/filename1.htm) | Mở được | Thư KBR ngày 2024-01-02, trích góp ý của nhân viên SEC ngày 2023-12-22 | Quy tắc chỉ gọi là EBITDA khi chỉ điều chỉnh lãi vay, thuế, khấu hao, phân bổ; dẫn C&DI 103.01. `CHƯA_BIẾT` trang C&DI gốc: URL thử trả HTTP 404 trong lượt này |
| [Damodaran — Return on Capital, ROIC and ROE (PDF, NYU Stern)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf) | Mở được (đọc qua trích văn bản PDF) | Bản 2007 | Định nghĩa ROE = lợi nhuận ròng năm t / vốn chủ sổ sách đầu kỳ |
| [Apple Inc. Form 10-K FY2025 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Mở được; nguồn **gốc** | FY kết thúc 2025-09-27; triệu USD; US GAAP | Báo cáo kết quả hoạt động FY2023–FY2025, bảng cân đối hai kỳ (gồm nợ vay, tiền, chứng khoán đầu tư, phải trả người bán), khấu hao FY2025, mua lại cổ phiếu và cổ tức FY2025, lỗ lũy kế, khoản thuế một lần FY2024 |
| [Vinamilk — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) | Mở được (PDF quét); nguồn **gốc** | Ngày ký 27/02/2026; đồng; VAS | Thuyết minh VI.11 (EPS sau trích quỹ khen thưởng, phúc lợi) ở dòng EPS mục 3 |
| [McDonald's Form 10-K FY2024 — bảng cân đối (R7)](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R7.htm) | Mở bởi nhánh `risk-bear-reviewer` trong phiên; nguồn **gốc** | Ngày 31/12/2024; triệu USD; US GAAP | Vốn chủ âm −3.797 (R7); lợi nhuận ròng 2024 là 8.223 ([R3](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R3.htm)) (phản ví dụ ROE) |
| [KPMG — IFRS 18 changes to the statement of cash flows](https://kpmg.com/us/en/articles/2026/ifrs-18-changes-statement-cash-flows.html) | Mở được; **nguồn thứ cấp** | 2026-06-01 | Hiệu lực và phân loại lãi vay, điểm xuất phát phương pháp gián tiếp theo IFRS 18 (đáp án Bài 6) |

**Trạng thái kiểm nguồn**: bài mới soạn; xem nhật ký kiểm duyệt ở [lộ trình](../roadmap.md).
