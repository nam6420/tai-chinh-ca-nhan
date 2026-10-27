# Bài A4 — Phân bổ tài sản, tương quan và tái cân bằng

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:24 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính tỷ trọng, mô phỏng tái cân bằng và góp định kỳ; giải thích vì sao đa dạng hóa không bảo đảm tránh lỗ.
- Bài trước liên quan: [N4](N4-time-value-returns.md), [N5](N5-portfolio-index-investing.md), [N7](N7-data-probability-uncertainty.md), [P3](P3-goals-risk-ips.md).
- Câu hỏi cốt lõi: Tỷ trọng tài sản thay đổi như thế nào, và điều gì có thể làm chiến lược dự kiến không còn phù hợp?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A4-fact-check.md), [phản biện](../reviews/A4-risk-review.md).

## Hiểu bài trong một phút

Phân bổ tài sản là chia danh mục giữa các loại tài sản theo mục tiêu và rủi ro. Nếu hai phần biến động khác nhau, tỷ trọng sẽ trôi khỏi mức dự kiến. Tái cân bằng đưa tỷ trọng về một đích đã chọn; đích, lịch và phí đều là giả định cần xem lại, không phải công thức bảo đảm kết quả.

## 1. Phân bổ và tương quan

`SỰ_THẬT` [SEC Hoa Kỳ — hướng dẫn phân bổ và tái cân bằng](https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset) mô tả đa dạng hóa giữa các nhóm và trong từng nhóm. Tài liệu là hướng dẫn giáo dục, không xác định tỷ trọng phù hợp cho người đọc Việt Nam.

Theo [NIST — hệ số tương quan](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm), tương quan Pearson mô tả quan hệ tuyến tính giữa hai biến. Với hai chuỗi lợi suất trong một mẫu: +1 là cùng chiều tuyến tính hoàn hảo, −1 là ngược chiều tuyến tính hoàn hảo, gần 0 là ít quan hệ tuyến tính trong mẫu. `SUY_LUẬN` Tương quan trong quá khứ có thể thay đổi; nhiều tài sản vẫn có thể cùng giảm trong khủng hoảng. Không suy không tương quan thành độc lập hay không có lỗ.

`KỊCH_BẢN` Danh mục gồm hai nhóm A và B, mục tiêu 50%/50% chỉ để tính bài. Cả hai có thể là nhiều tài sản bên trong; hai tên nhóm không tự chứng minh đã đa dạng hóa.

## 2. Tỷ trọng trôi và tái cân bằng

`KỊCH_BẢN` Ban đầu A = 50 triệu, B = 50 triệu. Sau đó A = 70 triệu, B = 50 triệu; không có dòng tiền mới, bỏ qua phí và thuế.

`PHÉP_TÍNH` Tổng = 120 triệu; A = 70/120 ≈ 58,33%, B ≈ 41,67%. Đích 50% mỗi bên tương đương 60 triệu. Bán 10 triệu A và mua 10 triệu B theo giả định không phí để về đích. Thực tế cần kiểm giá giao dịch, thanh khoản, phí, thuế, số lượng đơn vị tối thiểu và điều kiện tài khoản; không thể mặc định kết quả ròng đúng như ví dụ.

Một cách khác trong mô hình là góp thêm vào B thay vì bán A: để A/B đều 70 triệu phải góp 20 triệu vào B, tổng thành 140 triệu. Không được nhầm việc góp mới 20 triệu với việc chuyển 10 triệu trong danh mục không có dòng tiền mới. Có thể xem xét lịch định kỳ hoặc ngưỡng lệch do chính sách chọn; không có một lịch duy nhất luôn tốt hơn.

## 3. Góp đều theo kỳ

