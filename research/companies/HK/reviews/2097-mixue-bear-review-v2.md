# Biên bản kiểm duyệt: MIXUE Group (2097.HK), đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (bản nháp v2)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `risk-bear-reviewer` (lần kiểm 2). Giữ nguyên kết luận, mức độ và bằng chứng chính. Bên phản biện chạy độc lập, không đọc biên bản kiểm nguồn.

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-25` (agent không có đồng hồ; điều phối viên ghi nhận hoàn tất trước 2026-11-25 08:55 +07). Giá cổ phiếu lấy đến phiên đóng cửa 2026-11-24.
- Chốt dữ liệu lúc: `2026-11-25 08:35 +07` (khớp báo cáo đích v2)
- Phạm vi: toàn bộ v2; F1–F12 của lần 1; đối chiếu nguồn gốc cho các điểm v2 đang để nguồn thứ cấp (Guming, Auntea Jenny, Meituan, Luckin, cổ tức đặc biệt, giá cổ phiếu, quy định nhượng quyền); ngưỡng kịch bản; độ cân bằng; diễn đạt
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-draft-v2-sha-ddcbc7c1.md` (bản sao nguyên vẹn của v2)
- SHA-256 nội dung đích: `ddcbc7c1b55849ad6c4d6fdc068966a6a18d0f5d05b66e8013d83ec3d6916f2d` (do điều phối viên cung cấp; điều phối viên đã tự tính lại và khớp)
- Kết luận: `KHÔNG_ĐẠT` (gần đạt)
- Lỗi nghiêm trọng chưa xử lý: `0` (2 phát hiện CAO, 5 TRUNG_BÌNH, 3 THẤP chưa xử lý)

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

Ngày truy cập 2026-11-25. **Nguồn gốc (do bên phản biện mở; điều phối viên chưa tự mở):** Guming kết quả giữa kỳ (HKEXnews 2026-08-26), Meituan kết quả Q2/H1 (HKEXnews 2026-08-28), Luckin 6-K Q3 2026 (SEC, 2026-11-03), Auntea Jenny báo cáo giữa kỳ (HKEXnews 2026-08-28), thông báo cổ tức đặc biệt Mixue (HKEXnews 2026-08-27), bản sao Eastmoney của kết quả biểu quyết ĐHĐCĐ bất thường 2026-09-30. **Thứ cấp:** Investing.com (giá đến 2026-11-24), KrASIA/Nikkei (2026-11-17), KrASIA (Chagee, 2026-09-04), The Standard (Mixue H1; Meituan), Jiemian và Sina (giai thoại), Tân Hoa Xã (2026-08-12, 7 án điển hình về nhượng quyền), Winshang (dự thảo giám sát nhượng quyền, 2023-06-26). Không mở được: Chagee IR và Finviz (403), Huxiu (405), Nayuki HKEX (chỉ tóm tắt kết quả tìm kiếm).

## Phát hiện lần 1: trạng thái trong v2

`ĐÃ_SỬA`: F1, F2, F4, F6, F7, F8, F9 (lỗi gốc), F12 (phần lớn). `SỬA_CHƯA_ĐỦ`: F3 (tiền đề trợ giá sai mốc và đảo logic; ngưỡng chưa có căn cứ), F5 (bối cảnh ngành toàn nguồn thứ cấp), F10 (giao dịch bên liên quan chưa đọc; câu "đổi CEO ngay trước kỳ lợi nhuận giảm" sai nhãn), F11 (vẫn chỉ nguồn thứ cấp).

## Phát hiện mới trong v2

