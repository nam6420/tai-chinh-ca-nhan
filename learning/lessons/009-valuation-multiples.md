# Bài 009: Bội số định giá và cạm bẫy so sánh

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 14:20 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Dựng được cầu nối từ vốn hoá sang giá trị doanh nghiệp (EV) và biết các khoản điều chỉnh; chọn được bội số có nghĩa cho từng loại doanh nghiệp; nhận ra bốn kiểu bóp méo mẫu số (chu kỳ, khoản một lần, pha loãng, thuê tài sản/IFRS 16); chọn được nhóm so sánh đúng; giải thích được vì sao "P/E thấp hơn ngành" chưa phải là rẻ.
- Thời lượng: 40 phút đọc + 45 phút bài tập (2 phiên)
- Bài trước liên quan: [Bài 002](002-finding-a-cheap-stock.md) (ba câu hỏi), [Bài 003](003-business-quality-moat-and-roic.md) (ROIC), [Bài 005](005-debt-liquidity-survival.md) (nợ)
- Câu hỏi cốt lõi: **Với doanh nghiệp này, bội số nào có nghĩa và mẫu số nào đang bị bóp méo?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Ví dụ số học là hư cấu, trừ mục 6 dùng số của một doanh nghiệp thật từ **nguồn thứ cấp** (đã ghi rõ). Bài này chuẩn bị cho Bài 010 (chi phí vốn) và Bài 011 (DCF).

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Bội số không phải "giá trị của doanh nghiệp"; nó là **một cách viết lại câu hỏi "thị trường đang trả bao nhiêu cho một đồng lợi nhuận"**. Cùng một mức giá, doanh nghiệp bán hàng biên mỏng và doanh nghiệp bán hàng biên dày cho hai kết quả hoàn toàn khác nhau khi đem chia cho doanh thu.

Vì vậy câu hỏi đúng không phải "bội số này cao hay thấp", mà là: **chia cho cái gì là có nghĩa với mô hình kinh doanh này, và mẫu số đó có đang bị bóp méo bởi chu kỳ, khoản một lần, pha loãng hay cách hạch toán thuê tài sản không?**

> Câu cần nhớ: **Bội số chỉ có nghĩa khi tử số và mẫu số "cùng một chủ"** — cùng đo cho chủ nợ và cổ đông (EV), hoặc cùng đo cho riêng cổ đông (vốn hoá).

## Ôn bài cũ (5 phút)

Đáp án ở mục 9.

1. Vì sao ROIC phải so với chi phí vốn mới biết tăng trưởng tạo hay phá giá trị (Bài 003)?
2. Nêu ba dấu hiệu pha loãng và tác động lên EPS (Bài 006).
3. IFRS 16 ghi nhận gì trên bảng cân đối của bên đi thuê (Bài 005)?
4. Vì sao lợi nhuận một năm có thể không đại diện (Bài 003, mục 6)?

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy cầu nối EV và chọn bội số theo mô hình kinh doanh | Không tính chi phí vốn và WACC (Bài 010) |
| Dạy bốn nguồn bóp méo mẫu số và cách kiểm | Không dựng mô hình DCF (Bài 011) |
| Dạy chọn nhóm so sánh (cùng mô hình, cùng chu kỳ, cùng cấu trúc vốn) | Không kết luận "đắt/rẻ" cho một cổ phiếu cụ thể |
| Dạy đọc bội số của doanh nghiệp thật và giới hạn của nguồn thứ cấp | Không dạy giao dịch, không khuyến nghị mua/bán |

## Cách chia phiên và chọn phần cốt lõi

**Bài cốt lõi trong bộ bài tập:** 1, 2, 7. Các câu còn lại là luyện thêm; không bỏ kiến thức bắt buộc của thân bài. Phiên A làm câu 1, 2; phiên B làm câu 7.

`Ý_KIẾN` Phiên A: cầu nối EV, tử/mẫu cùng người hưởng lợi và ví dụ chọn nhóm. Phiên B: chu kỳ, khoản một lần, pha loãng, thuê và ví dụ thật. Sau bài quay lại N3 phần B, rồi N7; chưa cần tự ước tính WACC trước bài010.

Làm câu cốt lõi theo mục tiêu phiên trước khi xem đáp án; câu xen kẽ/chuyển giao kiểm hiểu sâu. Có thể dừng giữa bài; thời lượng ban đầu chưa được đo với người học. [Bảng thực hành và hai bài ôn](../practice/research-and-model-worksheets.md).

## 1. Cầu nối từ vốn hoá sang giá trị doanh nghiệp (EV)

`PHÉP_TÍNH` Công thức dùng trong bài này:

```text
EV (enterprise value) = Vốn hoá thị trường
                      + Tổng nợ vay (ngắn hạn + dài hạn + nợ thuê)
                      − Tiền và tương đương tiền − Đầu tư ngắn hạn
                      + Lợi ích cổ đông không kiểm soát
                      + Cổ phiếu ưu đãi (nếu có)
```

`SUY_LUẬN` Trực giác: **EV là giá phải trả để mua toàn bộ hoạt động kinh doanh**, không chỉ phần cổ đông. Người mua toàn bộ doanh nghiệp phải trả cho cổ đông (vốn hoá) **và** trả nợ, nhưng được nhận tiền mặt trong két. Vì vậy nợ **cộng** vào, tiền **trừ** ra.

`SUY_LUẬN` Hệ quả quan trọng: doanh nghiệp có **nhiều tiền hơn nợ** (net cash) sẽ có EV **nhỏ hơn** vốn hoá. Đây là chỗ rất nhiều người mới đọc sai — xem ví dụ Apple ở mục 6.

`KỊCH_BẢN` `PHÉP_TÍNH` Ví dụ hư cấu: doanh nghiệp có 120 triệu cổ phiếu, giá 10; tổng nợ 500; tiền 150; lợi ích cổ đông không kiểm soát 50; không có cổ phiếu ưu đãi.

- Vốn hoá = `120 × 10 = 1.200`.
- EV = `1.200 + 500 − 150 + 50 = 1.600`.

## 2. Bảng bội số: chia cho cái gì, khi nào

`Ý_KIẾN` Bảng dưới là quy ước thực hành, không phải chuẩn mực. Nguyên tắc chọn: **tử số và mẫu số phải cùng "chủ"**.

| Bội số | Tử số | Mẫu số | Dùng khi | Vô nghĩa/vô dụng khi |
|---|---|---|---|---|
| P/E | Vốn hoá (hoặc giá/cp) | Lợi nhuận sau thuế **thuộc cổ đông công ty mẹ** (EPS) | Doanh nghiệp ổn định, lợi nhuận đại diện | Lợi nhuận âm, chu kỳ đỉnh/đáy, có khoản một lần |
| EV/EBITDA | EV | EBITDA | So sánh doanh nghiệp khác cấu trúc vốn; ngành ít capex | Nợ dày, thuê nhiều, capex lớn (EBITDA bỏ qua cả ba) |
| EV/EBIT | EV | EBIT | Khi khấu hao là chi phí thật đáng kể | Khi EBIT bị bóp méo bởi khoản một lần |
| EV/Sales | EV | Doanh thu | Doanh nghiệp biên mỏng, đang tăng trưởng, chưa có lãi | Khi biên lợi nhuận khác nhau nhiều giữa các doanh nghiệp |
| P/B | Vốn hoá | Vốn chủ sở hữu | Ngân hàng, bảo hiểm (tài sản tài chính) | Doanh nghiệp tài sản vô hình lớn (giá trị sổ sách vô nghĩa) |
| P/S | Vốn hoá | Doanh thu | Như EV/Sales nhưng cho cổ đông | Như EV/Sales |

`SUY_LUẬN` Vì sao P/E và EV/EBITDA **không thay thế nhau**: P/E đo trên lợi nhuận **sau** lãi vay (đã trừ cho chủ nợ), còn EV/EBITDA đo trước lãi vay và thuế (chia cho cả chủ nợ và cổ đông). Hai doanh nghiệp cùng hoạt động nhưng khác đòn bẩy sẽ có P/E rất khác nhau trong khi EV/EBITDA gần nhau — và ngược lại. Muốn so sánh được, phải biết mình đang so cái gì.

`SUY_LUẬN` Cùng nguyên tắc "cùng một chủ": EV đã **cộng** lợi ích cổ đông không kiểm soát, nên mẫu số EBITDA/EBIT phải là của **toàn bộ** tập đoàn; còn vốn hoá chỉ là phần của cổ đông công ty mẹ, nên P/E phải dùng lợi nhuận **sau khi trừ** phần của cổ đông không kiểm soát.

`PHÉP_TÍNH` Ghi chú kỹ thuật: P/E tính bằng `giá / EPS` và tính bằng `vốn hoá / lợi nhuận ròng` có thể lệch nhau một chút, vì EPS dùng số cổ phiếu **pha loãng bình quân** còn vốn hoá dùng số cổ phiếu **hiện hành**. Chênh lệch này là thông tin (nó phản ánh pha loãng), không phải lỗi làm tròn.

## 3. Bốn nguồn bóp méo mẫu số

### 3.1 Chu kỳ

