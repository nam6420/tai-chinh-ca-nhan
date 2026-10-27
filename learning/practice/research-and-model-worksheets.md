# Bảng thực hành và mô hình nghiên cứu

- Ngày: `2026-10-26`.
- Chốt dữ liệu lúc: `2026-10-26 17:08 UTC+7 (Asia/Ho_Chi_Minh)`.
- Trạng thái: Mẫu học tập và ví dụ hư cấu; không phải báo cáo doanh nghiệp hay khuyến nghị.
- Các ngưỡng/giả định là quy ước bài tập, không phải chuẩn ngành hoặc mức thuế/phí hiện hành.

## 1. Phiếu theo dõi ba phiên đầu

Ghi mục tiêu và nền tảng trước khi học; chỉ dùng để hiệu chỉnh cho người học tham gia, không đại diện mọi người.

| Phiên/bài | Điều đã biết trước | Phút thực tế | Câu tự làm được | Lỗi/câu chưa hiểu | Việc ôn tiếp |
|---|---|---|---|---|---|
| 1 | Chưa ghi | Chưa ghi | Chưa ghi | Chưa ghi | Chưa ghi |
| 2 | Chưa ghi | Chưa ghi | Chưa ghi | Chưa ghi | Chưa ghi |
| 3 | Chưa ghi | Chưa ghi | Chưa ghi | Chưa ghi | Chưa ghi |

## 2. Bảng nguồn và chuyển đổi cho bài tổng kết

| Câu hỏi | Pháp nhân/thị trường | Tài liệu gốc, vị trí/URL | Ngày công bố/kỳ | Đơn vị, tiền tệ, chuẩn | Riêng/hợp nhất, bản sửa | Ngày truy cập |
|---|---|---|---|---|---|---|
| Điền câu hỏi hẹp | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT |

| Chỉ tiêu | Số gốc nguyên đơn vị | Nguồn/bảng | Công thức chuyển đổi | Số đã chuyển | Ý nghĩa và giới hạn |
|---|---|---|---|---|---|
| Chưa chọn | CHƯA_BIẾT | CHƯA_BIẾT | Chưa tính | CHƯA_BIẾT | Chưa kết luận |

Không ghi số thiếu thành0. Hai trang chép cùng thông cáo không được tính thành hai nguồn độc lập. Xem [N8](../lessons/N8-finding-verifying-sources.md) và [mẫu sổ nguồn](../../templates/source-register.md).

## 3. Bảng nợ và thanh khoản 12 tháng

`KỊCH_BẢN` Doanh nghiệp phi tài chính hư cấu; tỷ đồng; CFO dự kiến đã sau lãi/thuế; chi mua tài sản và trả gốc nợ được trình bày riêng. Không coi hạn mức chưa rút là tiền chắc có nếu chưa đọc điều kiện.

| Dòng | Đầu vào hư cấu | Cách kiểm với công ty thật |
|---|---:|---|
| Tiền đầu kỳ có thể sử dụng |30|Loại phần bị hạn chế nếu không phục vụ nghĩa vụ đang xét|
| CFO dự kiến 12 tháng |45|Giả định doanh thu, biên, vốn lưu động và phân loại lãi|
| Chi đầu tư trả tiền |20|Không trùng khoản đã nằm trong CFO|
| Gốc nợ đến hạn |60|Lịch đáo hạn và nghĩa vụ thuê phù hợp|
| Mức dự phòng tiền cuối kỳ giả định |10|Quy ước mô hình, chưa là chuẩn ngành|

`PHÉP_TÍNH` Tiền trước huy động mới = `30+45−20−60=−5`. Muốn còn10 thì thiếu `10−(−5)=15`. Không kết luận có thể vay thêm15: phải kiểm điều khoản, hạn mức, tài sản bảo đảm và sức chịu đựng của bên cho vay.

| Kỳ đến hạn | Gốc phải trả | Nguồn tiền chắc chắn/điều kiện | Dữ liệu chưa biết | Tình huống bất lợi |
|---|---|---|---|---|
| Điền từng kỳ | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT | Chưa mô phỏng |

## 4. Mô hình DCF nhỏ để tự dựng lại

`KỊCH_BẢN` Dùng lại bài011: tỷ đồng danh nghĩa, cuối năm; FCFF1=100,FCFF2=110,g2%,WACC10%,nợ ròng200,100 triệu cổ phần. Đầu vào giả định, không gắn cho Apple hay cổ phiếu thật.

| Ô khái niệm | Đầu vào/công thức | Kết quả kiểm |
|---|---|---:|
| FCFF3 |110×1,02|112,2|
| TV tại cuối năm2 |112,2/(0,10−0,02)|1.402,5|
| EV hôm nay |100/1,1+(110+1.402,5)/1,1²|1.340,9091|
| Vốn chủ |EV−200|1.140,9091|
| Đồng/cổ phần |Vốn chủ tỷ đồng /100 triệu cổ phần|11.409,09|

