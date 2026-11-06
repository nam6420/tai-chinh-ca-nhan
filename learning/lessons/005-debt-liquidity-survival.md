# Bài 005: Nợ, thanh khoản và khả năng sống sót

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 10:45 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc được cơ cấu nợ và lịch đáo hạn của một doanh nghiệp; tính bốn tỷ lệ sống còn và biết ngưỡng nào là nguy hiểm; hiểu thuê tài sản trở thành nợ trên bảng cân đối khi nào; so sánh được hai cách huy động vốn (vay hay phát hành cổ phiếu) trên cùng một ví dụ số học; nhận ra điều khoản vay (covenant) là rủi ro thật chứ không phải chi tiết hợp đồng.
- Thời lượng: 35 phút đọc + 40 phút bài tập (2 phiên)
- Bài trước liên quan: Thứ tự đọc **Bước 11/23 của Nhánh 1** — học ngay sau [Bài 004: Dòng tiền và chất lượng lợi nhuận](004-cash-flow-and-earnings-quality.md) (kế thừa [Bài 001](001-business-financial-statements.md) và [Bài N2](N2-statement-line-items.md)). Học tiếp: [Bài 006: Phân bổ vốn và quản trị](006-capital-allocation-governance.md) (Bước 12/23).
- Câu hỏi cốt lõi: **Doanh nghiệp có thể trả nợ trong 12–24 tháng tới bằng nguồn tiền nào?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Mọi ví dụ số học là hư cấu. Bài này kế thừa Bài 001 và Bài 004; nó chuẩn bị cho Bài 009 (bội số EV/EBITDA) và Bài 013 (ngân hàng).

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Một người vay 70% giá nhà với lãi suất 4,5%/năm, thu nhập hằng tháng trả lãi đúng bằng 45% lương. Ngân hàng vẫn cho vay vì giá trị tài sản bảo đảm lớn. Nhưng nếu lãi suất thả nổi tăng 2 điểm phần trăm, khoản trả hằng tháng vượt 60% lương và người đó bắt đầu dùng tiền ăn để trả lãi. **Tài sản vẫn còn đó, nhưng dòng tiền đã hết** — và đó là lúc vỡ.

Với doanh nghiệp cũng vậy. Nợ không xấu; nợ là một cách huy động vốn có lá chắn thuế và không pha loãng cổ đông. Nhưng nợ biến **rủi ro kinh doanh** thành **rủi ro sống còn**: doanh nghiệp không có nợ có thể lỗ ba năm và vẫn tồn tại; doanh nghiệp vay nhiều có lãi nhưng chỉ cần một năm dòng tiền yếu là mất quyền kiểm soát.

> Câu cần nhớ: **Nợ không giết doanh nghiệp trong năm xấu; lịch đáo hạn mới giết.**

## Ôn bài cũ (5 phút)

Ôn lại bài liền trước trong lộ trình Nhánh 1 là [Bài 004 — Dòng tiền và chất lượng lợi nhuận](004-cash-flow-and-earnings-quality.md) (cùng nền tảng từ [Bài 001](001-business-financial-statements.md)). Trả lời trước khi đọc tiếp (đáp án ở mục 9):

1. Theo [Bài 004](004-cash-flow-and-earnings-quality.md), nếu phải thu khách hàng tăng 100 trong năm, dòng tiền hoạt động (`CFO`) thay đổi bao nhiêu và theo chiều nào?
2. Vì sao "`CFO` âm" không đồng nghĩa "doanh nghiệp lỗ" ([Bài 001](001-business-financial-statements.md) & [Bài 004](004-cash-flow-and-earnings-quality.md))?
3. Với doanh nghiệp thuê nhiều cửa hàng, vì sao dòng tiền tự do tính bằng `CFO − capex` ([Bài 004](004-cash-flow-and-earnings-quality.md)) có thể **cao hơn** tiền thật để lại?
4. Nêu một lý do cần đọc 5 năm thay vì 1 năm khi đánh giá chất lượng lợi nhuận ([Bài 004](004-cash-flow-and-earnings-quality.md)).

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy đọc cơ cấu nợ, lịch đáo hạn, bốn tỷ lệ sống còn | Không tính chi phí vốn (WACC) — đó là Bài 010 |
| Dạy vì sao thuê tài sản là nợ (IFRS 16) và nó đổi bội số thế nào | Không dạy thiết kế cấu trúc vốn tối ưu (không có cấu trúc "tối ưu" chung) |
| So sánh vay với phát hành cổ phiếu bằng số học | Không khuyến nghị doanh nghiệp nên vay hay nên phát hành |
| Dạy đọc điều khoản vay và hạn mức tín dụng | Không phân tích ngân hàng (Bài 013) |

## Cách chia phiên và chọn phần cốt lõi

