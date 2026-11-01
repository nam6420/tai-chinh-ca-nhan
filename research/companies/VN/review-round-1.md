# Kiểm duyệt vòng 1 của bốn hồ sơ Việt Nam (Đợt 2)

- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Người ghi: phiên chính (vai điều phối viên) chép kết quả của tám nhánh độc lập; kiểm nguồn và phản biện rủi ro chạy riêng, không thấy kết luận của nhau.
- Mục đích: lưu vết phát hiện vòng 1 và cách xử lý. Biên bản có hiệu lực xuất bản là các tệp `fact-check.md` và `risk-review.md` trong thư mục từng mã, trên mã băm của bản đã sửa.

| Mã | Bản vòng 1 (SHA-256 đầu 12 ký tự) | Kiểm nguồn vòng 1 | Phản biện vòng 1 |
|---|---|---|---|
| FPT | c8d459f32165 | KHÔNG_ĐẠT, 3 nghiêm trọng | KHÔNG_ĐẠT, 4 nghiêm trọng |
| VNM | f19b000e49c7 | ĐẠT, 0 nghiêm trọng | KHÔNG_ĐẠT, 2 nghiêm trọng |
| VCB | 14b928e21947 | ĐẠT (thứ cấp), 0 nghiêm trọng | KHÔNG_ĐẠT, 4 nghiêm trọng |
| HPG | 9d2bf159aede | KHÔNG_ĐẠT, 3 nghiêm trọng | KHÔNG_ĐẠT, 3 nghiêm trọng |

## FPT

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Nghiêm trọng (kiểm nguồn) | Câu "tỷ giá yên tăng nhanh hơn đồng Việt Nam" sai chiều; doanh thu +25,2% theo yên và +17,2% theo VND nghĩa là yên mất giá khoảng 6,4% so với VND | Viết lại; tách `SỰ_THẬT`, `PHÉP_TÍNH` (1,172 / 1,252 − 1) và `SUY_LUẬN` |
| Nghiêm trọng (kiểm nguồn) | Kế hoạch lợi nhuận 11.629 tỷ bị ghi "không cùng cơ sở FTEL", trong khi báo cáo ACBS nói kế hoạch theo phương pháp hợp nhất mới | Sửa; ghi là thứ cấp, chưa xác nhận từ nghị quyết |
| Nghiêm trọng (kiểm nguồn) | Nhãn `SỰ_THẬT` trên dữ kiện thứ cấp (cổ tức 20%, cổ đông lớn, thưởng 10%); nguồn DNSE không xác minh được | Hạ nhãn, ghi ngày số liệu, bỏ nguồn DNSE |
| Nghiêm trọng (phản biện) | Chưa nêu quyền kiểm soát FTEL (Bộ Công an đại diện hơn 50% vốn nhà nước, FPT nắm 45,66%) | Thêm mục quyền kiểm soát FTEL với cả hai quan điểm |
| Nghiêm trọng (phản biện) | Rủi ro cổ tức FTEL và việc FTEL chưa đủ điều kiện công ty đại chúng | Thêm; chính sách cổ tức FTEL ghi `CHƯA_BIẾT` |
| Nghiêm trọng (phản biện) | ESOP và pha loãng để `CHƯA_BIẾT` dù có số: 10,8 triệu cổ phiếu giá 10.000 đồng, thị giá khoảng 76.300 đồng | Thêm phép tính chiết khấu khoảng 86,9% và pha loãng; EPS điều chỉnh `CHƯA_BIẾT` |
| Nghiêm trọng (phản biện) | Mục dòng tiền thiên về trấn an | Đổi tiêu đề trung tính; nêu điều chưa biết (CFO cùng cơ sở) |
| Trung bình | Kịch bản bất lợi chưa đủ khắc nghiệt; rủi ro AI để `Ý_KIẾN`; nhãn nguồn thứ cấp; nợ ròng không nêu cấu phần; ngày nguồn S9 | Thêm kịch bản căng, đoạn rủi ro AI, bổ sung nhãn, ghi rõ cấu phần, sửa ngày |

