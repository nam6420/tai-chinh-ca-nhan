# Bài F1 — Mô hình liên kết ba báo cáo và độ nhạy

- Ngày viết lại: `2026-10-31`. Bản này **thay thế** bản 2026-10-27; biên bản kiểm cũ gắn mã băm cũ, không còn áp dụng.
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Nguồn số Apple: Form 10-K FY2025 mở ngày `2026-10-31`.
- Mục tiêu: Dựng mô hình ba báo cáo ba năm cho một công ty bán lẻ hư cấu, tự kiểm cân đối; hiệu chỉnh giả định từ báo cáo thật; đọc độ nhạy; nhận ra nhu cầu tài trợ thiếu hụt.
- Bài trước liên quan: [001](001-business-financial-statements.md), [N2](N2-statement-line-items.md), [004](004-cash-flow-and-earnings-quality.md), [005](005-debt-liquidity-survival.md), [011](011-dcf-reverse-dcf.md).
- Thời lượng: 3 phiên (A: mục 1–3; B: mục 4–5; C: mục 6–7 và bài tập).
- Tệp thực hành: [valuation.py](../practice/models/valuation.py), hàm `three_statement()`.
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F1-fact-check.md), [phản biện](../reviews/F1-risk-review.md).
- Câu hỏi cốt lõi: **Một thay đổi ở kết quả kinh doanh đi qua lợi nhuận, vốn lưu động, tiền và bảng cân đối như thế nào, và mô hình báo cho tôi biết điều gì mà một con số riêng lẻ không báo?**

## Hiểu bài này trong 1 phút

Lợi nhuận không đồng nghĩa tiền thu được. Mô hình ba báo cáo ghép ba bảng bằng một sợi dây: kết quả kinh doanh sinh ra lợi nhuận, lợi nhuận cộng khấu hao rồi trừ phần vốn lưu động bị giam thành dòng tiền, dòng tiền làm đổi số dư tiền, và bảng cân đối phải cân. Cân không chứng minh mô hình đúng, nhưng **không cân chắc chắn là sai**. Giá trị lớn nhất của mô hình không nằm ở dự báo mà ở chỗ nó cho thấy: nếu giả định này sai thì tiền ở đâu, nợ ra sao, khi nào thiếu tiền.

## Ôn bài cũ hoặc kiểm tra đầu vào

1. 001: bút toán bán chịu 100 làm tài sản nào tăng, doanh thu tăng bao nhiêu, tiền tăng bao nhiêu?
2. 004: công thức cầu nối từ lợi nhuận sau thuế sang CFO gồm những khoản nào?
3. 005: vì sao công ty có lãi vẫn có thể hết tiền?
4. N2: DSO, DIO, DPO tính bằng công thức nào?

<details>
<summary>Mở sau khi tự làm</summary>

Đáp án ngắn: (1) phải thu tăng 100, doanh thu tăng 100, tiền không đổi; (2) lợi nhuận + khấu hao ± thay đổi vốn lưu động ± khoản khác; (3) vì lợi nhuận bị giam trong phải thu/tồn kho hoặc đầu tư và trả nợ vượt tiền vào; (4) `phải thu/doanh thu×365`, `tồn kho/giá vốn×365`, `phải trả người bán/giá vốn×365`.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Dựng mô hình một công ty hư cấu đủ ba báo cáo, có hàng kiểm cân đối | Không dự báo công ty thật |
| Hiệu chỉnh tỷ số từ báo cáo Apple FY2025 | Không dạy mô hình ngân hàng, bảo hiểm (xem 013) |
| Đọc độ nhạy và nhu cầu tài trợ | Không dựng vòng lặp lãi–nợ (dùng nợ đầu kỳ để tránh) |

## 1. Bốn nguyên tắc

1. **Giả định ở một nơi**: mọi con số tương lai đến từ một bảng giả định, không rải trong công thức.
2. **Một dòng chảy**: lợi nhuận → dòng tiền → tiền → bảng cân đối; không dán số vào bảng cân đối.
3. **Hàng kiểm**: `tài sản − (nợ phải trả + vốn chủ) = 0`; luôn hiển thị.
4. **Tiền là kết quả, không phải giả định**: tiền cuối kỳ là số dư còn lại; nếu âm, công ty cần tài trợ.

## 2. Công ty Delta (hư cấu) — năm gốc