**Bài cốt lõi trong bộ bài tập:** 1, 3, 4. Các câu còn lại là luyện thêm; không bỏ kiến thức bắt buộc của thân bài. Phiên A làm câu 1, 3; phiên B làm câu 4.

`Ý_KIẾN` Phiên A: mục 1–3, phân biệt nợ và dựng một tình huống trả lãi. Phiên B: điều khoản vay, gốc đến hạn, vay/phát hành và dự phòng thanh khoản; nối với bảng nợ thực hành, không dừng ở một hệ số trả lãi.

Làm câu cốt lõi theo mục tiêu phiên trước khi xem đáp án; câu xen kẽ/chuyển giao kiểm hiểu sâu. Có thể dừng giữa bài; thời lượng ban đầu chưa được đo với người học. [Bảng thực hành và hai bài ôn](../practice/research-and-model-worksheets.md).

## 1. Nợ trông như thế nào trên báo cáo

`SUY_LUẬN` Nợ phải trả trên bảng cân đối gồm nhiều thứ rất khác nhau về mức độ nguy hiểm. Cách đọc thực dụng: phân loại theo **ba câu hỏi** — có trả lãi không, khi nào phải trả, và có thể bị gọi nợ trước hạn không.

| Loại | Ví dụ | Trả lãi | Vì sao đáng chú ý |
|---|---|---|---|
| Nợ vay ngân hàng | Vay ngắn hạn, vay đầu tư dự án | Có | Thường có tài sản bảo đảm và điều khoản |
| Trái phiếu | Trái phiếu doanh nghiệp | Có | Có ngày đáo hạn cứng, không gia hạn tự động |
| Nợ thuê tài sản (IFRS 16) | Thuê cửa hàng 10 năm | Có (phần lãi) | Trước 2019 phần lớn nằm ngoài bảng cân đối |
| Phải trả người bán | Công nợ nhà cung cấp | Không | Không trả lãi nhưng mất uy tín thì mất hàng |
| Nợ tiềm ẩn | Bảo lãnh, cam kết ngoài bảng | Tùy | Chỉ hiện khi đọc thuyết minh |

`SỰ_THẬT` Về thuê tài sản: IFRS 16 (IFRS Foundation, trang chuẩn mở ngày `2026-10-26`) có hiệu lực với kỳ báo cáo năm bắt đầu từ hoặc sau `2019-01-01`. Chuẩn dùng **một mô hình kế toán duy nhất cho bên đi thuê**: ghi nhận **tài sản quyền sử dụng** (right-of-use asset) và **nợ thuê** (lease liability) cho các hợp đồng thuê **trên 12 tháng**; doanh nghiệp **được phép miễn** ghi nhận với thuê ngắn hạn và tài sản có giá trị thấp. Nghĩa là với doanh nghiệp bán lẻ, hàng không, khách sạn hay logistics, một phần lớn "nợ" thật sự đang nằm ở dòng nợ thuê — và trước đây không nằm trên bảng cân đối.

`SỰ_THẬT` Doanh nghiệp lập theo **US GAAP** (ASC 842) cũng đưa nợ thuê lên bảng cân đối, nhưng với **thuê hoạt động** thì chi phí thuê vẫn là một dòng chi phí hoạt động và tiền thuê vẫn nằm trong **dòng tiền hoạt động** (nguồn thứ cấp: Deloitte DART). Các hệ quả dưới đây chỉ đúng nguyên vẹn với báo cáo lập theo IFRS 16.

`SUY_LUẬN` Hệ quả khi so sánh: doanh nghiệp thuê nhiều và doanh nghiệp sở hữu nhiều có thể có cùng hoạt động kinh doanh nhưng chỉ số nợ rất khác. Vì vậy:
- **EBITDA** của doanh nghiệp thuê nhiều lập theo IFRS 16 trông đẹp hơn (tiền thuê nằm ở khấu hao tài sản quyền sử dụng và lãi, không ở chi phí hoạt động) — nhưng tiền thì vẫn phải trả. Với thuê hoạt động theo US GAAP, EBITDA **không** được "làm đẹp" theo cách này.
- **EV/EBITDA** vì thế có thể đánh lừa giữa hai doanh nghiệp cùng ngành có mức thuê khác nhau. Đây là một trong những lý do Bài 009 phải nói rõ bội số nào dùng cho ngành nào.

`SUY_LUẬN` Lịch đáo hạn ("maturity wall") là bảng số ngày càng đáng đọc hơn mọi tỷ lệ: nếu 50% nợ đến hạn trong 12 tháng mà hạn mức tín dụng đã dùng hết, doanh nghiệp buộc phải huy động **ở bất kỳ giá nào**. `Ý_KIẾN` Lịch đáo hạn thường được trình bày ở phần thuyết minh nợ vay, không nằm trên bảng cân đối — phải đọc thuyết minh, không suy ra từ bảng cân đối.

