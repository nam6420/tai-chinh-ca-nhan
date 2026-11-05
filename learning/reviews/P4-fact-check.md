# Biên bản kiểm nguồn — Bài P4

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-05 10:52 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-05 10:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; đối chiếu Luật KDBH (31/VBHN-VPQH), Nghị định 46/2023/NĐ-CP và VBHN 44/2026/VBHN-TT-BTC (Điều 12, 17, 20, 21, 22, 29, 51, 53 và Phụ lục VIII Mẫu 22-NT, 23-NT); tái tính bảng mô phỏng 10 năm UL vs. BTID và toàn bộ 10 bài tập cùng hàm trong learning/practice/models/insurance.py.`
- Báo cáo đích: `learning/lessons/P4-personal-insurance-contracts-and-costs.md`
- SHA-256 nội dung đích: `949f9d76dfc449ee837c195859946a90427ad82db16e4f077b953472aef3ca51`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập `source-fact-checker` (Vòng 1 và Vòng 2) ngày 05/11/2026 trên bản nháp cố định (`shasum -a 256`: `ba6c48f5688b2e92598779bb8f5cbc9f5fe99167461567661fc6631acf017cf7`); người kiểm không sửa bài.

## Các nguồn Internet và hồ sơ gốc đã đối chiếu trong lượt kiểm duyệt

| Nguồn / URL | Ngày xuất bản / kỳ / phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Văn phòng Quốc hội — Luật Kinh doanh bảo hiểm (31/VBHN-VPQH)](https://quochuoi.vn/) | Hợp nhất Luật 08/2022/QH15 ngày 16/06/2022, hiệu lực 01/01/2023; Việt Nam | 2026-11-05 | Đối chiếu Điều 21, 22 (kê khai trung thực), Điều 35 (21 ngày cân nhắc), Điều 37 (gia hạn đóng phí), Điều 54 & 68 (thế quyền), Điều 156 (Quỹ bảo vệ NĐBH) |
| [Chính phủ — Nghị định 46/2023/NĐ-CP](https://chinhphu.vn/) | Ban hành 01/07/2023; Việt Nam | 2026-11-05 | Đối chiếu Điều 95 (hạn mức chi trả tối đa 90% nhưng không quá 200 triệu đồng/người/hợp đồng của Quỹ bảo vệ NĐBH) |
| [Bộ Tài chính — VBHN 44/2026/VBHN-TT-BTC](https://mof.gov.vn/) | Ký 29/09/2026; Việt Nam; hợp nhất TT 67/2023/TT-BTC, TT 19/2025/TT-BTC, TT 65/2025/TT-BTC | 2026-11-05 | Đối chiếu Điều 12, 17 (thời gian chờ, bệnh có sẵn 36 tháng, gia hạn 60 ngày, khôi phục 24 tháng), Điều 20–22 (trần phí ban đầu 50%/30%/20%/2%/0%, phí quản lý quỹ), Điều 29 (`Mẫu 22-NT`, `23-NT`), Điều 51 (trần hoa hồng) và Điều 53 (cấm bán kèm vay $\pm 60$ ngày, ghi âm 5 năm) |

## Phát hiện và kiểm tra

1. **Điều khoản pháp lý bảo vệ người mua bảo hiểm tại Việt Nam:**
   - `SỰ_THẬT`: Đối chiếu khớp 100% với văn bản gốc:
     - `Điều 35 Luật KDBH`: Thời gian cân nhắc (`Free-look period`) **`21 ngày`** kể từ ngày nhận hợp đồng ($> 1$ năm), hoàn lại phí đã đóng trừ chi phí khám sức khỏe thực tế.
     - `Điều 12 & 17 VBHN 44/2026/VBHN-TT-BTC`: Thời gian chờ (tai nạn `0 ngày`, bệnh thông thường $\le 90$ ngày, thai sản $\le 270$ ngày / biến chứng $\le 90$ ngày, bệnh đặc biệt và bệnh có sẵn $\le 365$ ngày); bệnh có sẵn xác định trong vòng **`36 tháng`** (`03 năm`) trước ngày hiệu lực hợp đồng căn cứ hồ sơ y tế hoặc thông tin khách hàng tự kê khai (`Điểm d Khoản 3 Điều 12`); thời gian gia hạn đóng phí **`60 ngày`** (`Khoản 4 Điều 12`); thời hạn yêu cầu khôi phục hiệu lực tối thiểu **`24 tháng`** (`Khoản 6 Điều 12 & Điều 17`).
     - `Khoản 3 Điều 22 VBHN 44/2026/VBHN-TT-BTC`: Trần Phí ban đầu (`Initial Charge`) đóng phí định kỳ (`Điểm a`): **Năm 1 `50%`, Năm 2 `30%`, Năm 3–5 `20%`, Năm 6–10 `2%`, từ Năm 11 `0%`**, phí đóng thêm (`Top-up`) $\le 1,5\%$ trong 10 năm đầu; trần Phí quản lý quỹ (`Điểm d`): `UL` $\le 2,0\%/\text{năm}$, `ILP` cổ phiếu $\le 2,5\%$, trái phiếu $\le 1,5\%$, tiền tệ $\le 1,0\%$.
     - `Điều 53 VBHN 44/2026/VBHN-TT-BTC`: Cấm tổ chức tín dụng tư vấn/giới thiệu/chào bán/thu xếp giao kết hợp đồng `UL`/`ILP` cho khách hàng trong **`60 ngày trước` và `60 ngày sau`** ngày giải ngân toàn bộ khoản vay (`Điểm c Khoản 3 Điều 53`); bắt buộc **ghi âm** quá trình tư vấn và lưu trữ tối thiểu **`05 năm`** (`Điểm đ Khoản 2 & Khoản 5 Điều 53`).
     - `Điều 95 Nghị định 46/2023/NĐ-CP`: Quỹ bảo vệ người được bảo hiểm chi trả tối đa **`90%`** mức trách nhiệm nhân thọ nhưng không quá **`200 triệu đồng/người/hợp đồng`** (đã dừng trích nộp mới từ `01/01/2023` theo `Khoản 2 Điều 156 Luật KDBH`).
2. **Bảng mô phỏng 10 năm `UL` vs. `BTID` và bài tập:**
   - `PHÉP_TÍNH`: Chạy `vn_ul_initial_fee_rate()` và `ul_vs_term_invest()` trong [`learning/practice/models/insurance.py`](../practice/models/insurance.py) tái lập khớp tuyệt đối 100% cả 10 dòng từ Năm 1 ($AV_1 = 8,15\text{ triệu đồng}$, $CSV_1 = 1,63\text{ triệu đồng}$, $\text{BTID}_1 = 19,29\text{ triệu đồng}$) đến Năm 10 ($AV_{10} = CSV_{10} = 180,82\text{ triệu đồng}$, $\text{BTID}_{10} = 254,28\text{ triệu đồng}$, chênh lệch `+73,46 triệu đồng`, tổng phí ban đầu `30,00 triệu đồng`, tổng `COI` `21,82 triệu đồng`). Toàn bộ 10 bài tập tính tay và bài tập làm sạch dữ liệu lệch khớp chính xác.

## Hạn chế của lần kiểm duyệt

Không tư vấn lựa chọn sản phẩm bảo hiểm cá nhân hóa; biểu phí rủi ro (`COI`), phí hủy hợp đồng và quyền lợi thẻ sức khỏe cụ thể phụ thuộc vào quy tắc, điều khoản của từng sản phẩm được Bộ Tài chính phê chuẩn.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả.
