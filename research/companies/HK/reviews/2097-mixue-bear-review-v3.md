# Biên bản kiểm duyệt: MIXUE Group (2097.HK), đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (bản nháp v3)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `risk-bear-reviewer` (lần kiểm 3). Giữ nguyên kết luận, mức độ và bằng chứng chính. Bên phản biện chạy độc lập, không đọc biên bản kiểm nguồn.

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-25` (agent không có đồng hồ; điều phối viên ghi nhận hoàn tất trước 2026-11-25 09:30 +07)
- Chốt dữ liệu lúc: `2026-11-25 09:05 +07` (khớp báo cáo đích v3)
- Phạm vi: toàn bộ v3; N1–N10 của lần 2; các đoạn mới v3 tự thêm (nhân sự ≈ một phần tư chi phí tăng, "chi phí đi ngang", cổ tức đặc biệt hai chiều, FULU, tách số từng người); mở lại nguồn gốc Chagee, Nayuki, kết quả biểu quyết, giá, phần cổ phần AR 2025
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-draft-v3-sha-39cd1668.md` (bản sao nguyên vẹn của v3)
- SHA-256 nội dung đích: `39cd1668d645ec6b0b3da5e42b48de20b68b58ae0d56a9932ac5c78278607df7` (do điều phối viên cung cấp; điều phối viên đã tự tính lại và khớp)
- Kết luận: `ĐẠT` có điều kiện sửa văn bản (không còn phát hiện CAO hay NGHIÊM_TRỌNG; agent không tự bỏ nhãn nháp)
- Lỗi nghiêm trọng chưa xử lý: `0` (8 phát hiện TRUNG_BÌNH, 4 THẤP)

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

Ngày truy cập 2026-11-25. **Nguồn gốc:** Nayuki báo cáo giữa kỳ (HKEXnews 2026-08-26: doanh thu −13,1% còn 1.892,5 triệu so với 2.177,6; 1.685 cửa hàng); AR 2025 (tải lại, trang 54–65 và 107); thông báo giao dịch liên kết FULU (HKEXnews 2025-10-01, bản tiếng Trung); bản sao Eastmoney của kết quả biểu quyết 2026-09-30 (HKEXnews gốc chưa tìm thấy qua tìm kiếm của agent). **Thứ cấp:** bản sao thông báo Chagee Q2 (QuiverQuant), Inside Retail (Chagee), Winshang và BNext (lời ban lãnh đạo thuật lại), KrASIA/Nikkei, Sina (CSRC 2026-05-03), Investing.com (giá, trễ), Jiemian và The Paper (hành động phối hợp trước IPO), TipRanks, caiwennews. Không mở được: Chagee IR, kabutan, Smartkarma, Lixinger (403), Huxiu (405); cáo bạch đầy đủ quá lớn cho `WebFetch`.

## Phát hiện lần 2: trạng thái trong v3

`ĐÃ_SỬA`: N1, N3, N4 (phần cũ), N5, N6, N7, N8 (phần xếp nhóm), N9, N10. `SỬA_CHƯA_ĐỦ`: N2 (hạ từ CAO xuống TRUNG_BÌNH: khung "hiện tượng ngành" chắc hơn dữ liệu; bằng chứng bị dùng ngược chiều).

## Phát hiện mới trong v3

