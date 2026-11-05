# Biên bản phản biện rủi ro — Bài F8

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-05 10:51 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-05 10:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; kiểm giả định phương pháp Chain-Ladder, rủi ro đối tác tái bảo hiểm (fronting/counterparty risk), rủi ro lãi suất nhân thọ (negative spread), giới hạn chuẩn mực VAS so với IFRS 17 và ranh giới an toàn.`
- Báo cáo đích: `learning/lessons/F8-vietnam-insurance-analysis.md`
- SHA-256 nội dung đích: `bea4075e4f56e6c272bc3a15bcee6627f7b8eaec4da6f491beb204ca37ac0e58`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập `risk-bear-reviewer` (Vòng 1 và Vòng 2) ngày 05/11/2026 trên bản nháp cố định (`shasum -a 256`: `e73e96ff9835c254abc0c6eeb2bba1548a70080ec5b0f446e2c6bc7e5a37a12f`); người kiểm không sửa bài.

## Các nguồn Internet và hồ sơ gốc đã đối chiếu trong lượt kiểm duyệt

| Nguồn / URL | Ngày xuất bản / kỳ / phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Bộ Tài chính — VBHN 44/2026/VBHN-TT-BTC](https://mof.gov.vn/) | Ký 29/09/2026; Việt Nam | 2026-11-05 | Phản chứng giới hạn phương pháp `Chain-Ladder` (`Điều 36`), trần lãi suất kỹ thuật nhân thọ (`Điều 38–40`) và hệ số giảm trừ tài sản `Mẫu 7-PNT` |
| [BCTC hợp nhất kiểm toán năm 2025 của `BVH`, `PVI`, `BIC`](https://www.baoviet.com.vn/) | Kỳ 31/12/2025; Việt Nam; VAS | 2026-11-05 | Phản chứng rủi ro tập trung phải thu tái bảo hiểm tại `PVI` (`21.614,45 tỷ đồng`, gấp `2,53` lần VCSH) và biên thanh toán nhân thọ sát ngưỡng của `BVH` (`107%`) |

## Phát hiện và kiểm tra

1. **Đã xử lý đầy đủ các phản chứng và góc khuất kế toán `VAS`:**
   - **Điểm mù của `Chain-Ladder` trong năm siêu bão (`Yagi 09/2024`) và lạm phát chi phí sửa chữa:** Đã chỉ rõ giả định bất biến tốc độ giải quyết bồi thường của `Chain-Ladder` bị phá vỡ khi xảy ra thảm họa diện rộng hoặc thay đổi quy trình giám định, cần kết hợp `Bornhuetter-Ferguson (BF)`.
   - **Rủi ro đối tác tái bảo hiểm (`Reinsurance Counterparty Risk`) và ảo giác `Combined Ratio` sau hoa hồng nhượng tái:** Đã phân tích trường hợp `PVI` có Tài sản tái bảo hiểm `21.614,45 tỷ đồng` (gấp `2,53` lần VCSH `8.533,91 tỷ đồng`) và việc `Combined Ratio` trước hoa hồng nhượng tái của `PVI` là `106,06%` (lỗ gộp trước khi cộng `1.337,61 tỷ đồng` hoa hồng nhượng tái).
   - **Bẫy lệch kỳ hạn và chênh lệch lãi suất âm (`Negative Spread`) trong nhân thọ:** Đã dẫn chứng trực tiếp từ `BVH` (`FY2025`) với `16.544,35 tỷ đồng` dự phòng đảm bảo lãi suất cam kết tối thiểu và Biên KNTT mảng nhân thọ ở mức `107%` (`9.921,65 / 9.269,95 tỷ đồng`).
   - **Độ vênh giữa Biên KNTT hệ số cố định (`Solvency I`) và vốn `RBC` (`01/01/2028`):** Đã nêu rõ vì sao công thức $\max(25\%\text{ NWP},\; 12,5\%\text{ GWP})$ hiện hành phạt ngược doanh nghiệp tăng phí thận trọng và chưa phản ánh đầy đủ rủi ro kỳ hạn tài sản — nợ.
2. **Ranh giới an toàn:** Không đưa khuyến nghị mua/bán cổ phiếu `BVH`, `PVI`, `BIC`; gắn nhãn nhận định và nêu rõ các điều kiện làm luận điểm mất hiệu lực.

## Hạn chế của lần kiểm duyệt

Không truy cập được bảng tam giác phát triển bồi thường nội bộ chi tiết theo từng nghiệp vụ của từng công ty bảo hiểm Việt Nam do `VAS` không bắt buộc công bố công khai toàn bộ bảng tam giác trên thuyết minh BCTC.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả.