## 2. Bốn tỷ lệ sống còn

`PHÉP_TÍNH` Bốn tỷ lệ, cùng một bộ số liệu, trả lời bốn câu hỏi khác nhau:

```text
1. Nợ ròng / EBITDA          = (Nợ vay ngắn hạn + Nợ vay dài hạn + Nợ thuê theo IFRS 16 − Tiền và tương đương) / EBITDA
   (khi so sánh với doanh nghiệp sở hữu nhiều tài sản, phải gộp hoặc loại nợ thuê ở CẢ HAI bên)
2. Hệ số trả lãi (interest coverage) = EBIT / Chi phí lãi vay
3. Dòng tiền hoạt động / Nợ vay ngắn hạn = CFO / (Nợ vay ngắn hạn + phần nợ dài hạn đến hạn trong 12 tháng)
   (không lấy "nợ ngắn hạn" trên bảng cân đối, vì mẫu số đó gồm cả phải trả người bán)
4. Dự phòng thanh khoản      = (Tiền + Hạn mức tín dụng chưa dùng) / Nợ đến hạn 12 tháng
```

Cách đọc, có ghi rõ đây là quy ước phổ biến chứ không phải quy tắc chuẩn mực:

| Tỷ lệ | Mức thường được coi là an toàn | Vùng cần lo | Vì sao |
|---|---|---|---|
| Nợ ròng / EBITDA | dưới 2 lần | trên 4 lần | Ở 4 lần, EBITDA giảm 30% đẩy tỷ lệ lên 5,7 lần. `Ý_KIẾN` Ngưỡng covenant thường gặp nằm quanh 3,5–4,5 lần, nhưng con số này không có nguồn gốc trong bài — phải đọc ngưỡng thật trong thuyết minh |
| Hệ số trả lãi | trên 5 lần | dưới 2 lần | Ở đúng 2 lần, EBIT phải giảm **hơn 50%** mới không đủ trả lãi (giảm 40% còn 1,2 lần). Dưới 2 lần thì cú giảm cần thiết còn nhỏ hơn: ở 1,5 lần chỉ cần giảm hơn **33%** (`1 − 1/1,5`) |
| CFO / Nợ vay ngắn hạn | trên 100% | dưới 30% | Dưới 30% nghĩa là phải vay mới để trả nợ cũ |
| Dự phòng thanh khoản | trên 150% | dưới 80% | Đo khả năng trả nợ đến hạn trong 12 tháng bằng nguồn sẵn có hôm nay |

`PHÉP_TÍNH` Quy tắc tổng quát cho hệ số trả lãi: với hệ số hiện tại `k`, EBIT phải giảm hơn `1 − 1/k` thì mới không đủ trả lãi (k = 2 → 50%; k = 1,5 → 33,3%; k = 1,33 → 25%).

`CHƯA_BIẾT` Các ngưỡng trong bảng là quy ước thực hành, **chưa** dẫn được nguồn gốc. Một khung hay được trích là bảng "financial risk profile" của S&P (Nợ/EBITDA dưới 1,5 / 1,5–2 / 2–3 / 3–4 / 4–5 / trên 5 lần), nhưng lượt này mới thấy bảng đó qua nguồn thứ cấp; muốn dùng phải mở tài liệu *Corporate Methodology* của S&P và ghi đúng phiên bản.

`SUY_LUẬN` Cảnh báo về bản thân các ngưỡng: chúng phụ thuộc ngành và chu kỳ. Doanh nghiệp tiện ích có dòng tiền ổn định chịu được nợ cao hơn doanh nghiệp chu kỳ. Vì vậy **ngưỡng chỉ để phát hiện chỗ cần đọc tiếp**, không để kết luận.

## 3. Ví dụ số học hư cấu: từ "trả lãi được" đến "không trả nổi"

`KỊCH_BẢN` Công ty B, đơn vị: tỷ đồng.

| Chỉ tiêu | Số |
|---|---:|
| EBIT | 120 |
| Khấu hao | 40 |
| EBITDA | 160 |
| Chi phí lãi vay | 90 |
| Nợ vay ngắn hạn | 400 |
| Nợ vay dài hạn | 800 |
| Tiền và tương đương tiền | 50 |
| Dòng tiền hoạt động (CFO) | 60 |
| Trong đó nợ có lãi suất thả nổi | 720 (60% tổng nợ vay) |

`PHÉP_TÍNH` Bốn tỷ lệ:

