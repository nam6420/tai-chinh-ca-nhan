# Bài B2 — Margin và đòn bẩy: khoản vay có thể khuếch đại lỗ

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:07 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính được vốn ròng và tỷ lệ lỗ trong ví dụ vay mua chứng khoán; nhận diện rủi ro lãi vay, yêu cầu bổ sung tài sản và bán giải chấp.
- Bài trước liên quan: [P1](P1-budget-emergency-fund-insurance.md), [P2](P2-personal-debt.md), [V2](V2-vietnam-trading-rules.md).
- Câu hỏi cốt lõi: **Nếu giá giảm, khoản vay còn nguyên sẽ làm vốn của tôi thay đổi thế nào?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/B2-fact-check.md), [phản biện](../reviews/B2-risk-review.md).

## Hiểu bài trong một phút

Giao dịch ký quỹ (*margin*) dùng tiền vay để mua chứng khoán. Khi tài sản giảm giá, khoản nợ không tự giảm theo. Vốn của người vay chịu biến động trước và còn phải gánh lãi, phí. Bài này dạy nhận diện rủi ro; khả năng được vay không có nghĩa là nên vay.

## Ôn bài cũ

- Trong [Bài B1 — Công ty chứng khoán, phí và lưu ký](B1-broker-fees-custody.md) và [Bài 005 — Nợ, thanh khoản và khả năng sống sót](005-debt-liquidity-survival.md), bạn đã hiểu cấu trúc tài khoản và rủi ro đòn bẩy. Bài B2 giải thích toán học của vay ký quỹ (`Margin`), tỷ lệ ký quỹ duy trì và lệnh gọi ký quỹ (`Margin Call`).

---

## 1. Khoản vay và lớp đệm

