# Kiểm duyệt vòng 2 của bốn hồ sơ Việt Nam (Đợt 2)

- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Người ghi: phiên chính (vai điều phối viên) chép kết quả của tám nhánh độc lập; kiểm nguồn và phản biện rủi ro chạy riêng, không thấy kết luận của nhau. Lượt chạy đầu bị ngắt vì giới hạn sử dụng; các nhánh được đánh thức chạy tiếp từ chỗ dừng.
- Biên bản có hiệu lực xuất bản chưa được ghi: bản hiện tại đã sửa theo vòng 2 nên mã băm đổi và cần vòng 3.

| Mã | Bản vòng 2 (SHA-256 đầu 12 ký tự) | Kiểm nguồn vòng 2 | Phản biện vòng 2 | Bản sau sửa lượt 3 (đầu 12 ký tự) |
|---|---|---|---|---|
| FPT | 390aed0d534e | ĐẠT, 0 nghiêm trọng, 4 trung bình | ĐẠT có điều kiện, 0 nghiêm trọng, 6 trung bình | 0e108d4382d5 |
| VNM | 37ba074919f7 | ĐẠT, 0 nghiêm trọng, 4 trung bình | KHÔNG_ĐẠT, 0 nghiêm trọng, 3 mức cao | d3b06ba37e8e |
| VCB | 35277202405d | ĐẠT (thứ cấp), 0 nghiêm trọng, 1 trung bình và 1 thấp-trung bình | ĐẠT có điều kiện, 0 nghiêm trọng, 2 mức cao | a79b0e7c3ce0 |
| HPG | 8f479eaaf363 | KHÔNG_ĐẠT, 1 nghiêm trọng, 3 trung bình | KHÔNG_ĐẠT, 0 nghiêm trọng, 5 mức cao | 17a0ca9a05ac |

## FPT

| Mức | Phát hiện | Xử lý ở lượt 3 |
|---|---|---|
| Trung bình (kiểm nguồn) | Nhãn `SỰ_THẬT` thứ cấp; rủi ro AI để `SỰ_THẬT`; mã 27 của báo cáo lưu chuyển tiền tệ thuộc nhóm đầu tư; câu về quyền đại diện vốn nhà nước tại FTEL cần trích nguyên văn | Thêm quy ước nhãn; đổi AI sang `Ý_KIẾN`; sửa mã 27; trích đúng câu nguồn |
| Trung bình (phản biện) | Kịch bản căng chưa đủ khắc nghiệt; thiếu bằng chứng FPT vẫn chi phối hội đồng quản trị FTEL (2025) và lịch sử cổ tức FTEL; không tách phần FTEL trong lợi nhuận liên kết; rủi ro AI một chiều; tỷ giá yên chưa nêu sai số | Thêm kịch bản "căng 2" theo cơ chế (liên kết bằng 0, biên gộp −3 điểm); thêm nguồn 07/2025; thêm ước lượng thô FTEL; nêu sai số ±1 điểm |

## VNM

| Mức | Phát hiện | Xử lý ở lượt 3 |
|---|---|---|
| Cao (phản biện) | Kịch bản "căng" 60% không gắn cơ chế; "cơ sở" mang nguyên phần tăng bất thường quý 3 | Thêm kịch bản "Q4 lõi" và cột Q4 so với Q4/2025 cùng tốc độ chạy năm |
| Cao (phản biện) | Chưa dựng cầu nối từ số gốc, chưa đưa vào kịch bản | Dựng cầu nối từ báo cáo gốc: 77,4% mức tăng quý 3 nhưng 24,2% mức tăng 9 tháng |
| Cao (phản biện) | Bỏ sót xu hướng biên gộp và LNST theo quý (quý 2: 43,5% và 3.167 tỷ; quý 3: 41,36% và 2.964 tỷ) | Thêm bảng ba quý |
| Trung bình (kiểm nguồn) | Cầu nối quý 3 dùng số làm tròn của báo chí; Q4/2025 không mâu thuẫn (2.827,20 hợp nhất, 2.840,37 công ty mẹ); chi phí bán hàng không nằm trong danh mục phân loại lại; thiếu nguồn cho số Global Dairy Trade | Dùng số gốc; sửa; viết lại đoạn chuẩn mực; thêm nguồn |

## VCB

| Mức | Phát hiện | Xử lý ở lượt 3 |
|---|---|---|
| Cao (phản biện) | Suy luận xử lý nợ khoảng 5.040 tỷ mâu thuẫn với số dư dự phòng đầu năm gần 25.000 tỷ | Viết lại đoạn: hai định nghĩa bao phủ có thể khác nhau; không kết luận về xử lý nợ; loại số 5.040 |
| Cao (phản biện) | Kịch bản căng vẫn cao hơn năm 2025 | Thêm kịch bản "rất căng" (dự phòng gấp đôi quý 3): thấp hơn năm 2025 khoảng 0,7% |
| Trung bình | Opex 23.363 có trực tiếp trong nguồn; phát hành riêng lẻ và trái phiếu cấp hai dẫn từ kết quả tìm kiếm; công văn 9608 gán nguồn lẫn; dư nợ 8,5% so với 9% | Sửa nhãn; bỏ hai nội dung chỉ có trong kết quả tìm kiếm; tách nguồn công văn; nêu cả hai số |

## HPG

| Mức | Phát hiện | Xử lý ở lượt 3 |
|---|---|---|
| Nghiêm trọng (kiểm nguồn) | So giá 27.600 (trước thưởng 10%) với 21.000 (sau thưởng) cho "giảm 24%" | Điều chỉnh theo hệ số 1,1: giảm khoảng 16,3%; nêu cách tính |
| Cao (phản biện) | Kịch bản cực đoan chưa đủ khắc nghiệt; hệ số lãi vay +15% không nguồn; gộp trên lãi vay dễ bị hiểu là hệ số bảo chứng lãi | Thêm "chu kỳ xấu" (biên 8%, doanh thu quý 4 bằng quý 3/2025); độ nhạy lãi vay 15%, 30%, 50%; nêu rõ không phải hệ số bảo chứng lãi |
| Cao (phản biện) | Thiếu chuỗi giá HRC nội địa; giao dịch nội bộ chưa tính quy mô | Thêm giá HRC giảm hơn 10% từ đỉnh tháng 5 và tăng nhẹ cho tháng 11; thêm tỷ lệ so với số cổ phiếu lưu hành |
| Trung bình | "Than cốc" và "cốc (coke)"; nhãn nguồn EU và Trung Quốc; Q3 vượt dự báo gán nguồn; C/O; lãi chuyển nhượng 4.915 và 3.800 | Sửa theo nguồn; thêm C/O và so sánh hai số |