- Nợ ròng = `400 + 800 − 50 = 1.150`; Nợ ròng/EBITDA = `1.150 / 160 = 7,19 lần` → **rất cao**.
- Hệ số trả lãi = `120 / 90 = 1,33 lần` → **nguy hiểm**: EBIT giảm 25% là **vừa đủ** trả lãi (hệ số đúng 1,00), giảm hơn 25% là không đủ.
- CFO / Nợ vay ngắn hạn = `60 / 400 = 15%` → **thấp**: tiền hoạt động một năm chỉ trả được 15% nợ đến hạn trong năm.
- Dự phòng thanh khoản: `CHƯA_BIẾT` vì ví dụ chưa cho hạn mức tín dụng chưa dùng — **đây chính là dữ liệu phải đi tìm trong thuyết minh**.

`KỊCH_BẢN` `PHÉP_TÍNH` Cú sốc lãi suất: nếu lãi suất thị trường tăng **200 điểm cơ bản** (2 điểm phần trăm), phần nợ thả nổi 720 tăng chi phí lãi thêm `720 × 2% = 14,4`. Chi phí lãi thành `90 + 14,4 = 104,4`; hệ số trả lãi thành `120 / 104,4 = 1,15 lần`.

`SUY_LUẬN` Bài học: một doanh nghiệp có thể "vẫn có lãi" và "vẫn trả lãi được" hôm nay, nhưng hệ số 1,15 nghĩa là **không còn biên an toàn nào**. Trong tình huống đó, câu hỏi đúng không phải "doanh nghiệp có tốt không" mà là "doanh nghiệp có sống qua 12 tháng tới không" — và nếu câu trả lời phụ thuộc vào việc gia hạn nợ, thì đó là rủi ro cấu trúc, không phải rủi ro kinh doanh.

## 4. Điều khoản vay: rủi ro nằm ở chữ, không ở số

`SUY_LUẬN` Điều khoản vay (covenant) thường là cam kết trong hợp đồng: duy trì nợ ròng/EBITDA dưới mức X, không bán tài sản bảo đảm, không chia cổ tức quá Y, nộp báo cáo đúng hạn. Vi phạm có thể khiến ngân hàng có quyền **gọi nợ trước hạn** hoặc tăng lãi suất.

`SUY_LUẬN` Ba điểm cần đọc trong thuyết minh nợ vay:

1. **Ngưỡng cụ thể** của từng điều khoản và khoảng cách hiện tại tới ngưỡng đó.
2. **Đã được miễn trừ (waiver) lần nào chưa** — xin gia hạn một lần là dấu hiệu; xin ba lần là sự thật.
3. **Tài sản bảo đảm là gì** — nếu là toàn bộ hàng tồn kho và phải thu, khả năng tiếp cận vốn lưu động mới rất hẹp.

`SUY_LUẬN` Với trái phiếu doanh nghiệp, ba câu hỏi tương tự cộng thêm: ai đang nắm giữ, có điều kiện chuyển đổi không, và lịch thanh toán gốc như thế nào. Những thông tin này **phải** đọc từ công bố gốc, không suy ra từ tỷ lệ.

## 5. Vay hay phát hành cổ phiếu: cùng một nhu cầu, hai hậu quả

`KỊCH_BẢN` Quy ước đơn vị của mục này: khoản tiền tính bằng **tỷ đồng**; giá cổ phiếu và EPS tính bằng **nghìn đồng/cổ phiếu**.

`PHÉP_TÍNH` Công ty D cần huy động 200 tỷ. Hiện có EBIT 200, chi phí lãi vay 40, thuế suất 20%, 100 triệu cổ phiếu đang lưu hành, giá 10.000 đồng/cổ phiếu (tức 10 đơn vị tiền mỗi cổ phiếu trong ví dụ).

Hai phương án:

- **Phương án nợ**: vay 200 với lãi suất 10% → chi phí lãi vay thành 60.
  `PHÉP_TÍNH` Lợi nhuận sau thuế = `(200 − 60) × 0,8 = 112` → EPS = `112 / 100 = 1,120`.
- **Phương án cổ phiếu**: phát hành 20 triệu cổ phiếu mới ở giá 10 → 120 triệu cổ phiếu.
  `PHÉP_TÍNH` Lợi nhuận sau thuế = `(200 − 40) × 0,8 = 128` → EPS = `128 / 120 = 1,067`.

`PHÉP_TÍNH` EBIT hoà vốn giữa hai phương án: giải `(E − 60) × 0,8 / 100 = (E − 40) × 0,8 / 120`, được `120(E − 60) = 100(E − 40)` → `20E = 3.200` → **E = 160**.

Cách đọc:

- EBIT trên 160 → phương án nợ cho EPS cao hơn (ở ví dụ này EBIT 200: 1,120 so với 1,067).
- EBIT dưới 160 → phương án cổ phiếu cho EPS cao hơn. `PHÉP_TÍNH` Nếu EBIT rơi về 100: nợ cho EPS `(100−60)×0,8/100 = 0,320`; cổ phiếu cho `(100−40)×0,8/120 = 0,400`.

