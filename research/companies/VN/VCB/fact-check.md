# Biên bản kiểm nguồn: VCB — vòng 6

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
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

| Mức | Phát hiện | Bằng chứng / xử lý | Trạng thái |
|---|---|---|---|
| Trung bình | Chưa khớp PDF với miền ngân hàng/HOSE | Đã tự tải CDN, khớp SHA-256; chỉ xác nhận bản gương, không chứng minh bản phát hành miền ngân hàng | Đã công khai, không chặn |
| Trung bình | Khoản 5.000 tỷ Q3 chưa nối được vào số dư cuối kỳ | Vietcap nêu khoản trái phiếu; BCTC ghi số dư dự phòng cụ thể 6.303,616 tỷ nhưng không nêu danh tính/cầu nối riêng | Giữ thứ cấp, không chặn |

## Kiểm tra phép tính

- Nhóm 3–5: 2.571.437 + 1.657.212 + 8.588.936 = 12.817.585 triệu VND. Đầu kỳ trình bày lại: 761.291 + 301.991 + 8.650.658 = 9.713.940 triệu.
- NPL: 12.817,585 / 1.816.093,286 = 0,7058%. Nhóm 3–4 tăng khoảng 3,977 lần.
- Dự phòng chung: 12.422.952 + 1.002.848 − 1.177 = 13.424.623 triệu; cụ thể: 12.557.439 + 5.186.666 − 621 = 17.743.484 triệu. Cộng: 31.168.107 triệu. Dòng xử lý bằng dự phòng để gạch.
- Bao phủ: 31.168,107 / 12.817,585 = 243,17%.
- Dự phòng cụ thể trái phiếu: 6.303,616 − 3.306,873 = 2.996,743 tỷ, tăng 90,62%. Dự phòng chung 54,742 xuống 48,309; trái phiếu tổ chức kinh tế nắm đến đáo hạn 6.501,250 tỷ. Không coi mọi số cùng một khách hàng.
- LNTT9T làm tròn 40.440; trừ 2.905 theo nguồn thứ cấp: 37.535 / 33.133 − 1 = 13,29%.

## Hạn chế của lần kiểm duyệt

PDF tải trực tiếp khớp byte với bản lưu cục bộ (15.769.585 byte; SHA-256 `13caf1e063f5f3b551a793646833a9598a99a67aec439ab69c3ed6d2b2b4ba3a`). Chưa khớp byte với bản từ miền ngân hàng/HOSE. Các số ngoài thuyết minh đã đọc vẫn là thứ cấp; thông tin khách hàng năng lượng và NIM do Vietcap phân tích, không phải xác nhận trực tiếp của ngân hàng. Không suy danh tính khách hàng.

Bản kiểm duyệt chạy trên bản nháp có hash trên. Điều phối viên chỉ bỏ tiền tố nháp và đổi hai dòng trạng thái vòng đời; nội dung chuẩn không đổi.

## Kết luận của agent kiểm duyệt

`ĐẠT` theo tiêu chí không có lỗi nghiêm trọng/cao chưa xử lý; giữ các hạn chế và phát hiện trung bình/thấp dưới đây cho lần nâng cấp tiếp.