`KỊCH_BẢN` Công ty bán lẻ Delta, đơn vị tỷ đồng, tiền tệ danh nghĩa. Năm gốc:

| Kết quả | Số | Bảng cân đối | Số |
|---|---:|---|---:|
| Doanh thu | 1.000 | Tiền | 100 |
| | | Phải thu | 50 |
| | | Tồn kho | 120 |
| | | Tài sản cố định ròng | 300 |
| | | **Tổng tài sản** | **570** |
| | | Phải trả người bán | 100 |
| | | Nợ vay | 150 |
| | | Vốn chủ | 320 |
| | | **Nợ phải trả + vốn chủ** | **570** |

Năm gốc cân: `570 = 100+150+320`.

Giả định hằng năm (**không phải dự báo**):

| Giả định | Giá trị | Ghi chú |
|---|---:|---|
| Tăng trưởng doanh thu | 8% | |
| Biên gộp | 30% | Giá vốn = 70% doanh thu |
| Chi phí hoạt động (chưa gồm khấu hao) | 18% doanh thu | |
| Khấu hao | 10% tài sản cố định đầu kỳ | |
| Lãi vay | 6% nợ đầu kỳ | Nợ đầu kỳ để tránh vòng lặp |
| Thuế | 20% lợi nhuận trước thuế | |
| DSO | 18,25 ngày | = 50/1.000×365, giữ nguyên |
| DIO | 62,57 ngày | = 120/700×365 |
| DPO | 52,14 ngày | = 100/700×365 |
| Chi đầu tư | 6% doanh thu | |
| Trả nợ gốc | 20/năm | |
| Cổ tức | 40% lợi nhuận sau thuế | |

## 3. Chạy mô hình năm 1 bằng tay

`PHÉP_TÍNH`

- Doanh thu `1.000×1,08 = 1.080`; giá vốn `1.080×0,70 = 756`; chi phí hoạt động `1.080×0,18 = 194,4`; khấu hao `300×0,10 = 30`.
- EBIT `1.080−756−194,4−30 = 99,6`; lãi vay `150×0,06 = 9`; trước thuế `90,6`; thuế `18,12`; **lợi nhuận sau thuế 72,5** (làm tròn).
- Phải thu `1.080×18,25/365 = 54`; tồn kho `756×62,57/365 = 129,6`; phải trả `756×52,14/365 = 108`.
- Thay đổi vốn lưu động ròng `(54−50)+(129,6−120)−(108−100) = 5,6`.
- **CFO** `72,5+30−5,6 = 96,9`. Chi đầu tư `64,8`; trả nợ `20`; cổ tức `0,4×72,5 = 29`.
- Tiền cuối `100+96,9−64,8−20−29 = 83,1`.
- Tài sản cố định `300+64,8−30 = 334,8`; vốn chủ `320+72,5−29 = 363,5`; nợ `130`.
- Kiểm: tài sản `83,1+54+129,6+334,8 = 601,5`; nợ + vốn chủ `108+130+363,5 = 601,5`. **Cân.**

## 4. Kết quả ba năm (công thức giống nhau)

`PHÉP_TÍNH` (chạy `three_statement()`)

| Chỉ tiêu | Năm 1 | Năm 2 | Năm 3 |
|---|---:|---:|---:|
| Doanh thu | 1.080,0 | 1.166,4 | 1.259,7 |
| EBIT | 99,6 | 106,5 | 114,0 |
| Lợi nhuận sau thuế | 72,5 | 79,0 | 85,9 |
| CFO | 96,9 | 106,4 | 116,5 |
| Chi đầu tư | 64,8 | 70,0 | 75,6 |
| Tiền cuối kỳ | 83,1 | 67,9 | 54,5 |
| Nợ vay | 130 | 110 | 90 |
| Vốn chủ | 363,5 | 410,9 | 462,4 |
| Tổng tài sản | 601,5 | 637,5 | 678,4 |
| Kiểm cân đối | 0,0 | 0,0 | 0,0 |

Điều mô hình báo ngoài lợi nhuận tăng đều: **tiền giảm đều** (100 → 54,5) dù lợi nhuận tăng, vì chi đầu tư, trả nợ và cổ tức cộng lại lớn hơn CFO. Mô hình cho thấy một câu chuyện mà bảng lợi nhuận một mình không cho thấy.