`PHÉP_TÍNH` `KỊCH_BẢN` Doanh nghiệp chu kỳ có EPS 5 năm: 8; 2; 5; 4; 6 (bình quân 5). Giá 60:

| Cách tính | P/E | Kết luận vội vàng |
|---|---:|---|
| Dùng năm đỉnh (EPS 8) | 7,5 | "Rẻ!" |
| Dùng năm đáy (EPS 2) | 30,0 | "Đắt!" |
| Dùng EPS chuẩn hoá (5) | 12,0 | Trung tính |

`SUY_LUẬN` Cùng một cổ phiếu, cùng một giá, ba kết luận trái ngược. Đây là bẫy P/E của Bài 002, nay có công cụ cụ thể: **luôn chuẩn hoá mẫu số qua ít nhất một chu kỳ** và ghi rõ đã dùng cách nào.

### 3.2 Khoản một lần và thước đo tự định nghĩa

`SUY_LUẬN` Lợi nhuận có thể chứa: bán tài sản, hoàn nhập dự phòng, lãi đánh giá lại, chi phí tái cấu trúc. Dùng mẫu số có khoản một lần làm bội số sai lệch cả hai chiều.

`PHÉP_TÍNH` `KỊCH_BẢN` EV 5.160; EBITDA theo IFRS 600. Nếu dùng "EBITDA điều chỉnh" 700 (cộng lại 100 chi phí tái cấu trúc), bội số từ `5.160/600 = 8,6` thành `5.160/700 = 7,4` — trông "rẻ" hơn 14% chỉ vì đổi mẫu số. Với kỳ báo cáo năm bắt đầu từ `2027-01-01`, nếu thước đo điều chỉnh kiểu này được dùng trong truyền thông công khai thì phải được thuyết minh và đối chiếu theo IFRS 18 (MPM — xem [Bài 007](007-notes-and-accounting-red-flags.md)); EBITDA "thuần" đúng bằng tiểu tổng loại trừ của IFRS 18 thì không phải MPM.

### 3.3 Pha loãng

`SUY_LUẬN` Dùng EPS pha loãng (diluted) thay vì EPS cơ bản là bắt buộc về mặt kỹ thuật, nhưng vẫn phải nhìn **xu hướng số cổ phiếu** (Bài 006): doanh nghiệp phát hành 5%/năm sẽ làm EPS tăng chậm hơn lợi nhuận, và P/E sẽ trông đắt hơn một cách "vô cớ".

### 3.4 Thuê tài sản (IFRS 16)

`SỰ_THẬT` IFRS 16 buộc bên đi thuê ghi nhận tài sản quyền sử dụng và nợ thuê với hợp đồng thuê **trên 12 tháng** (Bài 005). Hệ quả với bội số: tiền thuê trước đây nằm trong chi phí hoạt động, nay nằm ở khấu hao và lãi vay — nên **EBITDA tăng** và **EV cũng tăng** (vì nợ thuê vào EV). `SỰ_THẬT` Với **thuê hoạt động theo US GAAP** (ASC 842), chi phí thuê vẫn là chi phí hoạt động nên EBITDA **không** tăng (Bài 005, mục 1). So một doanh nghiệp IFRS với một doanh nghiệp US GAAP thì phải biết chuẩn của từng bên trước khi quyết định có gộp nợ thuê vào EV hay không.

`PHÉP_TÍNH` `KỊCH_BẢN` Hai doanh nghiệp cùng hoạt động, cùng vốn hoá 900, cùng tiền 100:

| Doanh nghiệp | Nợ vay | Nợ thuê | EBITDA | EV | EV/EBITDA |
|---|---:|---:|---:|---:|---:|
| S — sở hữu cửa hàng | 400 | 0 | 150 | 1.200 | 8,0 |
| L — thuê, trình bày **trước** IFRS 16 | 200 | (ngoài bảng) | 130 | 1.000 | 7,7 |
| L — thuê, trình bày **sau** IFRS 16 | 200 | 200 | 150 | 1.200 | 8,0 |

`SUY_LUẬN` Bài học: nếu gộp nợ thuê vào cả tử số và mẫu số, hai doanh nghiệp **hội tụ** về 8,0. Nếu chỉ chỉnh một bên (ví dụ dùng EBITDA đã loại tiền thuê nhưng EV chưa gộp nợ thuê), bạn đang so hai cách hạch toán chứ không so hai mức định giá. Đây là lý do khi so sánh phải **gộp hoặc loại thuê ở cả hai bên**.

## 4. Chọn nhóm so sánh: ba tiêu chí và một hộp bắt buộc

`Ý_KIẾN` Ba tiêu chí chọn peer (doanh nghiệp so sánh):

