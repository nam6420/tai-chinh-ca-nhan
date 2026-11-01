# Bài A5 — Đầu tư nước ngoài: tỷ giá, thuế và quyền tiếp cận

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:33 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính lợi suất quy đổi theo tỷ giá, nhận diện rủi ro xuyên biên giới và lập danh sách điều kiện pháp lý/thuế cần kiểm.
- Bài trước liên quan: [N4](N4-time-value-returns.md), [A4](A4-allocation-correlation-rebalancing.md), [L3](L3-personal-income-tax-reporting.md).
- Câu hỏi cốt lõi: Đầu tư bằng một đồng tiền nhưng chi tiêu bằng đồng khác làm kết quả thay đổi thế nào, và ai được phép tiếp cận sản phẩm?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A5-fact-check.md), [phản biện](../reviews/A5-risk-review.md).

## Hiểu bài trong một phút

Một tài sản tăng giá bằng USD vẫn có thể giảm khi quy đổi sang VND nếu USD mất giá đủ mạnh so với VND. Ngoài tỷ giá, cần kiểm quyền đầu tư, nơi tài sản lưu ký, thuế, phí và cách giải quyết tranh chấp. Ví dụ dưới là mô hình học, không hướng dẫn chuyển tiền ra nước ngoài hay mở tài khoản.

## 1. Hai nguồn thay đổi giá trị

