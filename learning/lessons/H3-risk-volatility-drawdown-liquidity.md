# Bài H3 — Đo rủi ro: biến động, sụt giảm và thanh khoản

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:39 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính mức sụt giảm tối đa của chuỗi mẫu và phân biệt nó với biến động, thanh khoản, tập trung và mất vốn.
- Bài trước liên quan: [N7](N7-data-probability-uncertainty.md), [A4](A4-allocation-correlation-rebalancing.md), [H2](H2-decisions-stress-position-size.md).
- Câu hỏi cốt lõi: Một con số rủi ro cho biết điều gì và không cho biết điều gì?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/H3-fact-check.md), [phản biện](../reviews/H3-risk-review.md).

## Hiểu bài trong một phút

Biến động đo độ phân tán lợi suất; sụt giảm từ đỉnh đến đáy đo đường đi vốn; thanh khoản hỏi có thể bán nhanh ở mức giá nào. Ba câu hỏi liên quan nhưng không thể thay nhau. Dữ liệu quá khứ không bảo đảm mức lỗ tương lai sẽ nhỏ hơn mức từng thấy.

## 1. Đường đi và sụt giảm

`SỰ_THẬT` Goldberg và Mahmoud, [Drawdown: From Practice to Theory and Back Again](https://arxiv.org/abs/1404.7493), bản đầu 2014, bản sửa 2016, mô tả mức sụt giảm tối đa là khoản giảm tích lũy lớn nhất từ đỉnh đến đáy trong cửa sổ nghiên cứu. Phải nêu khoảng thời gian, đơn vị, tần suất dữ liệu và liệu có tính cổ tức/dòng tiền.

`KỊCH_BẢN` Danh mục không có nạp/rút trong kỳ, các giá trị hư cấu: `100 → 110 → 88 → 101,2 → 106,26`. Từ đỉnh 110 xuống đáy 88, `PHÉP_TÍNH` mức giảm = `88/110 − 1 = −20%`. Trong chuỗi này đó là mức sụt giảm lớn nhất từ một đỉnh trước đó tới đáy sau đó. Để từ 88 về 110 cần `110/88 − 1 = +25%`; mẫu số khác nhau.

Nếu lấy dữ liệu thưa theo tháng, đáy giữa tháng có thể không hiện trong mẫu. Nếu có nạp/rút, phải điều chỉnh cách đo để không biến dòng tiền thành lợi suất hoặc sụt giảm đầu tư.

## 2. Biến động, thanh khoản, tập trung

Biến động thường được đo bằng độ lệch chuẩn của chuỗi lợi suất quanh mức trung bình; kết quả phụ thuộc kỳ và tần suất. Một thước đo phân tán không tự mô tả đầy đủ thiệt hại cực đoan, khả năng thanh toán hay rủi ro bán không được.

`SỰ_THẬT` [SEC Hoa Kỳ — Liquidity](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability) giải thích thanh khoản liên quan khả năng mua hoặc bán nhanh mà không ảnh hưởng lớn tới giá. Giá hiển thị không bảo đảm toàn bộ lượng nắm giữ bán được tại giá đó; spread, độ sâu sổ lệnh và thị trường căng thẳng cần xem riêng.

`KỊCH_BẢN` Danh mục 100 triệu gồm 60 triệu A và 40 triệu B, trong đó hai quỹ đều giữ phần lớn cùng một ngành. Hai tên quỹ không tự chứng minh rủi ro đã phân tán; cần xem danh mục nắm giữ, chủ thể phát hành và các yếu tố chung. Tập trung còn có thể xảy ra theo đồng tiền hoặc nguồn thu nhập, không chỉ theo tên mã.

## 3. Mất vốn tạm thời hay vĩnh viễn?

`SUY_LUẬN` Giá giảm hôm nay không tự chứng minh tổn thất sẽ hồi phục hoặc là vĩnh viễn. Cần xem khả năng tạo tiền, nợ, quyền của người nắm giữ, pha loãng và liệu người đó có buộc phải bán khi cần tiền. Một doanh nghiệp phá sản hoặc quyền sở hữu bị pha loãng có thể thay đổi khả năng thu hồi; cũng không thể xác định chỉ bằng một điểm giá.

Không đo tương lai bằng một con số duy nhất. Thử kết hợp đường đi, biến động, mức tập trung, thanh khoản và tình huống bất lợi; giữ lại điều chưa biết.

## Năm câu hỏi khi đọc

1. Cửa sổ thời gian và tần suất nào được dùng để tính?
2. Lợi suất có gồm dòng tiền, phí, thuế và cổ tức phù hợp không?
3. Sụt giảm, biến động hay thanh khoản đang được đo?
4. Danh mục có rủi ro chồng lấn dù tên quỹ khác nhau không?
5. Điều gì có thể khiến mất vốn không hồi phục hoặc buộc bán?

## Bài tập

1. Chuỗi 100 → 120 → 90 → 108: mức giảm từ đỉnh tới đáy là bao nhiêu?
2. Từ 90 về 120 cần tăng bao nhiêu phần trăm?
3. Sụt giảm tối đa quá khứ có bảo đảm mức lỗ tương lai không lớn hơn không?
4. Giao dịch ít và spread rộng có thể ảnh hưởng khả năng bán thế nào?
5. Hai quỹ cùng giữ một nhóm tài sản có tự phân tán rủi ro không?
6. Giá giảm có tự chứng minh tổn thất vĩnh viễn không?

## Đáp án

1. 90/120 − 1 = −25%; đó là mức giảm lớn nhất trong chuỗi này.
2. 120/90 − 1 ≈ +33,33%.
3. Không; tương lai có thể khác và tần suất lấy mẫu có thể bỏ lỡ đáy.
4. Có thể khó bán nhanh, phải chấp nhận giá kém hơn hoặc không bán hết.
5. Không; cần xem mức chồng lấn và yếu tố rủi ro chung.
6. Không; cần đánh giá quyền, dòng tiền, nợ và hoàn cảnh người nắm giữ.

## Lỗi thường gặp và ranh giới an toàn

Gọi độ biến động là toàn bộ rủi ro; so mức giảm không cùng cửa sổ/đồng tiền; coi đáy lịch sử là mức lỗ tối đa. Đây là phương pháp học, không dự báo hay khuyến nghị danh mục.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Tương lai giá, thanh khoản, dòng tiền và khả năng hồi phục của tài sản cụ thể; cần dữ liệu và điều kiện phù hợp trước khi kết luận.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [Goldberg & Mahmoud — Drawdown](https://arxiv.org/abs/1404.7493), 2014, sửa 2016; [SEC — Liquidity](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability), không ghi ngày, Hoa Kỳ. Các chuỗi số đều hư cấu.
