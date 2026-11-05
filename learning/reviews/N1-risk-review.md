# Biên bản phản biện rủi ro: Bài N1 — Đợt 4, nhóm 1

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 14:47 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 14:28 Asia/Ho_Chi_Minh`
- Phạm vi: bản chụp cố định của N1, nhận định và phép tính trọng yếu, bài tập và đáp án.
- Báo cáo đích: `learning/lessons/N1-market-basics.md`
- SHA-256 nội dung đích: `227dec97d9b6eeff5fb3a240459dd41c69ced3a5b0727661e540312e478a28d8`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính chép tóm lược kết quả nhánh độc lập cuối, không thay kết luận. Thời điểm trên là lúc chốt sổ sau khi nhận kết quả. Toàn văn nhánh được trả trong cuộc trao đổi ngày 02/11/2026. Tiêu chíĐẠT: không còn nghiêm trọng/cao; trung bình/thấp ghi lại không chặn.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| Nguồn | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [SEC Investor.gov — cổ phiếu](https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks) | Hoa Kỳ; ngày xuất bản không hiển thị | 02/11/2026 | Quyền sở hữu, cổ tức, thanh lý |
| [SEC Investor.gov — từ điển](https://www.investor.gov/introduction-investing/investing-basics/glossary) | Trang hiện hành; ngày xuất bản không hiển thị | 02/11/2026 | Sơ cấp/thứ cấp và vốn hóa |
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Nộp 31/10/2025; FY27/09/2025; USD; US GAAP | 02/11/2026 | Cổ phần trên bìa hoặc bảng tổng lợi suất |
| [Apple Proxy2026](https://www.sec.gov/Archives/edgar/data/320193/000130817926000008/aapl014016-def14a.htm) | 08/01/2026; số cổ phần 02/01/2026 | 02/11/2026 | Phản chứng cho mẫu số cổ phần được coi là hiện hành |
| [SEC — loại lệnh](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders) | Hoa Kỳ; ngày xuất bản không hiển thị | 02/11/2026 | Giá chào, khớp và giới hạn lệnh |
| [HOSE — hướng dẫnT2/2026](https://staticfile.hsx.vn/Uploads/UploadDocuments/2453338/HTGD_Quy%20dinh%20can%20biet%20khi%20GDCK%20tren%20HOSE_T2.2026.pdf) | BảnT2/2026; Việt Nam | 02/11/2026 | Không áp sổ lệnh giả định thành quy tắcHOSE |

## Phát hiện

| Mức | Phát hiện | Cách khắc phục / trạng thái |
|---|---|---|
| Thấp | Mẫu số Apple là lịch sử, không phải hiện hành | Proxy ghi 14.697.926.000 cổ phần 02/01/2026; bài đã gắn mẫu số 17/10/2025 và giá 250 giả định. Giữ cảnh báo sát phép nhân; không chặn. |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Không hứa chia cổ tức hoặc trả đủ nợ. Tiền cổ phần mới/cũ tách đúng; vốn hóa tăng không tự cấp tiền cho công ty. Các phép chia tỷ lệ sở hữu, vốn hóa, EV và sổ lệnh khớp môđun. Quy tắc HOSE có các cơ chế riêng; bài đã ghi sổ lệnh hư cấu không mô tảHOSE. Không dùng vốn hóa để chứng minh giá trị hợp lý.

## Hạn chế của lần kiểm duyệt

Nhánh chỉ đọc bản chụp `data/raw/payloads/lesson-review-2026-11-02-1428/N1-market-basics.md`; không thấy kết quả nhánh còn lại và không sửa tệp. Hash là nội dung chuẩn theo `canonical_report`, không phải SHA-256 byte thô. Giá trị do Apple/Vanguard công bố có một nguồn gốc là chính hồ sơ nhà phát hành; bản sao không được tính là nguồn độc lập thứ hai. Nguồn giáo dục có phạm vi thị trường riêng; chưa đánh giá hiệu quả học thực tế.

Điều phối kiểm bài trên đĩa khớp hash bản chụp trước khi chốt; sau kiểm chỉ bỏ tiền tố nháp và đổi hai dòng trạng thái vòng đời, không đổi nội dung chuẩn. Mọi sửa nội dung sau đó làm biên bản hết hiệu lực.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không có lỗi nghiêm trọng/cao chưa xử lý; giữ các phát hiện trung bình/thấp và giới hạn nêu trên.