`SUY_LUẬN` Đây là lý do "vay để tăng EPS" là một lập luận **có điều kiện**, không phải chân lý: nó đúng khi doanh nghiệp chắc chắn duy trì được EBIT trên điểm hoà vốn. Và quan trọng hơn: **EPS cao hơn không có nghĩa là cổ đông giàu hơn** — EPS tăng bằng cách tăng rủi ro thì không tạo ra giá trị, chỉ chia lại rủi ro. Đây là điểm nối sang Bài 010 (chi phí vốn) và Bài 012 (kịch bản).

## 6. Năm câu hỏi khi đọc nợ

1. Tổng nợ vay là bao nhiêu, bao nhiêu phần thả nổi lãi suất, và lịch đáo hạn 3 năm tới ra sao?
2. Nợ ròng/EBITDA và hệ số trả lãi đang ở mức nào, xu hướng 3 năm?
3. Tiền mặt cộng hạn mức tín dụng chưa dùng có đủ trả nợ đến hạn 12 tháng không?
4. Thuê tài sản chiếm bao nhiêu trong nợ; nếu gộp vào thì tỷ lệ nợ thay đổi thế nào?
5. Điều khoản vay nào đang gần bị vi phạm, và đã xin miễn trừ lần nào chưa?

## 7. Bài tập (8 câu, 40 phút)

`KỊCH_BẢN` Đơn vị: khoản tiền tính bằng **tỷ đồng**; giá cổ phiếu và EPS tính bằng **nghìn đồng/cổ phiếu**. Số liệu hư cấu.

### Bài 1 (nhớ lại) — bốn tỷ lệ

Cho: EBIT 300; khấu hao 80; lãi vay 100; nợ vay ngắn hạn 250; nợ vay dài hạn 950; tiền 150; CFO 220. Tính Nợ ròng/EBITDA, hệ số trả lãi, CFO/Nợ vay ngắn hạn. Nêu tỷ lệ nào đáng lo nhất và vì sao.

### Bài 2 (nhớ lại) — tác động của thuê tài sản

Một doanh nghiệp bán lẻ có: nợ vay 500; nợ thuê tài sản 700; EBITDA báo cáo 300 (đã loại tiền thuê ra khỏi chi phí hoạt động); EBIT 180; lãi vay thuần 60. Tính Nợ ròng/EBITDA khi **gộp** nợ thuê vào. Nêu một câu về hệ quả khi so sánh với một doanh nghiệp sở hữu cửa hàng.

### Bài 3 (vận dụng) — cú sốc lãi suất

Dùng lại số liệu Bài 1. Giả sử 70% nợ vay là thả nổi. Tính hệ số trả lãi nếu lãi suất tăng 150 điểm cơ bản. Doanh nghiệp còn "an toàn" không?

### Bài 4 (vận dụng) — lịch đáo hạn

Cho lịch nợ: trong 12 tháng 600; năm 2: 200; năm 3: 100; sau đó 400. CFO 250; tiền 100; hạn mức tín dụng chưa dùng 150. Tính dự phòng thanh khoản cho 12 tháng và nêu hai cách xử lý nếu dự phòng dưới 100%.

### Bài 5 (vận dụng) — vay hay cổ phiếu

Công ty cần 500. EBIT hiện tại 400; lãi vay 50; thuế 20%; 200 triệu cổ phiếu. Phương án nợ: lãi suất 10%. Phương án cổ phiếu: phát hành ở giá 20. Tính EPS mỗi phương án và EBIT hoà vốn.

### Bài 6 (vận dụng, câu cũ xen kẽ) — nối Bài 004

Doanh nghiệp có EBIT 150; lãi vay 60; CFO 40; capex 90; nợ vay ngắn hạn 300. Tính hệ số trả lãi và CFO/Nợ vay ngắn hạn. Sau đó trả lời: nếu phải chọn **một** con số để quyết định có nên lo hay không, bạn chọn con số nào và vì sao vẫn phải xem thêm lịch đáo hạn?

### Bài 7 (chuyển giao) — tìm lỗi

"Hệ số trả lãi 6 lần nên doanh nghiệp chắc chắn an toàn. Nợ ròng/EBITDA 3,5 lần cũng không sao vì EBITDA là tiền." Hãy chỉ ra **hai** lỗi và cách kiểm.

### Bài 8 (chuyển giao) — ba câu hỏi cho hồ sơ mới

Bạn nhận một hồ sơ có: nợ ròng/EBITDA 2,1 lần; hệ số trả lãi 4,5 lần; CFO/nợ vay ngắn hạn 120%; 40% nợ là trái phiếu đến hạn trong 8 tháng; hạn mức tín dụng chưa dùng 0. Nêu ba câu hỏi phải hỏi trước khi nói "nợ ở mức chấp nhận được".

## 8. Đáp án

