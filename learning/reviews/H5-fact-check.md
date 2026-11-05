# Biên bản kiểm nguồn: H5 — Đợt 4, nhóm 2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 15:44 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Phạm vi: toàn bản chụp H5, nguồn CFA và Sullivan–Timmermann–White, ví dụ, 10 bài tập/đáp án, đối chiếu mô hình và test.
- Báo cáo đích: `learning/lessons/H5-statistics-backtest-overfitting.md`
- SHA-256 nội dung đích: `a115d41d57c777a39c1f2c2db6c6040840ee3b1817ec2d71ac87b1195d62de30`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Điều phối ghi kết quả nhánh độc lập `h5_fact_final`, giữ kết luận. Nhánh chỉ đọc bản chụp `data/raw/payloads/learning-wave4-group2-snapshot-2026-11-02-1541/H5-statistics-backtest-overfitting.md`, không đọc bài khác, learning/reviews hay kết quả phản biện; kiểm hash chuẩn bằng script. Toàn văn trong cuộc trao đổi02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [CFA Backtesting & Simulation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation) | CFA LevelII2026; ngày phát hành cụ thể không hiển thị | 02/11/2026 | Cuốn chiếu, nhìn trước/sống sót, thay đổi cấu trúc/đuôi dày |
| [Sullivan–Timmermann–White PDF](https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Sullivan_Timmermann_White.pdf) | Journal of Finance54(5),10/1999,tr1647–1691; DJIA1897–1996 | 02/11/2026 | Đọc luồng tải PDF công khai;1654–1655, chú thích14tr1659, phần1676 |
| [Wiley DOI](https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00163) | Số tạp chí10/1999; trang ghi First published17/12/2002 | 02/11/2026 | Tác giả, DOI, trang, tóm tắt; phân biệt mốc trang trực tuyến với kỳ số tạp chí |

## Phát hiện

| Mức | Phần | Phát hiện / bằng chứng | Khắc phục / trạng thái |
|---|---|---|---|
| Không có lỗi | CFA | Trang tóm tắt xác nhận cuốn chiếu, sai lệch và giới hạn; bài công khai chỉ dùng tóm tắt | ĐẠT; không tự gán ngày phát hành |
| Không có lỗi | Nghiên cứu1999 |26→7.846,100năm DJIA và phụ thuộc giữa quy tắc đúng bài gốc; Wiley đối chiếu metadata | ĐẠT; giữ hai mốc1999/2002 riêng |
| Không có lỗi | Lợi suất năm hóa | Chú thích14 là trung bình ngày×252;1676nêu thiếu cổ tức và chi phí lịch sử | ĐẠT; không gọi CAGR sau phí |
| Không có lỗi | Số học/mã/đáp án | Ghép, mẫu sống sót, xác suất độc lập và chi phí khớp; mô hình có kiểm đầu vào | ĐẠT trong phạm vi kiểm nguồn |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

`PHÉP_TÍNH`7.846−26=7.820;7.846/26≈301,7692. Mẫu ba mã:(10%+5%−90%)/3=−25%,vốn75triệu; hai mã:+7,5%,107,5triệu;chênh32,5điểm phần trăm.

Bốn quý xây dựng A16,985856%,B8,243216%,C3,978809%; ngoài mẫu trước phí−5,91%,+2,01%,−0,04%.100kiểm định độc lập: kỳ vọng5, có ít nhất một≈99,407947%. Tổng mua+bán80triệu×0,15%=120.000; lãi ròng380.000,0,38%. Mỗi quý trừ1điểm phần trăm theo quy ước; ghép ngoài mẫu A−7,84%,B0%,C−2,03%. Không sai dấu,đơn vị,phần trăm/số thập phân hoặc ghép/cộng.

## Hạn chế của lần kiểm duyệt

Web mở PDF bị timeout nhưng nhánh đã đọc PDF công khai qua luồng tải trực tuyến; Wiley mở metadata/tóm tắt, không có toàn văn Wiley. Không tái lập toàn bộ nghiên cứu1999 hoặc xác nhận khả năng giao dịch/dữ liệu thị trường hiện hành. Điều phối tự kiểm phép tính và trang trích trước khi nhận kết quả; sau kiểm chỉ đổi vòng đời, không đổi nội dung chuẩn.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không nghiêm trọng/cao; ví dụ hư cấu được phân biệt với bằng chứng thực nghiệm, nguồn và phép tính trọng yếu được hỗ trợ.