1. **Cùng mô hình kinh doanh**: bán lẻ vs bán buôn; phần mềm thuê bao vs bán license; ngân hàng vs công ty chứng khoán. Nhãn ngành không đủ.
2. **Cùng độ chín chu kỳ**: doanh nghiệp đang ở đỉnh chu kỳ không so được với doanh nghiệp đang đáy — bội số sẽ phản ánh chu kỳ, không phản ánh chất lượng.
3. **Cùng cấu trúc vốn và cách hạch toán**: nếu một bên thuê nhiều, một bên sở hữu nhiều, phải xử lý thuê ở cả hai bên.

`Ý_KIẾN` **Hộp bắt buộc ở đầu mọi so sánh** (vì Bài 014 nằm sau): cấu trúc ngành là gì, rào cản gia nhập là gì, và ai là 3–5 doanh nghiệp thực sự cùng mô hình. Nếu không viết được hộp này, chưa nên so bội số.

`SUY_LUẬN` Một cách kiểm nhanh: lấy bội số của chính doanh nghiệp qua 5–10 năm (so với chính nó) trước khi so với người khác. Nếu bội số của nó dao động 8–30 lần trong 10 năm thì "trung bình ngành 12 lần" không có nhiều ý nghĩa.

## 5. Ví dụ số học: cùng doanh thu, cùng EV, ba kết luận khác nhau

`KỊCH_BẢN` Ba doanh nghiệp hư cấu A, B, C: cùng doanh thu 500, cùng EV 600, cùng EBITDA 100, nhưng biên hoạt động khác nhau (khấu hao khác nhau). Giả định đơn giản: vốn hoá 500 cho cả ba, không có tiền mặt nên nợ vay = nợ ròng = 100; lãi vay 10 (10%/năm) và thuế suất 20% cho cả ba.

| Chỉ tiêu | A | B | C |
|---|---:|---:|---:|
| Doanh thu | 500 | 500 | 500 |
| EBITDA | 100 | 100 | 100 |
| EBIT | 80 | 60 | 40 |
| Lợi nhuận sau thuế `(EBIT − 10) × 0,8` | 56 | 40 | 24 |
| EV/Sales | 1,20 | 1,20 | 1,20 |
| EV/EBITDA | 6,0 | 6,0 | 6,0 |
| **EV/EBIT** | **7,5** | **10,0** | **15,0** |
| **P/E** | **8,9** | **12,5** | **20,8** |

`SUY_LUẬN` EV/Sales và EV/EBITDA nói "ba doanh nghiệp giống nhau"; EV/EBIT và P/E nói "khác nhau rất nhiều". Điều này cho thấy: A tạo ra nhiều lợi nhuận hoạt động hơn trên cùng doanh thu và cùng EV — tức thị trường **chưa** trả giá cao hơn cho chất lượng đó, hoặc đang định giá ba doanh nghiệp như nhau vì lý do khác (rủi ro, tăng trưởng, thanh khoản). Khi phân tích (và khi làm Bài 5, Bài 8 ở mục 8), phải chỉ ra **cả hai khả năng**, không chỉ một.

`SUY_LUẬN` Đây là câu trả lời cho "bội số nào có nghĩa": với ba doanh nghiệp này, **EV/EBIT hoặc P/E** phân biệt được — **với điều kiện** khấu hao phản ánh đúng nhu cầu chi tái đầu tư. Nếu khấu hao cao của C chủ yếu là phân bổ tài sản vô hình từ một thương vụ mua lại (không cần chi tiền để duy trì), EV/EBIT và P/E lại phạt C oan; kiểm bằng chi tiêu vốn và dòng tiền tự do (Bài 004). EV/Sales là một tỷ lệ, không đo quy mô; nó chỉ hữu ích khi doanh nghiệp chưa có lãi hoặc khi đọc kèm biên lợi nhuận, không dùng để kết luận đắt/rẻ.

## 6. Doanh nghiệp thật: bội số của Apple và ba điều đọc được

`SỰ_THẬT` Số dưới đây lấy từ trang thống kê của Apple trên `stockanalysis.com` (mở ngày `2026-10-26`, HTTP 200), giá đóng cửa **23/10/2026**, dữ liệu **TTM** (12 tháng gần nhất), đơn vị USD. Đây là **nguồn thứ cấp** tổng hợp từ dữ liệu thị trường; nguồn gốc là báo cáo 10-K/10-Q và giá giao dịch. `CHƯA_BIẾT` số liệu TTM đã đối chiếu 10-Q/10-K gốc: lượt soạn bài gặp HTTP 403 từ `sec.gov`; lượt review sau xác nhận SEC truy cập được khi gửi User-Agent khai báo (Bài 004) nhưng **chưa** đối chiếu các con số TTM dưới đây.

