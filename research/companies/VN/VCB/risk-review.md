# Biên bản phản biện: VCB — vòng 6

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 13:45 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: nhóm nợ 2–5, dự phòng cho vay và trái phiếu, thông tin Vietcap, kịch bản và phép tính liên quan.
- Báo cáo đích: `research/companies/VN/VCB/report.md`
- SHA-256 nội dung đích: `6ea21e9ad0273c942b2504b7c675907d88ef950ab330c15876a39864633f9e33`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập vòng 6; không tự thay kết luận. Tiêu chí: không còn lỗi nghiêm trọng/cao; trung bình/thấp được lưu, không chặn. Toàn văn kết quả nhánh có trong cuộc trao đổi ngày 02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Trang lưu BCTC](https://24hmoney.vn/report/72954/financialstatements) | 31/10/2026; kỳ 30/09/2026 | 02/11/2026 | Loại và ngày lưu báo cáo |
| [PDF BCTC](https://cdn.24hmoney.vn/upload/file/2026-4/2026-10-31/no-name-1793388232.pdf) | Ký 30/10/2026; Q3/9T2026 | 02/11/2026 | Tải trực tiếp, đọc ảnh PDF27–29, kiểm hash |
| [Vietcap](https://www.vietcap.com.vn/trung-tam-phan-tich/vcb-loi-nhuan-thap-hon-ky-vong-do-chi-phi-du-phong-ngoai-du-kien-nhung-da-tang-truong-kinh-doanh-cot-loi-van-duy-tri-tich-cuc-bao-cao-kqkd) | 30/10/2026; Q3/9T2026 | 02/11/2026 | Khoản trái phiếu năng lượng, NIM, bằng chứng đối trọng |

## Phát hiện

| Mức | Phát hiện | Bằng chứng / khắc phục | Trạng thái |
|---|---|---|---|
| Trung bình | Lặp chi phí dự phòng Q3 sang Q4 có thể bị hiểu là mức thường xuyên | Vietcap nêu 5.000 tỷ khoản trái phiếu riêng lẻ. Hồ sơ đã gọi minh họa; lần nâng cấp nên nêu rõ nền Q3 gồm bất thường hoặc thêm độ nhạy loại khoản này | Còn, không chặn |
| Trung bình | Câu chưa giải thích NII bỏ sót lời giải thích NIM của Vietcap | Vietcap nêu NIMQ3 3,09%, +12 điểm cơ bản theo quý; chưa phải giải trình ngân hàng | Còn, không chặn |
| Thấp | So bao phủ VCB với 79% ngành chưa rõ đồng nhất kỳ/định nghĩa | S33 cho VCB; S20 ngành chưa mở lại trong vòng này | Còn, không chặn |

## Bằng chứng trái chiều và kiểm tra

Các phép cộng nhóm nợ, cầu nối dự phòng và tỷ lệ bao phủ khớp ảnh PDF27–29. Không phát sinh xử lý bằng dự phòng ở dòng tương ứng của thuyết minh cho vay. Dự phòng chứng khoán tách riêng dự phòng cho vay. Vietcap đánh giá nếu loại khoản trái phiếu năng lượng thì chất lượng tài sản còn vững; hồ sơ không bỏ qua hướng thuận này và không suy toàn bộ nhóm 3–4 tăng là nợ mới. Giới hạn bản gương được công khai.

## Hạn chế của lần kiểm duyệt

PDF tải trực tiếp khớp byte với bản lưu cục bộ (15.769.585 byte; SHA-256 `13caf1e063f5f3b551a793646833a9598a99a67aec439ab69c3ed6d2b2b4ba3a`). Chưa khớp byte với bản từ miền ngân hàng/HOSE. Các số ngoài thuyết minh đã đọc vẫn là thứ cấp; thông tin khách hàng năng lượng và NIM do Vietcap phân tích, không phải xác nhận trực tiếp của ngân hàng. Không suy danh tính khách hàng.

Bản kiểm duyệt chạy trên bản nháp có hash trên. Điều phối viên chỉ bỏ tiền tố nháp và đổi hai dòng trạng thái vòng đời; nội dung chuẩn không đổi.

## Kết luận của agent kiểm duyệt

`ĐẠT` theo tiêu chí không có lỗi nghiêm trọng/cao chưa xử lý; giữ các hạn chế và phát hiện trung bình/thấp dưới đây cho lần nâng cấp tiếp.
