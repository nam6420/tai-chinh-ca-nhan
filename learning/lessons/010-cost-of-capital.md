# Bài 010 — Chi phí vốn: mức sinh lời phải bù cho ai?

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 17:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt chi phí nợ/vốn chủ; tính WACC từ đầu vào giả định; kiểm tiền tệ, thuế và độ nhạy.
- Bài trước liên quan: N4, N7, [003](003-business-quality-moat-and-roic.md), [008](008-macro-transmission.md). Học tiếp 011.
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Cần tạo bao nhiêu lợi nhuận để bù rủi ro của người cấp vốn?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Vay tiền có lãi vay thấy được. Vốn cổ đông không có hóa đơn lãi cố định nhưng người góp vốn vẫn đòi phần bù cho thời gian và rủi ro. Chi phí vốn là một ước tính để so với hiệu quả kinh doanh và chiết khấu dòng tiền.

## Ôn bài cũ hoặc kiểm tra đầu vào

N4: tăng tỷ lệ chiết khấu thì PV của cùng khoản nhận dương đổi ra sao? Giảm. N7: xác suất tự gán có phải dữ kiện không? Không. 003: ROIC cần so với gì? Chi phí vốn có cách tính nhất quán.

## Bài này làm gì và chưa làm gì

Dạy công thức và cách kiểm giả định cho doanh nghiệp phi tài chính. Không cung cấp mức WACC hiện hành cho cổ phiếu cụ thể; không dùng bảng ngành như mức chuẩn bắt buộc.

## 1. Hai người cấp vốn, hai yêu cầu

`SỰ_THẬT` Theo khung Damodaran, mô hình CAPM ước tính chi phí vốn cổ đông `ke = Rf + beta×ERP`. Rf là lãi suất phi rủi ro thích hợp; ERP là phần bù rủi ro cổ phiếu; beta đo độ nhạy rủi ro thị trường theo mô hình. Beta không đo mọi dạng rủi ro và không phải thước đo chất lượng doanh nghiệp. [Định nghĩa](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/definitions.html).

Chi phí nợ kd là chi phí vay phù hợp hiện tại, không mặc định bằng coupon cũ. Nếu có thể dùng lợi ích thuế lãi vay, chi phí nợ sau thuế là `kd×(1−T)`; doanh nghiệp lỗ có thể chưa dùng được lợi ích này.

## 2. Trộn theo trọng số, không cộng thẳng

`KỊCH_BẢN` Một doanh nghiệp phi tài chính hư cấu dùng cùng tiền tệ danh nghĩa, số năm nhất quán: Rf3%, beta1,2, ERP5%; kd5%, thuế biên25%; vốn chủ thị trường70%, nợ thị trường30%, lợi ích thuế dùng ngay.

`PHÉP_TÍNH` `ke=3%+1,2×5%=9%`; `kd sau thuế=5%×0,75=3,75%`. WACC là chi phí vốn bình quân gia quyền: `ke×E/(D+E)+kd×(1−T)×D/(D+E)`, với E và D là giá trị thị trường. Kết quả `9%×70%+3,75%×30%=7,425%`.

ROIC sau thuế so với WACC sau thuế; dòng tiền cho toàn doanh nghiệp chiết khấu bằng WACC. Dòng tiền riêng cổ đông dùng ke, học tiếp011.

## 3. Một con số không đủ

`KỊCH_BẢN` Giữ FCFF năm tới100 và tăng trưởng dài hạn2% trong mô hình ổn định: dùng WACC7%,8%,9% cho EV lần lượt `100/0,05=2.000`, `100/0,06≈1.666,67`, `100/0,07≈1.428,57`. Đây chỉ là kiểm độ nhạy, không phải ba định giá công ty thật.

Không ghép dòng tiền VND với tỷ lệ USD; không dùng dòng tiền thực với tỷ lệ danh nghĩa. Phải kiểm ERP đã chứa rủi ro quốc gia chưa trước khi cộng thêm; không cộng trùng.

Điểm dừng: viết một giả định bạn muốn thay đổi, tính lại và giải thích vì sao kết quả đổi.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Trang Cost of Capital của Damodaran công bố dữ liệu ngành Hoa Kỳ theo mốc tháng1/2026, kèm phạm vi mẫu và liên kết dữ liệu toàn cầu. Đó là dữ liệu tham chiếu theo mẫu/thời điểm, không tự cho WACC của doanh nghiệp Việt Nam hay một doanh nghiệp riêng lẻ. [Bảng gốc](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html). Bài này không chép một tỷ lệ thị trường vào ví dụ giả định.

## Năm câu hỏi khi đọc

1. Dòng tiền thuộc mọi người cấp vốn hay riêng cổ đông?
2. Rf và dòng tiền có cùng tiền tệ/kỳ hạn phù hợp?
3. Trọng số là giá trị thị trường hay sổ sách?
4. Lợi ích thuế có thực dùng được không?
5. Độ nhạy và nguy cơ cộng trùng rủi ro ở đâu?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Tính ke với Rf3%, beta1,2 và ERP5%.
2. Tính WACC theo ví dụ70/30.
3. Không sử dụng được lá chắn thuế ngay, các đầu vào khác giữ nguyên: WACC bao nhiêu?
4. ke tăng từ9% lên11%, cấu trúc/thuế/kd như ví dụ: WACC mới?
5. Vì sao không lấy WACC ngành Mỹ làm số chính xác cho một doanh nghiệp khác?
6. ROIC10% có chắc tạo giá trị không nếu chi phí vốn chưa biết?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` 3%+1,2×5%=9%; kiểm ERP không phải lợi suất thị trường toàn bộ.
2. `PHÉP_TÍNH` 6,3%+1,125%=7,425%; trọng số cộng100%.
3. `PHÉP_TÍNH` 9%×0,7+5%×0,3=7,8%; kiểm điều kiện thuế.
4. `PHÉP_TÍNH` 11%×0,7+3,75%×0,3=8,825%.
5. Khác rủi ro, tiền tệ, cơ cấu vốn, phương pháp và ngày; cần giải thích điều chỉnh.
6. Chưa. Ghi CHƯA_BIẾT chi phí vốn, phân tích khoảng và dữ liệu cần kiểm; không tự bịa tỷ lệ.

</details>

## Lỗi thường gặp

- Gọi lợi nhuận giữ lại là vốn miễn phí.
- Cộng ke với kd thay vì dùng trọng số.
- Dùng lãi nợ cũ thay chi phí huy động phù hợp mà không giải thích.
- Lấy lợi ích thuế ngay khi chưa dùng được.
- Ghép khác tiền tệ hoặc cộng trùng rủi ro quốc gia.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Mô hình CAPM bỏ sót rủi ro nào?
- Cơ cấu vốn tương lai có khác hiện tại không?
- Khoảng WACC nào làm kết luận thay đổi?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [Damodaran — Definitions](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/definitions.html) | NYU, Hoa Kỳ; tài liệu phương pháp, ngày phiên bản CHƯA_BIẾT | CAPM, WACC, thuế |
| [Damodaran — Cost of Capital (US)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html) | Tháng1/2026; mẫu ngành Hoa Kỳ; không dùng số làm ví dụ | Phạm vi dữ liệu và giới hạn tham chiếu |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/010-fact-check.md), [phản biện](../reviews/010-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