## 5. Độ nhạy: đổi một biến, đọc cả ba bảng

`PHÉP_TÍNH`

| Kịch bản | Tiền cuối năm 3 | Lợi nhuận sau thuế năm 3 | Ghi chú |
|---|---:|---:|---|
| Cơ sở | 54,5 | 85,9 | |
| Biên gộp 27% (thay 30%) | **2,9** | 55,7 | Lợi nhuận giảm 35%, tiền gần hết |
| Tăng trưởng 0% | 72,9 | 62,2 | Tiền ít giảm hơn nhờ vốn lưu động không phình |
| Tăng trưởng 12%, chi đầu tư 9%, cổ tức 60% (cả ba cùng đổi) | **−114,9** | 93,9 | Lợi nhuận tăng nhưng tiền âm từ năm 2 |
| Chỉ tăng trưởng 12% | 44,2 | — | Vốn lưu động và chi đầu tư 6% theo doanh thu |
| Chỉ chi đầu tư 9% | **−45,7** | — | Chi đầu tư cao là yếu tố lớn nhất |
| Chỉ cổ tức 60% | 7,0 | — | |

Đọc kết quả: (1) biên gộp giảm 3 điểm đã đủ làm tiền gần hết sau 3 năm; (2) kịch bản ba biến cùng đổi có lợi nhuận cao nhất nhưng **tiền âm từ năm 2 (−40,1)**: công ty cần vay thêm hoặc cắt cổ tức. Tách từng biến cho thấy nguyên nhân chính là **giả định chi đầu tư 9% doanh thu** (một mình kéo tiền năm 3 xuống −45,7), tiếp theo là cổ tức 60% (7,0), còn riêng tăng trưởng 12% với chi đầu tư 6% thì tiền vẫn dương (44,2). Bài học: đừng gán nguyên nhân cho một biến khi nhiều biến cùng đổi; tách từng biến. Hàng "tăng trưởng 0%" giữ chi đầu tư 6% doanh thu (gấp đôi khấu hao) nên không thực tế; nếu doanh thu đứng yên, chi đầu tư hợp lý gần khấu hao. Tiền âm không phải lỗi mô hình mà là kết quả cần đọc: nó là nhu cầu tài trợ.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Hiệu chỉnh giả định từ [Form 10-K FY2025 của Apple](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (27/09/2025, US GAAP, triệu USD): doanh thu 416.161; giá vốn `194.116+26.844 = 220.960`; lợi nhuận gộp 195.201; thu nhập hoạt động 133.050; thuế 20.719 trên lợi nhuận trước thuế 132.729; phải thu 39.777; tồn kho 5.718; phải trả người bán 69.860; chi mua tài sản cố định 12.715; khấu hao 11.698; cổ tức 15.421; mua lại cổ phiếu 90.711; lợi nhuận sau thuế 112.010.

`PHÉP_TÍNH` Tỷ số tương ứng với bảng giả định của Delta:

| Giả định | Công thức | Apple FY2025 |
|---|---|---:|
| Biên gộp | `195.201/416.161` | 46,9% |
| Chi phí hoạt động/doanh thu | `(195.201−133.050)/416.161` | 14,9% |
| Thuế suất hiệu dụng | `20.719/132.729` | 15,6% |
| DSO | `39.777/416.161×365` | 34,9 ngày |
| DIO (trên giá vốn) | `5.718/220.960×365` | 9,4 ngày |
| DPO (trên giá vốn) | `69.860/220.960×365` | 115,4 ngày |
| Chi đầu tư/doanh thu | `12.715/416.161` | 3,1% |
| Khấu hao/doanh thu | `11.698/416.161` | 2,8% |
| Cổ tức/lợi nhuận sau thuế | `15.421/112.010` | 13,8% |
| Mua lại cổ phiếu/lợi nhuận sau thuế | `90.711/112.010` | 81,0% |

Điều đáng học: (1) `DSO+DIO−DPO ≈ 34,9+9,4−115,4 = −71,1` ngày nếu chỉ dùng phải thu thương mại. Nhưng 10-K còn ghi **phải thu phi thương mại từ nhà cung cấp** 33.180 (Note 4 của 10-K mô tả đây là khoản phải thu từ một số nhà sản xuất đối tác do bán linh kiện cho họ; bài chưa kiểm cơ chế chi tiết), tương đương `33.180/416.161×365 ≈ 29,1` ngày doanh thu; cộng vào, chu kỳ còn khoảng **−42 ngày**, và vốn lưu động ròng `39.777+33.180+5.718−69.860 = +8.815` (dương), thay vì −24.365 khi bỏ khoản này. `SUY_LUẬN` Phải trả người bán có thể còn gồm khoản mua không thuộc giá vốn (chi phí hoạt động, tài sản cố định) nên DPO trên giá vốn có thể bị thổi lớn. `SUY_LUẬN` Vì vậy kết luận "chu kỳ tiền mặt âm, tăng trưởng sinh tiền" **phụ thuộc cách đo và độ lớn rất nhỏ** so với CFO 111.482; không dùng nó làm bằng chứng Apple "được nhà cung cấp tài trợ". Điều chắc chắn hơn: **không thể dùng nguyên giả định của Delta cho Apple**. (2) Apple trả cổ đông gần như toàn bộ lợi nhuận (cổ tức + mua lại = `15.421+90.711 = 106.132`, 94,8% lợi nhuận) nhưng phần lớn qua mua lại cổ phiếu, không phải cổ tức: một mô hình chỉ có "payout cổ tức" sẽ bỏ sót. So với dòng tiền, chi trả này bằng `106.132/98.767 ≈ 107%` FCF thô và `≈ 124%` FCF sau SBC: Apple chi cổ đông nhiều hơn dòng tiền tự do năm đó. `SUY_LUẬN` Phần chênh có thể lấy từ tiền và chứng khoán; nhưng FCF này là FCF thô bị kéo thấp bởi thuế nộp tiền mặt vượt chi phí thuế (khoảng 22.650, xem 011 mục 5), nên nếu chuẩn hóa thì tỷ lệ chi trả/FCF thô chỉ khoảng 87% (`106.132/(98.767+22.650) ≈ 87,4%`; `CHƯA_BIẾT` phần một lần thật sự). `SỰ_THẬT` Theo 10-K FY2025 (báo cáo dòng tiền, hoạt động tài chính), Apple còn chi 5.960 triệu USD thuế liên quan thanh toán ròng cổ phiếu thưởng; chưa tính khoản này (cộng vào chi trả thì khoảng 92%). Mô hình Delta không có lãi tiền gửi hay vay bù, nên không mô tả được hành vi này. `CHƯA_BIẾT` Chưa kiểm tra vì sao DPO cao (điều khoản nhà cung cấp, loại hàng); phải đọc thuyết minh.

## 6. Giả định từ lịch sử: cách hiệu chỉnh

1. Lấy ít nhất 3–5 năm dữ liệu cùng chuẩn và kỳ; tính từng tỷ số mỗi năm, không chỉ năm gần nhất.
2. Tìm xu hướng và ngoại lệ (năm có sự kiện bất thường). Giải thích vì sao tương lai giống hoặc khác.
3. Cho giả định **một lý do kinh tế**: giá vốn tăng vì gì, DSO đổi vì chính sách tín dụng nào.
4. Ghi nguồn từng giả định (báo cáo, quý, thuyết minh) và đánh dấu `Ý_KIẾN` nếu là phán đoán.
5. Kiểm tính hợp lý: tăng trưởng dài hạn không vượt nhiều so với nền kinh tế; biên không tăng mãi.

## Năm câu hỏi khi đọc

1. Bảng cân đối có cân không, và có hàng kiểm không?
2. Tiền là kết quả hay bị gán cứng?
3. Giả định tăng trưởng có đi cùng đủ vốn lưu động và chi đầu tư?
4. Lãi vay dùng nợ đầu kỳ, bình quân hay có vòng lặp, và có nêu không?
5. Nếu tiền âm, mô hình xử lý nhu cầu tài trợ thế nào?

## Bài tập — làm trước khi mở đáp án

1. Tính tay năm 1 của Delta nếu doanh thu tăng 5% (các giả định khác không đổi): doanh thu, EBIT, lợi nhuận sau thuế.
2. Cùng giả định câu 1: tính phải thu, tồn kho, phải trả và thay đổi vốn lưu động ròng.
3. Tiếp tục: CFO năm 1 và tiền cuối kỳ.
4. Kiểm cân đối năm 1 cho câu 1–3: tài sản bằng nợ + vốn chủ?
5. Tính khấu hao năm 2 của Delta (cơ sở), biết tài sản cố định cuối năm 1 là 334,8.
6. Vì sao tiền của Delta giảm dù lợi nhuận tăng (cơ sở)? Chỉ ra ba khoản.
7. Với biên gộp 27%, vì sao lợi nhuận sau thuế năm 3 giảm 35% còn doanh thu không đổi?
8. Từ bảng tỷ số Apple: tính chu kỳ tiền mặt (DSO+DIO−DPO) chỉ với phải thu thương mại, rồi thêm phải thu phi thương mại từ nhà cung cấp 33.180; nêu vì sao hai kết quả đưa tới hai kết luận khác nhau.
9. (Chuyển giao) Chọn một công ty bán lẻ niêm yết; lấy 3 năm số liệu, tính bảng tỷ số như mục Ví dụ từ nguồn thật.
10. (Chuyển giao) Dựa vào câu 9, dựng giả định ba năm có lý do cho từng tỷ số và chạy `three_statement()`; nộp bảng ba báo cáo và hàng kiểm.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` Doanh thu `1.050`; giá vốn `735`; chi phí hoạt động `189`; khấu hao `30`; EBIT `1.050−735−189−30 = 96`; lãi `9`; trước thuế `87`; thuế `17,4`; sau thuế `69,6`.
2. Phải thu `1.050×18,25/365 = 52,5`; tồn kho `735×62,57/365 = 126`; phải trả `735×52,14/365 = 105`. Thay đổi vốn lưu động `(52,5−50)+(126−120)−(105−100) = 3,5`.
3. CFO `69,6+30−3,5 = 96,1`; chi đầu tư `1.050×0,06 = 63`; trả nợ 20; cổ tức `0,4×69,6 = 27,84`; tiền cuối `100+96,1−63−20−27,84 = 85,26`.
4. Tài sản cố định `300+63−30 = 333`; vốn chủ `320+69,6−27,84 = 361,76`; nợ 130. Tài sản `85,26+52,5+126+333 = 596,76`; nợ + vốn chủ `105+130+361,76 = 596,76`. Cân.
5. `334,8×0,10 = 33,48`.
6. Chi đầu tư (64,8 → 75,6), trả nợ gốc (20/năm) và cổ tức (29 → 34,4) cộng lại lớn hơn CFO (năm 1: `113,8 > 96,9`). Vốn lưu động tăng đã nằm trong CFO nên không tính thêm như một khoản riêng.
7. Giảm 3 điểm biên gộp trên doanh thu 1.259,7 làm lợi nhuận gộp giảm `37,8`. Trong mô hình chi phí hoạt động chỉ bằng 18% doanh thu (biến phí), nên EBIT giảm đúng 37,8, từ 114,0 xuống 76,2 (−33%), vì biên EBIT ban đầu mỏng (`114,0/1.259,7 ≈ 9%`). Lãi vay cố định 6,6 làm lợi nhuận trước thuế giảm thêm về tỷ lệ (đòn bẩy **tài chính**); lợi nhuận sau thuế giảm 35%. Đây **không** phải đòn bẩy vận hành (cần chi phí cố định lớn trong cơ cấu chi phí; mô hình này chỉ có khấu hao và lãi vay là chi phí cố định). Bài học: biên mỏng khuếch đại mọi sai số biên.
8. `34,9+9,4−115,4 ≈ −71,1` ngày; thêm `33.180/416.161×365 ≈ 29,1` ngày thì còn khoảng `−42,0` ngày, và vốn lưu động ròng đổi từ −24.365 sang +8.815. Hai cách đo cho độ lớn và dấu tác động khác nhau; vì vốn lưu động chỉ là phần nhỏ so với CFO, không nên kết luận mạnh về "nhà cung cấp tài trợ"; cần đọc thuyết minh.
9. Rubric: nêu kỳ, đơn vị, tiền tệ, nguồn (2đ); tính đủ 8–10 tỷ số cho 3 năm (3đ); nêu năm ngoại lệ (1đ).
10. Rubric: mỗi giả định có lý do (3đ); hàng kiểm bằng 0 (2đ); đọc tiền và nhu cầu tài trợ (1đ).

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty Iota năm 1: doanh thu 500, lợi nhuận 60, khấu hao 20, tăng phải thu 40. Công ty cho biết dòng tiền hoạt động là 55. Hãy dựng bảng cân đối năm 2 với tăng trưởng 10%."

Phát hiện: (a) CFO theo cầu nối `60+20−40 = 40`, không phải 55; chênh 15 chưa giải thích (tồn kho, phải trả, khoản khác); (b) thiếu bảng cân đối năm gốc; (c) thiếu giá vốn, nợ, thuế, cổ tức; (d) kỳ và đơn vị không nêu.

`Đáp án` Không dựng được bảng cân đối khi thiếu năm gốc. Phải yêu cầu bảng cân đối và thuyết minh dòng tiền; đối chiếu CFO 55 với cầu nối bằng cách tìm 15 còn lại; ghi `CHƯA_BIẾT` cho đến khi có. Không điền số bằng trí nhớ.

## Sai ở đâu

Học viên viết: "Doanh thu tăng 8% nên mọi khoản tăng 8%: giá vốn, phải thu, tài sản cố định. Lãi vay tính trên nợ cuối kỳ, nợ cuối kỳ phụ thuộc tiền, tiền tính từ lợi nhuận, nên em để tiền bằng 100 cho đơn giản. Bảng cân đối lệch 12 nên em cộng 12 vào vốn chủ."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. Gán cứng tiền = 100 phá nguyên tắc "tiền là kết quả"; bảng cân đối lệch vì tiền không theo dòng tiền.
2. Cộng 12 vào vốn chủ là "chèn số cho cân"; che đi lỗi thật.
3. Tăng mọi khoản 8% bỏ qua khấu hao và chi đầu tư của tài sản cố định, thay đổi vốn lưu động phụ thuộc DSO/DIO/DPO.
4. Lãi vay trên nợ cuối kỳ gây vòng lặp; cần nêu rõ chọn nợ đầu kỳ hoặc bình quân.
5. Không có hàng kiểm và không ghi giả định.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Lợi nhuận sau thuế 50, khấu hao 10, phải thu tăng 8, tồn kho tăng 4, phải trả tăng 6: tính CFO. Nếu chi đầu tư 15, trả nợ 5, cổ tức 20, tiền đổi bao nhiêu?
2. Nếu tiền cuối kỳ âm 30, mô hình cho bạn biết điều gì và bạn làm gì?
3. Nêu hai việc phải làm trước khi dùng giả định DSO của một công ty khác cho công ty mình.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `CFO = 50+10−8−4+6 = 54`; tiền đổi `54−15−5−20 = +14`. Câu 2: nhu cầu tài trợ 30; kiểm lại giả định (cổ tức, đầu tư, tăng trưởng) và nêu nguồn tài trợ. Câu 3: so sánh mô hình kinh doanh và điều khoản bán chịu; kiểm kỳ và định nghĩa phải thu.

</details>

## Lỗi thường gặp

- Gán cứng tiền hoặc chèn số cho bảng cân đối cân.
- Quên khấu hao khi chuyển từ lợi nhuận sang tiền.
- Tăng trưởng nhưng vốn lưu động và chi đầu tư không đổi.
- Lãi vay vòng lặp không nêu cách xử lý.
- Dùng giả định của doanh nghiệp khác cơ cấu.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số Delta hoàn toàn hư cấu; số Apple là số lịch sử đã công bố, không là dự báo.
- Trước khi áp dụng cho thị trường khác, kiểm lại chuẩn kế toán và định nghĩa tại đó.

## Điều tôi vẫn chưa hiểu

- Khi nào cần mô hình hàng quý thay vì hằng năm?
- Doanh nghiệp có nhiều bộ phận thì tôi gộp hay tách?
- Tôi xử lý vòng lặp lãi–nợ thế nào khi cần chính xác hơn?

## Nguồn Internet đã mở

Truy cập `2026-10-31`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; 27/09/2025; triệu USD | Tỷ số thật ở mục Ví dụ từ nguồn thật |

Công ty Delta và Iota hoàn toàn hư cấu. Phép tính tái lập bằng [valuation.py](../practice/models/valuation.py). `CHƯA_BIẾT` Chưa có nguồn bên ngoài cho nguyên tắc kỹ thuật dựng mô hình; đây là thực hành tiêu chuẩn do người soạn tổng hợp, cần nguồn khi kiểm duyệt.
