# Biên bản phản biện rủi ro: H3 — Đợt 4, nhóm 2

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 15:43 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Phạm vi: toàn bản chụp, bài tập/đáp án, giả định an toàn và phép tính; đọc mô hình và test liên quan.
- Báo cáo đích: `learning/lessons/H3-risk-volatility-drawdown-liquidity.md`
- SHA-256 nội dung đích: `31f86268818194f8cb7b1bb9ad0380560e61d78da5afb068e5b91b9902e091ab`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Điều phối ghi kết quả nhánh độc lập `h3_risk_final`, giữ kết luận và phát hiện. Nhánh chỉ đọc bản chụp `data/raw/payloads/learning-wave4-group2-snapshot-2026-11-02-1541/H3-risk-volatility-drawdown-liquidity.md`, không đọc bài khác, learning/reviews hay kết quả nhánh kiểm nguồn; xác nhận hash chuẩn bằng chuẩn hóa, không hash byte thô. Toàn văn nhánh trả trong cuộc trao đổi02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [Berkshire thư2024](https://www.berkshirehathaway.com/letters/2024ltr.pdf) | 22/02/2025; PDF15, S&P2008–2009 | 02/11/2026 | −37,0%,+26,5% có cổ tức |
| [SEC Liquidity](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability) | Không ghi ngày; Hoa Kỳ | 02/11/2026 | Khả năng bán/tác động giá |
| [NIST Scale](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm) | Không ghi ngày | 02/11/2026 | Độ lệch chuẩn và giới hạn |
| [Goldberg & Mahmoud](https://arxiv.org/abs/1404.7493) | 2014, sửa21/09/2016 v5 | 02/11/2026 | Drawdown và biến động không đồng nhất |
| [SEC DERA Market Liquidity](https://www.sec.gov/files/access-to-capital-and-market-liquidity-study-dera-2017.pdf) | 08/2017; Hoa Kỳ | 02/11/2026 | Tốc độ, chi phí, độ sâu không thay nhau |
| [Fed — low-frequency measures](https://www.federalreserve.gov/econres/feds/when-do-low-frequency-measures-really-measure-transaction-costs.htm) | 07/2019, cập nhật09/01/2020 | 02/11/2026 | Đại diện thanh khoản tần suất thấp có thể sai lệch |

## Phát hiện

| Mức | Phần | Phát hiện / tác động | Bằng chứng / khắc phục |
|---|---|---|---|
| Thấp | “Cơ sở USD” | Bảng tỷ lệ S&P không trực tiếp ghi tiền tệ; không làm sai số học | Berkshire PDF15. Khi biên tập sau ghi thị trường/chỉ số Hoa Kỳ hoặc nêu suy ra; không chặn |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

`PHÉP_TÍNH` Chuỗi10%,−20%,15%,5% ghép6,26%; trung bình2,5%; căn(0,0725/3)=15,5456%. Drawdown theo đỉnh0%,0%,−20%,−8%,−3,4%; hồi phục25% hoặc3,52% tùy đáy.100×0,63×1,265=79,695,−20,305% toàn kỳ; từ63 về100 cần58,73%, không bảo đảm sẽ hồi phục.

Sổ mua khớp1.000 thu19,44triệu, còn200 chưa khớp; hụt560.000/20triệu=2,8%. Bài không gán giá cho lượng còn lại và phân biệt tiền khớp với tiền dùng được đúng hạn. Đã rà10đáp án với nội dung/mã, đọc nhưng không chạy test.

NIST cho thấy độ lệch chuẩn nhạy với đuôi; Goldberg–Mahmoud phân biệt drawdown với volatility và nhấn mạnh tương quan chuỗi. SEC DERA cho thấy thanh khoản có nhiều chiều; Fed cảnh báo đại diện tần suất thấp thiếu chính xác. Bài đã giữ các giới hạn, không dùng báo giá đứng yên làm bằng chứng an toàn. Giả định sổ tĩnh chỉ đúng khi lệnh không đổi, không phí và không bảo đảm nhận tiền ngay.

## Hạn chế của lần kiểm duyệt

Không đánh giá tài sản/thị trường thực, quy tắc lô/thanh toán/phí tại Việt Nam hoặc khả năng hiểu bài. Không mở nguồn thứ hai xác minh riêng hai số S&P; bài công khai một nguồn gốc. Không mô phỏng hủy lệnh hoặc thay đổi thanh khoản. Sau kiểm, điều phối chỉ đổi siêu dữ liệu vòng đời; sửa nội dung sau làm biên bản hết hiệu lực.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không nghiêm trọng/cao; lưu một điểm thấp về cách ghi tiền tệ, không chặn.
