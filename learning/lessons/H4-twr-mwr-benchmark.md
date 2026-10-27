# Bài H4 — Đo kết quả: TWR, MWR và chuẩn tham chiếu

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính lợi suất theo thời gian, thiết lập phương trình lợi suất theo dòng tiền và chọn cách so sánh nhất quán.
- Bài trước liên quan: [N4](N4-time-value-returns.md), [N5](N5-portfolio-index-investing.md), [H3](H3-risk-volatility-drawdown-liquidity.md).
- Câu hỏi cốt lõi: Kết quả danh mục và kết quả tiền thực góp khác nhau thế nào khi vốn được nạp hoặc rút?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/H4-fact-check.md), [phản biện](../reviews/H4-risk-review.md).

## Hiểu bài trong một phút

Hai người nắm cùng danh mục nhưng góp thêm tiền vào thời điểm khác nhau có thể có kết quả tiền của mình khác nhau. Lợi suất theo thời gian nhìn chuỗi tăng giảm của danh mục theo từng đoạn; lợi suất theo dòng tiền nhạy với số tiền và thời điểm nạp/rút. Không nên so hai số này mà không ghi phương pháp.

## 1. Lợi suất theo thời gian

`SỰ_THẬT` [CFA Institute — Rates and Returns](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/rates-and-returns) trình bày các cách đo lợi suất, trong đó lợi suất theo thời gian (time-weighted return, TWR) ghép lợi suất các giai đoạn để giảm ảnh hưởng của thời điểm dòng tiền bên ngoài.

`KỊCH_BẢN` Đầu năm 1 có 100 triệu, cuối năm 1 thành 110 triệu; ngay khi đó góp thêm 100 triệu, tổng 210 triệu. Cuối năm 2 còn 189 triệu. Bỏ thuế và phí; định giá chính xác ngay trước và sau lần góp.

`PHÉP_TÍNH` Năm 1: 110/100 − 1 = +10%. Năm 2: 189/210 − 1 = −10%. TWR gộp hai năm = `(1 + 10%) × (1 − 10%) − 1 = −1%`. Đây là kết quả toàn kỳ hai năm, không phải −1%/năm. Nếu cần năm hóa: `sqrt(0,99) − 1 ≈ −0,50%/năm` với giả định hai năm bằng nhau.

## 2. Lợi suất theo dòng tiền

Lợi suất theo dòng tiền (money-weighted return, MWR) ở ví dụ này là nghiệm r của phương trình giá trị hiện tại ròng bằng 0, theo quan điểm người góp vốn: `−100 − 100/(1+r) + 189/(1+r)² = 0`. `PHÉP_TÍNH` Nghiệm phù hợp khoảng **−3,71%/năm**; khác TWR vì khoản góp 100 triệu đi vào trước năm giảm. Tính theo cùng đơn vị triệu và giả định thời điểm chính xác.

Không phải mọi chuỗi dòng tiền đều có một nghiệm nội suy duy nhất hoặc một nghiệm có ý nghĩa; nhiều lần đổi dấu có thể tạo nhiều nghiệm hoặc không có nghiệm phù hợp. Ghi rõ quy ước dấu, ngày nạp/rút, định giá, thuế/phí và công cụ tính. Một kết quả máy tính không tự chứng minh tính duy nhất của nghiệm.

## 3. So với chuẩn tham chiếu

Một chỉ số chỉ hữu ích nếu phù hợp câu hỏi: cùng kỳ, đồng tiền, loại lợi suất giá hay tổng lợi suất, cách xử lý cổ tức và chi phí; khác biệt rủi ro, loại tài sản và khả năng đầu tư cũng cần xem xét. [CFA — tài liệu GIPS](https://www.cfainstitute.org/-/media/documents/code/gips/2020-gips-standards-asset-owners.pdf) trình bày các yêu cầu về báo cáo và chuẩn tham chiếu trong phạm vi chuẩn GIPS; không suy mọi danh mục cá nhân đã tuân thủ GIPS.

`KỊCH_BẢN` Danh mục tăng 8%, chỉ số tăng 6% cùng kỳ và cùng cơ sở giả định; chênh lệch thô = 2 điểm phần trăm. Chênh lệch này chưa điều chỉnh rủi ro hoặc chứng minh kỹ năng và không tự là alpha.

## Năm câu hỏi khi đọc

1. Dùng TWR hay MWR, thời gian đo và tiền tệ nào?
2. Định giá khi nào; cổ tức, phí, thuế và dòng tiền được xử lý ra sao?
3. Con số là toàn kỳ hay năm hóa?
4. Chuẩn tham chiếu có cùng kỳ, loại lợi suất và phạm vi tài sản không?
5. Nếu dùng IRR, có nhiều nghiệm hoặc dòng tiền thay dấu nhiều lần không?

## Bài tập

1. Chuỗi +10%, −10% cho TWR toàn kỳ bao nhiêu?
2. Bỏ tiền vào ngay trước giai đoạn thua lỗ có thể khiến MWR khác TWR không?
3. Đầu 100, cuối 110, không có dòng tiền: lợi suất một năm?
4. Danh mục 8%, chỉ số 6% cùng cơ sở: chênh lệch thô?
5. Có thể so lợi suất có cổ tức với chỉ số chỉ giá như thể hai bên cùng định nghĩa không?
6. IRR của chuỗi dòng tiền nhiều lần đổi dấu có luôn duy nhất không?

## Đáp án

1. 1,10 × 0,90 − 1 = −1% toàn kỳ.
2. Có; MWR nhạy với số tiền và thời điểm dòng tiền.
3. 110/100 − 1 = 10%.
4. 2 điểm phần trăm; chưa điều chỉnh rủi ro.
5. Không; cần thống nhất cách tính hoặc nêu rõ sự khác biệt.
6. Không; cần kiểm nghiệm và cách diễn giải.

## Lỗi thường gặp và ranh giới an toàn

Cộng +10% và −10% thành 0%, quên phân biệt toàn kỳ với năm hóa, hoặc gọi mọi mức vượt chỉ số là kỹ năng. Các số chỉ là ví dụ học tập, không là dự báo hay khuyến nghị.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Dòng tiền, định giá, phí và chuẩn phù hợp của một danh mục thực tế; phải lấy dữ liệu gốc và thống nhất quy ước trước khi tính.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [CFA Institute — Rates and Returns, ấn bản 2026](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/rates-and-returns); [CFA — 2020 GIPS Standards for Asset Owners](https://www.cfainstitute.org/-/media/documents/code/gips/2020-gips-standards-asset-owners.pdf), tiêu chuẩn 2020. Ví dụ dòng tiền hư cấu.
