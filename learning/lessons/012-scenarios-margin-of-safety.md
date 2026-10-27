# Bài 012 — Kịch bản, biên an toàn và kết quả sau chi phí

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 17:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính ba kịch bản và biên an toàn; ghi xác suất giả định; đưa phí/thuế vào mô hình và viết điều kiện bác bỏ.
- Bài trước liên quan: 011,N7,N5B. Học tiếp015 hoặc nhánh013/014.
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Nếu giả định sai, khoản đệm có đủ và điều gì buộc tôi đổi kết luận?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Một khoảng giá trị chỉ hữu ích khi biết nó có thể sai ở đâu. Kịch bản giúp đổi đồng thời các giả định có liên hệ; biên an toàn là khoản đệm theo quy ước, không phải bảo hiểm. Sau đó còn phải trừ chi phí và thuế đúng trường hợp.

## Ôn bài cũ hoặc kiểm tra đầu vào

011: tăng WACC thì giá trị dòng tiền dương cố định giảm. N7: kỳ vọng không phải kết quả chắc chắn. N5: đa dạng hóa không bảo đảm tránh lỗ toàn thị trường.

## Bài này làm gì và chưa làm gì

Ví dụ đều hư cấu, cùng tiền tệ và thời điểm; không nêu mức thuế/phí hiện hành của bất kỳ nước nào. Không chỉ định quy mô vị thế cá nhân.

## 1. Ba kịch bản cùng một đối tượng

`KỊCH_BẢN` Giá trị vốn chủ trên **mỗi cổ phần** hôm nay, đơn vị nghìn đồng, đã quy về cùng ngày:

| Kịch bản | Điều kiện giả định | Giá trị | Xác suất tự gán |
|---|---|---:|---:|
| Bất lợi | Biên co, tái đầu tư kém hiệu quả |50|25%|
| Cơ sở | Biên và hiệu quả vốn giữ mức đã chuẩn hóa |80|50%|
| Thuận lợi | Sản lượng tốt, giữ được biên và hiệu quả vốn |120|25%|

`PHÉP_TÍNH` Kỳ vọng giá trị = `50×0,25+80×0,5+120×0,25=82,5`. Nếu giá minh họa60, khoản đệm so cơ sở theo quy ước `(80−60)/80=25%`. Mẫu số là giá trị ước tính, không phải giá trả. So bất lợi50, giá60 vẫn cao hơn giá trị của kịch bản đó.

Không đem EV tổng doanh nghiệp so với giá mỗi cổ phần. Xác suất giả định không được gọi là tần suất quan sát; đổi xác suất để xem kết luận bền tới đâu.

## 2. Từ lãi trên màn hình tới kết quả sau chi phí

`KỊCH_BẢN` Một giao dịch mô phỏng100 cổ phần, giá mua60.000 và giá bán65.000 đồng; không cổ tức; phí mỗi chiều0,1% giá trị giao dịch; thuế giả định bằng0,1% giá trị bán. Đây **không phải mức thuế/phí đã xác minh tại Việt Nam**.

`PHÉP_TÍNH` Giá trị mua6.000.000; phí mua6.000; giá trị bán6.500.000; phí bán6.500; thuế giả định6.500. Lãi ròng = `6.500.000−6.000.000−6.000−6.500−6.500=481.000 đồng`; lợi suất trên chi tiền ban đầu `481.000/6.006.000≈8,01%`, không phải8,33% trước chi phí.

`SỰ_THẬT` SEC giải thích phí làm giảm khoản vốn tiếp tục sinh lời. [SEC](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated). Với ví dụ thật, thêm chênh lệch mua–bán, tác động giá, lưu ký, thuế đúng căn cứ và thời điểm; không tự điền thuế từ ví dụ.

## 3. Viết điều kiện bác bỏ trước

`Ý_KIẾN` Thay “nếu giá giảm thì luận điểm sai” bằng dữ kiện cơ chế: doanh thu cốt lõi suy giảm qua những kỳ đã định; khoản phải thu/vốn lưu động vượt giả định; tái cấp vốn không còn khả thi. Ghi ngưỡng/kỳ theo doanh nghiệp, không dùng ngưỡng chung cho mọi ngành. Một cú giảm giá có thể tạo thông tin để xem lại, nhưng tự nó chưa xác nhận cơ chế kinh doanh đã sai.

Điểm dừng: tự nêu một kịch bản khiến giá trị xuống dưới giá minh họa và dữ liệu dùng để nhận diện.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Bản tin phí của SEC ngày23/07/2025 dùng các mô phỏng khác nhau về phí để cho thấy kết quả tích lũy thay đổi. Đây là tài liệu giáo dục Hoa Kỳ, không bảng thuế Việt Nam. Nguồn về đa dạng hóa còn nêu rõ không bảo đảm tránh thiệt hại khi thị trường giảm. [Giới hạn](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments).

## Năm câu hỏi khi đọc

1. Các kịch bản có cùng loại giá trị/đơn vị/ngày không?
2. Xác suất dựa trên gì và có cộng100% không?
3. Biên an toàn tính theo mẫu số nào?
4. Phí/thuế nào đã nằm trong số công bố?
5. Dữ kiện nào làm luận điểm mất hiệu lực?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Tính kỳ vọng giá trị và biên an toàn so cơ sở trong bảng.
2. Giá60 so giá trị bất lợi50: cao hơn bao nhiêu phần trăm giá trị bất lợi?
3. Tái tính lãi ròng giao dịch sau mọi khoản giả định.
4. Đổi xác suất bất lợi/cơ sở/thuận lợi thành50%/40%/10%: kỳ vọng?
5. Biên an toàn25% có bảo đảm không lỗ không?
6. Viết một điều kiện bác bỏ có dữ kiện, thời gian và nguồn cần kiểm.

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` 82,5 nghìn; (80−60)/80=25%. Kỳ vọng và cơ sở là hai mốc khác.
2. `PHÉP_TÍNH` (60−50)/50=20%; khoản đệm so cơ sở không xóa bất lợi.
3. 481.000 đồng, khoảng8,01% chi tiền ban đầu; kiểm phí cả hai chiều và căn cứ thuế.
4. `PHÉP_TÍNH` 50×0,5+80×0,4+120×0,1=69; độ chính xác phụ thuộc đầu vào.
5. Không; giá trị ước tính có thể sai sâu hơn khoản đệm, thanh khoản và thời điểm còn gây rủi ro.
6. Đáp án mở: ví dụ phải nêu chỉ tiêu cốt lõi, kỳ kiểm và hồ sơ gốc; không tự đặt ngưỡng rồi gọi là chuẩn ngành.

</details>

## Lỗi thường gặp

- Nhầm giá trị kỳ vọng với giá chắc chắn nhận.
- Đổi mẫu số biên an toàn giữa các phép so.
- Gắn xác suất chính xác giả tạo.
- Chép thuế giả định thành luật hiện hành.
- Gọi mọi giảm giá là thất bại kinh doanh.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Kịch bản nào chưa đưa vào, như mất khả năng hoạt động?
- Các giả định có liên hệ khiến kịch bản quá lạc quan không?
- Nguồn thuế/phí/thanh khoản nào chưa xác minh?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [SEC — Fees and Expenses](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated) | 23/07/2025; Hoa Kỳ; ví dụ giáo dục | Chi phí và kết quả tích lũy |
| [Investor.gov — Diversify](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT | Phản chứng đối với bảo đảm an toàn |
| [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) | NYU; tài liệu phương pháp, ngày phiên bản CHƯA_BIẾT | Giá trị phụ thuộc giả định |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/012-fact-check.md), [phản biện](../reviews/012-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

