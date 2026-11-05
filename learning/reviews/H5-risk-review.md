# Biên bản phản biện rủi ro: H5 — Đợt 4, nhóm 2

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 15:45 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Phạm vi: toàn bản chụp, bài tập/đáp án, đọc mô hình/test; thông tin, mẫu, thử nhiều phương án, chi phí và khả thi.
- Báo cáo đích: `learning/lessons/H5-statistics-backtest-overfitting.md`
- SHA-256 nội dung đích: `a115d41d57c777a39c1f2c2db6c6040840ee3b1817ec2d71ac87b1195d62de30`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Điều phối ghi kết quả nhánh độc lập `h5_risk_final`, không đổi kết luận hoặc bỏ ý kiến bất đồng. Nhánh chỉ đọc bản chụp `data/raw/payloads/learning-wave4-group2-snapshot-2026-11-02-1541/H5-statistics-backtest-overfitting.md`, không đọc bài khác, learning/reviews hoặc kết quả kiểm nguồn. Hash chuẩn khớp. Toàn văn trong cuộc trao đổi02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [CFA Backtesting & Simulation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation) | Chương trình2026; ngày phát hành riêng không hiển thị | 02/11/2026 | Cuốn chiếu, sống sót/nhìn trước, cấu trúc và đuôi |
| [Sullivan–Timmermann–White PDF](https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Sullivan_Timmermann_White.pdf) | Journal of Finance54(5),10/1999,tr1647–1691; DJIA1897–1996; ngoài mẫu1987–1996; futures1984–1996 | 02/11/2026 |7.846quy tắc, phụ thuộc và kết quả hai chiều |
| [Wiley DOI](https://doi.org/10.1111/0022-1082.00163) | Số tạp chí10/1999; First published17/12/2002 trên trang | 02/11/2026 | Tác giả/tên/phạm vi26quy tắc mở rộng/100năm |

## Phát hiện

| Mức | Phần | Phát hiện / tác động | Bằng chứng | Khắc phục / trạng thái |
|---|---|---|---|---|
| Trung bình | Ví dụ nghiên cứu thật | Số quy tắc đúng và bài không kết luận mọi quy tắc vô dụng, nhưng chưa tóm lược đầy đủ kết quả thuận/nghịch: một số kết quả trong mẫu vẫn bền sau điều chỉnh; hiệu quả không lặp lại ngoài mẫu DJIA1987–1996 và không xác nhận trên futures1984–1996. Ví dụ có thể nghiêng về thông điệp người thắng do may mắn | Bài gốc phầnIV/VI | Có thể bổ sung tóm lược cân bằng khi biên tập sau; giữ giới hạn lịch sử/thị trường. MỞ, không chặn theo tiêu chí đã chấp nhận |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

`PHÉP_TÍNH` Mẫu xây dựng chọnA; ngoài mẫu A/B/C−5,91%,+2,01%,−0,04%; sau quy ước chi phí−7,84%,0%,−2,03%. Sống sót:−25%so+7,5%,chênh32,5điểm phần trăm. Kỳ vọng dương giả5, xác suất có ít nhất một≈99,4079% dưới giả định độc lập. Sáu quý chỉ là ví dụ, không ước lượng xác suất thành công chiến lược.

Bằng chứng trái chiều giữ lại: bài1999 không chỉ nói về chọn lọc; một số kết quả trong mẫu đứng vững sau điều chỉnh, nhưng kết quả ngoài mẫu không có ý nghĩa ở mức thông thường và futures không cho thấy vượt trội. Vì vậy kết luận phụ thuộc kỳ/thị trường. Điều phối đã đọc lại phần trong mẫu và ngoài mẫu trước khi quyết định giữ phát hiện ở mức trung bình, không tự sửa bài khi đang kiểm.

Đã đọc mã/test, không chạy kiểm thử. Phí tính cả mua và bán; bài nêu thuế, spread,tác động giá và hạn chế khớp còn thiếu, không gọi các số sau quy ước phí là khả thi thực.

## Hạn chế của lần kiểm duyệt

CFA chỉ tóm tắt công khai; PDF toàn văn bài1999 đã mở trực tiếp, Wiley chỉ đối chiếu xuất bản. Không có kiểm định với thị trường hiện tại hoặc người học thật; không xác nhận chiến lược/khả năng sinh lời. Sau đủ hai biên bản, điều phối chỉ đổi vòng đời; sửa nội dung sau làm biên bản hết hiệu lực.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không nghiêm trọng/cao; giữ một phát hiện trung bình về sự cân bằng khi trình bày nghiên cứu, không chặn. Đây không phải chứng nhận chiến lược.