`SỰ_THẬT` [FINRA — Margin Debt](https://syndication.finra.org/content/margin-debt-record-levels-know-risks) giải thích mua ký quỹ là vay từ công ty chứng khoán và phải trả gốc, lãi ngay cả khi đầu tư thua lỗ. Tài liệu này thuộc Hoa Kỳ; quyền và thủ tục tại Việt Nam cần đọc quy định và hợp đồng áp dụng.

`PHÉP_TÍNH` Trong mô hình đơn giản không có tài sản khác: `vốn ròng = giá trị tài sản − dư nợ`; `đòn bẩy ban đầu = giá trị vị thế ÷ vốn tự có`. Đây là phép tính minh họa; hợp đồng thật có thể dùng giá trị tài sản được chấp nhận, tỷ lệ định giá và khoản phải trả khác.

`KỊCH_BẢN` An có 100 triệu đồng, vay 100 triệu và mua vị thế trị giá 200 triệu. Bỏ qua lãi/phí và giả sử dư nợ không đổi: đòn bẩy `200 ÷ 100 = 2 lần`. Khi giá trị vị thế giảm 20%, còn `200 × 80% = 160` triệu; vốn ròng còn `160 − 100 = 60` triệu. Vốn giảm `40 ÷ 100 = 40%`. Giá giảm 20% nhưng lỗ trên vốn là 40%; nếu giá trị thấp hơn nợ, sau bán tài sản người vay vẫn có thể còn nghĩa vụ trả nợ.

## 2. Bổ sung tài sản và bán giải chấp

Một công ty có thể theo dõi tỷ lệ an toàn; nếu tài sản giảm, hợp đồng có thể yêu cầu người vay bổ sung tiền/tài sản hoặc giảm dư nợ. Nếu không đáp ứng, có thể phát sinh bán giải chấp theo quy định và hợp đồng. Ngưỡng, lịch thông báo, tài sản đủ điều kiện và quyền xử lý **không giống nhau trong mọi hợp đồng**.

`KỊCH_BẢN` Để hiểu phép chia, giả sử ngưỡng duy trì là 30% và tỷ lệ giả định tính bằng `(giá trị tài sản − dư nợ) ÷ giá trị tài sản`. Với nợ 100 triệu, ngưỡng này xảy ra tại `100 ÷ (1 − 30%) ≈ 142,86` triệu đồng tài sản. Đây chỉ là điều kiện toán học của bài, **không xác nhận ngưỡng thực tế hay thời điểm công ty được bán**; chưa tính lãi, phí, tỷ lệ định giá tài sản.

`SỰ_THẬT` FINRA cảnh báo trong khung Hoa Kỳ rằng công ty có thể bán chứng khoán để xử lý thiếu hụt, có thể nâng yêu cầu nội bộ và nhà đầu tư có thể vẫn còn thiếu nợ sau khi bán. [FINRA](https://syndication.finra.org/content/margin-debt-record-levels-know-risks). Không suy quy định Hoa Kỳ áp dụng nguyên vẹn cho hợp đồng Việt Nam.

`SỰ_THẬT` Điều 9 [Thông tư 120/2020/TT-BTC trong Công báo, đã hợp nhất các sửa đổi đến TT08/2026](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/29/469538-1779683486_v1_1780016834_signed.pdf) yêu cầu hợp đồng ghi tối thiểu tài sản bảo đảm, thời hạn bổ sung, cách xử lý nếu không bổ sung, rủi ro và chi phí. Khi tỷ lệ ký quỹ thấp hơn mức duy trì theo hợp đồng, công ty phát hành lệnh gọi bổ sung; nếu nhà đầu tư không bổ sung, công ty có quyền bán chứng khoán bảo đảm theo điều khoản hợp đồng, cùng nghĩa vụ công bố/thông báo theo quy định. Sở công bố danh sách đủ hoặc không đủ điều kiện, công ty chọn danh sách được vay tại mình; danh sách có thể thay đổi. Đây không xác định tỷ lệ hay thời hạn của một hợp đồng cụ thể.

`CHƯA_BIẾT` Mức ký quỹ tối thiểu, cách tính tỷ lệ, điều kiện thông báo và quyền xử lý của một công ty chứng khoán Việt Nam cụ thể tại thời điểm sử dụng: cần đối chiếu quy định hiện hành, danh sách chứng khoán đủ điều kiện và hợp đồng của chính công ty đó.

## 3. Lãi làm lớp đệm mỏng đi

`KỊCH_BẢN` Giả sử vay 100 triệu đồng, lãi đơn 13,5%/năm, 30 ngày trên cơ sở 365 ngày, không phí: `100.000.000 × 13,5% × 30 ÷ 365 ≈ 1.109.589` đồng. Đây là giả định để học công thức, không phải báo giá hay phương pháp tính của một hợp đồng cụ thể; lãi có thể tiếp tục phát sinh khi giá giảm.

`SỰ_THẬT` [VFS — Biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi) công bố biểu giá và điều kiện dịch vụ của công ty. Biểu phí có thể đổi, phụ thuộc sản phẩm, ngày và hợp đồng; bài không lấy một biểu giá làm mức chung toàn thị trường.

## Năm câu hỏi khi đọc hợp đồng

1. Nợ gốc và lãi tính theo ngày, cơ sở và thời hạn nào?
2. Tài sản nào được chấp nhận và được định giá bao nhiêu?
3. Ngưỡng cảnh báo, duy trì và quyền xử lý ghi thế nào?
4. Có phí, điều kiện quá hạn, thay đổi danh mục được vay hay không?
5. Điều gì xảy ra nếu giá giảm nhanh hoặc bán tài sản không đủ trả nợ?

## Bài tập

1. Vì sao giá giảm mà nợ vay không tự giảm?
2. Vốn 80 triệu, vay 80 triệu; vị thế 160 triệu giảm 25%. Giá trị còn bao nhiêu, vốn ròng còn bao nhiêu và lỗ bao nhiêu phần trăm vốn? Bỏ lãi/phí.
3. Vì sao một thông báo yêu cầu bổ sung tiền không tự chứng minh người vay chắc chắn có đủ thời gian xử lý?
4. Giả sử vay 80 triệu, lãi đơn 12%/năm, 45 ngày/365: tiền lãi là bao nhiêu?
5. Nếu bán tài sản không đủ trả nợ, có thể còn nghĩa vụ gì?
6. Vì sao không lấy quy tắc FINRA của Mỹ làm kết luận pháp lý cho một hợp đồng Việt Nam?

## Đáp án

1. Nợ là nghĩa vụ hợp đồng; biến động giá không tự xóa khoản vay.
2. Tài sản `160 × 75% = 120` triệu; vốn ròng `120 − 80 = 40` triệu; lỗ vốn `(80 − 40) ÷ 80 = 50%`.
3. Điều kiện xử lý phụ thuộc quy định/hợp đồng; ví dụ FINRA là Hoa Kỳ, còn quyền ở Việt Nam cần kiểm nguồn và hợp đồng.
4. `80.000.000 × 12% × 45 ÷ 365 ≈ 1.183.562` đồng, theo giả định lãi đơn.
5. Có thể còn nợ gốc, lãi và phí theo điều kiện áp dụng; không tự coi tài sản bán hết là hết nghĩa vụ.
6. Hai thị trường có luật và hợp đồng khác; cần kiểm văn bản Việt Nam tại thời điểm áp dụng.

## Lỗi thường gặp và ranh giới an toàn

- Chỉ nhìn lãi suất mà bỏ qua bán giải chấp, thời điểm xử lý, biến động giá và thiếu thanh khoản.
- Nhầm khoản vay mua cổ phiếu với ký quỹ phái sinh; cơ chế và rủi ro cần học riêng.
- Không khuyến nghị sử dụng đòn bẩy hoặc một ngưỡng vay; ví dụ chỉ là số giả định.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Danh sách chứng khoán được vay, ngưỡng duy trì, cách định giá và quyền xử lý ở công ty cụ thể; phải kiểm hợp đồng, biểu phí và quy định hiện hành trước khi đánh giá.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [TT120 hợp nhất, Công báo 29/05/2026](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/29/469538-1779683486_v1_1780016834_signed.pdf), Điều 9; [FINRA — Margin Debt](https://syndication.finra.org/content/margin-debt-record-levels-know-risks), 18/01/2018, Hoa Kỳ; [VFS — Biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi), Việt Nam, ngày hiệu lực từng dòng cần kiểm trên biểu giá.
