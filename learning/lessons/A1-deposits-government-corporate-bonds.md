# Bài A1 — Tiền gửi và trái phiếu

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt tiền gửi với trái phiếu Chính phủ và doanh nghiệp; tính ví dụ lãi đơn và giá trái phiếu một kỳ.
- Bài trước liên quan: [N4](N4-time-value-returns.md), [P1](P1-budget-emergency-fund-insurance.md), [005](005-debt-liquidity-survival.md).
- Câu hỏi cốt lõi: Ai có nghĩa vụ trả tiền, khi nào, và rủi ro nào không được lãi suất công bố thể hiện?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A1-fact-check.md), [phản biện](../reviews/A1-risk-review.md).

## Hiểu bài trong một phút

Tiền gửi là khoản tiền theo hợp đồng với tổ chức nhận tiền. Trái phiếu là khoản nợ của tổ chức phát hành: người nắm giữ trông đợi các khoản thanh toán theo điều khoản, nhưng vẫn đối mặt với rủi ro tín dụng, giá, thanh khoản và lạm phát. Một mức lãi cao không tự bảo đảm người phát hành có khả năng trả.

## 1. Tiền gửi

`KỊCH_BẢN` Gửi 100 triệu đồng, lãi đơn giả định 5%/năm, giữ tròn một năm, không tính thuế và điều khoản khác. `PHÉP_TÍNH` Lãi = 100 × 5% × 1 = 5 triệu; gốc và lãi = 105 triệu đồng. Rút trước hạn, nhập lãi vào gốc và cách đếm ngày có thể làm kết quả khác; xem hợp đồng cụ thể.

