# Biên bản kiểm nguồn: Bài N5 — Đợt 4, nhóm 1

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 14:47 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 14:28 Asia/Ho_Chi_Minh`
- Phạm vi: bản chụp cố định của N5, nhận định và phép tính trọng yếu, bài tập và đáp án.
- Báo cáo đích: `learning/lessons/N5-portfolio-index-investing.md`
- SHA-256 nội dung đích: `7da5421172af966fc71d0d231e794ec249387c4a6753b7da02730f967d8ede3b`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính chép tóm lược kết quả nhánh độc lập cuối, không thay kết luận. Thời điểm trên là lúc chốt sổ sau khi nhận kết quả. Toàn văn nhánh được trả trong cuộc trao đổi ngày 02/11/2026. Tiêu chíĐẠT: không còn nghiêm trọng/cao; trung bình/thấp ghi lại không chặn.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| Nguồn | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [SEC — phân bổ và đa dạng hóa](https://www.investor.gov/introduction-investing/getting-started/asset-allocation) | Ngày xuất bản không hiển thị | 02/11/2026 | Giới hạn đa dạng hóa, tái cân bằng |
| [SEC — quỹ chỉ số](https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-4) | Ngày xuất bản không hiển thị | 02/11/2026 | Mục tiêu, rủi ro, phí và bám chỉ số |
| [SEC — phí quỹ/ETF](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin) | 23/07/2025; Hoa Kỳ | 02/11/2026 | Chi phí thường xuyên và giao dịch |
| [S&P DJI — phương pháp](https://www.spglobal.com/spdji/en/research-insights/index-literacy/methodology-matters/) | Trang phương pháp; ngày xuất bản không thấy | 02/11/2026 | Trọng số, giá và tổng lợi suất |
| [Vanguard VOO F0968](https://fund-docs.vanguard.com/F0968.pdf) | Chốt 30/09/2026; USD; F0968_092026 | 02/11/2026 | Holdings, NAV/chỉ số, chi phí; URL động |
| [GIPS Handbook](https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/) | Trang chuẩn; ngày phát hành không hiển thị | 02/11/2026 | Ghép hình học và dòng tiền |

## Phát hiện

| Mức | Phát hiện | Cách khắc phục / trạng thái |
|---|---|---|
| Trung bình | Nguồn Fidelity là phương pháp nhà cung cấp, URL20.04 không nêu ngày xuất bản | GIPS có thể dùng làm nguồn chuẩn cho phép ghép hình học khi cập nhật. Phép tính hiện đúng, không chặn. |
| Thấp | Ngày xuất bản một số trang SEC/S&P không hiển thị | Giữ CHƯA_BIẾT, không dùng ngày truy cập hay crawler thay ngày phát hành. Không chặn. |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

50/30/20 với 10/−5/2 cho 3,9%, cuối 103,9 triệu, trọng số 52,94/27,43/19,63%. Nămhai không tái 95,75 triệu, tái miễn phí 96,627 triệu; không suy luôn thắng. VOO30/09/2026 ghi 505/503 cổ phiếu, NAV 12 tháng 15,70% so 15,74%, chi phí 0,03%; số quỹ tái đầu tư, trước thuế, sau chi phí. Chênh−0,04 điểm=−4 điểm cơ bản; không quy toàn bộ cho phí. Phí tĩnh 100 triệu×0,03%=30.000 đồng.

## Hạn chế của lần kiểm duyệt

Nhánh chỉ đọc bản chụp `data/raw/payloads/lesson-review-2026-11-02-1428/N5-portfolio-index-investing.md`; không thấy kết quả nhánh còn lại và không sửa tệp. Hash là nội dung chuẩn theo `canonical_report`, không phải SHA-256 byte thô. Giá trị do Apple/Vanguard công bố có một nguồn gốc là chính hồ sơ nhà phát hành; bản sao không được tính là nguồn độc lập thứ hai. Nguồn giáo dục có phạm vi thị trường riêng; chưa đánh giá hiệu quả học thực tế.

Điều phối kiểm bài trên đĩa khớp hash bản chụp trước khi chốt; sau kiểm chỉ bỏ tiền tố nháp và đổi hai dòng trạng thái vòng đời, không đổi nội dung chuẩn. Mọi sửa nội dung sau đó làm biên bản hết hiệu lực.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không có lỗi nghiêm trọng/cao chưa xử lý; giữ các phát hiện trung bình/thấp và giới hạn nêu trên.
