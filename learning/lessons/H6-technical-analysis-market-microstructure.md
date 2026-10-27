# Bài H6 — Phân tích kỹ thuật và vi cấu trúc thị trường

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:41 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt mô tả giá với dự báo có chứng cứ; tính spread và nêu giới hạn của các loại lệnh.
- Bài trước liên quan: [V2](V2-vietnam-trading-rules.md), [H5](H5-statistics-backtest-overfitting.md), [N8](N8-finding-verifying-sources.md).
- Câu hỏi cốt lõi: Một mẫu giá có thông tin hữu ích hay chỉ là kết quả của lựa chọn mẫu và chi phí bị bỏ qua?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/H6-fact-check.md), [phản biện](../reviews/H6-risk-review.md).

## Hiểu bài trong một phút

Phân tích kỹ thuật dùng quy tắc hoặc hình mẫu của giá và khối lượng để mô tả dữ liệu hoặc đặt giả thuyết. Một đường vẽ hấp dẫn không tự cho biết xác suất tăng giá hoặc lợi nhuận sau phí. Vi cấu trúc giúp xem lệnh, sổ giá và thanh khoản ảnh hưởng giá thực hiện ra sao.

## 1. Bằng chứng có giới hạn và phản chứng

`SỰ_THẬT` [Lo, Mamaysky & Wang — Foundations of Technical Analysis](https://www.nber.org/papers/w7613), NBER 2000, dùng phương pháp nhận dạng mẫu trên dữ liệu cổ phiếu Hoa Kỳ giai đoạn lịch sử của nghiên cứu và tìm thấy một số mẫu có thông tin bổ sung. Kết luận đó không bảo đảm giao dịch có lãi sau phí hoặc lặp lại tại Việt Nam hiện nay.

`SỰ_THẬT` [Sullivan, Timmermann & White](https://eprints.lse.ac.uk/119144/1/dp303.pdf), bản nghiên cứu 1998, xét vấn đề thử nhiều quy tắc và nguy cơ chọn kết quả tốt do tình cờ. `SUY_LUẬN` Hai hướng nghiên cứu có thể cùng hữu ích: một mẫu có thông tin trong một nghiên cứu vẫn cần kiểm lại lựa chọn mẫu, dữ liệu ngoài mẫu, chi phí và điều kiện thị trường khác. Không coi một bài nghiên cứu cũ là bằng chứng cho mọi chỉ báo.

## 2. Spread và giá khớp

`KỊCH_BẢN` Giá mua tốt nhất (*bid*) 100 đồng/cổ phần, giá bán tốt nhất (*ask*) 102 đồng/cổ phần, cùng thời điểm; bỏ phí và giả định khối lượng đủ để khớp một cổ phần. `PHÉP_TÍNH` Spread tuyệt đối = 102 − 100 = 2 đồng; giá giữa = (100 + 102)/2 = 101 đồng; spread/giá giữa = 2/101 ≈ 1,98%. Nếu mua ở 102 rồi bán ngay ở 100, chênh lệch là 2 đồng/cổ phần, khoảng 1,96% giá mua, trước các phí khác.

[SEC — Ask Price](https://www.investor.gov/introduction-investing/investing-basics/glossary/ask-price) giải thích giá chào bán; sổ lệnh thay đổi và có thể không đủ khối lượng ở mức giá hiển thị. Một spread không đo hết chiều sâu và rủi ro thanh khoản.

## 3. Loại lệnh và ranh giới

Lệnh giới hạn đặt điều kiện giá nhưng có thể không khớp; lệnh thị trường ưu tiên thực hiện theo điều kiện thị trường nhưng giá có thể thay đổi hoặc trải nhiều mức. Tên, thời gian và điều kiện lệnh tại Việt Nam cần xem [V2](V2-vietnam-trading-rules.md) và quy định hiện hành, không áp máy móc quy tắc Hoa Kỳ.

`Ý_KIẾN` Khi đọc một tuyên bố về chỉ báo, hỏi: quy tắc được định nghĩa trước hay sau khi xem dữ liệu; đã thử bao nhiêu biến thể; có doanh nghiệp hủy niêm yết; có kiểm ngoài mẫu và trừ phí, spread, trượt giá; điều gì làm giả thuyết sai? Tránh các lời hứa chắc thắng, biểu đồ chọn lọc và đòn bẩy không hiểu rõ.

## Năm câu hỏi khi đọc

1. Mẫu giá có định nghĩa và kỳ dữ liệu rõ không?
2. Nghiên cứu nào, thị trường và thời gian nào hỗ trợ hay phản bác?
3. Có kiểm việc chọn nhiều chỉ báo và dữ liệu ngoài mẫu không?
4. Spread, độ sâu sổ lệnh và chi phí ảnh hưởng giá thực hiện thế nào?
5. Loại lệnh có thể không khớp hoặc khớp ở giá khác mong đợi không?

## Bài tập

1. Bid 100, ask 102: spread tuyệt đối là bao nhiêu?
2. Giá giữa của hai mức đó? Spread chia giá giữa?
3. Mua 102, bán 100, bỏ phí: chênh lệch trên giá mua?
4. Một mẫu có thông tin trong nghiên cứu cũ có bảo đảm lợi nhuận hiện nay không?
5. Lệnh giới hạn có bảo đảm được khớp không?
6. Nêu hai sai sót cần tránh trong backtest chỉ báo.

## Đáp án

1. 2 đồng/cổ phần.
2. 101 đồng; 2/101 ≈ 1,98%.
3. Mất 2/102 ≈ 1,96% trước phí.
4. Không; cần xem thị trường, mẫu, phương pháp, chi phí và kiểm định mới.
5. Không; giá và thanh khoản có thể không đáp ứng điều kiện.
6. Ví dụ: thử nhiều biến thể rồi chỉ báo kết quả tốt; dùng thông tin tương lai; bỏ phí và khả năng khớp.

## Lỗi thường gặp và ranh giới an toàn

Nhầm mô tả với nguyên nhân, mẫu lịch sử với dự báo chắc chắn, và giá hiển thị với giá khớp toàn bộ. Bài không đề xuất chỉ báo, lệnh hay chiến lược cho cá nhân.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Hiệu quả ngoài mẫu và sau chi phí của từng quy tắc; thanh khoản thực và quy tắc lệnh mới nhất của từng thị trường.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [Lo, Mamaysky & Wang — NBER 7613](https://www.nber.org/papers/w7613), 2000; [Sullivan, Timmermann & White](https://eprints.lse.ac.uk/119144/1/dp303.pdf), 1998; [SEC — Ask Price](https://www.investor.gov/introduction-investing/investing-basics/glossary/ask-price), không ghi ngày, Hoa Kỳ. Số ví dụ hư cấu.