Tự thay WACC hoặc g một biến mỗi lần, ghi lý do, tính lại và diễn giải. Chỉ dùng công thức khi WACC>g và giả định tăng trưởng/tái đầu tư nhất quán. Mô hình cho mọi người cấp vốn phải ghép FCFF với WACC. [Cách tiếp cận Damodaran](https://pages.stern.nyu.edu/adamodar/New_Home_Page/lectures/approach.html), [bài011](../lessons/011-dcf-reverse-dcf.md).

## 5. Bảng kịch bản và điều kiện bác bỏ

| Thành phần | Bất lợi | Cơ sở | Thuận lợi | Nguồn hoặc nhãn giả định |
|---|---|---|---|---|
| Động lực doanh thu | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT | Chưa thu thập |
| Biên và tái đầu tư | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT | Chưa thu thập |
| Dòng tiền/tỷ lệ | CHƯA_BIẾT | CHƯA_BIẾT | CHƯA_BIẾT | Chưa thu thập |
| Loại giá trị, ngày, đơn vị | Chưa tính | Chưa tính | Chưa tính | Phải cùng cơ sở |
| Xác suất nếu dùng | Chưa gán | Chưa gán | Chưa gán | Tổng100%, ghi cơ sở và thử độ nhạy |
| Bằng chứng bác bỏ | Chưa ghi | Chưa ghi | Chưa ghi | Nêu chỉ tiêu, kỳ kiểm, nguồn |

Không dùng bảng trống để tuyên bố đã phân tích đủ ba kịch bản. Đọc [012](../lessons/012-scenarios-margin-of-safety.md).

## 6. Hai bài ôn tích lũy

`Ý_KIẾN` Dùng khối1 sau005, khối2 sau009. Đây là ôn tự chọn để phát hiện chỗ hổng, không là điều kiện mở khóa016; khi chưa tự giải được, quay lại bài liên quan trước khi dùng kiến thức đó trong bài tổng kết.

### Khối 1 — Từ sổ sách tới tiền và nợ

Đầu vào hư cấu, tỷ đồng, cùng năm: lợi nhuận80,khấu hao10,phải thu tăng20,tồn kho tăng10,phải trả người bán tăng5; không khoản điều chỉnh khác; phân loại lãi/thuế đã khớp trong CFO. Chi đầu tư15. Tiền đầu năm10, gốc nợ phải trả90, không nguồn huy động mới; không cổ tức.

1. Dựng CFO giản lược và CFO trừ chi đầu tư.
2. Sau trả gốc, tiền cuối kỳ âm hay dương? Cần kiểm gì tiếp?
3. Lợi nhuận dương có đủ kết luận không thiếu tiền không?

<details>
<summary>Đáp án khối1</summary>

1. `PHÉP_TÍNH` CFO=`80+10−20−10+5=65`; CFO−capex=`65−15=50`, chưa gọi là FCFF chuẩn hóa.
2. `PHÉP_TÍNH` Tiền cuối=`10+65−15−90=−30`; mô hình thiếu30 trước mức dự phòng. Kiểm điều kiện tái cấp vốn, tiền bị hạn chế và khả năng điều chỉnh dòng tiền, không tự giả định vay được.
3. Không. Cần kỳ thu/chi, đầu tư và nghĩa vụ gốc. Kiểm năng lực giải thích, không chỉ đáp số.

</details>

### Khối 2 — Quản trị, kế toán và định giá

Đầu vào hư cấu: doanh nghiệp A tăng EPS vì số cổ phần giảm nhưng lợi nhuận không tăng; B lãi tăng nhờ giá đầu vào giảm tạm thời; C có P/E thấp hơn nhóm nhưng dùng lợi nhuận đỉnh chu kỳ.

1. EPS tăng của A tự chứng minh hoạt động tốt hơn không? Cần kiểm gì khi mua lại?
2. Dữ kiện của B có đủ chứng minh lợi thế định giá không? Nêu phản chứng cần tìm.
3. Có thể gọi C rẻ chỉ từ P/E không? Sửa cách so sánh thế nào?

<details>
<summary>Đáp án khối2</summary>

1. Không. Kiểm giá mua lại, nguồn tài trợ, lợi nhuận thực, cổ phần pha loãng và nhu cầu đầu tư; EPS là tỷ số có mẫu số đổi.
2. Không. Kiểm giá bán/giữ khách so đối thủ và tình huống đầu vào tăng lại; chi phí giảm chung không tự là sức mạnh định giá.
3. Chưa. Chuẩn hóa lợi nhuận qua chu kỳ, kiểm nhóm cùng mô hình/phạm vi/chu kỳ, cơ cấu vốn và dữ kiện thiếu. Không suy một bội số thành quyết định đầu tư.

</details>

## 7. Bảng kiểm 20 câu trước kết luận

Đánh dấu ĐÃ_CÓ/CHƯA_BIẾT kèm địa chỉ bằng chứng; không cộng số câu thành điểm mua/bán.

1. Đúng pháp nhân/thị trường?
2. Đúng kỳ và ngày công bố?
3. Đúng tiền tệ/đơn vị?
4. Đúng riêng/hợp nhất và chuẩn?
5. Đã kiểm bản sửa?
6. Khách hàng trả tiền cho điều gì?
7. Doanh thu tăng do giá/lượng/cơ cấu nào?
8. Chi phí/hiệu quả đơn vị có hiểu được?
9. Dòng tiền khác lợi nhuận ở đâu?
10. Vốn lưu động đang hút hay tạo tiền?
11. Đầu tư duy trì/mở rộng phân biệt được tới đâu?
12. Nợ đến hạn và tiền có sử dụng được đã khớp?
13. Điều kiện vay/tái cấp vốn là gì?
14. Pha loãng và quyền lợi không thuộc cổ đông phổ thông đã xét?
15. Chọn đúng nhóm so sánh và pha chu kỳ?
16. Dòng tiền/tỷ lệ chiết khấu có khớp?
17. Phí/thuế/thanh khoản được nêu rõ?
18. Ba kịch bản và độ nhạy có tái lập?
19. Phản chứng mạnh nhất và điều chưa biết là gì?
20. Điều kiện bác bỏ, nguồn và mốc xem lại đã ghi?

## 8. Bảng kiểm quản trị 12 điểm

Đây là câu hỏi đọc, không phải thang điểm đã kiểm định:

1. Ai kiểm soát quyền biểu quyết?
2. Ai phê duyệt giao dịch quan trọng?
3. Đãi ngộ gắn chỉ tiêu nào, có khuyến khích làm đẹp ngắn hạn không?
4. Quyền lợi cổ đông thiểu số được công bố ra sao?
5. Giao dịch bên liên quan có mục đích/điều kiện rõ không?
6. Lịch sử huy động vốn có đi cùng kết quả sử dụng vốn không?
7. Mua lại có đi cùng pha loãng từ trả công cổ phiếu không?
8. Cổ tức/mua lại có lấn nhu cầu tiền bắt buộc không?
9. Mua bán doanh nghiệp có kiểm kết quả sau thương vụ không?
10. Ban điều hành giải thích sai dự báo và thay đổi chính sách thế nào?
11. Kiểm toán/kiểm soát có lưu ý trọng yếu gì?
12. Khi bằng chứng xung đột, có nguồn độc lập và ý kiến bất đồng được giữ không?

## 9. Phiếu tự học tài chính cá nhân và an toàn

Các phiếu trống dưới đây dùng cùng [P1](../lessons/P1-budget-emergency-fund-insurance.md), [P2](../lessons/P2-personal-debt.md), [P3](../lessons/P3-goals-risk-ips.md) và [B3](../lessons/B3-account-security-scams.md); các bài đang kiểm duyệt lại. Không ghi thông tin nhạy cảm vào kho dùng chung.

| Câu hỏi | Người học tự điền |
|---|---|
| Thu nhập thực nhận và chi thiết yếu theo tháng | Chưa ghi |
| Số tháng quỹ tự chọn và tiền dự phòng đã có | Chưa ghi |
| Nợ, ngày đến hạn, lãi và phí cần đối chiếu hợp đồng | Chưa ghi |
| Mục tiêu, số tiền, thời hạn và điều chưa chắc chắn | Chưa ghi |
| Kênh chính thức tự tìm để xác minh và báo sự cố | Chưa ghi |

Quỹ dự kiến = số tháng tự chọn × chi thiết yếu hằng tháng. Đây là phiếu tự tính, không đề xuất mức quỹ, sản phẩm hay hành động mua/bán.

## Nguồn và giới hạn

Các bảng là `Ý_KIẾN` về thiết kế học tập và `KỊCH_BẢN` hư cấu, được tổng hợp từ bài004–016/N8. Khung DCF mở lại từ nguồn NYU nêu ở mục4 trong lượt26/10/2026. Các dữ kiện công ty thật phải dùng nguồn gốc tại thời điểm thực hành; bảng này không điền hộ số công ty. Mẫu vĩ mô riêng tại [đây](../../data/processed/macro-observation-template.md). Chưa có dữ liệu chứng minh bảng kiểm giúp tăng lợi nhuận.
