# Biên bản phản biện rủi ro — Bài P4

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-05 10:51 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-05 10:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; kiểm giả định chiến lược BTID (Buy Term and Invest the Difference), rủi ro từ chối tái tục (renewability risk), rủi ro lạm phát y tế của thẻ sức khỏe rời, bẫy tăng COI ở tuổi già và ranh giới an toàn tư vấn tài chính cá nhân.`
- Báo cáo đích: `learning/lessons/P4-personal-insurance-contracts-and-costs.md`
- SHA-256 nội dung đích: `949f9d76dfc449ee837c195859946a90427ad82db16e4f077b953472aef3ca51`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập `risk-bear-reviewer` (Vòng 1 và Vòng 2) ngày 05/11/2026 trên bản nháp cố định (`shasum -a 256`: `ba6c48f5688b2e92598779bb8f5cbc9f5fe99167461567661fc6631acf017cf7`); người kiểm không sửa bài.

## Các nguồn Internet và hồ sơ gốc đã đối chiếu trong lượt kiểm duyệt

| Nguồn / URL | Ngày xuất bản / kỳ / phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Bộ Tài chính — VBHN 44/2026/VBHN-TT-BTC](https://mof.gov.vn/) | Ký 29/09/2026; Việt Nam | 2026-11-05 | Phản chứng cấu trúc phí `UL`/`ILP` (`Điều 22`), bảng minh họa (`Mẫu 22-NT`, `23-NT`) và quy định kênh `Bancassurance` (`Điều 53`) |
| [Văn phòng Quốc hội — Luật Kinh doanh bảo hiểm (31/VBHN-VPQH) & Nghị định 46/2023/NĐ-CP](https://quochuoi.vn/) | Hiệu lực 01/01/2023 & 01/07/2023; Việt Nam | 2026-11-05 | Phản chứng rủi ro vô hiệu hợp đồng do đại lý kê khai sai (`Điều 22 Luật KDBH`) và giới hạn trần `200 triệu đồng/hợp đồng` của Quỹ bảo vệ người được bảo hiểm (`Điều 95 NĐ 46`) |

## Phát hiện và kiểm tra

1. **Đã xử lý đầy đủ các phản chứng và điều kiện làm chiến lược `BTID` thất bại:**
   - **Rủi ro thiếu kỷ luật tiết kiệm — đầu tư (`Behavioral Failure`) và thua lỗ đầu tư:** Đã cảnh báo rõ trong Mục 2.4 và Mục 3.4 rằng chiến lược `BTID` chỉ vượt trội khi phần tiền chênh lệch thực sự được đầu tư kỷ luật vào tài sản sinh lời dài hạn, không bị tiêu dùng mất hoặc đầu cơ thua lỗ.
   - **Rủi ro từ chối tái tục (`Renewability Risk`) và tăng phí của thẻ sức khỏe 1 năm:** Đã phân biệt rõ hợp đồng nhân thọ dài hạn (cam kết tái tục) với thẻ sức khỏe phi nhân thọ 1 năm (có thể tăng phí mạnh hoặc từ chối tái tục sau năm phát sinh bệnh nặng).
   - **Bẫy hủy hợp đồng `UL` cũ đã đóng qua năm thứ 4–5:** Đã chứng minh bằng số liệu và Bài tập 9 rằng khi hợp đồng đã đi qua giai đoạn khấu trừ Phí ban đầu nặng nhất (`Năm 1–3`) hoặc người được bảo hiểm đã phát sinh bệnh nền (`Pre-existing Condition`), việc hủy ngang sẽ biến chi phí chìm thành lỗ thật và mất quyền bảo vệ bệnh có sẵn.
   - **Bẫy "Tạm ngưng đóng phí (`Premium Holiday`)" làm mất hiệu lực hợp đồng ở tuổi già:** Đã chỉ rõ cơ chế khấu trừ `COI` tăng theo cấp số nhân từ tuổi `55–60` khiến Giá trị tài khoản về `0` và hợp đồng tự động chấm dứt hiệu lực (`Lapse`).
2. **Ranh giới an toàn:** Bài học không tư vấn mua/hủy một sản phẩm bảo hiểm cá nhân cụ thể; chỉ cung cấp khung pháp lý, công thức toán học và danh mục kiểm tra để người đọc tự thẩm định.

## Hạn chế của lần kiểm duyệt

Không đánh giá quy tắc, điều khoản riêng của từng doanh nghiệp bảo hiểm thương mại ngoài các quy định khung bắt buộc của `Luật KDBH`, `Nghị định 46/2023/NĐ-CP` và `VBHN 44/2026/VBHN-TT-BTC`.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả.