`SỰ_THẬT` [SEC — International Investing](https://www.investor.gov/introduction-investing/investing-basics/investment-products/international-investing), tài liệu giáo dục Hoa Kỳ, nêu tỷ giá có thể làm tăng hoặc giảm lợi suất bằng đồng tiền nhà đầu tư; rủi ro còn gồm thông tin, chi phí, kiểm soát tiền tệ, thanh khoản và khả năng thực thi quyền. Không suy quy tắc dành cho nhà đầu tư Hoa Kỳ thành quyền đầu tư của người cư trú Việt Nam.

`KỊCH_BẢN` Một khoản tài sản ban đầu 1.000 USD, tăng 10% lên 1.100 USD. Tỷ giá đầu kỳ 25.000 VND/USD, cuối kỳ 23.000 VND/USD; bỏ qua cổ tức, phí và thuế, giả định toàn bộ giá trị được quy đổi đúng tỷ giá đó.

`PHÉP_TÍNH` Đầu kỳ = 1.000 × 25.000 = 25.000.000 VND. Cuối kỳ = 1.100 × 23.000 = 25.300.000 VND. Lợi suất VND = 25.300.000/25.000.000 − 1 = **1,2%**, dù lợi suất USD là 10%. Tỷ giá giảm 8%; hệ số kết hợp là `(1 + 10%) × (1 − 8%) − 1 = 1,2%`. Phải nhân các hệ số, không cộng đơn giản 10% − 8% thành 2%.

`KỊCH_BẢN` Nếu cuối kỳ là 20.000 VND/USD, 1.100 USD = 22.000.000 VND; lợi suất VND = −12%. Các tỷ giá chỉ là số giả định, không là báo giá hay dự báo.

## 2. Tiếp cận và vận hành

`SỰ_THẬT` Điều 5 [Nghị định 135/2015/NĐ-CP trong bản hợp nhất năm 2019](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2019/2/28533/26003-1-2019267-26808-vbhn-nhnn.pdf) quy định trong phạm vi đầu tư gián tiếp ra nước ngoài của nghị định rằng cá nhân có quốc tịch Việt Nam chỉ thực hiện theo hình thức tham gia chương trình thưởng cổ phiếu phát hành ở nước ngoài. Đây là một rào cản pháp lý quan trọng, không phải quy tắc chung cho mọi hình thức sở hữu tài sản ở nước ngoài. `CHƯA_BIẾT` Quan hệ và chuyển tiếp giữa quy định đó với Luật Đầu tư 2025, văn bản hướng dẫn mới, từng nguồn tiền và hình thức nắm giữ chưa được xác định đầy đủ; không suy từ điều này rằng mọi cách nắm giữ tài sản nước ngoài đều bị cấm hay được phép.

`CHƯA_BIẾT` Quyền mở tài khoản, mua tài sản nước ngoài và chuyển ngoại tệ của người cư trú Việt Nam phụ thuộc pháp luật, loại giao dịch và tư cách cụ thể. Bài chưa xác minh đầy đủ văn bản hiện hành cho từng trường hợp; không suy rằng có ứng dụng hoặc ngân hàng chấp nhận giao dịch thì giao dịch chắc chắn hợp pháp. Trước khi thực hiện, đối chiếu cơ quan quản lý, ngân hàng được phép và tư vấn pháp lý phù hợp.

`Ý_KIẾN` Khi xem một sản phẩm, ghi rõ thị trường niêm yết, pháp nhân phát hành, đồng tiền tài sản, đồng tiền giao dịch và đồng tiền chi tiêu; đơn vị môi giới, lưu ký, giấy phép, cách đối chiếu tài sản và xử lý tranh chấp. Quỹ niêm yết trong nước có thể có mức tiếp xúc nước ngoài khác với việc trực tiếp mua chứng khoán ở nước ngoài; phải đọc tài liệu của sản phẩm cụ thể, không tự suy quyền hoặc phạm vi đầu tư.

## 3. Thuế và sổ hồ sơ

`SỰ_THẬT` [Báo điện tử Chính phủ, 16/10/2026](https://baochinhphu.vn/luong-nuoc-ngoai-chuyen-ve-tai-khoan-viet-nam-co-phai-nop-thue-102261015162615642.htm) trích quy định về phạm vi thu nhập chịu thuế: cá nhân cư trú gồm thu nhập phát sinh trong và ngoài Việt Nam, còn cá nhân không cư trú là thu nhập phát sinh tại Việt Nam. Ví dụ tư vấn trong trang nói về tiền lương, không tự xác định thuế suất hay cách khai từng loại tài sản đầu tư nước ngoài.

`CHƯA_BIẾT` Thuế tại nước nguồn, Việt Nam, khả năng khấu trừ hoặc hiệp định, tỷ giá thuế và hạn kê khai của một người cụ thể chưa được xác minh. Đọc [L3](L3-personal-income-tax-reporting.md), đối chiếu cơ quan thuế các nước và lưu sao kê, chứng từ khấu trừ, ngày, đơn vị và tiền tệ. Có thuế ở nước ngoài không tự chứng minh được miễn hay khấu trừ toàn bộ ở Việt Nam.

Phí chuyển đổi tiền, chênh lệch mua/bán ngoại tệ, phí giao dịch, lưu ký và thuế làm kết quả thực tế khác ví dụ không phí. Xem cả thanh khoản và thời điểm có thể chuyển tiền về, không chỉ giá niêm yết.

## Năm câu hỏi khi đọc

1. Đồng tiền định giá tài sản, đồng tiền giao dịch và đồng tiền chi tiêu là gì?
2. Tỷ giá đầu/cuối kỳ là bao nhiêu và dùng chiều VND/USD hay USD/VND?
3. Loại giao dịch, tư cách cư trú và đường chuyển tiền có được phép theo quy định hiện hành không?
4. Ai giữ tài sản, ai được cấp phép và xử lý tranh chấp ở đâu?
5. Phí, thuế, khấu trừ và chứng từ thuộc những nước nào?

## Bài tập

1. Mua 1.000 USD ở 25.000 VND/USD, quy đổi giá trị đầu kỳ sang VND.
2. Tài sản lên 1.100 USD, cuối kỳ 23.000 VND/USD: giá trị và lợi suất VND là bao nhiêu, không phí?
3. Tài sản giữ 1.000 USD, tỷ giá giảm từ 25.000 xuống 20.000: lợi suất VND?
4. Ứng dụng nhận mở tài khoản có tự chứng minh mọi giao dịch của cư dân Việt Nam hợp pháp không?
5. Thuế bị khấu trừ ở nước ngoài có tự được trừ toàn bộ ở Việt Nam không?
6. Kể ba chi phí hoặc rủi ro ngoài biến động giá tài sản.

## Đáp án

1. 25.000.000 VND.
2. 25.300.000 VND; 25.300.000/25.000.000 − 1 = 1,2%.
3. 20.000.000/25.000.000 − 1 = −20%, theo giả định.
4. Không; kiểm loại giao dịch và tư cách theo nguồn có thẩm quyền.
5. Không tự động; điều kiện và chứng từ cần xác minh.
6. Ví dụ: chênh lệch tỷ giá, phí môi giới/lưu ký, rủi ro pháp lý, thuế và thanh khoản.

## Lỗi thường gặp và ranh giới an toàn

Đảo chiều tỷ giá; cộng đơn giản hai tỷ lệ; nhầm rủi ro USD của tài sản với quyền đầu tư hợp pháp; bỏ qua thuế và nơi lưu ký. Bài không tư vấn đầu tư, thuế hoặc pháp lý cho cá nhân.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Quy định và thủ tục tiếp cận cụ thể cho từng đối tượng tại Việt Nam và thị trường nước ngoài; thuế/hiệp định và chi phí từng tài khoản. Phải kiểm lại các nguồn chính thức hiện hành trước khi hành động.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [Nghị định 135/2015, bản hợp nhất năm 2019](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2019/2/28533/26003-1-2019267-26808-vbhn-nhnn.pdf); [Chính phủ — phạm vi thu nhập cư trú](https://baochinhphu.vn/luong-nuoc-ngoai-chuyen-ve-tai-khoan-viet-nam-co-phai-nop-thue-102261015162615642.htm), 16/10/2026; [SEC — International Investing](https://www.investor.gov/introduction-investing/investing-basics/investment-products/international-investing), không ghi ngày trong phần đọc, Hoa Kỳ; [Báo điện tử Chính phủ — thuế chuyển nhượng chứng khoán](https://xaydungchinhsach.chinhphu.vn/thue-thu-nhap-ca-nhan-doi-voi-thu-nhap-tu-chuyen-nhuong-chung-khoan-119260703164200344.htm), 04/07/2026, chỉ là một nguồn Việt Nam về loại thu nhập được nêu, không xác lập quy tắc cho mọi tài sản nước ngoài. Ví dụ số hư cấu.
