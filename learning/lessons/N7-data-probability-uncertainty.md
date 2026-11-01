# Bài N7 — Đọc dữ liệu và bất định

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 16:54 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt phần trăm/điểm phần trăm, trung bình/trung vị; tính kỳ vọng đơn giản; tránh trộn kỳ và dùng dữ liệu tương lai.
- Bài trước liên quan: [N4](N4-time-value-returns.md); không yêu cầu kế toán ở nhánh quỹ. Học tiếp N5B và 010.
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Con số này nói được gì, và điều gì nó chưa chứng minh?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Một nhóm người có thu nhập trung bình cao có thể chỉ vì một người rất giàu. Một xác suất viết đến hai chữ số thập phân có thể vẫn chỉ là phỏng đoán. Học số liệu là học cả giới hạn của kết luận.

## Ôn bài cũ hoặc kiểm tra đầu vào

N4: khoản đầu 100, góp thêm 50 ngay cuối kỳ, tài khoản cuối160 thì lãi bao nhiêu? Đáp án10, không phải60. Trước khi tính phải phân biệt dòng tiền với lợi nhuận.

## Bài này làm gì và chưa làm gì

Dạy kiểm đơn vị, kỳ và bất định bằng bảng số nhỏ tự đủ đầu vào. Không dạy thống kê suy luận đầy đủ hay biến xác suất tự gán thành dự báo.

## 1. So cái gì với cái gì?

`PHÉP_TÍNH` Biên lợi nhuận tăng từ10% lên12% là **2 điểm phần trăm**; tăng tương đối `(12−10)/10=20%`. Mức tăng doanh thu20% không cùng nghĩa với biên lợi nhuận20%. Số danh nghĩa và sức mua thực khác nhau như N4.

Mỗi số cần tên, quốc gia, kỳ, mẫu số, đơn vị và ngày công bố. Tăng tháng này so cùng kỳ không thể đem so trực tiếp với mức bình quân cả năm rồi kết luận vượt mục tiêu.

## 2. Trung bình có thể giấu phân bố

`KỊCH_BẢN` Năm cửa hàng có lợi nhuận tháng, triệu đồng: `10,10,10,10,100`.

