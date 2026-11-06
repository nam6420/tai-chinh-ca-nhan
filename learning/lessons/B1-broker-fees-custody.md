# Bài B1 — Công ty chứng khoán, phí, thuế và lưu ký

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 10:57 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc biểu phí theo kênh và giá trị giao dịch; phân biệt phí giao dịch, thuế chuyển nhượng và phí lưu ký; lập bảng câu hỏi trước khi chọn trung gian.
- Bài trước liên quan: [B3](B3-account-security-scams.md), [V1](V1-vietnam-market-structure.md), [V2](V2-vietnam-trading-rules.md).
- Câu hỏi cốt lõi: **Một giao dịch đi qua ai, và tổng chi phí thực tế gồm những khoản nào?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/B1-fact-check.md), [phản biện](../reviews/B1-risk-review.md).

## Hiểu bài trong một phút

Công ty chứng khoán là một trung gian cung cấp tài khoản và dịch vụ nhận lệnh, không phải chính sở giao dịch. Chọn theo phí thấp nhất mà bỏ qua giấy phép, loại dịch vụ, rút tiền và hỗ trợ có thể bỏ sót chi phí hoặc rủi ro khác. Không có công ty nào được bài này khuyến nghị.

## Ôn bài cũ

- Trong [Bài B3 — Bảo mật tài khoản và lừa đảo](B3-account-security-scams.md) và [Bài N1 — Thị trường chứng khoán vận hành thế nào?](N1-market-basics.md), bạn đã biết nguyên tắc an toàn tài khoản và cơ chế khớp lệnh. Bài B1 hướng dẫn kiểm tra công ty chứng khoán, biểu phí giao dịch và lưu ký tài sản.

---

## 1. Bảng kiểm một trung gian

`SUY_LUẬN` Đọc cùng [B3](B3-account-security-scams.md): kiểm tra tên pháp nhân và giấy phép qua kênh cơ quan quản lý tự tìm; danh sách thành viên VNX có thể đối chiếu bổ sung nhưng không thay thế giấy phép. Cần kiểm dịch vụ, thị trường phục vụ, phí, điều khoản lưu ký/rút tiền, hỗ trợ, bảo mật và xung đột lợi ích.

`SỰ_THẬT` [SEC Investor.gov — Brokers](https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/brokers) gợi ý tìm hiểu đăng ký, lịch sử, dịch vụ, chi phí và cách trung gian được trả tiền. Đây là khung tham khảo Hoa Kỳ; cơ quan tra cứu và quy định Việt Nam khác.

`CHƯA_BIẾT` Địa chỉ danh sách giấy phép UBCKNN cập nhật nhất chưa được xác nhận trực tiếp trong bài; không coi danh sách thành viên VNX hoặc lời giới thiệu của người lạ là xác nhận đầy đủ. Xem giới hạn ở B3.

## 2. Phí không chỉ là một con số

