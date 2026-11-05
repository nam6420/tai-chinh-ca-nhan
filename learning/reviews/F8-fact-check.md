# Biên bản kiểm nguồn — Bài F8

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-05 10:52 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-05 10:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; mở văn bản pháp quy gốc (Luật KDBH 31/VBHN-VPQH, NĐ 46/2023/NĐ-CP, VBHN 44/2026/VBHN-TT-BTC) và BCTC hợp nhất kiểm toán FY2025 của BVH, PVI, BIC; tái tính ví dụ Chain-Ladder, Mẫu 7-PNT và toàn bộ 10 bài tập cùng hàm trong learning/practice/models/insurance.py.`
- Báo cáo đích: `learning/lessons/F8-vietnam-insurance-analysis.md`
- SHA-256 nội dung đích: `bea4075e4f56e6c272bc3a15bcee6627f7b8eaec4da6f491beb204ca37ac0e58`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập `source-fact-checker` (Vòng 1 và Vòng 2) ngày 05/11/2026 trên bản nháp cố định (`shasum -a 256`: `e73e96ff9835c254abc0c6eeb2bba1548a70080ec5b0f446e2c6bc7e5a37a12f`); người kiểm không sửa bài.

## Các nguồn Internet và hồ sơ gốc đã đối chiếu trong lượt kiểm duyệt

| Nguồn / URL | Ngày xuất bản / kỳ / phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Bộ Tài chính — VBHN 44/2026/VBHN-TT-BTC hợp nhất Thông tư hướng dẫn Luật KDBH](https://mof.gov.vn/) | Ký 29/09/2026; Việt Nam; hợp nhất TT 67/2023/TT-BTC, TT 19/2025/TT-BTC, TT 65/2025/TT-BTC | 2026-11-05 | Đối chiếu Điều 33, 35, 36 (ví dụ Chain-Ladder tr. 42–45), 37, 38–40 và Phụ lục XII Mẫu 7-PNT (tr. 137–138) |
| [Chính phủ — Nghị định 46/2023/NĐ-CP quy định chi tiết Luật KDBH](https://chinhphu.vn/) | Ban hành 01/07/2023; Việt Nam | 2026-11-05 | Đối chiếu Điều 33 (xếp hạng tái BH `BBB`/`B++`/`Baa1`), Điều 35 (vốn tối thiểu), Điều 43 (trần đầu tư từ dự phòng) |
| [Tập đoàn Bảo Việt (`BVH`) — BCTC hợp nhất kiểm toán năm 2025](https://www.baoviet.com.vn/) | Kỳ 31/12/2025; Việt Nam; VAS (`TT 232/2012/TT-BTC`, `TT 199/2014/TT-BTC`); tỷ đồng | 2026-11-05 | Đối chiếu Bảng cân đối, KQKD, Thuyết minh 14 (đầu tư tài chính), Thuyết minh 18 (hoa hồng nhượng tái) và Thuyết minh 40 (Biên KNTT) |
| [CTCP PVI (`PVI`) & Tổng Công ty Bảo hiểm BIDV (`BIC`) — BCTC hợp nhất kiểm toán năm 2025](https://www.pvi.com.vn/) | Kỳ 31/12/2025; Việt Nam; VAS; tỷ đồng | 2026-11-05 | Đối chiếu cầu nối phí, tái bảo hiểm, dự phòng gộp/nhượng tái và hiệu quả đầu tư của `PVI` và `BIC` |

## Phát hiện và kiểm tra

1. **Văn bản pháp quy (`VBHN 44/2026/VBHN-TT-BTC`, `NĐ 46/2023/NĐ-CP`, `Luật KDBH 31/VBHN-VPQH`):**
   - `SỰ_THẬT`: Trần giữ lại mỗi rủi ro đơn lẻ $\le 10\%$ VCSH (`Khoản 4 Điều 33 VBHN 44`); công thức `UPR` theo tỷ lệ `25%`/`50%`, hệ số `1/8`, `1/24` và theo ngày (`Điều 35`); ví dụ tam giác `Chain-Ladder` `2016–2023` tại `Điểm a Khoản 2 Điều 36` (tr. 42–45: hệ số phát triển $f = [1,625; 1,236; 1,163; 1,089; 1,047; 1,030; 1,013]$, tổng bồi thường ước tính `208.341 triệu đồng` trừ đã trả `149.872 triệu đồng` = dự phòng bồi thường `58.469 triệu đồng`); dự phòng dao động lớn `1%–3%` phí giữ lại (`Điều 37`); dự phòng toán học nhân thọ và trần lãi suất kỹ thuật $\min(80\% \times \text{lãi suất TPCP }\ge 10\text{ năm bình quân 24 tháng},\; \text{lợi suất đầu tư 4 quý},\; \text{lãi suất tính phí})$ (`Điều 38–40`); Biên KNTT phi nhân thọ `Mẫu 7-PNT` (`Phụ lục XII` tr. 137–138: $\max(25\%\text{ phí giữ lại},\; 12,5\%\text{ tổng phí gốc và nhận tái})$, tỷ lệ giảm trừ tài sản `100%`, `1%`, `3%`, `15%`, `20%`, `25%`); trần đầu tư từ nguồn dự phòng nghiệp vụ (`Điều 43 NĐ 46/2023/NĐ-CP`) và lộ trình vốn trên cơ sở rủi ro (`RBC`) từ `01/01/2028` (`Khoản 2 Điều 157 Luật KDBH`).
2. **Số liệu BCTC kiểm toán `FY2025` của `BVH`, `PVI`, `BIC`:**
   - **`BVH`:** Tổng tài sản `291.805,65 tỷ đồng`, đầu tư tài chính thuần `266.535,57 tỷ đồng` (TM 14 tr. 48), dự phòng gộp `201.682,49 tỷ đồng` (DP toán học `171.409,33 tỷ đồng`, DP lãi cam kết tối thiểu `16.544,35 tỷ đồng`), tài sản tái BH `3.682,41 tỷ đồng`, VCSH `25.480,34 tỷ đồng`, `GWP` `43.716,18 tỷ đồng`, nhận tái `399,97 tỷ đồng`, nhượng tái `-3.808,52 tỷ đồng`, `NWP` `40.307,63 tỷ đồng` (`Retention = 91,37%`), `NEP` `40.123,67 tỷ đồng`, hoa hồng nhượng tái & thu khác `824,59 tỷ đồng` (hoa hồng nhượng tái `776,40 tỷ đồng`, TM 18 tr. 57), lãi gộp KDBH `+1.237,95 tỷ đồng`, lãi tài chính thuần `11.120,47 tỷ đồng`, `EBT` `3.554,43 tỷ đồng`, `NPAT` `2.921,57 tỷ đồng`, Biên KNTT PNT `141%` và NT `107%` (TM 40 tr. 84).
   - **`PVI`:** Tổng tài sản `44.512,14 tỷ đồng`, đầu tư tài chính `16.707,55 tỷ đồng` (chưa kể BĐSĐT `661,03 tỷ đồng`), dự phòng gộp `28.417,50 tỷ đồng`, tài sản tái BH `21.614,45 tỷ đồng` (DP bồi thường nhượng tái `15.368,84 tỷ đồng`), VCSH `8.533,91 tỷ đồng`, `GWP` `14.908,34 tỷ đồng`, nhận tái `10.498,98 tỷ đồng`, nhượng tái `-17.178,02 tỷ đồng`, `NWP` `8.229,30 tỷ đồng` (`Retention = 32,39%`), `NEP` `7.633,90 tỷ đồng`, hoa hồng nhượng tái `1.337,61 tỷ đồng`, bồi thường giữ lại `3.286,62 tỷ đồng` (`Loss Ratio = 43,05%`), `Combined Ratio` `106,06%` / `88,54%`, lãi tài chính `918,21 tỷ đồng`, `EBT` `1.459,67 tỷ đồng`, `NPAT` `1.152,11 tỷ đồng`.
   - **`BIC`:** Tổng tài sản `10.079,69 tỷ đồng`, đầu tư tài chính `7.202,47 tỷ đồng`, dự phòng gộp `4.447,34 tỷ đồng`, tài sản tái BH `1.625,29 tỷ đồng`, VCSH `3.384,46 tỷ đồng`, `GWP` `5.696,79 tỷ đồng`, nhận tái `92,70 tỷ đồng`, nhượng tái `-1.760,93 tỷ đồng`, `NWP` `4.028,55 tỷ đồng` (`Retention = 69,58%`), `NEP` `3.948,22 tỷ đồng`, hoa hồng nhượng tái & thu khác `338,33 tỷ đồng` (hoa hồng nhượng tái `272,28 tỷ đồng`), bồi thường giữ lại `1.189,95 tỷ đồng` (`Loss Ratio = 30,14%`), `Combined Ratio` `83,37%` / `74,80%`, lãi gộp KDBH `+994,94 tỷ đồng`, lãi tài chính `510,29 tỷ đồng`, `EBT` `678,79 tỷ đồng`, `NPAT` `551,89 tỷ đồng`.
3. **Khớp hàm [`learning/practice/models/insurance.py`](../practice/models/insurance.py) và bài tập:** Toàn bộ tên hàm và đầu ra bài tập khớp chính xác. Ghi chú nhỏ không trọng yếu ở Bài tập 10 giả định cuối bài: $B_0^{\text{adj}} = 2.960\text{ tỷ đồng}$ khớp tuyệt đối; phần chiết khấu `RIM` 5 năm có khác biệt nhỏ về quy ước vốn đầu/cuối kỳ (`3.863,92 tỷ` vs. `3.821,24 tỷ`), không ảnh hưởng kết luận hay số liệu nguồn.

## Hạn chế của lần kiểm duyệt

Không thay thế kiểm toán độc lập hoặc báo cáo精算 (actuarial report) nội bộ của doanh nghiệp; công thức vốn `RBC` chính thức sau `01/01/2028` đang chờ văn bản hướng dẫn tiếp theo của Bộ Tài chính (`CHƯA_BIẾT`).

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả.