| Chỉ tiêu | Số | Ghi chú |
|---|---:|---|
| Vốn hoá | 5.070 tỷ USD | |
| Enterprise value (EV) | 5.010 tỷ USD | **nhỏ hơn** vốn hoá |
| Tổng nợ | 84,34 tỷ USD | |
| Tiền và chứng khoán | 146,52 tỷ USD | |
| Net cash | 62,17 tỷ USD | `PHÉP_TÍNH` 146,52 − 84,34 = 62,18 (chênh làm tròn) |
| Doanh thu (TTM) | 466,82 tỷ USD | |
| EBITDA (TTM) | 167,96 tỷ USD | |
| Lợi nhuận ròng (TTM) | 128,93 tỷ USD | |
| EPS (TTM) | 8,72 USD | |
| P/E | 39,89 | `PHÉP_TÍNH` 347,73 / 8,72 = 39,88 |
| EV/EBITDA | 29,84 | `PHÉP_TÍNH` 5.010 / 167,96 = 29,83 |
| EV/Sales | 10,74 | `PHÉP_TÍNH` 5.010 / 466,82 = 10,73 |
| Beta (5 năm) | 1,07 | |
| WACC (trang ước tính) | 9,96% | `Ý_KIẾN` cách ước tính của bên thứ ba — xem Bài 010 |

`PHÉP_TÍNH` Kiểm tra cầu nối EV: `5.070 + 84,34 − 146,52 = 5.007,82` tỷ USD ≈ **5.010** tỷ USD (trang ghi 5,01 nghìn tỷ). Khớp sau làm tròn.

Ba điều đọc được:

1. **EV < vốn hoá** vì net cash. `PHÉP_TÍNH` Ai dạy "EV = vốn hoá + nợ" mà quên trừ tiền sẽ ra `5.070 + 84,34 = 5.154` tỷ USD, cao hơn EV đúng khoảng **146 tỷ USD** — đúng bằng lượng tiền và chứng khoán bị bỏ sót.
2. **P/E và EV/EBITDA đo trên hai mẫu số khác nhau** (39,9 lần so với 29,8 lần). Vì net cash chỉ khoảng 1% vốn hoá, tử số của hai bội số gần như bằng nhau (EV ≈ vốn hoá); chênh lệch gần như toàn bộ đến từ **mẫu số**: `PHÉP_TÍNH` EBITDA / lợi nhuận ròng = `167,96 / 128,93 = 1,30` lần, tức khấu hao, thuế và lãi/thu nhập tài chính nằm giữa hai dòng này. Phần còn lại (`39,89 / 29,84 = 1,34` so với 1,30) đến từ hai chỗ nhỏ: P/E dùng EPS pha loãng (`39,89` so với vốn hoá/lợi nhuận `5.070 / 128,93 = 39,32`), và EV nhỏ hơn vốn hoá khoảng 1%. Vì vậy không được coi hai bội số là "hai thước đo tương đương", kể cả khi doanh nghiệp gần như không có nợ ròng.
3. **Bội số cao tuyệt đối không tự nói đắt/rẻ**: 39,9 lần P/E chỉ có nghĩa khi so với chính nó trong quá khứ, với doanh nghiệp cùng mô hình, và với mức tăng trưởng kỳ vọng — mà kỳ vọng đó phải dựng bằng DCF (Bài 011) và chi phí vốn (Bài 010).

## 7. Năm câu hỏi khi dùng bội số

1. EV đã gồm nợ thuê chưa; có lợi ích cổ đông không kiểm soát hoặc cổ phiếu ưu đãi không?
2. Mẫu số là gì: doanh thu, EBITDA, EBIT hay lợi nhuận ròng; đã chuẩn hoá chu kỳ và loại khoản một lần chưa?
3. Doanh nghiệp đang ở pha nào của chu kỳ; bội số của chính nó 5–10 năm dao động ra sao?
4. Nhóm so sánh có thực sự cùng mô hình kinh doanh và cùng cách hạch toán thuê tài sản không?
5. Chênh lệch bội số so với nhóm là do chất lượng (ROIC, tăng trưởng) hay do rủi ro (đòn bẩy, thanh khoản, quản trị)?

## 8. Bài tập (8 câu, 45 phút)

`KỊCH_BẢN` Số liệu hư cấu trừ khi ghi rõ.