## VNM

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Nghiêm trọng (phản biện) | Kịch bản bất lợi vẫn cao hơn năm 2025 (+18%) và cột giả định (nội địa +11%, nước ngoài +28%) không khớp quý 3 (+8,8%, +8,3%) | Thêm kịch bản căng; sửa giả định; nêu rõ 9 tháng đã bằng 91% LNST mẹ năm 2025 |
| Nghiêm trọng (phản biện) | Không tách lợi nhuận quý 3 do thu nhập tài chính và lãi liên kết (khoảng 441 tỷ, khoảng 78% mức tăng) | Thêm cầu nối từ số thứ cấp; cầu nối từ báo cáo gốc ghi `CHƯA_BIẾT` |
| Trung bình | Hàng tồn kho +14,4% là so với đầu năm, không cùng mốc; rủi ro tỷ giá lẫn sự thật và suy luận; nhãn nguồn FY2025; nguyên nhân chênh lệch cổ tức; Miraka còn hay không; chi trả theo EPS 108%; chuẩn mực Thông tư 43 | Sửa nhãn và mốc; thêm Taupomh 13,55%, chi trả theo EPS, Thông tư 43/2026 |

## VCB

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Nghiêm trọng (phản biện) | Kịch bản dựa trên nửa đầu năm đã gồm khoảng 2.905 tỷ khoản một lần; loại ra thì tăng 9 tháng khoảng 13,3% | Thêm cột loại khoản một lần; dựng lại kịch bản thuận lợi |
| Nghiêm trọng (phản biện) | Kịch bản bất lợi vẫn cao hơn năm 2025; chi phí tín dụng quý 3 quy năm 1,36% bị bỏ | Thêm kịch bản căng và chi phí tín dụng theo tốc độ quý 3 |
| Nghiêm trọng (phản biện) | Bỏ qua nợ nhóm 2 và nợ nghi ngờ tăng nhiều quý | Thêm đoạn nợ nhóm 2 theo quý |
| Nghiêm trọng (phản biện) | Chênh số dư dự phòng và chi phí dự phòng hàm ý xử lý nợ khoảng 5.040 tỷ | Thêm như câu hỏi mở, `CHƯA_BIẾT` |
| Trung bình | Nhận định room tín dụng viện dẫn nguồn không nói điều đó; nhân quả NIM; CASA lệch nguồn; pha loãng; so sánh DBS thiếu chi phí tín dụng; ngưỡng không nguồn | Sửa theo nguồn mở được; thêm tính pha loãng, chi phí tín dụng DBS; ngưỡng ghi là `Ý_KIẾN` |
| Trung bình (kiểm nguồn) | Dư nợ ghi "trên 1.816.000 (+8,5%)" trong khi nguồn ghi "gần 1,82 triệu tỷ (+9%)"; số 6 tháng gán sai nguồn; nhãn `SỰ_THẬT` lẫn diễn giải | Sửa số, thêm nguồn, tách nhãn |

## HPG

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Nghiêm trọng (kiểm nguồn) | Kịch bản bất lợi tính lợi nhuận gộp cả năm thấp hơn số 9 tháng đã thực hiện | Dựng lại: giữ 9 tháng đã thực hiện và chỉ áp biên giả định lên Q4 |
| Nghiêm trọng (kiểm nguồn) | Nguyên nhân tăng lãi vay quý 3 ghi `SỰ_THẬT` và gán sai nguồn | Tách số liệu, nguyên nhân do công ty nêu cho từng kỳ và suy luận |
| Nghiêm trọng (kiểm nguồn) | Giao dịch của con trai chủ tịch gán sai nguồn và lỗi thời | Thêm nguồn đúng; thực mua gần 33,3 triệu cổ phiếu |
| Nghiêm trọng (phản biện) | Chống lẩn tránh thuế HRC ghi `CHƯA_BIẾT` dù có Quyết định 612/QĐ-BCT | Thêm Quyết định 612 và phạm vi, miễn trừ |
| Nghiêm trọng (phản biện) | Dự án Phú Yên lỗi thời, thiếu bằng chứng dư cung | Cập nhật: đề nghị tạm dừng, vốn chuyển sang mở rộng khác |
| Nghiêm trọng (phản biện) | Kịch bản bất lợi chưa khắc nghiệt (13% thay vì đáy 10,9%, bỏ lãi vay tăng, doanh thu Q4 bằng Q3) | Thêm kịch bản cực đoan; lãi vay Q4 tăng 15%; nêu giới hạn chưa trừ chi phí |
| Trung bình | Cơ sở doanh thu khác nhau; ghi chú quy trình lẫn nội dung; EU nâng thuế gán sai; lãi đột biến quý 1; bảng P/E nghiêng khuyến nghị | Ghi chú cơ sở; chuyển ghi chú; sửa nguồn; nêu lãi đột biến; bảng P/E đặt là bài tập mẫu số |