| Mức độ | Mã | Phát hiện | Bằng chứng | Trạng thái (sau khi sửa v4) |
|---|---|---|---|---|
| TB | M1 | Bỏ sót lời ban lãnh đạo (thuật lại, chưa có bản ghi): sụt do nền trợ giá "chưa từng có" và cạnh tranh trà-cà phê; cùng cửa hàng giảm hai chữ số; Lucky Cup và FULU kéo trung bình xuống; giảm mở mới trong nước là chủ động; chu kỳ đầu tư ≈ 3 năm; mục tiêu biên gộp ≈ 30%. Chỉ báo mở mới < 5.000 có thể thỏa vì chủ ý | Winshang; BNext; KrASIA | Đã sửa trong v4 (gắn `Ý_KIẾN`, `CHƯA_XÁC_MINH`) |
| TB | M2 | Dữ liệu ngành tách đôi: Guming và Auntea Jenny (doanh thu/cửa hàng xấp xỉ phẳng) khác nhóm Chagee (GMV/cửa hàng ≈ −16,3%), Nayuki (−13,1%), Luckin (−11,1%). Chagee còn sụt hai chữ số suốt 2025, nên "nền cao 2026" không giải thích hết. Câu "hiện tượng ngành" chắc hơn dữ liệu; Guming và Auntea không nên xếp là bằng chứng ủng hộ "ngành" | Nayuki HKEXnews; QuiverQuant; Inside Retail | Đã sửa trong v4 |
| TB | M3 | "Chi phí đã bước lên từ H2 2025 rồi đi ngang" gắn `PHÉP_TÍNH` nhưng là `SUY_LUẬN` lạc quan: tỷ lệ bán hàng + quản lý 9,1% (H1 2025), 9,5% (H2 2025), 11,4% (H1 2026); mùa vụ; FULU chỉ một tháng trong H2 2025; trái với "chu kỳ đầu tư 3 năm" | S7 trang 3; AR 2025 trang 107 | Đã sửa trong v4 |
| TB | M4 | "Nhân sự ≈ một phần tư" so sánh khác phạm vi: tử số là chi phí nhân sự toàn công ty (+102,3 triệu), mẫu số chỉ bán hàng + quản lý; 25–27% là cận trên; chi phí quản lý +172,4 triệu trong khi tổng nhân sự +102,3 triệu nên câu của công ty khó khớp; con số +102 có sẵn trong S7 | S7 trang 3 và 5 | Đã sửa trong v4 |
| TB | M5 | Cổ tức đặc biệt: số tiền tới người kiểm soát tính được (một lô ≈ 412 triệu; hai lô ≈ 816–825 triệu RMB); cổ tức chia đều theo cổ phiếu nên không tự nó là chuyển giá trị; điều đáng nêu là người kiểm soát tự biểu quyết nên 99,999% không chứng minh đồng thuận của cổ đông không kiểm soát; chưa xác minh đã trả; chiều "ít cơ hội tái đầu tư" cần đối chiếu với tiền mặt 21,6 tỷ | kết quả biểu quyết; AR 2025 trang 54–56 | Đã sửa trong v4 |
| TB | M6 | Tổng sở hữu hai nhà sáng lập: bằng chứng nghiêng mạnh về hai lô riêng (≈ 81–82%): số học hiện diện 90,30%, tỷ lệ trước IPO (≈ 84,9%) khớp hai lô | AR 2025 trang 54–57; nguồn thứ cấp | Đã sửa trong v4 (nâng lên `SỰ_THẬT` dựa vào cáo bạch, xem biên bản kiểm nguồn v3) |
| TB | M7 | FULU: cơ chế là góp vốn tăng vốn điều lệ 285,6 triệu (51% vốn sau tăng) cộng mua 2% từ ông Zhao Jie 11,2 triệu; bên liên quan nắm ≈ 80,46% (bà Tian Haixia 60,05% + Mailang Tongzhou 20,41%); định giá ngầm định ≈ 560,0 triệu; công bằng hay không `CHƯA_BIẾT` | HKEXnews 2025-10-01; AR 2025 trang 59 | Đã sửa trong v4 |
| TB | M8 | Bỏ sót chuyển đổi cổ phiếu H (22,8 triệu, 6,01%) và kế hoạch thưởng cổ phiếu | Sina | Đã sửa trong v4 (nay có nguồn HKEXnews gốc, đã lưu) |
| THẤP | M9 | Nước ngoài so hai kỳ khác độ dài; theo nửa năm: −3,3%, −5,6%, −2,0% | số trong bảng v3 | Đã sửa trong v4 |
| THẤP | M10 | Ngưỡng chi phí neo mức H1 2026, bỏ qua mùa vụ; thiếu tham chiếu ngoài | S7 | Đã sửa trong v4 |
| THẤP | M11 | Cân bằng nguồn và giá: Nayuki có số gốc; số Chagee (16,1)% trùng ở hai quý; thêm mốc đỉnh HK$ 618,5 (6/2025) và đáy 52 tuần 154,50; giá 158,90 phiên 25/11 | các nguồn trên | Đã sửa trong v4 |
| THẤP | M12 | Nhãn: +102 triệu nay là `SỰ_THẬT` [S7]; không có câu nào nghe như lời khuyên | v3 | Đã sửa trong v4 |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Agent tính tay; các phép chính khớp (hiệu ứng biên −184,7 và +107,9; tỷ lệ chi phí 9,1/9,5/11,4%; cổ tức tới người kiểm soát; FULU 285,6/0,51 = 560,0). Bằng chứng trái chiều: ủng hộ "ngành/nền trợ giá" (ban lãnh đạo; Chagee, Nayuki, Luckin) và ủng hộ "đặc thù Mixue" (Guming, Auntea Jenny doanh thu/cửa hàng phẳng; Chagee, Nayuki giảm trước 2026; chi phí và biên Mixue xấu đi trong khi Guming tốt lên); trường hợp lạc quan đúng (tỷ lệ đóng thấp hơn; tiền tăng không nợ; mở mới giảm có thể chủ động; doanh thu bán buôn chịu nhiễu thời điểm nhập hàng). Mixue không công bố doanh số cùng cửa hàng nên mọi phép chia vẫn là suy luận.

## Hạn chế của lần kiểm duyệt

Không có Bash và đồng hồ; không mở được Chagee IR, kabutan, Smartkarma, Lixinger, Huxiu; không tìm thấy bản HKEXnews gốc của kết quả biểu quyết bằng tìm kiếm (điều phối viên và bên kiểm nguồn đã tìm thấy sau đó); không tìm thấy thông báo đã trả cổ tức; cáo bạch đầy đủ quá lớn cho công cụ của agent; lời ban lãnh đạo chỉ qua nguồn thứ cấp. **Agent không biết rằng báo cáo giữa kỳ đầy đủ (với báo cáo lưu chuyển tiền tệ H1 2026) đã được đăng ngày 2026-09-23**; điểm này do bên kiểm nguồn phát hiện (F1) và là điểm bên phản biện bỏ sót.

## Kết luận của agent kiểm duyệt

`ĐẠT` ở nghĩa không còn phát hiện CAO hay NGHIÊM_TRỌNG: hai CAO của lần 2 đã sửa đúng logic cốt lõi, các số gốc khớp, bản nháp nói rõ điều chưa biết, không khuyến nghị và không gắn xác suất. Điều kiện: sửa trước khi gỡ nhãn nháp 8 phát hiện TRUNG_BÌNH (M1–M8). Không phải lời khuyên mua, bán hay nắm giữ.