### Bài 1

`PHÉP_TÍNH` EBITDA = `300 + 80 = 380`; nợ ròng = `250 + 950 − 150 = 1.050`; Nợ ròng/EBITDA = `1.050/380 = 2,76 lần`; hệ số trả lãi = `300/100 = 3,0 lần`; CFO/nợ vay ngắn hạn = `220/250 = 88%`.
`SUY_LUẬN` Tỷ lệ đáng lo nhất là **hệ số trả lãi 3,0** so với nợ ròng/EBITDA 2,76 (mức trung bình). Lý do: một cú giảm EBIT 30% đưa hệ số về 2,1, và 50% về 1,5 — đó là vùng phải gia hạn nợ. Câu này kiểm: bạn có biết mỗi tỷ lệ nhạy với loại cú sốc nào không.

### Bài 2

`PHÉP_TÍNH` Gộp nợ thuê: nợ ròng = `500 + 700 = 1.200` (ví dụ không cho tiền, coi tiền bằng 0 và ghi rõ giả định); Nợ ròng/EBITDA = `1.200/300 = 4,0 lần`.
`SUY_LUẬN` Nếu so với doanh nghiệp sở hữu cửa hàng (nợ vay cao nhưng không có dòng nợ thuê, và EBITDA thấp hơn vì không loại tiền thuê), so sánh trực tiếp hai bên là **so sánh hai cách hạch toán**, không phải hai mức rủi ro. Phải gộp hoặc loại thuê ở cả hai bên.

### Bài 3

`PHÉP_TÍNH` Nợ vay = `250 + 950 = 1.200`; nợ thả nổi = `1.200 × 70% = 840`; lãi tăng = `840 × 1,5% = 12,6`; lãi vay mới = `112,6`; hệ số trả lãi = `300/112,6 = 2,66 lần`.
`SUY_LUẬN` Vẫn trên 2,0 nhưng đã mất khoảng một phần ba khoảng đệm tới ngưỡng 2,0 lần chỉ với 150 điểm cơ bản. Không nên kết luận "an toàn" chỉ vì còn trên ngưỡng; cần nói rõ mức nhạy và cú sốc nào sẽ đưa về dưới 2,0: `PHÉP_TÍNH` lãi vay để hệ số bằng 2,0 là `150`, tức tăng `50` so với 100 — ứng với lãi suất thả nổi tăng khoảng `50/840 = 5,95` điểm phần trăm.

### Bài 4

`PHÉP_TÍNH` Dự phòng = `(100 + 150)/600 = 41,7%`. Lưu ý: CFO 250 **cố ý không** đưa vào tử số, vì đây là phép đo "sống qua 12 tháng tới bằng nguồn sẵn có hôm nay". Nếu muốn tính cả CFO trong năm thì `(100 + 150 + 250)/600 = 83,3%` — vẫn dưới 100%, nên kết luận không đổi.
`SUY_LUẬN` Dưới 100% nghĩa là **không đủ** trả nợ đến hạn bằng nguồn sẵn có. Hai cách xử lý cần nêu: (a) tái cấp vốn (đảo nợ) — nghĩa là phụ thuộc thị trường tín dụng, rủi ro nếu thị trường đóng; (b) giảm nhu cầu tiền: hoãn capex, bán tài sản không cốt lõi, giảm cổ tức. Câu này kiểm: bạn có phân biệt "trả được nợ" với "vay mới để trả nợ cũ" không.

### Bài 5

`PHÉP_TÍNH` Phương án nợ: lãi vay 100; lợi nhuận sau thuế `(400−100)×0,8 = 240`; EPS = `240/200 = 1,20`.
`PHÉP_TÍNH` Phương án cổ phiếu: phát hành `500/20 = 25` triệu cổ phiếu → 225 triệu; lợi nhuận sau thuế `(400−50)×0,8 = 280`; EPS = `280/225 = 1,244`.
`PHÉP_TÍNH` EBIT hoà vốn: `(E−100)×0,8/200 = (E−50)×0,8/225` → `225(E−100) = 200(E−50)` → `25E = 22.500 − 10.000 = 12.500` → **E = 500**.
`SUY_LUẬN` Ở EBIT hiện tại 400 (dưới 500), phương án cổ phiếu cho EPS cao hơn — ngược với trực giác "nợ luôn tốt hơn vì không pha loãng". Đây là câu quan trọng nhất của bài: **không có lựa chọn nào tốt hơn tuyệt đối**, chỉ có lựa chọn phù hợp với mức EBIT kỳ vọng và khả năng chịu rủi ro.

### Bài 6

