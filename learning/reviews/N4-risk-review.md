# Biên bản phản biện rủi ro: Bài N4 — Đợt 4, nhóm 1

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 14:47 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 14:28 Asia/Ho_Chi_Minh`
- Phạm vi: bản chụp cố định của N4, nhận định và phép tính trọng yếu, bài tập và đáp án.
- Báo cáo đích: `learning/lessons/N4-time-value-returns.md`
- SHA-256 nội dung đích: `96ac0f808b21075be1a9a60b769e7e23f1f7ef36dd38fc47d8134297606f41d4`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính chép tóm lược kết quả nhánh độc lập cuối, không thay kết luận. Thời điểm trên là lúc chốt sổ sau khi nhận kết quả. Toàn văn nhánh được trả trong cuộc trao đổi ngày 02/11/2026. Tiêu chíĐẠT: không còn nghiêm trọng/cao; trung bình/thấp ghi lại không chặn.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| Nguồn | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [CFPB — lãi kép](https://www.consumerfinance.gov/ask-cfpb/how-does-compound-interest-work-en-1683/) | Cập nhật 07/11/2023; USD ví dụ | 02/11/2026 | Phân biệt lãi trả với lãi nhập gốc |
| [California BOE — bài1](https://www.boe.ca.gov/info/tvm/lesson1.html) | Tài liệu giáo dục Hoa Kỳ; ngày xuất bản chưa thấy | 02/11/2026 | Lãi kép, PV/FV |
| [California BOE — bài9](https://www.boe.ca.gov/info/tvm/lesson9.html) | Tài liệu giáo dục Hoa Kỳ; ngày xuất bản chưa thấy | 02/11/2026 | Tần suất ghép lãi |
| [BLS — CPIFAQ](https://www.bls.gov/cpi/questions-and-answers.htm) | Hoa Kỳ; ngày cập nhật chưa xác định | 02/11/2026 | Rổ giá và giới hạn áp dụng cá nhân |
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Nộp 31/10/2025; FY27/09/2025; USD; US GAAP | 02/11/2026 | Cổ phần trên bìa hoặc bảng tổng lợi suất |

## Phát hiện

| Mức | Phát hiện | Cách khắc phục / trạng thái |
|---|---|---|
| Trung bình | Dữ kiện thiếu trong ví dụ trả lãi tháng dễ bị hiểu thành lỗi số học | 125,44 triệu có thể khớp 12% hiệu dụng năm ghép năm; nên phân biệt dữ kiện thiếu với phép tính sai. Bài đã giải thích mơ hồ nên không chặn. |
| Thấp | Lợi suất thực chỉ áp cùng kỳ/đồng tiền/rổ giá phù hợp | Bài cảnh báo CPI Hoa Kỳ không đại diện hộViệt Nam; giữ giới hạn khi rời ví dụ giả định. Không chặn. |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Không thấy lỗi nghiêm trọng/cao về PV/FV, tỷ lệ ghép, lợi suất thực, góp tiền hay đổi tiền tệ. Apple 234/217 được nguồn SEC ghi là tổng lợi suất tái đầu tư, không cộng cổ tức lần nữa. Phản ví dụ+40% rồi−13,57% cho cùngCAGR 10% giúp tránh coiCAGR là đường đi từng năm.

## Hạn chế của lần kiểm duyệt

Nhánh chỉ đọc bản chụp `data/raw/payloads/lesson-review-2026-11-02-1428/N4-time-value-returns.md`; không thấy kết quả nhánh còn lại và không sửa tệp. Hash là nội dung chuẩn theo `canonical_report`, không phải SHA-256 byte thô. Giá trị do Apple/Vanguard công bố có một nguồn gốc là chính hồ sơ nhà phát hành; bản sao không được tính là nguồn độc lập thứ hai. Nguồn giáo dục có phạm vi thị trường riêng; chưa đánh giá hiệu quả học thực tế.

Điều phối kiểm bài trên đĩa khớp hash bản chụp trước khi chốt; sau kiểm chỉ bỏ tiền tố nháp và đổi hai dòng trạng thái vòng đời, không đổi nội dung chuẩn. Mọi sửa nội dung sau đó làm biên bản hết hiệu lực.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không có lỗi nghiêm trọng/cao chưa xử lý; giữ các phát hiện trung bình/thấp và giới hạn nêu trên.