### Bài 1 (nhớ lại) — cầu nối EV
Doanh nghiệp có 150 triệu cổ phiếu, giá 12; nợ vay ngắn hạn 200; nợ vay dài hạn 400; tiền 120; lợi ích cổ đông không kiểm soát 30; cổ phiếu ưu đãi 0. Tính vốn hoá và EV.

### Bài 2 (vận dụng) — năm bội số
Dùng số liệu: EV 1.600; doanh thu 640; EBITDA 160; EBIT 120; lợi nhuận ròng 80; vốn chủ sở hữu 400; vốn hoá 1.100. Tính EV/Sales, EV/EBITDA, EV/EBIT, P/E, P/B.

### Bài 3 (vận dụng) — chuẩn hoá chu kỳ
EPS 6 năm: 6; 3; 1; 4; 7; 5. Giá hiện tại 42. Tính P/E theo năm gần nhất, theo đáy, theo bình quân, và nêu cách nào dùng để so sánh giữa hai doanh nghiệp chu kỳ.

### Bài 4 (vận dụng) — IFRS 16 và bội số
Doanh nghiệp thuê nhiều: EBITDA **trước** khi vốn hoá thuê 120; tiền thuê 25/năm; nợ thuê 180; nợ vay 200; tiền 80; vốn hoá 900. Tính EV/EBITDA **trước** và **sau** IFRS 16 và giải thích chênh lệch.

### Bài 5 (vận dụng, câu cũ xen kẽ) — nối Bài 004
Một doanh nghiệp có EV/EBITDA 12 lần, EBITDA 200, lợi nhuận ròng 110, CFO 55 (tỷ lệ chuyển hoá tiền mặt `55/110 = 50%`). Nêu hai câu hỏi phải hỏi trước khi coi bội số này là "bình thường".

### Bài 6 (vận dụng, câu cũ xen kẽ) — nối Bài 007
Doanh nghiệp công bố "EBITDA điều chỉnh" 700 trong khi EBITDA theo IFRS 600; EV 5.160. Tính EV/EBITDA theo hai mẫu số và nêu một câu hỏi về MPM.

### Bài 7 (chuyển giao) — chọn peer
Bốn doanh nghiệp: (1) bán lẻ thực phẩm, sở hữu cửa hàng; (2) bán lẻ thực phẩm, thuê cửa hàng; (3) chuỗi nhà hàng sở hữu mặt bằng; (4) nền tảng giao hàng thu phí. Chọn hai doanh nghiệp nên so trực tiếp với doanh nghiệp (1) và giải thích; nêu một điều chỉnh cần làm.

### Bài 8 (chuyển giao) — tìm lỗi
"P/E 9 lần trong khi trung bình ngành 15 lần nên cổ phiếu rẻ 40%. Vì P/E thấp nên rủi ro cũng thấp." Chỉ ra **ba** lỗi và cách kiểm.

## 9. Đáp án

### Bài 1

`PHÉP_TÍNH` Vốn hoá = `150 × 12 = 1.800`; EV = `1.800 + 200 + 400 − 120 + 30 = 2.310`.
`SUY_LUẬN` Câu này kiểm: dấu của tiền mặt (trừ) và việc cộng lợi ích cổ đông không kiểm soát.

### Bài 2

`PHÉP_TÍNH` EV/Sales = `1.600/640 = 2,50`; EV/EBITDA = `1.600/160 = 10,0`; EV/EBIT = `1.600/120 = 13,3`; P/E = `1.100/80 = 13,75`; P/B = `1.100/400 = 2,75`.
`SUY_LUẬN` Câu này kiểm: bạn có dùng đúng tử số cho từng bội số (EV cho ba bội số đầu, vốn hoá cho P/E và P/B).

### Bài 3

`PHÉP_TÍNH` Bình quân 6 năm = `(6+3+1+4+7+5)/6 = 26/6 = 4,33`.
- P/E theo năm gần nhất (EPS 5): `42/5 = 8,4`.
- P/E theo đáy (EPS 1): `42/1 = 42`.
- P/E chuẩn hoá (EPS 4,33): `42/4,33 = 9,7`.
`SUY_LUẬN` Để so giữa hai doanh nghiệp chu kỳ, dùng **EPS chuẩn hoá cùng một cách tính** cho cả hai (ví dụ trung bình 5–7 năm, hoặc EBIT chuẩn hoá). Nêu rõ quy ước, vì bình quân số học và bình quân có trọng số cho kết quả khác nhau.

### Bài 4

