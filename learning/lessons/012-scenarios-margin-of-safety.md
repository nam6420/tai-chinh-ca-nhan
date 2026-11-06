# Bài 012 — Kịch bản, biên an toàn và điều kiện bác bỏ

- Ngày viết lại: `2026-10-31`. Bản này **thay thế** bản 2026-10-26; biên bản kiểm cũ gắn mã băm cũ, không còn áp dụng.
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Nguồn số Apple: Form 10-K FY2025 mở ngày `2026-10-31`.
- Mục tiêu: Biến một mô hình DCF thành ba kịch bản có điều kiện; hiểu vì sao xác suất gán cho kịch bản là giả định; tính biên an toàn và nhìn thấy giới hạn của nó; viết điều kiện bác bỏ đo được; tính tác động của chi phí giao dịch.
- Bài trước liên quan: Thứ tự đọc **Bước 21/23 của Nhánh 1** — học ngay sau [Bài 011: DCF và định giá ngược](011-dcf-reverse-dcf.md) (kế thừa [Bài 010](010-cost-of-capital.md), [Bài N7](N7-data-probability-uncertainty.md) và [Bài 009](009-valuation-multiples.md)). Học tiếp: chuỗi thực hành định lượng [Bài Q4](Q4-getting-data-edgar-xbrl-vietnam.md) → [Bài Q2](Q2-sbc-dilution-buybacks-dividends.md) → [Bài Q1](Q1-earnings-quality-toolkit.md) → [Bài Q3](Q3-normalizing-earnings-cyclical.md), hoặc sang thẳng [Bài 015: Tâm lý, bảng tự kiểm và nhật ký quyết định](015-behavior-decision-journal.md) (Bước 22/23) và [Bài 016: Bài tổng kết nghiên cứu doanh nghiệp](016-company-research-capstone.md) (Bước 23/23).
- Thời lượng: 2–3 phiên (A: mục 1–3; B: mục 4–6; C: bài tập).
- Tệp thực hành: [valuation.py](../practice/models/valuation.py) (hàm `dcf`, `per_share`, `sensitivity`).
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/012-fact-check.md), [phản biện](../reviews/012-risk-review.md).
- Câu hỏi cốt lõi: **Nếu tôi sai về tương lai, tôi sai theo hướng nào, mất bao nhiêu, và dấu hiệu nào cho tôi biết sớm?**

## Hiểu bài này trong 1 phút

Một mô hình chỉ cho một con số, nhưng tương lai không có một con số. Ba kịch bản (thấp hơn cơ sở, cơ sở, thuận lợi) cho thấy **khoảng** giá trị theo các câu chuyện khác nhau. Biên an toàn là khoảng cách giữa giá và giá trị ước tính; khoảng cách ấy chỉ bảo vệ nếu mô hình đã tính đủ những cách mình có thể sai. Điều kiện bác bỏ là danh sách sự việc quan sát được mà nếu xảy ra thì luận điểm phải bị xem lại, viết **trước** khi mình gắn bó cảm xúc với kết quả.

## Ôn bài cũ hoặc kiểm tra đầu vào

Ôn lại các bài liền trước trong Nhánh 1 ([Bài N7](N7-data-probability-uncertainty.md) → [Bài 010](010-cost-of-capital.md) → [Bài 011](011-dcf-reverse-dcf.md)):
1. [Bài 011](011-dcf-reverse-dcf.md): `TV` chiếm khoảng bao nhiêu phần `EV` trong mô hình Apple của bài đó, và điều đó cảnh báo điều gì?
2. [Bài 011](011-dcf-reverse-dcf.md): nếu `g` tiến sát `WACC` thì giá trị mô hình đổi thế nào?
3. [Bài N7](N7-data-probability-uncertainty.md): xác suất tự gán 30% cho một kịch bản có phải số đo từ dữ liệu không?
4. [Bài 010](010-cost-of-capital.md): vì sao `WACC` nên báo khoảng thay vì một số?

<details>
<summary>Mở sau khi tự làm</summary>

Đáp án ngắn: (1) khoảng 76,6%; cảnh báo mô hình nhạy giả định sau năm 5; (2) tăng rất nhanh; (3) không, chỉ là ý kiến chủ quan; (4) vì một điểm phần trăm làm giá trị đổi khoảng 14–17%.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Dựng ba kịch bản từ cùng một mô hình, với giả định ghi rõ | Không gán xác suất "đúng" cho kịch bản |
| Dùng số Apple FY2025 làm gốc và làm ví dụ điều kiện bác bỏ | Không nói giá Apple hôm nay rẻ hay đắt |
| Tính biên an toàn và tác động chi phí | Không hướng dẫn quy mô vị thế cá nhân (xem H2) |