`SỰ_THẬT` [SEC — Dollar Cost Averaging](https://www.investor.gov/introduction-investing/investing-basics/glossary/dollar-cost-averaging) mô tả góp số tiền bằng nhau theo khoảng thời gian đều: giá thấp mua được nhiều đơn vị hơn, giá cao mua ít hơn, trước khi xét điều kiện giao dịch.

`KỊCH_BẢN` Mỗi kỳ góp 1 triệu đồng, giá lần lượt 10.000 và 20.000 đồng/đơn vị; giả định mua được đơn vị lẻ, không phí. `PHÉP_TÍNH` Lần đầu mua 100, lần sau 50; tổng 150 đơn vị với 2 triệu đồng, giá vốn bình quân ≈ 13.333 đồng/đơn vị. Giá bình quân số học của hai thời điểm là 15.000 đồng, nhưng không phải giá vốn vì số đơn vị mua khác nhau.

Góp đều không bảo đảm có lãi và không luôn tốt hơn đầu tư một lần khi đã có sẵn tiền; kết quả phụ thuộc đường đi giá, thời điểm, tiền chưa đầu tư và chi phí. Chỉ minh họa cách tính, không đề xuất lịch góp cho cá nhân.

## Năm câu hỏi khi đọc

1. Mục tiêu, thời hạn, nhu cầu tiền và khả năng chịu rủi ro là gì?
2. Danh mục phân tán trong và giữa các nhóm hay chỉ đổi tên nhiều sản phẩm cùng rủi ro?
3. Tương quan được đo bằng chuỗi, kỳ và đồng tiền nào; có thể thay đổi không?
4. Tái cân bằng bằng bán/mua hay bằng tiền mới; phí, thuế và thanh khoản ra sao?
5. Góp đều có giả định mua đơn vị lẻ, mức phí tối thiểu và giá thực hiện nào?

## Bài tập

1. A 80 triệu, B 20 triệu: tỷ trọng A là bao nhiêu?
2. Với tổng 100 triệu và đích A/B 50/50, chuyển bao nhiêu từ A sang B nếu bỏ qua phí?
3. A 70, B 50 triệu: cần góp vào B bao nhiêu để về 50/50 mà không bán A?
4. Hai lần góp 600.000 đồng khi giá lần lượt 6.000 và 12.000 đồng: mua tổng bao nhiêu đơn vị? Bỏ phí và cho phép mua lẻ.
5. Tương quan quá khứ thấp có bảo đảm hai tài sản không cùng giảm không?
6. Kể hai chi phí hoặc giới hạn khiến kết quả tái cân bằng thực tế khác phép tính giả định.

## Đáp án

1. `PHÉP_TÍNH` 80/100 = 80%.
2. Đích 50 triệu mỗi bên; chuyển 30 triệu từ A sang B, theo giả định.
3. Góp 20 triệu, để mỗi bên 70 triệu.
4. 600.000/6.000 + 600.000/12.000 = 100 + 50 = 150 đơn vị; tổng góp 1,2 triệu đồng.
5. Không; tương quan thay đổi, dữ liệu mẫu không bảo đảm tương lai và không mô tả mọi rủi ro cực đoan.
6. Ví dụ: phí mua bán, thuế, thanh khoản, lô/đơn vị tối thiểu hoặc chênh lệch giá.

## Lỗi thường gặp và ranh giới an toàn

Nhầm tỷ trọng với số tiền, tiền góp với tiền chuyển, tương quan với nhân quả; tin rằng tái cân bằng hoặc góp đều loại bỏ rủi ro. Không dùng con số 50/50 trong bài như khuyến nghị danh mục.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Tỷ trọng, loại tài sản, thuế và phí phù hợp từng người; tương quan tương lai và lợi suất thực tế. Cần xem mục tiêu, ràng buộc và dữ liệu mới theo từng tình huống.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [SEC — phân bổ, đa dạng hóa và tái cân bằng](https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset), không ghi ngày trong phần đã đọc, Hoa Kỳ; [SEC — góp đều](https://www.investor.gov/introduction-investing/investing-basics/glossary/dollar-cost-averaging), không ghi ngày, Hoa Kỳ; [NIST — hệ số tương quan](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm), không ghi ngày. Ví dụ số đều hư cấu.