`PHÉP_TÍNH` Hệ số trả lãi = `150/60 = 2,5 lần`; CFO/nợ vay ngắn hạn = `40/300 = 13,3%`; FCF = `40 − 90 = −50`.
`SUY_LUẬN` Nếu chỉ chọn một con số, chọn **CFO/nợ vay ngắn hạn 13,3%** vì nó kết hợp cả dòng tiền (Bài 004) với hạn trả nợ. Nhưng vẫn phải xem lịch đáo hạn: nếu phần lớn nợ vay ngắn hạn đã có cam kết gia hạn bằng văn bản thì rủi ro khác hẳn; nếu là trái phiếu đến hạn thì khác hẳn.

### Bài 7

`SUY_LUẬN` Lỗi 1: "hệ số trả lãi 6 lần ⇒ chắc chắn an toàn" — hệ số này đo khả năng trả **lãi**, không đo khả năng trả **gốc**; một doanh nghiệp trả lãi dễ dàng vẫn có thể không trả nổi gốc đến hạn. Lỗi 2: "EBITDA là tiền" — EBITDA là lợi nhuận trước lãi vay, thuế, khấu hao; nó **bỏ qua** capex, thay đổi vốn lưu động và thuế, nên không phải tiền. Cách kiểm: dựng lại CFO từ EBITDA trừ capex và vốn lưu động, rồi so với lịch đáo hạn.

### Bài 8

`SUY_LUẬN` Ba câu hỏi: (1) 40% nợ là trái phiếu đến hạn trong 8 tháng — doanh nghiệp có kế hoạch tái cấp vốn nào, đã có cam kết chưa; (2) hạn mức tín dụng chưa dùng bằng 0 nghĩa là không còn đệm — điều khoản vay có cấm vay thêm không; (3) chỉ tiêu CFO/nợ vay ngắn hạn 120% được tính trên mẫu số **bao gồm** phần trái phiếu sắp đáo hạn hay không (chỉ tiêu có thể đang bị tính trên mẫu số nhỏ).

## 9. Đáp án phần ôn bài cũ

1. CFO **giảm 100** — tăng phải thu là dùng tiền của mình cho khách.
2. Vì lợi nhuận kế toán và dòng tiền là hai phép đo khác nhau; doanh nghiệp có thể lãi mà CFO âm do tăng vốn lưu động, và có thể lỗ mà CFO dương do thu hồi phải thu (Bài 004).
3. Vì theo IFRS 16, phần trả gốc nợ thuê nằm ở dòng tiền tài chính, nên `CFO − capex` chưa trừ khoản tiền thuê phải trả hằng năm và FCF "hẹp" cao hơn tiền thực sự còn lại. Lưu ý: theo US GAAP, tiền thuê hoạt động đã nằm trong CFO, nên điều này không xảy ra với thuê hoạt động (Bài 004, mục 2.3).
4. Vì một năm có thể là đỉnh chu kỳ hoặc có sự kiện một lần; xu hướng nhiều năm cho thấy chất lượng lặp lại hay không (Bài 003, mục 6).

## 10. Lỗi thường gặp

- Nhìn nợ tuyệt đối mà không nhìn **lịch đáo hạn**: nợ 5.000 tỷ đến hạn sau 10 năm khác hoàn toàn nợ 500 tỷ đến hạn trong 6 tháng.
- Dùng EBITDA như thể là tiền, rồi kết luận "trả nợ tốt".
- So sánh Nợ ròng/EBITDA giữa doanh nghiệp thuê nhiều và sở hữu nhiều mà không gộp hoặc loại thuê ở cả hai bên.
- Bỏ qua hạn mức tín dụng chưa dùng — đây thường là đệm sống còn thật sự.
- Nghĩ "vay tốt hơn phát hành vì không pha loãng" mà không tính điểm hoà vốn EBIT.
- Đọc điều khoản vay như chi tiết pháp lý, không đọc ngưỡng và lịch sử xin miễn trừ.
- Áp ngưỡng chung (nợ ròng/EBITDA < 2) cho mọi ngành, kể cả ngân hàng và bất động sản.
- Kết luận "an toàn" từ một năm, trong khi phần lớn nợ đáo hạn ở năm sau.

## 11. Ranh giới an toàn

- Bài này là khung phân tích, **không** phải khuyến nghị mua/bán/nắm giữ.
- Không khuyến khích vay nợ, đòn bẩy hay bất kỳ cấu trúc vốn cụ thể nào cho cá nhân hay doanh nghiệp thật.
- Các ngưỡng trong bảng mục 2 là **quy ước phổ biến**, không phải chuẩn mực kế toán hay quy định pháp luật.
- Với ngân hàng, bảo hiểm và công ty chứng khoán, nợ là nguyên liệu kinh doanh — không áp các tỷ lệ này (Bài 013).

## 12. Điều tôi vẫn chưa hiểu