| Mức độ | Mã | Phát hiện | Bằng chứng | Trạng thái (sau khi sửa v3) |
|---|---|---|---|---|
| CAO | N1 | Tiền đề trợ giá sai mốc và đảo logic: Meituan Q2 2026 có lãi nhưng cả H1 2026 vẫn lỗ hoạt động ≈ −3.778,6 triệu RMB, nên trợ giá hạ nhiệt từ Q2, không phải đầu 2026; việc trợ giá giảm chính là cơ chế của giả thuyết "nền cao" (Guming: doanh số mỗi cửa hàng "broadly stable", bù trừ một phần bởi giảm trợ giá; Luckin Q3 2026 cùng cửa hàng −11,1% "primarily reflecting a high prior-year comparison base due to elevated subsidies"). Nền so sánh H2 2026 có thể khó hơn (Q3 2025 là kỳ trợ giá cao; doanh thu H2 2025 của Mixue +32%), làm kịch bản cơ sở thiếu căn cứ | Meituan HKEX trang 1–4; Guming HKEX trang 17; Luckin SEC 6-K | Đã sửa trong v3 |
| CAO | N2 | Chưa tách "sụt doanh số mỗi cửa hàng mang tính ngành" khỏi "biên và chi phí đặc thù Mixue": Guming doanh thu/cửa hàng ≈ +2,7%, biên gộp 33,4% so với 31,5%, chi phí bán hàng 5,05% so với 5,51%, quản lý 2,79% so với 3,27%; Auntea Jenny 13.155 so với 9.436 cửa hàng; Luckin −11,1%. Doanh thu bán buôn của Mixue và GMV bán lẻ của Guming không cùng loại. Nayuki và Chagee là `CHƯA_XÁC_MINH` | Guming trang 1–2, 16–18; Auntea trang 4–7 | Đã sửa trong v3 (nhưng số gốc do bên phản biện mở, điều phối viên chưa tự mở) |
| TB | N3 | Ngưỡng 5.000 / 11% / 30% chưa có căn cứ, chồng lấn giữa Cơ sở và Bất lợi; chỉ báo chi phí ≥ 11% đã thỏa ngay lúc viết (11,4%); biên gộp H2 2025 ≈ 30,7% nên phần lớn mức giảm xảy ra từ H2 2025 | tái tính | Đã sửa trong v3 |
| TB | N4 | Đóng khung chi phí: phân rã theo hiệu ứng cho biên gộp ≈ 37% mức giảm; nhân sự chỉ giải thích ≈ 27% mức tăng chi phí; chi phí đã bước lên từ H2 2025 và đi ngang; lỗ tỷ giá nằm trong "thu nhập khác, ròng", tác động ròng ≈ 31 triệu | S7 | Đã sửa trong v3 |
| TB | N5 | Rủi ro nước ngoài "4.895 → 4.378" bỏ qua 4.467: đà thu hẹp chậm lại (−8,7% rồi −2,0%); câu "hướng suy luận vững" mạnh hơn bằng chứng, thiếu nhiễu thời điểm nhập hàng | S7 | Đã sửa trong v3 |
| TB | N6 | Dữ kiện bị sót: tiền, tiền gửi và tài sản tài chính 21.640,7 triệu (+8,3%), vay bằng 0, nợ/tài sản 17,7% | S7 trang 4–5 (điều phối viên đã grep và xác nhận) | Đã sửa trong v3 |
| TB | N7 | Giá cổ phiếu: đóng cửa HK$ 176,60 (9/11) và HK$ 155,70 (24/11), ≈ −11,8%; không thấy công bố trọng yếu nào trong giai đoạn đó | Investing.com (trễ, thứ cấp) | Đã thêm với cảnh báo nguồn |
| TB | N8 | Hai bằng chứng xếp sai nhóm ("tiền lớn, có cổ tức" không phản bác luận điểm tăng trưởng; "cổ phiếu giảm" là lập luận vòng); cổ tức đặc biệt chỉ nêu một chiều (chỉ 2 cổ đông hiện diện, 90,30% quyền biểu quyết; dòng chảy tới nhóm kiểm soát) | thông báo cổ tức; bản sao Eastmoney | Đã sửa trong v3 |
| THẤP | N9 | Quy định nhượng quyền: 7 án điển hình ngày 2026-08-12 là hướng dẫn tư pháp, không phải quy tắc mới; dự thảo giám sát của Bộ Thương mại là tháng 6/2023; không thấy xử phạt Mixue năm 2026 | Tân Hoa Xã; Winshang | Đã thêm trong v3 |
| THẤP | N10 | "Đổi CEO ngay trước kỳ lợi nhuận đầu tiên giảm" gắn `PHÉP_TÍNH` là sai nhãn, hàm ý nhân quả; tin giai thoại sau H1 là nguồn yếu; kế hoạch cổ phiếu thưởng chưa mở | Sina, Jiemian | Đã sửa trong v3 |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Agent tính tay (không có Bash); các phép chính khớp (biên gộp H2 2025 30,75%; hiệu ứng biên −184,6 triệu và hiệu ứng doanh thu +107,9 triệu; tiền +1.650,7 triệu ≈ 71% lợi nhuận H1; chia cổ tức; Guming và Meituan). Bằng chứng trái chiều đề xuất: tỷ lệ đóng cửa hàng Mixue thấp hơn Guming và Auntea; sụt doanh số mỗi cửa hàng là hiện tượng ngành; tiền tăng 8,3% không còn vay. Trường hợp luận điểm bi quan đúng: biên gộp và chi phí của Mixue xấu đi trong khi Guming cải thiện; cổ phiếu giảm tiếp không có công bố mới; nền H2 2025 khó hơn.

## Hạn chế của lần kiểm duyệt

Không có Bash, không tự tính SHA-256 và giờ. Chagee (−16,1%), Nayuki (−13,1%), Auntea Jenny (doanh thu +42,4%) chưa có nguồn gốc mở được; giá cổ phiếu lấy từ trang tổng hợp trễ; bản sao Eastmoney không phải HKEXnews; chưa có Q3 2026 của Mixue, chưa có doanh số cùng cửa hàng chính thức, chưa đọc toàn văn báo cáo thường niên 2025 và phần giao dịch bên liên quan. Meituan và Luckin chỉ cho thấy xu hướng trợ giá của hai công ty đó, không đo được trợ giá giải thích bao nhiêu phần sụt của Mixue.

## Kết luận của agent kiểm duyệt

`KHÔNG_ĐẠT`, nhưng tiến bộ rõ so với v1: số gốc của Mixue khớp, F1/F2/F4/F6–F9 đã xử lý đúng, bản nháp trung thực về điều chưa biết. Lý do chưa đạt là hai phát hiện mức CAO ở đúng hai chỗ v1 đã yêu cầu sửa (F3 và F5): tiền đề trợ giá và việc chưa tách hiện tượng ngành khỏi điểm đặc thù Mixue. Bất đồng còn lại: bên phản biện cho rằng bằng chứng nguồn gốc nghiêng về "nền trợ giá tác động chung, điểm riêng của Mixue nằm ở biên và chi phí", trong khi v2 coi "đặc thù Mixue" là giả thuyết mở; cả hai chưa được chứng minh nên cần giữ cả hai. Không phải lời khuyên mua, bán hay nắm giữ.