## 1. Từ một mô hình sang ba kịch bản

`SUY_LUẬN` Ba kịch bản hữu ích khi chúng khác nhau ở **nguyên nhân kinh tế**, không phải chỉ nhân đôi hay chia đôi một con số. Mỗi kịch bản cần một câu chuyện: điều gì khiến tăng trưởng thấp, WACC cao, biên lợi nhuận đổi.

`KỊCH_BẢN` Dùng mô hình 011 (FCF0 = 85.904 triệu USD từ [10-K FY2025 Apple](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm), tiền ròng +33.763, 14.776,353 triệu cổ phiếu). Các giả định dưới đây **không phải dự báo**; FCF0 là FCF thô chưa chuẩn hóa thuế một lần (011 mục 5), nên mọi kịch bản có thể thiên thấp:

| Kịch bản | Tăng trưởng FCF năm 1–5 | WACC | g dài hạn | Câu chuyện giả định |
|---|---|---:|---:|---|
| Thấp hơn cơ sở | 2% đều | 9,8% | 2% | Doanh số thiết bị chững, cạnh tranh và quy định làm yếu dịch vụ, rủi ro cao hơn |
| Cơ sở | 6; 5,5; 5; 4,5; 4% | 8,8% | 3% | Tăng trưởng giảm dần về mức danh nghĩa nền kinh tế |
| Thuận lợi | 9; 8,5; 8; 7; 6% | 8,3% | 3,5% | Dịch vụ tăng nhanh, rủi ro thấp hơn |

`PHÉP_TÍNH` (chạy `valuation.py`)

| Kịch bản | EV (triệu USD) | TV/EV | Giá mỗi cổ phần (USD) |
|---|---:|---:|---:|
| Thấp hơn cơ sở | 1.123.360 | 69,2% | **78,3** |
| Cơ sở | 1.667.254 | 76,6% | **115,1** |
| Thuận lợi | 2.229.437 | 80,8% | **153,2** |

Nhận xét: khoảng giá `153,2/78,3 ≈ 1,96` lần. Một "giá trị hợp lý" duy nhất che mất khoảng này. **Cả ba đều là kịch bản có tăng trưởng dương**; không kịch bản nào là đáy. Thêm một kịch bản đuôi (FCF **giảm** 3%/năm, WACC 9,8%, g 1%) cho ≈ 58,5 USD. Đối chiếu thực tế: `SỰ_THẬT` theo [10-Q quý 3 FY2026 của Apple](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000020/aapl-20260627.htm) (kỳ kết thúc 27/06/2026; doanh thu 109.417 so với 94.036, +16%; dịch vụ 30.739 so với 27.423, +12,1%; mở 31/10/2026) (tăng trưởng doanh thu, khác đại lượng với tăng trưởng FCF của mô hình). Với số đó, tăng trưởng 2% không phải "bất lợi vừa" mà là rất xa quỹ đạo gần đây; vì vậy tên cột là "thấp hơn cơ sở".

## 2. Xác suất gán cho kịch bản: một giả định, không phải dữ kiện

`SUY_LUẬN` Gán xác suất rồi lấy trung bình có trọng số cho cảm giác chính xác. Nhưng xác suất ở đây là **ý kiến chủ quan chưa được kiểm chứng**; dữ liệu lịch sử của Apple không cho tần suất của các kịch bản này.

`PHÉP_TÍNH` Ba bộ trọng số khác nhau cho cùng ba giá trị:

| Thấp hơn cơ sở / Cơ sở / Thuận lợi | Giá trị kỳ vọng (USD) |
|---|---:|
| 25% / 50% / 25% | 115,4 |
| 40% / 40% / 20% | 108,0 |
| 20% / 40% / 40% | 123,0 |

Chỉ đổi cảm giác lạc quan đã làm giá trị kỳ vọng đổi `(123,0−108,0)/115,4 ≈ 13%`. Cách dùng đúng: **không báo cáo giá trị kỳ vọng như một số cứng**; báo cáo khoảng giá và nêu bộ trọng số chỉ là minh họa. Nếu không có cơ sở dữ liệu cho xác suất, dùng trọng số bằng nhau và ghi `CHƯA_BIẾT`.

## 3. Biên an toàn: định nghĩa, phép tính, giới hạn

