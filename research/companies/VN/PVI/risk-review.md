# Biên bản phản biện rủi ro: Công ty Cổ phần PVI (PVI)

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-05 11:56 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: Mô hình bảo hiểm công nghiệp & tái bảo hiểm của PVI, tỷ lệ giữ lại (32,39%), sự phân hóa giữa mảng bảo hiểm gốc (EBT -41,66%) và mảng tái bảo hiểm (EBT gấp 8,80 lần), đòn bẩy đối tác tái bảo hiểm (Tài sản tái bảo hiểm 21.614,45 tỷ VND + Phải thu tái bảo hiểm 1.470,03 tỷ VND = 2,70x VCSH), điều chỉnh hồi tố năm 2024 theo Kiểm toán Nhà nước, 3 kịch bản định giá Justified P/B và điều kiện làm luận điểm mất hiệu lực.
- Báo cáo đích: `research/companies/VN/PVI/report.md`
- SHA-256 nội dung đích: `a964f9640c703ba69c77a7bbf93d95f9adb119b4d43c63d51766211a3134177c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `risk_bear_reviewer` ([conversation](conversation://4a892290-8931-423e-ab78-33d09d4a1966)); không tự thay kết luận.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| `https://static2.vietstock.vn/data/HNX/2025/BCTC/VN/NAM/PVI_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf` | BCTC hợp nhất kiểm toán FY2025 của `PVI` (PwC Việt Nam ký 15/02/2026) | 2026-11-05 | Đối chiếu Tài sản tái bảo hiểm (`21.614,45 tỷ VND`, TM 5 tr. 32), phải thu tái bảo hiểm (`3.433,80 tỷ VND`, TM 6 tr. 32), báo cáo bộ phận (TM 31 tr. 51) và thuyết minh điều chỉnh hồi tố năm 2024 (TM 36 tr. 55–57) |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| `TRUNG_BÌNH` | Mục Chất lượng BCTC & Rủi ro — Độ trễ `IBNR` của mảng Nhận tái bảo hiểm tăng nóng `+82,87%` (dòng 71–81, 111–113) | Báo cáo đã phát hiện rất sắc sảo rằng lợi nhuận trước thuế bộ phận Bảo hiểm phi nhân thọ gốc giảm `-41,66%` (`129,57 tỷ VND`), còn toàn bộ tăng trưởng đến từ bộ phận Tái bảo hiểm (`EBT` tăng `8,80 lần` lên `443,01 tỷ VND` khi phí nhận tái tăng `+82,87%` lên `10.498,98 tỷ VND`), đồng thời chỉ ra việc điều chỉnh hồi tố năm 2024 do độ trễ chứng từ đối chiếu (`Bordereaux`). Dưới góc nhìn phản biện định phí (`Actuarial Bear Case`), trong nghiệp vụ nhận tái bảo hiểm quốc tế theo hợp đồng cố định (`Treaty Inward`), thông báo tổn thất thực tế thường đến trễ 4–8 quý. Do đó, biên lợi nhuận rất cao ghi nhận ở năm đầu tăng trưởng nóng (2025) có rủi ro bị điều chỉnh giảm vào năm 2026–2027 khi các bảng kê tổn thất (`Loss Bordereaux`) từ nước ngoài gửi về đầy đủ (`Adverse Reserve Development`). | TM 23 (tr. 46), TM 31 (tr. 51) và TM 36 (tr. 55–57) BCTC hợp nhất FY2025 của `PVI`. | Ghi nhận rủi ro phát triển tổn thất bất lợi (`Adverse Development`) có độ trễ 1–2 năm của danh mục nhận tái bảo hiểm mới mở rộng vào `risk-review.md`. | `ĐÃ_GHI_NHẬN` |
| `THẤP` | Mục Phân bổ vốn — Tỷ lệ chi trả cổ tức tiền mặt `86,36%` vs. nhu cầu tăng vốn công ty con (dòng 91–94) | Công ty mẹ `PVI` chi trả tới `86,36%` LNST công ty mẹ làm cổ tức tiền mặt (`737,86 tỷ VND`), trong khi vừa phải tăng vốn điều lệ cho `PVI Insurance` lên `4.320 tỷ VND` (T9/2025) và `5.000 tỷ VND` (T1/2026) để đỡ khối lượng phí nhận tái và tài sản tái bảo hiểm tăng mạnh. Nếu quy mô nhận tái tiếp tục tăng hoặc khi áp dụng `RBC 2028` đánh trọng số rủi ro vào `25.048,25 tỷ VND` phơi nhiễm tái bảo hiểm, tỷ lệ chi trả cổ tức tiền mặt `>80%` có thể phải điều chỉnh giảm để giữ lại vốn. | TM 1 (tr. 10), TM 19b (tr. 43), TM 37 (tr. 64) BCTC hợp nhất FY2025 của `PVI`. | Ghi chú vào `risk-review.md`. | `ĐÃ_GHI_NHẬN` |

## Kiểm tra phép tính và bằng chứng trái chiều

- Toàn bộ số liệu trong `pvi_metrics()` và `pvi_scenarios()` của `calc_insurance_profiles.py` khớp tuyệt đối với BCTC kiểm toán FY2025. Kịch bản Bất lợi (`Bear`) đặt `ROE = 11,0% < k_e = 11,5%`, `g = 4,5%`, định giá `P/B hợp lý = 0,9286x` (`7.599,41 tỷ VND` hay `32.442,58 VND/CP`, thấp hơn sổ sách `-7,1%`), phản ánh hợp lý kịch bản chu kỳ phí tái bảo hiểm hạ nhiệt kèm chi phí trích lập dự phòng phải thu tái bảo hiểm khó đòi.
- Báo cáo không bị đánh lừa bởi con số lợi nhuận hợp nhất tăng `+29,27%`; trái lại đã bóc tách rõ: (1) tổng phơi nhiễm đối tác tái bảo hiểm (`21.614,45 tỷ` tài sản tái bảo hiểm + `3.433,80 tỷ` phải thu tái bảo hiểm = `25.048,25 tỷ VND`, gấp `2,93 lần` VCSH) với bài kiểm tra sức chịu đựng nếu `2%–3%` phát sinh tranh chấp/quá hạn sẽ lấy đi `500–750 tỷ VND` `EBT`; (2) `Combined Ratio` tính đủ G&A trước hoa hồng nhượng tái lên tới `117,02%` (phụ thuộc vào `1.337,61 tỷ VND` hoa hồng nhượng tái để kéo về `99,50%`); và (3) khoản phải thu khó đòi lịch sử `275,92 tỷ VND` tại `PVI AM` (TM 8 tr. 34).

## Hạn chế của lần kiểm duyệt

- Báo cáo đã nêu rõ hai điểm `CHƯA_BIẾT` do giới hạn thuyết minh `VAS`: phân bổ chi tiết theo bậc xếp hạng tín nhiệm (`AAA/AA/A/BBB`) của các nhà nhận tái bảo hiểm nắm giữ `21.614,45 tỷ VND` tài sản tái bảo hiểm và bảng tỷ lệ biên khả năng thanh toán riêng lẻ của `PVI Insurance` và `Hanoi Re`.

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Đã lượng hóa đầy đủ rủi ro đối tác tái bảo hiểm (`2,93x` VCSH), rủi ro nhận tái quốc tế tăng nóng và điều kiện làm luận điểm mất hiệu lực.
