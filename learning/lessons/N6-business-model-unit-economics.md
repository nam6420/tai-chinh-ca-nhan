# Bài N6 — Doanh nghiệp kiếm tiền thế nào?

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 16:54 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Vẽ chuỗi khách hàng–sản phẩm–thu tiền; tính phần đóng góp và hòa vốn; phân biệt lợi nhuận với tiền.
- Bài trước liên quan: [N1](N1-market-basics.md); học tiếp [001](001-business-financial-statements.md).
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Bán thêm một sản phẩm có thực sự giúp doanh nghiệp khá hơn?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Quán đông khách chưa chắc có lãi. Cần biết mỗi đơn bán được còn bao nhiêu sau chi phí đi cùng đơn đó, rồi phần còn lại có đủ trả tiền thuê và nhân viên hay không. Kế tiếp phải hỏi khách đã trả tiền chưa.

## Ôn bài cũ hoặc kiểm tra đầu vào

Ai nhận tiền khi mua cổ phần cũ? Đáp án: người bán trước phí. Doanh thu bán cà phê khác tiền huy động từ cổ đông: doanh thu đến từ khách, vốn góp đến từ chủ sở hữu.

## Bài này làm gì và chưa làm gì

Dạy một mô hình đơn sản phẩm có giả định rõ. Chưa dạy lập báo cáo kế toán hay định giá; không coi công thức hòa vốn là mô hình cho mọi ngành.

## 1. Sáu câu để hiểu một mô hình kinh doanh

`Ý_KIẾN` Viết sáu dòng: khách là ai; họ cần giải quyết việc gì; sản phẩm là gì; thu tiền theo đơn/thuê bao/dự án ra sao; những chi phí nào đổi theo lượng bán; những khoản nào vẫn phải trả khi ít khách. Ghi thêm thời điểm thu tiền và trả nhà cung cấp. Nếu chưa trả lời được, khoan đặt tỷ số lên doanh nghiệp.

## 2. Mỗi ly còn lại bao nhiêu?

`KỊCH_BẢN` Quán Sao Biển bán một loại ly giá 50.000 đồng; biến phí 30.000 đồng/ly; định phí tháng 120 triệu đồng. Giả định giá/biến phí ổn định, chưa tính thuế, lãi vay hay đầu tư máy móc; định phí giữ nguyên trong phạm vi công suất đang xét.

`PHÉP_TÍNH` Phần đóng góp mỗi ly = `50.000 − 30.000 = 20.000 đồng`. Đây là phần để bù định phí, chưa phải lãi ròng mỗi ly. Hòa vốn lượng = `120.000.000/20.000 = 6.000 ly/tháng`; doanh thu hòa vốn = `6.000 × 50.000 = 300 triệu đồng`. Bán 7.000 ly cho kết quả giản lược `7.000 × 20.000 − 120 triệu = 20 triệu đồng`.

`SỰ_THẬT` Công thức đơn sản phẩm được SBA trình bày trong hướng dẫn hòa vốn. [SBA](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point). Nếu phần đóng góp không dương thì không có điểm hòa vốn hữu hạn trong mô hình này với định phí dương.

## 3. Đông khách hơn nhưng chưa chắc có tiền hơn

`KỊCH_BẢN` Quán nhận đơn công ty, ghi doanh thu tháng này nhưng khách trả tháng sau; nguyên liệu và lương phải trả ngay. Lợi nhuận tính theo đơn có thể dương trong khi tiền hiện tại thiếu. Nếu mở thêm cửa hàng, định phí có thể nhảy bậc; không dùng nguyên 120 triệu cho mọi quy mô.

Điểm dừng: tự diễn giải vì sao giảm giá 10% có thể làm phần đóng góp giảm mạnh hơn 10%, rồi học 001 để hiểu doanh thu/lợi nhuận/tiền.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Starbucks phân biệt cửa hàng tự vận hành với cửa hàng cấp phép trong Form 10-K FY2025, kỳ kết thúc 28/09/2025, Hoa Kỳ, US GAAP, các bảng tài chính tính bằng triệu USD. Hai cách kiếm doanh thu cần đọc riêng; không chia tổng doanh thu cho tổng số cửa hàng rồi gọi đó là doanh thu của một cửa hàng tự vận hành. [Starbucks 10-K](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm).

## Năm câu hỏi khi đọc

1. Khách trả tiền cho giá trị nào?
2. Đơn vị bán hàng thích hợp là ly, thuê bao hay dự án?
3. Chi phí nào tăng theo lượng?
4. Hòa vốn đang tính lợi nhuận hay tiền?
5. Công suất và cơ cấu sản phẩm có đổi không?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Tính phần đóng góp nếu giá 50.000, biến phí 30.000 đồng.
2. Định phí 120 triệu; cần bán bao nhiêu ly để hòa vốn?
3. Vẫn bán 7.000 ly nhưng giảm giá còn 45.000; kết quả giản lược là bao nhiêu?
4. Biến phí tăng lên 35.000, giá vẫn 50.000: hòa vốn mới?
5. Có lãi 20 triệu nhưng khách còn nợ 50 triệu: đủ biết tiền cuối tháng không?
6. Hai sản phẩm phần đóng góp khác nhau: vì sao chưa thể lấy tổng số ly áp một mức hòa vốn?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` 20.000 đồng/ly; kiểm phân biệt đóng góp với lãi ròng.
2. `PHÉP_TÍNH` 120 triệu/20.000 = 6.000 ly; đầu vào phải cùng đơn vị.
3. `PHÉP_TÍNH` 7.000 × (45.000−30.000) − 120 triệu = −15 triệu; giảm giá có thể đổi dấu lợi nhuận.
4. `PHÉP_TÍNH` 120 triệu/15.000 = 8.000 ly; kiểm độ nhạy chi phí.
5. Chưa: cần tiền đầu kỳ, thực thu/thực chi, nợ và đầu tư; nối 001.
6. Cần cơ cấu bán và phần đóng góp bình quân theo cơ cấu đó; cơ cấu thay đổi thì hòa vốn thay đổi.

</details>

## Lỗi thường gặp

- Gọi phần đóng góp là lãi ròng.
- Bỏ định phí hoặc chi phí nhảy bậc.
- Trộn đồng với triệu đồng.
- Coi doanh thu là tiền đã thu.
- Dùng một công thức đơn sản phẩm cho mọi doanh nghiệp.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Khoản chi hỗn hợp nào chưa tách được?
- Khách trả tiền trước hay sau khi doanh nghiệp trả chi phí?
- Phải thay mô hình thế nào khi vượt công suất?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [SBA — Break-even point](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT; một sản phẩm/dịch vụ | Công thức và giới hạn hòa vốn |
| [Starbucks FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm) | FY kết thúc 28/09/2025; nộp 14/11/2025; US GAAP; triệu USD | Ví dụ mô hình tự vận hành/cấp phép |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/N6-fact-check.md), [phản biện](../reviews/N6-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