`Ý_KIẾN` Khái niệm biên an toàn (*margin of safety*) gắn với Graham và Dodd (*Security Analysis*, 1934, theo [Wikipedia](https://en.wikipedia.org/wiki/Margin_of_safety_(financial)), nguồn thứ cấp, sửa lần cuối 25/03/2026): mua với giá thấp hơn giá trị ước tính để có đệm cho sai sót. Buffett nhắc nguyên tắc này trong [thư cổ đông 1992](https://www.berkshirehathaway.com/letters/1992.html). Nguồn không nêu mức MoS cố định. `CHƯA_BIẾT` Chưa đối chiếu với sách gốc của Graham trong [danh sách đọc](../reading-list.md).

`PHÉP_TÍNH` Định nghĩa dùng trong bài: `MoS = (V − P)/V`, với V là giá trị mô hình, P là giá thị trường. Với V cơ sở = 115,1:

| P (USD; 345 là giá đóng cửa 30/10/2026 theo nguồn thứ cấp, các mức khác giả định) | MoS so với cơ sở | Chênh lệch giá nếu giá hội tụ ngay về 78,3 (không phải lãi/lỗ thực): `(78,3−P)/P` |
|---:|---:|---:|
| 90 | 21,8% | −13,0% |
| 115,1 | 0% | −32,0% |
| 150 | −30,3% | −47,8% |
| 345 | ≈ −200% | −77,3% |

Cách đọc: dòng 345 cho MoS rất âm vì bộ giả định cơ sở của bài thấp hơn nhiều so với giá thị trường quan sát; điều đó cho thấy mô hình bất đồng mạnh với thị trường (xem 011 mục 6), **không** nói cổ phiếu đắt hay rẻ. MoS dương so với kịch bản cơ sở **không** bảo đảm không lỗ: nếu kịch bản thấp hơn cơ sở xảy ra và giá hội tụ ngay về 78,3, giá vẫn thấp hơn 13% so với P = 90. MoS dương chỉ nghĩa là mô hình cơ sở cho giá trị cao hơn giá; nó không trả lời câu hỏi mô hình có đúng không.

Biên an toàn cần lớn hơn khi: TV chiếm phần lớn EV (mục 1: 69–81%); bảng độ nhạy dải rộng (011: từ 88,8 đến 168,9); dữ liệu lịch sử ngắn; doanh nghiệp có rủi ro tập trung. `Ý_KIẾN` Không có "MoS đủ" cố định như 30%; mức đủ phụ thuộc mức độ tự tin vào mô hình, và sự tự tin đó thường quá cao.

## 4. Chi phí, thuế và thanh khoản

`SUY_LUẬN` Kết quả thực của người đầu tư là kết quả **sau chi phí**. Chi phí gồm phí giao dịch, thuế, chênh lệch giá mua–bán và chi phí cơ hội. Mức phí, thuế khác nhau theo thị trường và thay đổi theo thời gian; xem B1 và L3 và kiểm nguồn hiện hành.

`KỊCH_BẢN` Giả định tổng chi phí khứ hồi 1% (phí + thuế + chênh lệch), lãi gộp 20%: `(1+0,20)×(1−0,01)−1 = 18,8%` (xấp xỉ, minh họa). Với giao dịch thường xuyên, chi phí cộng dồn; với quỹ, phí quản lý hằng năm cộng dồn hơn nhiều (xem N5). Thanh khoản: nếu cổ phiếu ít giao dịch, không bán được tại giá mong muốn; kịch bản xấu có thể xảy ra cùng lúc với thanh khoản khô (xem H3).

## 5. Điều kiện bác bỏ: viết trước, đo được

## Ví dụ từ nguồn thật

`SỰ_THẬT` Từ [10-K Apple FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm): doanh thu dịch vụ 109.158 và giá vốn dịch vụ 26.844 triệu USD, biên gộp dịch vụ **75,4%** (FY2024: 73,9%); doanh thu sản phẩm 307.003, giá vốn 194.116, biên gộp sản phẩm **36,8%** (FY2024: 37,2%). `PHÉP_TÍNH` Lợi nhuận gộp: sản phẩm `307.003−194.116 = 112.887`; dịch vụ `109.158−26.844 = 82.314`; tổng 195.201. Dịch vụ chiếm `82.314/195.201 ≈ 42,2%` lợi nhuận gộp dù chỉ khoảng 26,2% doanh thu: luận điểm "dịch vụ bù thiết bị" dựa vào đúng con số này.

`KỊCH_BẢN` Điều kiện bác bỏ cho luận điểm mô hình cơ sở, viết dưới dạng quan sát được (ngưỡng là giả định bài học):

| Điều kiện | Ngưỡng giả định | Nguồn kiểm | Hành động |
|---|---|---|---|
| Biên gộp dịch vụ | dưới 70% trong hai năm liên tiếp | 10-K hằng năm | Chạy lại kịch bản thấp hơn cơ sở |
| Tăng trưởng doanh thu dịch vụ | dưới 5% hai năm liên tiếp | 10-K, 10-Q | Hạ chuỗi tăng trưởng |
| Tỷ lệ FCF sau SBC / doanh thu (FY2025: `85.904/416.161 ≈ 20,6%`, FCF thô chưa chuẩn hóa thuế, xem 011 mục 5) | dưới 15% | Dòng tiền, SBC | Xem lại giả định FCF0 |
| Quyết định pháp lý/quy định làm mất hoặc giảm khoản thu dịch vụ | ước tính mất trên 5% doanh thu dịch vụ (ngưỡng giả định) | 10-K, 10-Q, hồ sơ cơ quan quản lý | Viết lại giả định dịch vụ |

Mỗi điều kiện có **một con số, một nguồn, một hành động**. Điều kiện kiểu "nếu triển vọng xấu đi" là vô dụng vì không đo được.

## 6. Kiểm tra trước thất bại (pre-mortem)

Trước khi kết luận, viết một đoạn: "Một năm sau tôi sai. Nguyên nhân khả dĩ nhất là…". `Ý_KIẾN` Ba nguyên nhân hay gặp (không có nguồn thống kê): giả định g dài hạn quá cao; xử lý SBC hoặc cầu nối sai; sự kiện bên ngoài mô hình (pháp lý, địa chính trị). Ghi vào nhật ký (015) kèm ngày.

## Năm câu hỏi khi đọc

1. Ba kịch bản khác nhau ở nguyên nhân kinh tế hay chỉ khác một con số?
2. Xác suất có dữ liệu kiểm chứng hay chỉ là ý kiến?
3. Biên an toàn tính trên giá trị nào, và mô hình đã tính cách mình có thể sai chưa?
4. Chi phí, thuế, thanh khoản đã vào kết quả chưa?
5. Điều kiện bác bỏ có số, nguồn và hành động không?

## Bài tập — làm trước khi mở đáp án

1. Ba giá trị 78,3; 115,1; 153,2 với xác suất 30/50/20: giá trị kỳ vọng?
2. Cùng giá trị, xác suất 20/50/30: giá trị kỳ vọng và chênh so với câu 1?
3. P = 100, V = 115,1: tính MoS.
4. P = 100 và giá trị kịch bản thấp hơn cơ sở 78,3: chênh lệch giá nếu giá hội tụ ngay về giá trị đó?
5. Chi phí khứ hồi 1,5%, lãi gộp 12%: lãi sau chi phí (cách nhân)?
6. Viết lại điều kiện "doanh nghiệp xấu đi" thành điều kiện đo được, có số, nguồn, hành động.
7. Vì sao giá trị kỳ vọng ở câu 1 không nên báo cáo là "giá trị đúng"?
8. Chạy `valuation.py`: kịch bản thấp hơn cơ sở nếu đổi g dài hạn từ 2% sang 1% thì giá mỗi cổ phần là bao nhiêu? (tính tay một bước kiểm tra TV).
9. (Chuyển giao) Chọn doanh nghiệp bạn quen; viết ba kịch bản với câu chuyện khác nhau về nguyên nhân kinh tế.
10. (Chuyển giao) Cho doanh nghiệp ở câu 9, viết bốn điều kiện bác bỏ và nguồn kiểm.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` `0,3×78,3 + 0,5×115,1 + 0,2×153,2 = 23,49 + 57,55 + 30,64 = 111,68`.
2. `0,2×78,3 + 0,5×115,1 + 0,3×153,2 = 15,66 + 57,55 + 45,96 = 119,17`; chênh `7,49` (≈ 6,7%).
3. `(115,1−100)/115,1 ≈ 13,1%`.
4. `(78,3−100)/100 = −21,7%`.
5. `1,12×0,985−1 = 10,32%`.
6. Ví dụ đạt: "Biên gộp dịch vụ dưới 70% trong hai năm liên tiếp theo 10-K → chạy lại kịch bản thấp hơn cơ sở." Phải có số, nguồn, hành động.
7. Xác suất chủ quan; chỉ đổi trọng số làm kết quả đổi nhiều (câu 1 và 2); báo cáo khoảng.
8. `PHÉP_TÍNH` ≈ 71,9 USD (so với 78,3 khi g = 2%). Kiểm tay: `TV = FCF5×(1+g)/(WACC−g)`; g nhỏ hơn làm TV giảm, vì tử `×1,01` thay `×1,02` và mẫu `0,098−0,01` thay `0,098−0,02`.
9. Rubric: ba câu chuyện khác nguyên nhân (3đ); giả định số khớp câu chuyện (2đ); có ghi `KỊCH_BẢN` (1đ).
10. Rubric: mỗi điều kiện có số, nguồn, hành động (4đ).

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty Theta có ba kịch bản: giá trị 60, 100, 160. Xác suất do chuyên gia nói là 20%, 50%, 40%. Giá thị trường 85. Biên an toàn bao nhiêu và có nên mua?"

Phát hiện: (a) xác suất cộng 110%, không hợp lệ; (b) nguồn xác suất và cơ sở dữ liệu không rõ; (c) giá trị tính bằng đồng tiền, kỳ nào, trước hay sau chi phí; (d) "có nên mua" là câu hỏi cá nhân hóa, không trả lời được từ đề.

`Đáp án` Không tính biên an toàn trước khi sửa xác suất (chuẩn hóa hoặc hỏi lại); nêu chênh lệch khi dùng bộ trọng số khác; không đưa lời khuyên mua bán; báo khoảng và điều kiện bác bỏ.

## Sai ở đâu

Học viên viết: "Giá trị kỳ vọng của Apple là 115,4 USD, giá thị trường 90, biên an toàn 22%, nên lãi chắc chắn. Rủi ro đã được tính vì tôi dùng ba kịch bản. Điều kiện bác bỏ: nếu triển vọng xấu đi thì bán."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. "Lãi chắc chắn": MoS dương so với cơ sở không loại trừ kịch bản thấp hơn cơ sở (giá thấp hơn 13% so với P = 90 nếu giá hội tụ về 78,3).
2. Giá trị kỳ vọng phụ thuộc xác suất chủ quan (mục 2).
3. Ba kịch bản không tự tính mọi rủi ro (pháp lý, địa chính trị, sai mô hình).
4. Điều kiện bác bỏ không đo được, không nguồn, không hành động.
5. Không có chi phí, thuế.
6. Giá 90 là giả định, không phải giá thị trường tại ngày; phải ghi ngày.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Giá trị ba kịch bản 50, 80, 120; xác suất 25/50/25: giá trị kỳ vọng? Giá 70: biên an toàn so với giá trị kỳ vọng và lãi/lỗ nếu xảy ra kịch bản 50?
2. Giải thích vì sao đổi xác suất thành 40/40/20 làm biên an toàn nhỏ đi (nhớ: xác suất cũng là giả định).
3. Viết một điều kiện bác bỏ đo được cho một công ty bạn chọn.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `12,5+40+30 = 82,5`; `MoS = (82,5−70)/82,5 ≈ 15,2%`; `(50−70)/70 ≈ −28,6%`. Câu 2: `0,4×50+0,4×80+0,2×120 = 76` thấp hơn 82,5 nên biên an toàn nhỏ lại (`(76−70)/76 ≈ 7,9%`). Câu 3: có số, nguồn, hành động.

</details>

## Lỗi thường gặp

- Gán xác suất rồi coi kỳ vọng là sự thật.
- Coi MoS dương là bảo đảm không lỗ.
- Ba kịch bản chỉ khác một con số, không khác nguyên nhân kinh tế.
- Quên chi phí, thuế, thanh khoản.
- Điều kiện bác bỏ mơ hồ, viết sau khi đã có kết quả.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa; giá Apple trong bài là giá giả định.
- Mọi giả định tương lai là `KỊCH_BẢN`; kết quả không là dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho thị trường khác, kiểm lại phí, thuế và quy định tại đó.

## Điều tôi vẫn chưa hiểu

- Dữ liệu nào cho phép tôi gán xác suất có cơ sở?
- Ba kịch bản của tôi có bỏ sót sự kiện ngoài mô hình không?
- Điều kiện bác bỏ nào tôi chưa dám viết vì sợ nó xảy ra?

## Nguồn Internet đã mở

Truy cập `2026-10-31` (Apple 10-K). Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; 27/09/2025; triệu USD | Doanh thu, giá vốn, biên gộp, FCF |
Định nghĩa biên an toàn xem mục 3 (nguồn thứ cấp và thư cổ đông 1992). Phép tính tái lập bằng [valuation.py](../practice/models/valuation.py).