`PHÉP_TÍNH` **Trước** IFRS 16: EV = `900 + 200 − 80 = 1.020`; EV/EBITDA = `1.020/120 = 8,5`.
`PHÉP_TÍNH` **Sau** IFRS 16: EBITDA = `120 + 25 = 145` (tiền thuê chuyển khỏi chi phí hoạt động); EV = `900 + 200 + 180 − 80 = 1.200`; EV/EBITDA = `1.200/145 = 8,3`.
`SUY_LUẬN` Hai con số gần nhau (8,5 và 8,3) chứ không "rẻ đi" — vì cả tử và mẫu cùng tăng. Nếu chỉ chỉnh mẫu số (EBITDA 145) mà giữ EV 1.020 thì được `1.020/145 = 7,0` — con số **sai** vì bỏ nợ thuê ra khỏi tử số.

### Bài 5

`SUY_LUẬN` Hai câu hỏi: (a) lợi nhuận có chuyển thành tiền không — CFO 55 chỉ bằng 50% lợi nhuận ròng và `55/200 = 27,5%` EBITDA, nghĩa là phần lớn lợi nhuận đang nằm ở vốn lưu động hoặc khoản không phải tiền (Bài 004); lưu ý tỷ lệ chuyển hoá của Bài 004 chia cho **lợi nhuận sau thuế**, không chia cho EBITDA; (b) capex và tiền thuê có lớn không, vì EV/EBITDA bỏ qua cả hai — nếu capex bằng 80% EBITDA thì bội số đang che chi phí thật.

### Bài 6

`PHÉP_TÍNH` Theo IFRS: `5.160/600 = 8,6`. Theo "EBITDA điều chỉnh": `5.160/700 = 7,4`. Chênh 14%.
`SUY_LUẬN` Câu hỏi về MPM: khoản 100 bị cộng lại là gì, có lặp lại 3 năm không, và — với kỳ báo cáo năm từ `2027-01-01` — doanh nghiệp có đối chiếu thước đo này về chỉ tiêu IFRS gần nhất trong thuyết minh không (Bài 007).

### Bài 7

`SUY_LUẬN` Nên chọn **(2) bán lẻ thực phẩm, thuê cửa hàng** — cùng mô hình bán lẻ thực phẩm, khác cách hạch toán thuê; đây chính là cặp cần điều chỉnh IFRS 16 ở cả hai bên. (3) khác ngành (nhà hàng có biên và vòng quay khác); (4) khác mô hình hoàn toàn (nền tảng thu phí, không giữ hàng).
`SUY_LUẬN` Điều chỉnh cần làm: gộp nợ thuê vào EV và dùng EBITDA sau IFRS 16 cho cả hai (hoặc loại thuê ở cả hai), rồi mới so. Nếu (1) sở hữu mặt bằng thì tài sản của nó nằm ở tài sản cố định — so sánh phải nêu rõ khác biệt này.

### Bài 8

`SUY_LUẬN` Lỗi 1: "P/E thấp hơn ngành 40% ⇒ rẻ" — chưa biết mẫu số (EPS) có đại diện không; có thể lợi nhuận đang ở đỉnh chu kỳ hoặc có khoản một lần. Lỗi 2: "P/E thấp ⇒ rủi ro thấp" — P/E thấp thường **chính là** dấu hiệu thị trường đang định giá rủi ro cao hơn (chu kỳ, đòn bẩy, quản trị, thanh khoản). Lỗi 3: so với "trung bình ngành" mà không nêu nhóm ngành gồm những ai, cùng mô hình không, cùng chu kỳ không, và bình quân tính theo cách nào (trung vị hay bình quân, có loại doanh nghiệp lỗ không).
`SUY_LUẬN` Cách kiểm: dựng EPS chuẩn hoá 5 năm; so với chính nó 10 năm; xem ROIC so chi phí vốn (Bài 003/010); và đọc thuyết minh cho khoản một lần (Bài 007).

### Đáp án phần ôn bài cũ

1. ROIC thấp hơn chi phí vốn nghĩa là mỗi đồng tái đầu tư phá huỷ giá trị (Bài 003).
2. Phát hành thêm, ESOP, trái phiếu chuyển đổi; tác động: EPS tăng chậm hơn lợi nhuận (Bài 006).
3. Ghi nhận tài sản quyền sử dụng và nợ thuê với hợp đồng thuê trên 12 tháng (Bài 005).
4. Vì một năm có thể là đỉnh/đáy chu kỳ hoặc có khoản một lần (Bài 003, mục 6).

## 10. Lỗi thường gặp

