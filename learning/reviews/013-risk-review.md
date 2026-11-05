# Biên bản phản biện rủi ro — Bài 013

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-05 10:51 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-05 09:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; kiểm giả định, trường hợp công thức không còn đúng, giới hạn quốc gia/chuẩn kế toán (US GAAP, IFRS 17, VAS), điều kiện bác bỏ luận điểm ngân hàng/bảo hiểm và ranh giới an toàn; tự tìm nguồn phản chứng.`
- Báo cáo đích: `learning/lessons/013-banks-insurers.md`
- SHA-256 nội dung đích: `e3dd723f16ce65b3f20c751b4aecd2f139a80acf97772382cc797eb95abcf7f2`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập `risk-bear-reviewer` (Vòng 1 và Vòng 2) ngày 05/11/2026 trên bản nháp cố định (`shasum -a 256`: `0ce17d31bca8685f53733e6e4dd34843ba3ce08a2dc8233b145b59e14387841f`); người kiểm không sửa bài.

## Các nguồn Internet và hồ sơ gốc đã đối chiếu trong lượt kiểm duyệt

| Nguồn / URL | Ngày xuất bản / kỳ / phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Berkshire Hathaway Inc. — FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1067983/000106798326000009/brka-20251231.htm) | Nộp 02/03/2026; kỳ 31/12/2025; Hoa Kỳ; US GAAP | 2026-11-05 | Phản chứng về chu kỳ `Float` khi `GEICO` lỗ nghiệp vụ `-$1.880M` năm 2022 (`Combined Ratio` = `104,8%`) và rủi ro tái bảo hiểm thảm họa |
| [JPMorgan Chase & Co. — FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/19617/000001961726000289/jpm-20251231.htm) | Nộp 13/02/2026; kỳ 31/12/2025; Hoa Kỳ; US GAAP | 2026-11-05 | Phản chứng độ trễ tín dụng, chênh lệch kỳ hạn tài sản — nợ (`HTM` unrealized losses) và giới hạn của `PPOP` |

## Phát hiện và kiểm tra

1. **Đã xử lý triệt để các rủi ro nhận thức và phản chứng:**
   - **Ảo tưởng `Float` miễn phí vĩnh viễn:** Đã nêu rõ phản chứng thực nghiệm ngay tại `GEICO` năm `2022` lỗ nghiệp vụ trước thuế `-$1.880 triệu USD` (`Combined Ratio` = `104,8%`) do lạm phát phụ tùng và chi phí sửa chữa xe hơi, cũng như các năm thảm họa thiên tai lớn (`Katrina 2005`, `2017`) khiến `Cost of Float` chuyển dương.
   - **Bẫy dự phòng bồi thường đuôi dài (`Long-tail IBNR` & `Social Inflation`):** Đã chứng minh cơ chế trích thiếu dự phòng tạo `ROE` ảo và bào mòn `Book Value` thực tế qua công thức điều chỉnh `reserve_understatement_adjustment()` và Bài tập 6.
   - **Rủi ro kỳ hạn (`Asset-Liability Mismatch`) và rút tiền hàng loạt (`Bank Run` / `Surrender Run`):** Đã cảnh báo trường hợp trái phiếu nắm giữ đến ngày đáo hạn (`HTM`) lỗ chưa thực hiện khi lãi suất tăng vọt (bài học `SVB 2023`) và làn sóng rút giá trị hoàn lại trong bảo hiểm nhân thọ.
   - **Giới hạn thể chế giữa `US GAAP`, `IFRS 17` và `VAS`:** Đã tách bạch `Berkshire Hathaway` báo cáo theo `US GAAP` (nhánh `LDTI` cho hợp đồng dài hạn), `IFRS 17` dùng `CSM` và Việt Nam đang áp dụng `VAS` (`Thông tư 232/2012/TT-BTC`).
2. **Ranh giới an toàn:** Không có khuyến nghị mua/bán/nắm giữ cổ phiếu; mọi nhận định trọng yếu đều gắn nhãn `SỰ_THẬT`, `PHÉP_TÍNH`, `SUY_LUẬN`, `KỊCH_BẢN` và có điều kiện làm luận điểm mất hiệu lực rõ ràng.

## Hạn chế của lần kiểm duyệt

Không đánh giá hiệu quả sư phạm thực tế trên người học; các kịch bản căng thẳng (`Stress Test`) trong bài là mô phỏng phục vụ học tập, không thay thế kiểm định sức chịu đựng vốn (`CCAR` / `Solvency II`) của cơ quan quản lý.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả.
