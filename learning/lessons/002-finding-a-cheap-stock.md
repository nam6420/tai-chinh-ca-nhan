# Bài 002: Hiểu và tìm một cổ phiếu đang được định giá rẻ

- Ngày: `2026-08-10`
- Chốt dữ liệu lúc: `2026-08-10 15:47 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt giá cổ phiếu thấp với cổ phiếu được định giá rẻ, sau đó xây một quy trình học và sàng lọc phù hợp cho người mới.

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Các ví dụ số học đều là doanh nghiệp hư cấu. Form 10-K và SEC chỉ là ví dụ cho thị trường Mỹ; với thị trường khác phải dùng hồ sơ và cơ quan quản lý tương ứng.

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Bài này giải quyết một nhầm lẫn phổ biến: **giá mỗi cổ phiếu thấp không có nghĩa cổ phiếu đang rẻ**.

Ví dụ, một chiếc bánh nhỏ giá 20.000 đồng chưa chắc rẻ hơn chiếc bánh lớn giá 50.000 đồng. Muốn so sánh, phải biết mình nhận được bao nhiêu và chất lượng ra sao. Với cổ phiếu cũng vậy: phải đặt **giá phải trả** bên cạnh **doanh nghiệp mình nhận quyền sở hữu**, khả năng tạo lợi nhuận và tiền mặt, nợ, triển vọng cùng rủi ro.

### Ba câu hỏi theo đúng thứ tự

| Thứ tự | Câu hỏi | Nếu chưa trả lời được |
|---:|---|---|
| 1 | Doanh nghiệp kiếm tiền bằng cách nào? | Chưa nên định giá. |
| 2 | Doanh nghiệp có đủ khỏe và lợi nhuận có đáng tin không? | Phải đọc báo cáo tài chính, dòng tiền, nợ và thuyết minh. |
| 3 | Giá thị trường có thấp so với một khoảng giá trị hợp lý không? | Chưa thể gọi cổ phiếu là rẻ. |

### Bốn điều cần nhớ

- `SỰ_THẬT` Giá 5.000 đồng một cổ phiếu không tự động rẻ hơn giá 100.000 đồng; số cổ phiếu lưu hành và quy mô toàn doanh nghiệp cũng quan trọng.
- `SUY_LUẬN` P/E thấp không tự động có nghĩa là rẻ; lợi nhuận có thể tăng tạm thời, mang tính bất thường hoặc sắp giảm.
- `SUY_LUẬN` Bộ lọc và tỷ số chỉ tạo ra **danh sách để nghiên cứu**, không tạo tín hiệu mua.
- `SUY_LUẬN` Giá trị hợp lý là một **khoảng ước tính phụ thuộc giả định**, không phải con số chắc chắn.

### Bài này làm gì và chưa làm gì?

- **Bài này làm:** dạy quy trình loại bỏ các cổ phiếu trông có vẻ rẻ nhưng có thể là bẫy.
- **Bài này chưa làm:** tìm ra một cổ phiếu chắc chắn sinh lời hoặc quyết định mua thay bạn.
- Muốn nghiên cứu doanh nghiệp thật, phải dùng hồ sơ gốc tại đúng thị trường, lập kịch bản bất lợi, cơ sở và thuận lợi, rồi chủ động tìm bằng chứng chống lại nhận định của mình.

> Câu cần nhớ: **Đừng hỏi “giá cổ phiếu có thấp không?”; hãy hỏi “giá này có thấp so với giá trị của doanh nghiệp sau khi tính cả nợ, chất lượng lợi nhuận và rủi ro không?”**

## Giải thích đơn giản

Cách nói chính xác hơn `cheap company` là `cheap stock` — cổ phiếu đang được thị trường định giá thấp so với một ước tính giá trị có căn cứ.

Có thể hình dung theo cách của một lập trình viên backend:

```text
Giá cổ phiếu       = một field trong API response
Doanh nghiệp       = toàn bộ system phía sau
Báo cáo tài chính  = telemetry và database snapshot
Mô hình định giá   = business logic chứa assumptions
Giá trị hợp lý     = một khoảng kết quả, không phải constant
```

`SUY_LUẬN` Trong bài này, một cổ phiếu được gọi là “rẻ” khi giá thị trường thấp hơn khoảng giá trị hợp lý do người phân tích ước tính từ chất lượng doanh nghiệp, lợi nhuận và dòng tiền bền vững, bảng cân đối, triển vọng và rủi ro. Giá trị hợp lý là một ước tính chủ quan, không phải sự thật chắc chắn.

### Giá mỗi cổ phiếu thấp không có nghĩa là rẻ

`SỰ_THẬT`

```text
Vốn hóa thị trường = Giá hiện tại mỗi cổ phiếu × Số cổ phiếu đang lưu hành
```

`PHÉP_TÍNH` Ví dụ hư cấu:

- Công ty A: `100.000 đồng × 10 triệu cổ phiếu = 1.000 tỷ đồng` vốn hóa.
- Công ty B: `10.000 đồng × 200 triệu cổ phiếu = 2.000 tỷ đồng` vốn hóa.

B có giá mỗi cổ phiếu chỉ bằng một phần mười A, nhưng toàn bộ vốn chủ sở hữu đang được thị trường định giá gấp đôi A. Vì vậy, lọc “cổ phiếu dưới 20.000 đồng” gần như không phải là lọc định giá.

## Ba câu hỏi phải trả lời theo đúng thứ tự

### 1. Doanh nghiệp kiếm tiền bằng cách nào?

Cần giải thích được bằng lời đơn giản:

- Khách hàng là ai?
- Khách hàng trả tiền để giải quyết vấn đề gì?
- Doanh thu tính theo số lượng, thuê bao, giao dịch hay dự án?
- Ba chi phí lớn nhất là gì?
- Điều gì khiến khách hàng không chuyển sang đối thủ?

Nếu chưa mô tả được luồng `khách hàng → doanh thu → lợi nhuận → tiền mặt`, chưa nên định giá.

### 2. Doanh nghiệp có đủ khỏe không?

Tối thiểu phải đọc:

- Báo cáo kết quả kinh doanh: doanh thu, chi phí và lợi nhuận.
- Bảng cân đối: tiền, tài sản, nợ và vốn chủ sở hữu.
- Báo cáo lưu chuyển tiền tệ: tiền thực sự vào và ra.
- Thuyết minh: nợ đáo hạn, cam kết, nghĩa vụ tiềm tàng, kiện tụng, giao dịch liên quan và chính sách kế toán.
- Báo cáo kiểm toán: ý kiến kiểm toán, khả năng hoạt động liên tục và điểm yếu kiểm soát.

Đối với doanh nghiệp niêm yết Mỹ, Form 10-K có phần Business, Risk Factors, MD&A và các báo cáo tài chính kiểm toán. Kiểm toán chỉ cung cấp mức bảo đảm hợp lý, không có nghĩa số liệu chắc chắn không chứa gian lận hoặc sai sót.

### 3. Mức giá hiện tại có đủ thấp không?

Một số tỷ số khởi đầu:

- `P/E = giá cổ phiếu / EPS`: chỉ trực quan khi lợi nhuận dương và có tính đại diện.
- `P/B = giá cổ phiếu / giá trị sổ sách mỗi cổ phiếu`: thường có ý nghĩa hơn với ngành nhiều tài sản hữu hình.
- `EV ≈ vốn hóa + tổng nợ − tiền`: công thức xấp xỉ ban đầu cho doanh nghiệp phi tài chính; phân tích đầy đủ có thể cần thêm điều chỉnh.
- Biên lợi nhuận, khả năng trả lãi, dòng tiền và mức pha loãng cổ phiếu.

Không so P/E của ngân hàng với công ty phần mềm. Ngân hàng, bảo hiểm, bất động sản, khai khoáng, doanh nghiệp chu kỳ và doanh nghiệp chưa có lợi nhuận cần cách phân tích riêng. Đặc biệt, không dùng EV/EBITDA như công thức chung cho ngân hàng hoặc bảo hiểm.

## Ví dụ: vì sao P/E thấp vẫn có thể đắt?

`PHÉP_TÍNH` Một công ty hư cấu có:

- Giá hiện tại: 80 đơn vị tiền tệ mỗi cổ phiếu.
- EPS báo cáo: 8.
- `P/E = 80 / 8 = 10 lần`.

Nếu EPS 8 chứa lợi nhuận bất thường từ bán tài sản và EPS bền vững trong kịch bản bất lợi chỉ là 4:

```text
P/E trên EPS bất lợi = 80 / 4 = 20 lần
```

Bảng sau chỉ là `MINH HỌA SỐ HỌC`, không phải định giá:

| Kịch bản | EPS giả định | P/E giả định | Kết quả phép nhân |
|---|---:|---:|---:|
| Stress | Âm hoặc 0 | Không dùng được | Vốn chủ có thể gần 0 |
| Bất lợi | 4 | 10 | 40 |
| Cơ sở | 6 | 12 | 72 |
| Thuận lợi | 8 | 14 | 112 |

Các EPS và bội số trong bảng đều là giả định chưa gắn với doanh nghiệp thật. Kết quả 40 không phải giá sàn. Nếu doanh nghiệp mất khả năng trả nợ, bị pha loãng mạnh, gian lận hoặc phá sản, cổ đông có thể mất gần toàn bộ vốn.

## Quy trình sàng lọc đề xuất

Bộ lọc chỉ tạo một hàng đợi để nghiên cứu, không tạo tín hiệu mua.

1. Chọn một doanh nghiệp phi tài chính có mô hình dễ giải thích.
2. Thu thập nhiều năm dữ liệu từ hồ sơ gốc: doanh thu, lợi nhuận hoạt động, lợi nhuận ròng, dòng tiền hoạt động, chi đầu tư, tiền, nợ và số cổ phiếu.
3. So sánh với chính lịch sử doanh nghiệp và một nhóm doanh nghiệp thực sự tương đồng về mô hình, địa lý, tăng trưởng, đòn bẩy và chu kỳ.
4. Kiểm tra lợi nhuận bất thường, vốn lưu động, dòng tiền, lịch đáo hạn nợ, covenant, nghĩa vụ hợp đồng, pha loãng và giao dịch bên liên quan.
5. Lập kịch bản bất lợi, cơ sở và thuận lợi với giả định được công khai.
6. Viết bằng chứng trái chiều, điều chưa biết và điều kiện làm luận điểm mất hiệu lực.

Một nhóm ba đến năm doanh nghiệp dùng để nghiên cứu không phải là một danh mục đa dạng hóa.

## Học tiếp theo thứ tự nào

Bốn câu hỏi của bài này được dạy kỹ ở các bài sau — xem thứ tự đọc đầy đủ trong [lộ trình](../roadmap.md#51-bài-nền-bổ-sung-n1n5--thêm-sau-review-2026-10-26):

| Câu hỏi | Bài dạy |
|---|---|
| Đọc từng dòng báo cáo, EBITDA, ROE | [Bài N2](N2-statement-line-items.md) |
| Doanh nghiệp có chất lượng không | [Bài 003](003-business-quality-moat-and-roic.md) |
| Lợi nhuận có thành tiền không, nợ có an toàn không | [Bài 004](004-cash-flow-and-earnings-quality.md), [Bài 005](005-debt-liquidity-survival.md) |
| Giá có thấp so với giá trị không: EV, bội số, nhóm so sánh | [Bài 009](009-valuation-multiples.md), rồi Bài 010–012 |

Đọc hết các bài trên chỉ tạo khả năng đọc hồ sơ và dựng giả thuyết. Nó không chứng nhận người học đã sẵn sàng chọn cổ phiếu bằng tiền thật.

## Lỗi thường gặp

- Nghĩ cổ phiếu 5.000 đồng rẻ hơn cổ phiếu 100.000 đồng.
- Mua vì P/E thấp mà không kiểm tra lợi nhuận bất thường hoặc chu kỳ.
- So sánh tỷ số giữa các ngành có economics khác nhau.
- Chỉ đọc lợi nhuận, bỏ qua dòng tiền, nợ và nghĩa vụ hợp đồng.
- Chỉ dùng một năm dữ liệu.
- Tin screener, ứng dụng hoặc mạng xã hội mà không mở hồ sơ gốc.
- Chỉ chọn các doanh nghiệp đang tồn tại và bỏ qua những doanh nghiệp đã thất bại.
- Dùng ba kịch bản với độ chính xác giả nhưng không chứng minh đầu vào.
- Đồng nhất doanh nghiệp mình thích với cổ phiếu đáng mua ở mọi giá.

## Bài tập

### Bài 1

Cổ phiếu X giá 8.000 đồng và có 2 tỷ cổ phiếu. Y giá 80.000 đồng và có 100 triệu cổ phiếu. Công ty nào có vốn hóa lớn hơn?

### Bài 2

Một cổ phiếu có P/E 6 nhưng lợi nhuận năm vừa rồi tăng do bán trụ sở. Có thể kết luận cổ phiếu rẻ không?

### Bài 3

Doanh nghiệp có lợi nhuận ròng 100 nhưng dòng tiền hoạt động chỉ 20; khoản phải thu tăng mạnh. Hãy đặt các giả thuyết cần xác minh.

## Đáp án gợi ý

### Bài 1

- X: `8.000 × 2 tỷ = 16.000 tỷ đồng`.
- Y: `80.000 × 100 triệu = 8.000 tỷ đồng`.
- X có giá mỗi cổ phiếu thấp hơn nhưng vốn hóa gấp đôi Y.

### Bài 2

Không. Cần loại lợi nhuận một lần, ước tính lợi nhuận có tính đại diện, kiểm tra dòng tiền, nợ và triển vọng hoạt động cốt lõi.

### Bài 3

Có thể doanh thu chưa thu được tiền, điều khoản tín dụng đã nới lỏng hoặc chất lượng doanh thu giảm. Đây chỉ là giả thuyết; phải đọc thuyết minh và biến động vốn lưu động để xác minh.

## Ranh giới an toàn

- Tuổi tác không tự động xác định khả năng chịu rủi ro; còn phải xét quỹ khẩn cấp, nợ, mục tiêu sử dụng tiền và khả năng chịu lỗ.
- Không đặt lệnh chỉ dựa trên bài học hoặc bộ lọc này.
- Đa dạng hóa giúp giảm rủi ro nhưng không bảo đảm tránh thua lỗ.
- Không sử dụng đòn bẩy để thực hành chọn cổ phiếu.

## Điều tôi vẫn chưa hiểu

- Người học muốn tập trung vào thị trường Việt Nam, Mỹ hay một thị trường khác.
- Khả năng đọc báo cáo tài chính và tài liệu tiếng Anh hiện tại.
- Ngành kinh doanh người học muốn chọn làm bài thực hành đầu tiên.
- Mục tiêu, thời hạn và khả năng chịu rủi ro cá nhân; không suy diễn các thông tin này để đưa khuyến nghị.

## Nguồn Internet đã mở và nghiên cứu liên quan

Các nguồn dưới đây được mở lại ngày `2026-08-10`. Trang không hiển thị lịch sử sửa đổi được ghi là `CHƯA_BIẾT` về phiên bản.

- [FINRA — Defining the Value of an Investment](https://www.finra.org/investors/insights/defining-value-investment), xuất bản `2025-11-12`; kỳ báo cáo, tiền tệ và đơn vị: không áp dụng; phiên bản sửa đổi: `CHƯA_BIẾT`.
- [FINRA — Value Investing](https://www.finra.org/investors/insights/value-investing), xuất bản `2025-07-01`; kỳ báo cáo, tiền tệ và đơn vị: không áp dụng; phiên bản sửa đổi: `CHƯA_BIẾT`.
- [FINRA — Evaluating Stocks](https://www.finra.org/investors/investing/investment-products/stocks/evaluating-stocks), ngày xuất bản hiển thị: `CHƯA_BIẾT`; kỳ báo cáo, tiền tệ và đơn vị: không áp dụng; phiên bản sửa đổi: `CHƯA_BIẾT`.
- [Investor.gov — How to Read a 10-K](https://www.investor.gov/introduction-investing/getting-started/researching-investments/how-read-10-k), ngày xuất bản hiển thị: `CHƯA_BIẾT`; phạm vi: Form 10-K hằng năm của Mỹ; tiền tệ và đơn vị: không áp dụng; phiên bản sửa đổi: `CHƯA_BIẾT`.
- [Investor.gov — Build Wealth Over Time Through Saving and Investing](https://www.investor.gov/build-wealth-over-time-through-saving-and-investing), ngày xuất bản hiển thị: `CHƯA_BIẾT`; kỳ báo cáo, tiền tệ và đơn vị: không áp dụng; phiên bản sửa đổi: `CHƯA_BIẾT`.
- [Investor.gov — Beginners’ Guide to Asset Allocation, Diversification, and Rebalancing](https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset), ngày xuất bản hiển thị: `CHƯA_BIẾT`; kỳ báo cáo, tiền tệ và đơn vị: không áp dụng; phiên bản sửa đổi: `CHƯA_BIẾT`.

## Câu chốt

> “Rẻ” không nằm ở con số giá trên màn hình. Nó nằm trong quan hệ giữa giá phải trả, tiền doanh nghiệp có thể tạo ra, nợ, tăng trưởng và khả năng người phân tích đã ước tính sai.
