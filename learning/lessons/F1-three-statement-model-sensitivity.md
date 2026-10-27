# Bài F1 — Mô hình liên kết ba báo cáo và độ nhạy

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:54 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Dựng mô hình một kỳ liên kết lợi nhuận, dòng tiền, tài sản và nguồn vốn; kiểm cân đối và độ nhạy.
- Bài trước liên quan: [001](001-business-financial-statements.md), [N2](N2-statement-line-items.md), [004](004-cash-flow-and-earnings-quality.md), [011](011-dcf-reverse-dcf.md).
- Câu hỏi cốt lõi: Một thay đổi ở kết quả kinh doanh đi qua tiền và bảng cân đối như thế nào?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F1-fact-check.md), [phản biện](../reviews/F1-risk-review.md).

## Hiểu bài trong một phút

Lợi nhuận không đồng nghĩa tiền thu được. Mô hình dùng lợi nhuận, điều chỉnh khoản không dùng tiền và thay đổi vốn lưu động để tính dòng tiền; dòng tiền cập nhật số dư tiền. Bảng cân đối phải bằng nhau nhưng cân không tự chứng minh giả định hợp lý.

## 1. Đầu vào và báo cáo kết quả

`KỊCH_BẢN` Doanh nghiệp hư cấu, tỷ VND, một năm. Đầu kỳ tiền 20, phải thu 20, tài sản cố định ròng 60: tổng tài sản 100; nợ vay 40, vốn chủ 60. Bỏ qua các tài sản/nợ khác. Năm nay doanh thu 100, chi phí hoạt động trả tiền 70, khấu hao 10, lãi vay trả tiền 4, thuế 20% lợi nhuận trước thuế và trả ngay. Doanh thu có một phần chưa thu, phải thu tăng 5; không có thay đổi vốn lưu động khác. Không dùng cho doanh nghiệp thật.

`PHÉP_TÍNH` Lợi nhuận hoạt động = 100 − 70 − 10 = 20; trước thuế = 20 − 4 = 16; thuế = 16 × 20% = 3,2; lợi nhuận sau thuế = **12,8**.

## 2. Dòng tiền và bảng cân đối

`SỰ_THẬT` [IFRS Foundation — IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) mô tả phương pháp gián tiếp điều chỉnh lợi nhuận cho khoản không dùng tiền và thay đổi dồn tích; luồng tiền được trình bày theo hoạt động, đầu tư và tài trợ. Phân loại lãi/thuế trong báo cáo thật phụ thuộc chuẩn và chính sách áp dụng; ví dụ dưới chỉ là mô hình đơn giản.

`KỊCH_BẢN` Khấu hao 10 không chi tiền; phải thu tăng 5. Công ty mua tài sản cố định bằng tiền 15, trả gốc vay 5 và trả cổ tức tiền 2. Giả định lãi vay và thuế đã nằm trong dòng tiền hoạt động.

| Bước | Công thức | Tỷ VND |
|---|---|---:|
| Dòng tiền hoạt động | 12,8 + 10 − 5 | 17,8 |
| Dòng tiền đầu tư | −15 | −15 |
| Dòng tiền tài trợ | −5 − 2 | −7 |
| Tiền cuối kỳ | 20 + 17,8 − 15 − 7 | 15,8 |
| Phải thu cuối kỳ | 20 + 5 | 25 |
| Tài sản cố định ròng | 60 + 15 − 10 | 65 |
| Nợ vay cuối kỳ | 40 − 5 | 35 |
| Vốn chủ cuối kỳ | 60 + 12,8 − 2 | 70,8 |

`PHÉP_TÍNH` Tài sản cuối = 15,8 + 25 + 65 = **105,8**; nợ + vốn chủ = 35 + 70,8 = **105,8**. Cầu nối tiền và phương trình tài sản = nợ + vốn chủ cùng cân. Không cộng lại chi phí lãi một lần nữa khi nó đã trừ trong lợi nhuận và giả định đã trả trong dòng tiền hoạt động.