`SỰ_THẬT` [Bảo hiểm tiền gửi Việt Nam](https://www.div.gov.vn/bao-hiem-tien-gui-chi-ap-dung-doi-voi-tien-gui-cua-ca-nhan-bang-dong-viet-nam) nêu bảo hiểm áp dụng cho tiền gửi thuộc diện được bảo hiểm của cá nhân bằng VND; các điều kiện và loại trừ phải kiểm trong luật. [Thông tư 05/2026/TT-NHNN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/05-nhnn.pdf) quy định hạn mức chi trả 350 triệu đồng tính gộp gốc và lãi được bảo hiểm của một người tại một tổ chức tham gia khi phát sinh nghĩa vụ chi trả; xem [P1](P1-budget-emergency-fund-insurance.md). Đây không phải hạn mức cho từng tài khoản hay bảo đảm mọi khoản đầu tư ở ngân hàng.

## 2. Hai loại trái phiếu

`SỰ_THẬT` [SEC Hoa Kỳ — Bonds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds) mô tả trái phiếu là khoản cho chính phủ, chính quyền địa phương hoặc doanh nghiệp vay theo điều khoản phát hành. Tài liệu giải thích cơ chế quốc tế, không thay cho quy định Việt Nam.

| Câu hỏi | Trái phiếu Chính phủ | Trái phiếu doanh nghiệp |
|---|---|---|
| Nghĩa vụ trả của ai? | Chính phủ phát hành theo điều khoản cụ thể | Doanh nghiệp phát hành theo điều khoản cụ thể |
| Điều cần đọc | Kỳ hạn, lãi/cách thanh toán, giá và thanh khoản | Khả năng trả nợ, điều khoản, bảo đảm/bảo lãnh nếu có, kỳ hạn và thanh khoản |
| Có phải tiền gửi bảo hiểm? | Không phải tiền gửi ngân hàng | Không phải tiền gửi ngân hàng |

`SỰ_THẬT` [Bộ Tài chính cảnh báo về trái phiếu doanh nghiệp](https://xaydungchinhsach.chinhphu.vn/nong-bo-tai-chinh-khuyen-cao-cac-chu-the-tham-gia-thi-truong-trai-phieu-doanh-nghiep-119221114165946867.htm), 17/11/2022: nhà đầu tư cần đánh giá doanh nghiệp phát hành và các rủi ro; tổ chức phân phối không mặc nhiên là bên bảo đảm thanh toán. Đây là cảnh báo rủi ro, không dùng để kết luận quy định chào bán năm 2026. `CHƯA_BIẾT` Điều kiện mua trái phiếu doanh nghiệp riêng lẻ và hồ sơ của một đợt cụ thể phải kiểm luật hiện hành và tài liệu đợt phát hành.

Tài sản bảo đảm hoặc bảo lãnh cần xem ai chịu trách nhiệm, giá trị, thứ tự ưu tiên và khả năng thực thi; không bảo đảm tự động thu hồi đủ. Người nắm giữ vẫn có thể gặp rủi ro lạm phát và thanh khoản dù không xảy ra vỡ nợ.

## 3. Giá khi lãi suất thay đổi

`KỊCH_BẢN` Trái phiếu còn một năm, cuối năm trả 10 triệu gốc và 0,5 triệu lãi; không có dòng tiền khác, giả định chắc chắn trả, bỏ thuế/phí. Nếu mức chiết khấu cho dòng tiền giả định là 6%/năm, `PHÉP_TÍNH` giá mô hình = 10,5/1,06 ≈ 9,906 triệu đồng. Nếu là 4%, giá = 10,5/1,04 ≈ 10,096 triệu đồng.

[SEC Hoa Kỳ](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-86) giải thích quan hệ thông thường giữa lãi suất và giá trái phiếu lãi cố định: khi lãi suất thị trường tăng, giá trái phiếu hiện hữu thường giảm. Đây là mô hình trực giác; giá thực tế còn chịu rủi ro tín dụng, kỳ hạn, thanh khoản và cách tính lãi. Nắm đến hạn không loại bỏ nguy cơ tổ chức phát hành không trả.

## Năm câu hỏi khi đọc

1. Ai nhận tiền và ai có nghĩa vụ trả gốc/lãi?
2. Tiền gửi có thuộc phạm vi bảo hiểm và hạn mức áp dụng không?
3. Lãi cố định hay thay đổi, ngày trả và điều kiện rút/bán là gì?
4. Người phát hành có dòng tiền và khả năng trả nợ nào; bảo đảm có thể thực thi không?
5. Nếu phải bán trước hạn, giá, phí và thanh khoản có thể thay đổi thế nào?

## Bài tập

1. Gửi 20 triệu, lãi đơn 4,5%/năm trong 9 tháng: lãi bao nhiêu?
2. Hạn mức bảo hiểm được tính riêng cho từng tài khoản hay gộp theo người và tổ chức như nguồn nêu?
3. Ngân hàng phân phối trái phiếu có tự là bên bảo lãnh trả nợ không?
4. Trái phiếu một năm trả tổng 21,2 triệu cuối kỳ, chiết khấu 8%: giá mô hình?
5. Giá mô hình có thể thay đổi nếu lãi suất tăng không?
6. Nêu hai lý do tài sản bảo đảm không tự bảo đảm thu hồi toàn bộ nợ.

## Đáp án

1. `PHÉP_TÍNH` 20.000.000 × 4,5% × 9/12 = 675.000 đồng; theo giả định lãi đơn.
2. Gộp khoản thuộc diện được bảo hiểm theo một người tại một tổ chức tham gia, gồm gốc và lãi, trong điều kiện luật quy định.
3. Không; kiểm hợp đồng và chủ thể bảo lãnh thực sự nếu có.
4. 21,2/1,08 ≈ 19,63 triệu đồng, theo mô hình một dòng tiền.
5. Có; trái phiếu lãi cố định thường giảm giá khi lãi suất thị trường tăng, các yếu tố khác cũng ảnh hưởng.
6. Giá trị tài sản có thể thiếu; quyền ưu tiên, thủ tục và khả năng bán/thực thi có thể giới hạn thu hồi.

## Lỗi thường gặp và ranh giới an toàn

Nhầm trái phiếu với tiền gửi, nhầm bên phân phối với bên bảo lãnh, xem lãi cao là bằng chứng an toàn, hoặc bỏ qua điều kiện bán trước hạn. Các con số là giả định học tập, không là khuyến nghị hay báo giá.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Lãi suất hiện hành, điều kiện cho từng sản phẩm, việc phát hành riêng lẻ và quyền bảo hiểm của tài khoản cụ thể. Phải đọc hợp đồng, tài liệu phát hành và nguồn có thẩm quyền tại ngày sử dụng.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [Bảo hiểm tiền gửi Việt Nam](https://www.div.gov.vn/bao-hiem-tien-gui-chi-ap-dung-doi-voi-tien-gui-cua-ca-nhan-bang-dong-viet-nam), 16/06/2026; [Thông tư 05/2026/TT-NHNN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/05-nhnn.pdf); [Bộ Tài chính — cảnh báo trái phiếu](https://xaydungchinhsach.chinhphu.vn/nong-bo-tai-chinh-khuyen-cao-cac-chu-the-tham-gia-thi-truong-trai-phieu-doanh-nghiep-119221114165946867.htm), 17/11/2022; [SEC — Bonds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds), và [SEC — lãi suất và trái phiếu](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-86), Hoa Kỳ. Ví dụ số hư cấu.
