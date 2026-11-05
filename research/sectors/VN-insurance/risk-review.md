# Biên bản phản biện rủi ro: Ngành Bảo hiểm Việt Nam (VN-insurance)

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-05 11:56 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: Cấu trúc cạnh tranh, chuỗi giá trị, cú sốc thể chế 2023–2025 (Luật KDBH 31/VBHN-VPQH, Nghị định 46/2023/NĐ-CP, Thông tư 67/2023/TT-BTC / 44/VBHN-BTC), bảng so sánh kinh tế đơn vị BVH – PVI – BIC (FY2025 đã kiểm toán), đối chiếu toàn cầu (GEICO/Berkshire), chu kỳ lãi suất/thiên tai/tái bảo hiểm và điều kiện làm luận điểm ngành mất hiệu lực.
- Báo cáo đích: `research/sectors/VN-insurance/report.md`
- SHA-256 nội dung đích: `795fa838ac2d630d3113c949c71bf55e725709df06cd19497fb38e97f111b97f`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `risk_bear_reviewer` ([conversation](conversation://4a892290-8931-423e-ab78-33d09d4a1966)); không tự thay kết luận.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| `https://vanban.chinhphu.vn/?pageid=27160&docid=215622` & `docid=208265` & `docid=217205` | Luật KDBH `31/VBHN-VPQH`, Nghị định `46/2023/NĐ-CP`, Thông tư `67/2023/TT-BTC (44/VBHN-BTC)` | 2026-11-05 | Kiểm tra rào cản vốn tối thiểu (Điều 35 NĐ 46), trần hoa hồng (Điều 51 TT 67), quy tắc Bancassurance `±60 ngày` (Điều 53, 62) và lộ trình `RBC 01/01/2028` (Điều 156/157 Luật KDBH) |
| Công bố BCTC hợp nhất kiểm toán FY2025 của `BVH`, `PVI`, `BIC` & `Berkshire Hathaway 2025 10-K` | FY2025 (kết thúc 31/12/2025) | 2026-11-05 | Đối chiếu chéo các chỉ số rủi ro ngành: dự phòng đảm bảo lãi suất cam kết của `BVH` (`16.544,35 tỷ VND`), tài sản tái bảo hiểm của `PVI` (`21.614,45 tỷ VND` = `2,53x` VCSH), và bồi thường bão lũ Q4/2025 của `BIC` |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| `TRUNG_BÌNH` | Cú sốc thể chế 2023–2025 — Lộ trình `RBC 01/01/2028` (dòng 52–55, 80) | Báo cáo đã chỉ ra rất đúng việc `BVH` Nhân thọ có biên khả năng thanh toán `107%` dưới chuẩn `Solvency I` hiện hành. Tuy nhiên, góc nhìn phản biện nhấn mạnh thêm rằng khi chuyển sang `RBC` từ `01/01/2028`, yêu cầu vốn sẽ tính thêm hệ số rủi ro thị trường (`Market Risk Charge` trên chênh lệch kỳ hạn tài sản - nợ phải trả và đòn bẩy Repo `53.229,07 tỷ VND` của `BVH`) cùng hệ số rủi ro tín dụng đối tác tái bảo hiểm (`Counterparty Credit Risk Charge` trên `21.614,45 tỷ VND` tài sản tái bảo hiểm của `PVI`). Do đó, cả những doanh nghiệp có vẻ dư vốn theo `Solvency I` vẫn có thể bị co hẹp tỷ lệ an toàn vốn (`CAR`) khi áp dụng `RBC`. | Nguyên tắc cấu phần rủi ro trong Điều 108, 109, 156 Luật KDBH `31/VBHN-VPQH` và thực tiễn chuyển đổi `Solvency I` sang `RBC` tại châu Á. | Ghi nhận lưu ý này vào biên bản phản biện rủi ro để người đọc theo dõi khi Bộ Tài chính ban hành thông tư hướng dẫn hệ số `RBC`. | `ĐÃ_GHI_NHẬN` |
| `THẤP` | Mục So sánh với chuẩn mực toàn cầu: `GEICO` (dòng 85) | Dòng 85 trích số `GEICO` theo bảng phân tích chi phí khai thác (`NEP = 44.096 triệu USD`, `CR = 86,81%`), lệch nhẹ với bảng tóm tắt `GEICO` tại trang `K-36` `Berkshire FY2025 10-K` (`NEP = 44.481 triệu USD`, `CR = 84,66%`). Dù vậy, số `Float 176 tỷ USD`, lãi khai thác hợp nhất sau thuế `7.258 triệu USD` và kết luận cấu trúc hoàn toàn không thay đổi. | `Berkshire Hathaway FY2025 Form 10-K` (trang `K-35`, `K-36`). | Ghi chú vào `risk-review.md`; không ảnh hưởng đến bất kỳ phép tính hay kết luận nào của 3 doanh nghiệp Việt Nam. | `ĐÃ_GHI_NHẬN` |

## Kiểm tra phép tính và bằng chứng trái chiều

- Toàn bộ số liệu và tỷ số tài chính của `BVH`, `PVI`, `BIC` trong bảng so sánh ngang (dòng 61–80) khớp 100% với BCTC hợp nhất kiểm toán FY2025 và mô-đun `calc_insurance_profiles.py`. Báo cáo đã trình bày minh bạch cả hai cách tính `Combined Ratio` (trước và sau hoa hồng nhượng tái; có và không có chi phí quản lý doanh nghiệp `G&A`).
- Báo cáo không rơi vào lỗi tô hồng ngành; đã bóc tách thẳng thắn cú xoay trục lợi nhuận kế toán của `BVH` nhờ hoàn nhập dự phòng lãi suất tối thiểu (`+197,39 tỷ VND` năm 2025 so với trích thêm `-3.081,91 tỷ VND` năm 2024), cú sụt giảm `-58,70%` lãi gộp bảo hiểm Q4/2025 của `BIC` vì bão lũ và áp lực cứng hóa phí tái bảo hiểm quốc tế. Ba điều kiện làm luận điểm ngành mất hiệu lực được lượng hóa rõ ràng.

## Hạn chế của lần kiểm duyệt

- Báo cáo đã tự công khai rõ giới hạn `CHƯA_BIẾT` về Niên giám thống kê thị trường bảo hiểm năm 2025 bản chi tiết từng doanh nghiệp chưa niêm yết của Cục Quản lý, giám sát bảo hiểm.

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Đủ điều kiện xuất bản kèm biên bản phản biện rủi ro.
