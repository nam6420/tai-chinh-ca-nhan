# Biên bản kiểm nguồn: Bài N1 — Đợt 4, nhóm 1

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
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
| [SEC staff — từ điển](https://www.sec.gov/resources-small-businesses/glossary) | Cập nhật 28/04/2026 theo nhánh kiểm nguồn | 02/11/2026 | Ngày phiên bản và thuật ngữ |
| [SEC — loại lệnh](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders) | Hoa Kỳ; ngày xuất bản không hiển thị | 02/11/2026 | Giá chào, khớp và giới hạn lệnh |
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Nộp 31/10/2025; FY27/09/2025; USD; US GAAP | 02/11/2026 | Cổ phần trên bìa hoặc bảng tổng lợi suất |
| [CFA Institute — EV](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/market-based-valuation-price-enterprise-value-multiples) | Chương trình 2026; ngày phát hành cụ thể chưa xác định | 02/11/2026 | EV đầy đủ so với mô hình giản lược |
| [SIFMA — thị trường vốn](https://www.sifma.org/wp-content/uploads/2024/09/SIFMA-Insights-Primer_Capital-Markets_FINAL.pdf) | 09/2024; nguồn hiệp hội ngành Hoa Kỳ | 02/11/2026 | Sơ cấp/thứ cấp |

## Phát hiện

| Mức | Phát hiện | Cách khắc phục / trạng thái |
|---|---|---|
| Trung bình | Bảng nguồn ghi ngày SEC Glossary 02/02/2024; trang mở hiện ghi 28/04/2026 | Nội dung thuật ngữ vẫn đúng; cập nhật ngày/loại trang SEC staff khi sửa tiếp. Không chặn. |
| Thấp | Bảng nguồn ghép EV vào Investor.gov quá rộng | Investor.gov không có mục EV; CFA được dẫn riêng tại phần EV. Nên phân vai nguồn chính xác hơn, không chặn. |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Luồng tiền hỗn hợp:200.000×10.000−100 triệu=1,9 tỷ cho công ty,50.000×10.000=0,5 tỷ cho cổ đông; tổng tiền người mua 2,5 tỷ. Sổ bán 300×20.100+100×20.300=8.060.000 đồng, bình quân 20.150. Mộc vốn hóa 1.000 tỷ, EVgiản lược 1.250 tỷ. Apple 14.776.353.000×250=3.694.088.250.000 USD; giá 250 hư cấu, mẫu số 17/10/2025. Quyền cổ đông/chủ nợ và sổ lệnh có giới hạn thị trường rõ.

## Hạn chế của lần kiểm duyệt

Nhánh chỉ đọc bản chụp `data/raw/payloads/lesson-review-2026-11-02-1428/N1-market-basics.md`; không thấy kết quả nhánh còn lại và không sửa tệp. Hash là nội dung chuẩn theo `canonical_report`, không phải SHA-256 byte thô. Giá trị do Apple/Vanguard công bố có một nguồn gốc là chính hồ sơ nhà phát hành; bản sao không được tính là nguồn độc lập thứ hai. Nguồn giáo dục có phạm vi thị trường riêng; chưa đánh giá hiệu quả học thực tế.

Điều phối kiểm bài trên đĩa khớp hash bản chụp trước khi chốt; sau kiểm chỉ bỏ tiền tố nháp và đổi hai dòng trạng thái vòng đời, không đổi nội dung chuẩn. Mọi sửa nội dung sau đó làm biên bản hết hiệu lực.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không có lỗi nghiêm trọng/cao chưa xử lý; giữ các phát hiện trung bình/thấp và giới hạn nêu trên.
