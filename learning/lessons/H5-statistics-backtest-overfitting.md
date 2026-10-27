# Bài H5 — Tương quan, nhân quả và kiểm định quá khứ

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt tương quan với nhân quả và lập danh sách rủi ro khi kiểm định chiến lược bằng dữ liệu quá khứ.
- Bài trước liên quan: [N7](N7-data-probability-uncertainty.md), [A4](A4-allocation-correlation-rebalancing.md), [H3](H3-risk-volatility-drawdown-liquidity.md).
- Câu hỏi cốt lõi: Kết quả đẹp trong dữ liệu cũ có còn đứng vững khi kiểm trên dữ liệu mới và sau chi phí?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/H5-fact-check.md), [phản biện](../reviews/H5-risk-review.md).

## Hiểu bài trong một phút

Hai đường cùng đi lên không tự chứng minh một đường gây ra đường kia. Một chiến lược được chọn sau hàng trăm lần thử có thể trông rất tốt chỉ vì may mắn. Phải ghi toàn bộ cách chọn và giữ dữ liệu chưa dùng để kiểm tra, đồng thời tính chi phí có thể phát sinh.

## 1. Tương quan không tự chứng minh nhân quả

`SỰ_THẬT` [NIST — thiết kế thí nghiệm](https://itl.nist.gov/div898/handbook/ppc/section1/ppc136.htm) phân biệt quan hệ quan sát với việc xác định tác động nhân quả qua thiết kế kiểm soát. `KỊCH_BẢN` Cả doanh thu ngành và giá cổ phiếu tăng cùng lúc; yếu tố thứ ba như nhu cầu chung hoặc thay đổi kỳ vọng có thể ảnh hưởng cả hai. Cần kiểm giả thuyết, thời điểm, biến gây nhiễu và bằng chứng khác; không suy nguyên nhân từ một biểu đồ.

## 2. Thử nhiều quy tắc

`KỊCH_BẢN` Giả sử thử 100 quy tắc độc lập, tất cả không có tác dụng thật, và mỗi kiểm định có xác suất báo dương giả 5%. `PHÉP_TÍNH` Số dương giả kỳ vọng = 100 × 5% = 5; xác suất có ít nhất một dương giả = `1 − 0,95^100 ≈ 99,4%`. Hai kết quả khác nhau: một là số kỳ vọng, một là xác suất có ít nhất một.

Thực tế các quy tắc thường phụ thuộc lẫn nhau; công thức xác suất trên không áp dụng nguyên xi khi không độc lập. Thống kê đáng chú ý cũng chưa là bằng chứng có thể giao dịch có lãi sau phí.

## 3. Kiểm định quá khứ và khớp quá mức

Kiểm định quá khứ (*backtest*) áp quy tắc lên dữ liệu lịch sử. *Overfitting* là chọn hoặc điều chỉnh quá sát dữ liệu đã thấy đến mức quy tắc thất bại khi gặp dữ liệu khác. [Sullivan, Timmermann và White — Data-Snooping, Technical Trading Rule Performance and the Bootstrap](https://eprints.lse.ac.uk/119144/1/dp303.pdf), bản nghiên cứu 1998, kiểm nhiều quy tắc và cho thấy kiểm định có xét việc tìm kiếm có thể khác kết luận từ quy tắc chọn sẵn. Bối cảnh lịch sử Hoa Kỳ trong nghiên cứu không chứng minh hiệu quả hay vô hiệu của mọi phương pháp ở Việt Nam hiện nay.

`Ý_KIẾN` Quy trình tối thiểu để học: (1) ghi rõ giả thuyết và tất cả quy tắc đã thử; (2) chia dữ liệu theo thời gian cho phát triển và kiểm tra; (3) tránh dùng thông tin chưa có tại thời điểm quyết định; (4) tính cả cổ tức, hủy niêm yết, phí, spread, khối lượng và khả năng khớp; (5) kiểm trên giai đoạn và điều kiện khác. Nếu xem đi xem lại phần kiểm tra rồi chỉnh quy tắc theo đó, phần này không còn là kiểm tra độc lập đúng nghĩa.

`CHƯA_BIẾT` Dữ liệu point-in-time, khả năng khớp và chi phí thực của một chiến lược cụ thể; một bài tập trên giá đóng cửa không xác nhận lợi nhuận có thể đạt được.

## Năm câu hỏi khi đọc

1. Ai chọn giả thuyết, khi nào, và đã thử tổng cộng bao nhiêu cách?
2. Có biến gây nhiễu, đảo chiều nhân quả hay lựa chọn mẫu không?
3. Dữ liệu có sẵn thực sự tại thời điểm mô phỏng không?
4. Có bỏ doanh nghiệp hủy niêm yết, cổ tức, phí và thanh khoản không?
5. Kết quả còn giữ được ngoài mẫu và sau chi phí không?

## Bài tập

1. Hai biến tăng cùng lúc có chứng minh một biến gây biến kia không?
2. Giả định 100 kiểm định độc lập, dương giả 5% mỗi kiểm định: số dương giả kỳ vọng?
3. Cùng giả định, xác suất không có dương giả là công thức gì?
4. Vì sao không nên áp công thức độc lập cho các quy tắc phụ thuộc?
5. Tại sao dùng giá đóng cửa chưa bảo đảm thực tế mua bán được giá đó?
6. Phần kiểm tra bị dùng nhiều lần để chỉnh quy tắc còn là dữ liệu hoàn toàn độc lập không?

## Đáp án

1. Không; cần thiết kế và bằng chứng bổ sung về nhân quả.
2. 100 × 0,05 = 5.
3. `0,95^100`; xác suất có ít nhất một là `1 − 0,95^100`.
4. Vì sự phụ thuộc thay đổi xác suất chung; cần phương pháp phù hợp.
5. Cần xem thời điểm đặt lệnh, thanh khoản, spread và phí.
6. Không còn độc lập theo cách sử dụng ban đầu; cần dữ liệu kiểm tra mới.

## Lỗi thường gặp và ranh giới an toàn

Chọn một mẫu chiến thắng rồi giấu số lần thử; dùng dữ liệu tương lai; bỏ chi phí hoặc doanh nghiệp biến mất; gọi tương quan là nhân quả. Bài không cung cấp chiến lược giao dịch.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Kết quả ngoài mẫu, dữ liệu sẵn có lúc quyết định và chi phí giao dịch của một quy tắc cụ thể.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [NIST — thiết kế thí nghiệm](https://itl.nist.gov/div898/handbook/ppc/section1/ppc136.htm), không ghi ngày trong phần đọc; [Sullivan, Timmermann & White — Data-Snooping](https://eprints.lse.ac.uk/119144/1/dp303.pdf), bản 1998. Ví dụ kiểm định hư cấu.