`PHÉP_TÍNH` Bình quân = `140/5=28`; trung vị sau sắp xếp là10. Không có cửa hàng nào lãi28. Một điểm cực lớn kéo bình quân lên. `SỰ_THẬT` NIST giải thích sự khác nhau giữa trung bình và trung vị, đặc biệt với giá trị cực đoan. [NIST](https://itl.nist.gov/div898/handbook/eda/section3/eda351.htm).

Tương quan là cùng biến động; chưa đủ chứng minh nguyên nhân. Hai cửa hàng cùng tăng doanh thu khi trời nóng có thể vì thời tiết, không phải cửa hàng này làm cửa hàng kia tăng trưởng. Đây là phản ví dụ hư cấu cho yêu cầu kiểm cơ chế.

## 3. Xác suất và phiên bản dữ liệu

`KỊCH_BẢN` Kết quả lãi/lỗ sau một năm là −40, +10 hoặc +50 triệu với xác suất giả định25%,50%,25%. `PHÉP_TÍNH` Kỳ vọng = `−40×0,25+10×0,50+50×0,25=7,5 triệu`. Tổng xác suất =100%. Không kịch bản nào cho7,5; kỳ vọng không phải kết quả chắc xảy ra. Xác suất tự gán phải có nhãn và thử độ nhạy.

`SỰ_THẬT` BLS giải thích số ban đầu có thể được sửa khi thông tin đầy đủ hơn; ALFRED lưu phiên bản dữ liệu theo thời điểm. [BLS](https://www.bls.gov/about-bls/accurate-and-timely.htm), [ALFRED](https://alfred.stlouisfed.org/help). Khi đánh giá một quyết định quá khứ, chỉ dùng thông tin đã công bố tới lúc đó; không dùng bản sửa trong tương lai rồi trách người ra quyết định chưa biết.

Điểm dừng: tìm một câu trong ví dụ có thể đúng về số nhưng sai về diễn giải.

## Ví dụ từ nguồn thật

`SỰ_THẬT` ALFRED của Federal Reserve Bank of St. Louis cho phép khảo sát dữ liệu kinh tế theo phiên bản. Đây là ví dụ Hoa Kỳ về cách tái dựng điều đã biết tại một thời điểm, không có nghĩa mọi quốc gia đều có kho tương tự. Không đưa một số vĩ mô hiện hành vào bài để tránh nhầm ví dụ ổn định với bảng cập nhật thị trường.

## Năm câu hỏi khi đọc

1. Mẫu số và mốc so sánh là gì?
2. Bình quân có che ngoại lệ không?
3. Tương quan đã có cơ chế nhân quả chưa?
4. Xác suất lấy từ dữ liệu hay tự đặt?
5. Tại thời điểm quyết định, số này đã được công bố chưa?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Lãi suất từ4% lên5% tăng bao nhiêu điểm phần trăm, bao nhiêu phần trăm tương đối?
2. Tính bình quân và trung vị của1,2,3,4,40.
3. Tính kỳ vọng ví dụ −40/+10/+50 ở trên; vì sao không được gọi là lợi nhuận chắc chắn?
4. Xác suất trường hợp lỗ tăng lên50%, cơ sở25%, thuận lợi25%: kỳ vọng mới?
5. Một báo cáo tháng6 dùng số đã sửa tháng9 để mô tả 'điều thị trường biết tháng6': lỗi gì?
6. Một doanh nghiệp tăng giá và doanh thu tăng; cần thêm gì trước khi kết luận khách không nhạy giá?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` +1 điểm phần trăm; (5−4)/4=25% tương đối. Kiểm đơn vị diễn đạt.
2. `PHÉP_TÍNH` 50/5=10, trung vị3; quan sát phân bố trước diễn giải.
3. 7,5 triệu; là tổng có trọng số theo xác suất giả định, có thể mất40 triệu trong kịch bản bất lợi.
4. `PHÉP_TÍNH` −40×0,5+10×0,25+50×0,25=−5 triệu; luận điểm đổi khi xác suất đổi.
5. Dùng dữ liệu tương lai so với câu hỏi, gây thiên lệch nhìn lại; cần phiên bản đã có tới tháng6.
6. Lượng bán, cơ cấu sản phẩm, thời gian, đối thủ, khách rời bỏ và yếu tố chung; chỉ giá và doanh thu chưa đủ.

</details>

## Lỗi thường gặp

- Nhầm phần trăm với điểm phần trăm.
- Gọi trung bình là trải nghiệm của mọi thành viên.
- Lấy tương quan làm nguyên nhân.
- Gán xác suất chính xác giả tạo.
- Bỏ lịch sử sửa đổi hoặc chỉ nhìn công ty còn tồn tại.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Kỳ vọng có thể dương nhưng kết quả bất lợi khó chịu ở đâu?
- Mẫu có bỏ doanh nghiệp thất bại không?
- Bằng chứng nào làm tôi đổi xác suất đã giả định?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [NIST — Measures of Location](https://itl.nist.gov/div898/handbook/eda/section3/eda351.htm) | Hoa Kỳ; sổ tay thống kê; ngày phiên bản CHƯA_BIẾT | Trung bình, trung vị, ngoại lệ |
| [BLS — Accurate and Timely](https://www.bls.gov/about-bls/accurate-and-timely.htm) | Hoa Kỳ; chính sách dữ liệu; ngày xuất bản CHƯA_BIẾT | Số sơ bộ và sửa đổi |
| [St. Louis Fed — ALFRED Help](https://alfred.stlouisfed.org/help) | Hoa Kỳ; hướng dẫn kho dữ liệu; ngày xuất bản CHƯA_BIẾT | Phiên bản tại thời điểm |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/N7-fact-check.md), [phản biện](../reviews/N7-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