## 3. Độ nhạy một biến

`KỊCH_BẢN` Tăng doanh thu lên 110, các chi phí, khoản phải thu tăng 5, lãi, tỷ lệ thuế và mọi dòng tiền khác giữ nguyên; giả định phần doanh thu tăng được thu bằng tiền trong năm. `PHÉP_TÍNH` Lợi nhuận sau thuế tăng `10 × (1 − 20%) = 8`, thành 20,8; tiền và vốn chủ cuối cùng mỗi bên tăng 8 so với kịch bản cơ sở. Đây chỉ là độ nhạy có điều kiện, không phải dự báo. Trong thực tế chi phí, vốn lưu động, thuế, công suất và nhu cầu có thể cùng thay đổi.

## 4. Bố trí bảng tính và kiểm lỗi

Dùng một vùng đầu vào có đơn vị và nguồn, một vùng công thức và một vùng kiểm. Mỗi ô dự báo tham chiếu đầu vào hoặc ô kỳ trước; không nhập lại cùng một số ở nhiều nơi. Kiểm `tổng tài sản − nợ − vốn chủ = 0`, cầu nối tiền, dấu của tăng phải thu và chi đầu tư, dư nợ cuối không âm bất hợp lý. Một số cân bằng bằng 0 vẫn có thể ẩn chi phí bỏ sót, dòng tiền đếm hai lần hoặc giả định phi thực tế.

## Năm câu hỏi khi đọc

1. Báo cáo dùng kỳ, đơn vị, pháp nhân và chuẩn nào?
2. Lợi nhuận nào đi vào vốn chủ và dòng tiền hoạt động?
3. Phải thu, tồn kho, phải trả và khấu hao được xử lý ra sao?
4. Tiền đầu kỳ cộng các dòng tiền có khớp tiền cuối kỳ không?
5. Thay đổi giả định có tạo ảnh hưởng hợp lý lên cả ba báo cáo không?

## Bài tập

1. Với đầu vào cơ sở, lợi nhuận trước và sau thuế là bao nhiêu?
2. Tăng phải thu 5 làm dòng tiền hoạt động tăng hay giảm so với lợi nhuận đã điều chỉnh khấu hao?
3. Tiền cuối kỳ từ bảng là bao nhiêu?
4. Nợ 35 và vốn chủ 70,8 có bằng tổng tài sản không?
5. Nếu doanh thu tăng 10, thuế 20% và mọi giả định nhạy khác giữ nguyên, lợi nhuận tăng bao nhiêu?
6. Bảng cân đối cân có đủ chứng minh mô hình chính xác không?

## Đáp án

1. Trước thuế 16; thuế 3,2; sau thuế 12,8 tỷ.
2. Giảm 5, vì phần doanh thu tăng chưa thu bằng tiền trong giả định.
3. 15,8 tỷ VND.
4. Có, 35 + 70,8 = 105,8 tỷ, bằng tài sản cuối 105,8.
5. 8 tỷ nếu doanh thu tăng được thu tiền và các giả định khác giữ nguyên.
6. Không; còn cần kiểm dữ kiện, phân loại, dấu, điều kiện và tính hợp lý.

## Lỗi thường gặp và ranh giới an toàn

Đếm khấu hao là tiền chi hai lần, đổi dấu phải thu, đưa lãi vào hai chỗ, hoặc dùng ô tiền làm nút cân bằng mà không kiểm nguồn. Đây là bài tập, không là mô hình định giá công ty thật.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Chính sách kế toán, kỳ, dữ liệu và tác động tương hỗ của doanh nghiệp cụ thể; phải truy hồ sơ gốc và kiểm chuẩn trước khi áp dụng.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [IFRS Foundation — IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/), trang chuẩn IFRS; phân loại thực tế phụ thuộc chuẩn và kỳ áp dụng. Tất cả đầu vào và phép tính ở đây là kịch bản hư cấu.