`SỰ_THẬT` [PHS — Biểu phí giao dịch cơ sở](https://www.phs.vn/san-pham-dich-vu/bieu-phi-giao-dich-chung-khoan-co-so-26) ghi biểu giá áp dụng từ 30/03/2026, phân biệt giao dịch qua quầy/nhân viên và các kênh khác, với nhiều bậc giá trị giao dịch. Đây là ví dụ biểu giá một công ty tại Việt Nam, không phải mức chung và có thể thay đổi.

`KỊCH_BẢN` Một biểu phí giả định tính 0,2% giá trị mua và 0,2% giá trị bán. Mua 50 triệu đồng, sau đó bán 45 triệu đồng: phí mua `50.000.000 × 0,2% = 100.000` đồng; phí bán `45.000.000 × 0,2% = 90.000` đồng; cộng **190.000 đồng**. Đây chỉ là phí môi giới giả định, chưa gồm thuế, lưu ký, ứng tiền, chênh giá mua–bán hay dịch vụ khác.

`SỰ_THẬT` [VFS — Biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi) phân biệt một số khoản thu hộ dịch vụ và các dịch vụ khác. `CHƯA_BIẾT` Cấu phần và mức thực trả cho từng khách hàng/công ty chưa được so sánh đầy đủ; cần kiểm biểu giá và điều kiện ưu đãi hiệu lực tại thời điểm giao dịch.

## 3. Thuế và lưu ký

`SỰ_THẬT` [Cổng thông tin Chính phủ — thuế chuyển nhượng chứng khoán](https://xaydungchinhsach.chinhphu.vn/thue-thu-nhap-ca-nhan-doi-voi-thu-nhap-tu-chuyen-nhuong-chung-khoan-119260703164200344.htm), đăng 04/07/2026, trình bày Nghị định 253/2026/NĐ-CP: với phạm vi chuyển nhượng chứng khoán được nêu, thuế tính theo giá chuyển nhượng nhân 0,1%. Quy định cụ thể về cư trú, sản phẩm, miễn giảm và kê khai cần đọc văn bản hiện hành; bài này không xác định nghĩa vụ thuế cho một người.

`PHÉP_TÍNH` Nếu **giả định** giá bán 45 triệu đồng thuộc trường hợp áp dụng 0,1%, thuế minh họa `45.000.000 × 0,1% = 45.000` đồng. Cộng phí môi giới giả định ở trên, tổng hai loại chi phí `190.000 + 45.000 = 235.000` đồng. Phép tính dựa trên giá bán, không phải lãi ròng; chưa gồm chi phí khác và không phải bảng kê thuế thực tế.

Lưu ký liên quan đến việc ghi nhận và quản lý chứng khoán qua thành viên lưu ký và VSDC. Hãy phân biệt khoản trung gian thu hộ với phí dịch vụ trung gian thu thêm: giá khách hàng trả cần xem trên biểu phí, kỳ tính và điều khoản cụ thể. `CHƯA_BIẾT` Chưa đối chiếu đủ mọi biểu giá và cấu phần để nói một mức lưu ký áp dụng chung.

## Năm câu hỏi trước khi dùng dịch vụ

1. Pháp nhân, giấy phép và thị trường phục vụ đã được kiểm qua kênh nào?
2. Phí mua và bán theo kênh, bậc và chương trình nào?
3. Phí lưu ký, chuyển khoản, ứng tiền, lãi và thuế được tính ra sao?
4. Điều kiện rút tiền/chuyển chứng khoán và kênh hỗ trợ sự cố là gì?
5. Người giới thiệu nhận thù lao hay có xung đột lợi ích nào?

## Bài tập

1. Công ty chứng khoán và sở giao dịch có cùng vai trò không?
2. Mua 50 triệu, bán 45 triệu, phí giả định 0,2% mỗi chiều: tổng phí bao nhiêu?
3. Bán 45 triệu thuộc trường hợp thuế giả định 0,1%: thuế bao nhiêu?
4. Bán lỗ có tự đồng nghĩa thuế tính bằng 0 trong công thức trên không?
5. Biểu giá một công ty có đại diện mọi khách hàng và mọi thời điểm không?
6. Có tên trong danh sách thành viên VNX có loại trừ trường hợp bị mạo danh không?

## Đáp án

1. Không; trung gian nhận lệnh/dịch vụ, sở tổ chức thị trường theo quy định.
2. `100.000 + 90.000 = 190.000` đồng theo giả định.
3. `45.000.000 × 0,1% = 45.000` đồng theo giả định.
4. Không theo công thức tính trên giá bán của ví dụ; từng trường hợp cần kiểm quy định áp dụng.
5. Không; kênh, bậc, ưu đãi và ngày hiệu lực có thể khác.
6. Không; cần kiểm pháp nhân, giấy phép và kênh liên hệ tự tìm.

## Lỗi thường gặp và ranh giới an toàn

- Chỉ nhìn phí mua, quên phí bán, thuế và dịch vụ khác; coi biểu phí cũ là giá hôm nay.
- Nhầm danh sách thành viên với xác nhận toàn bộ giấy phép hoặc tin số điện thoại người lạ cung cấp.
- Bài không xếp hạng công ty, không tính thuế cá nhân hay đề xuất mua/bán/nắm giữ.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Giấy phép và giá cụ thể cho một khách hàng, cấu phần mọi mức phí lưu ký và áp dụng thuế cho tài sản nước ngoài; đọc biểu giá/hợp đồng và văn bản gốc hiệu lực cho trường hợp đó.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [PHS — biểu phí](https://www.phs.vn/san-pham-dich-vu/bieu-phi-giao-dich-chung-khoan-co-so-26), hiệu lực theo trang từ 30/03/2026; [VFS — biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi); [Cổng Chính phủ — thuế](https://xaydungchinhsach.chinhphu.vn/thue-thu-nhap-ca-nhan-doi-voi-thu-nhap-tu-chuyen-nhuong-chung-khoan-119260703164200344.htm), 04/07/2026; [SEC — Brokers](https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/brokers), Hoa Kỳ.
