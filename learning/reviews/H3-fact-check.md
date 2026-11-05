# Biên bản kiểm nguồn: H3 — Đợt 4, nhóm 2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 15:42 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Phạm vi: toàn thân bài, 10 bài tập và đáp án, công thức, nguồn, kỳ, đơn vị, dấu và các phép tính.
- Báo cáo đích: `learning/lessons/H3-risk-volatility-drawdown-liquidity.md`
- SHA-256 nội dung đích: `31f86268818194f8cb7b1bb9ad0380560e61d78da5afb068e5b91b9902e091ab`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi kết quả từ nhánh độc lập `h3_fact_final`, không đổi kết luận. Nhánh chỉ đọc bản chụp `data/raw/payloads/learning-wave4-group2-snapshot-2026-11-02-1541/H3-risk-volatility-drawdown-liquidity.md`, không đọc bài khác, learning/reviews hoặc kết quả nhánh phản biện. Toàn văn trả trong cuộc trao đổi ngày 02/11/2026. Hash theo `canonical_report`, không theo byte thô.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [Berkshire thư2024](https://www.berkshirehathaway.com/letters/2024ltr.pdf) | 22/02/2025; PDF15; S&P2008–2009, % có cổ tức | 02/11/2026 | Xác nhận −37,0%, +26,5% |
| [NIST Scale](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm) | Không ghi ngày; thống kê | 02/11/2026 | Mẫu số n−1, đuôi phân bố |
| [Goldberg & Mahmoud](https://arxiv.org/abs/1404.7493) | 29/04/2014, sửa21/09/2016 v5 | 02/11/2026 | Drawdown khác thước đo khác |
| [SEC Liquidity](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability) | Không ghi ngày; Hoa Kỳ | 02/11/2026 | Bán nhanh, tác động giá |
| [ICI Q4/2010](https://www.ici.org/system/files/attachments/pdf/ret_10_q4_data.pdf) | 04/2011; lợi suất1996–2010 | 02/11/2026 | Đối chiếu thứ cấp S&P−37,0%,+26,5%; không thay nguồn gốc |
| [SEC SPDR prospectus](https://www.sec.gov/Archives/edgar/data/884394/000095012309063860/y02598ae497.htm) | 18/11/2009; chỉ số đến2008 | 02/11/2026 | Phân biệt lợi suất giá không tái đầu tư cổ tức |

## Phát hiện

| Mức | Phần | Phát hiện / bằng chứng | Khắc phục / trạng thái |
|---|---|---|---|
| Thấp | Metadata Berkshire | Bảng ghi phần trăm S&P có cổ tức, không trực tiếp ghi tiền tệ ở cột. “Cơ sở USD” là chú giải suy ra từ chỉ số, không phải đơn vị của tỷ lệ phần trăm | Khi biên tập sau, có thể ghi thị trường Hoa Kỳ và % tổng lợi suất; không chặn |
| — | Chuỗi và công thức | Năm mốc tạo bốn lợi suất; n−1 đúng NIST, drawdown đúng đỉnh lũy kế | ĐẠT |
| — | Sổ mua | Khớp1.000/1.200, không gán giá cho200 chưa khớp; mẫu số hụt giá là phần đã bán | ĐẠT |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

`PHÉP_TÍNH`: lợi suất10%,−20%,15%,5%; ghép6,26%. Trung bình0,025; tổng bình phương độ lệch0,0725; căn(0,0725/3)=0,1554563. Drawdown0%,0%,−20%,−8%,−3,4%. Phục hồi110/88−1=25%;110/106,26−1≈3,5197%. S&P100×0,63×1,265=79,695; toàn kỳ−20,305%; hồi phục100/63−1≈58,7302%.

Sổ mua:200×20.000+300×19.800+500×19.000=19.440.000VND; hụt560.000/20.000.000=2,8%; thiếu1.560.000 so nhu cầu21triệu. Giảm20% rồi tăng20% cho96 từ100. Đã rà cả10đáp án: số học khớp, các câu thiếu dữ kiện không tự điền giả định.

## Hạn chế của lần kiểm duyệt

ICI là đối chiếu thứ cấp; số gốc chủ yếu từ bảng Berkshire. NIST/SEC không hiển thị ngày xuất bản. Không kiểm toán manifest hoặc đánh giá học thực tế. Đây là phương pháp, không xác nhận thanh khoản tương lai. Điều phối tự đối chiếu phép tính trọng yếu; chỉ đổi tiền tố nháp và hai trạng thái vòng đời sau khi đủ hai biên bản, không đổi nội dung chuẩn.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không có nghiêm trọng/cao chưa xử lý; ghi chú thấp lưu lại không chặn theo tiêu chí người dùng đã chấp nhận.