- Tính EV mà quên trừ tiền mặt (hoặc quên cộng nợ thuê), rồi so với bội số của người khác tính đúng.
- So P/E với EV/EBITDA như hai thước cùng loại, hoặc so P/E của hai doanh nghiệp khác đòn bẩy.
- Dùng EBITDA cho doanh nghiệp nợ dày/thuê nhiều/capex lớn mà không nêu cảnh báo.
- Không chuẩn hoá chu kỳ, rồi kết luận "rẻ" ở đỉnh chu kỳ.
- Lấy "trung bình ngành" mà không nêu nhóm gồm những ai và tính theo cách nào.
- Dùng "EBITDA điều chỉnh" của doanh nghiệp như thể là số liệu chuẩn mực.
- So bội số của doanh nghiệp Việt Nam với doanh nghiệp Mỹ mà bỏ qua khác biệt về lãi suất, rủi ro quốc gia và thanh khoản (Bài 010).
- Kết luận đắt/rẻ từ bội số mà chưa có chi phí vốn và kỳ vọng tăng trưởng.

## 11. Ranh giới an toàn

- Bài này **không** phải khuyến nghị mua/bán/nắm giữ; không có "ngưỡng bội số đúng".
- Số liệu Apple là **nguồn thứ cấp**, kỳ TTM, giá đóng cửa 23/10/2026; trước khi dùng cho quyết định thật phải đối chiếu 10-K/10-Q.
- Không so sánh bội số giữa hai thị trường khác nhau mà không nêu khác biệt lãi suất, rủi ro quốc gia, thanh khoản.
- Mọi ví dụ hư cấu không đại diện cho doanh nghiệp thật nào.

## 12. Điều tôi vẫn chưa hiểu

1. Bạn muốn luyện với danh sách peer của một ngành cụ thể nào (bán lẻ, ngân hàng, sản xuất)?
2. Bạn có cần một bảng tính để tự nhập EV và tính 5 bội số cho một doanh nghiệp không?
3. Bạn muốn đi tiếp Bài 010 (chi phí vốn, WACC) hay muốn ở lại luyện bội số thêm một tuần?
4. Với doanh nghiệp bạn đang theo dõi, bội số nào đang "trông rẻ" nhất — và bạn đã kiểm mẫu số chưa?

## 13. Nguồn Internet đã mở

<details>
<summary>Nguồn chi tiết và lịch sử kiểm — giữ mốc dữ liệu gốc</summary>

Tất cả mở ngày `2026-10-26`.

- [Apple statistics — stockanalysis.com](https://stockanalysis.com/stocks/aapl/statistics/) — HTTP 200; giá đóng cửa `2026-10-23`; trang ghi "Last updated: Oct 26, 2026"; dữ liệu **TTM**, đơn vị USD (T = nghìn tỷ, B = tỷ); **nguồn thứ cấp** (trang dẫn nguồn dữ liệu thị trường của bên thứ ba). Dùng cho mục 6.
- [Damodaran — Data page (NYU Stern)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html) — HTTP 200. Cung cấp: bản cập nhật đầy đủ gần nhất `2026-01-09`; nhịp cập nhật đầu mỗi năm.
- [Damodaran — Current data](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html) — HTTP 200. Cung cấp: kỳ dữ liệu (12 tháng tới quý III năm trước), đơn vị tuyệt đối tính bằng **triệu USD**; danh mục tệp bội số ngành (PE/PEG, P/B & EV/Invested Capital, P/S & EV/Sales, EV/EBIT & EV/EBITDA) theo khu vực.
- `CHƯA_BIẾT` Số bội số ngành cụ thể để xếp hạng một doanh nghiệp: các tệp là `.xls/.xlsx`, công cụ trong lượt này không đọc được Excel. Cách xác minh: tải tệp và mở bằng phần mềm bảng tính; ghi rõ kỳ (01/2026) và đơn vị (triệu USD).
- `CHƯA_BIẾT` Công thức EV từ một nguồn học thuật/chuẩn: lượt này không mở được giáo trình hay trang chuẩn nào định nghĩa EV; công thức ở mục 1 là `PHÉP_TÍNH` khớp với số liệu công bố của nguồn dữ liệu, **không phải** trích dẫn chuẩn. Cách xác minh: mở giáo trình định giá (Damodaran, `variable.htm`) hoặc sách giáo khoa tài chính doanh nghiệp.

**Trạng thái kiểm nguồn**: **chưa có biên bản `source-fact-checker` độc lập**. Lượt review ngày `2026-10-26` đã sửa: P/E dùng lợi nhuận thuộc cổ đông công ty mẹ; khác biệt US GAAP về thuê ở mục 3.4; giải thích lại chênh lệch P/E và EV/EBITDA của Apple; dữ kiện tự mâu thuẫn ở Bài 5 (lợi nhuận ròng bằng EBITDA); mốc áp dụng MPM. Số liệu Apple TTM vẫn là nguồn thứ cấp chưa đối chiếu 10-Q.


</details>