1. Bạn muốn học cách đọc **lịch đáo hạn** từ một bản thuyết minh thật (cần bạn tự mở PDF) hay qua ví dụ hư cấu là đủ?
2. Bạn đang quan tâm doanh nghiệp có nợ thuê lớn (bán lẻ, logistics) hay nợ vay ngân hàng là chính?
3. Có cần tôi thêm một bài ngắn riêng về **trái phiếu doanh nghiệp** (điều khoản, người nắm giữ, rủi ro thanh toán) không?
4. Bạn muốn bài 006 đi sâu vào pha loãng và mua lại cổ phiếu hay vào giao dịch bên liên quan?

## 13. Nguồn Internet đã mở

<details>
<summary>Nguồn chi tiết và lịch sử kiểm — giữ mốc dữ liệu gốc</summary>

Tất cả mở ngày `2026-10-26`.

- [IFRS 16 Leases — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/) — HTTP 200; trang chuẩn "Standard 2026 Issued"; hiệu lực kỳ báo cáo năm từ hoặc sau `2019-01-01`; phạm vi: chuẩn mực IFRS toàn cầu; không có đơn vị tiền. Cung cấp: một mô hình kế toán cho bên đi thuê; ghi nhận tài sản quyền sử dụng và nợ thuê cho hợp đồng thuê trên 12 tháng, trừ tài sản giá trị thấp.
- [IAS 7 Statement of Cash Flows — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) — HTTP 200. Cung cấp: phân loại dòng tiền hoạt động/đầu tư/tài chính (dùng ở mục 1 và 5 khi phân loại lãi vay), và sửa đổi do IFRS 18 về phân loại dòng tiền lãi vay, cổ tức.
- [IFRS 18 — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) — HTTP 200; hiệu lực kỳ báo cáo năm từ hoặc sau `2027-01-01`; cung cấp: hai tiểu tổng mới và công bố MPM (dùng ở lưu ý phân loại dòng tiền lãi vay).
- [Apple Balance Sheet — stockanalysis.com](https://stockanalysis.com/stocks/aapl/financials/balance-sheet/) — HTTP 200; đơn vị **triệu USD**, năm tài chính tháng 10 → tháng 9. Trong phiên, công cụ tải trang chỉ lấy được phần **Tài sản** (phần Nợ phải trả bị cắt do giới hạn tải trang — hạn chế của công cụ, không phải của nguồn), nên bài này **không** dùng số liệu nợ của doanh nghiệp thật; mọi ví dụ nợ là hư cấu. `CHƯA_BIẾT` cơ cấu nợ thật của Apple trong lượt này; cách xác minh: mở 10-K gốc trên EDGAR bằng trình duyệt.
- [SEC EDGAR](https://www.sec.gov/edgar/search/) — lượt soạn bài gặp HTTP 403; lượt review cùng ngày xác nhận `sec.gov` và `data.sec.gov` trả HTTP 200 khi gửi **User-Agent khai báo** (xem Bài 004). Bài này vẫn chưa dùng số nợ thật của doanh nghiệp nào.
- [Deloitte DART — 7.6 Leases](https://dart.deloitte.com/USDART/home/codification/presentation/asc230-10/roadmap-statement-cash-flow/chapter-7-common-issues-related-cash/7-6-leases) — HTTP 200; mở `2026-10-26`; **nguồn thứ cấp** trích ASC 842-20-45-5. Dùng cho khác biệt US GAAP ở mục 1.

**Trạng thái kiểm nguồn**: bài này đã qua một lượt `source-fact-checker` độc lập ngày `2026-10-26`; biên bản đầu tiên kết luận **KHÔNG ĐẠT** vì 2 lỗi số học trong bảng ngưỡng mục 2 (đã sửa: điều kiện mất khả năng trả lãi phải là EBIT giảm **hơn 50%**, không phải 40%; và ở hệ số 1,33 thì giảm 25% là **vừa đủ**, không phải "không đủ"). Bản đã sửa (hash `36f17d40c9fbce57…`) sau đó **được kiểm lại độc lập và kết luận ĐẠT, 0 lỗi nghiêm trọng** trong 13 nhóm phép tính tái lập; còn một lỗi nhãn "nợ ngắn hạn" lẫn với "nợ vay ngắn hạn" đã được sửa nốt. Biên bản chi tiết ở mục 16 của [lộ trình](../roadmap.md#16-nhật-ký-kiểm-duyệt). Bài **chưa** qua `risk_bear_reviewer` nên vẫn giữ trạng thái bản nháp về kiểm duyệt. Lượt review ngày `2026-10-26` sửa tiếp: câu "dưới 2 lần" trong bảng ngưỡng (chỉ đúng tại 2,0 lần), mô tả tỷ lệ dự phòng thanh khoản, khác biệt US GAAP về thuê, và ghi `CHƯA_BIẾT` cho nguồn của các ngưỡng; hash đã đổi nên cần kiểm nguồn lại.


</details>
