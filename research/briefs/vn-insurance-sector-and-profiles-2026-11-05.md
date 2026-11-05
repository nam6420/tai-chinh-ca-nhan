# Đề bài nghiên cứu: hồ sơ ngành Bảo hiểm Việt Nam và ba hồ sơ mẫu BVH, PVI, BIC (Đợt 3)

- Trạng thái: `HOÀN_THÀNH`
- Chủ trì: `research_coordinator`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi địa lý: Việt Nam, sàn HOSE (`BVH`, `BIC`) và HNX (`PVI`); tiền tệ VND; chuẩn kế toán VAS và chế độ kế toán doanh nghiệp bảo hiểm (Thông tư 232/2012/TT-BTC, Thông tư 199/2014/TT-BTC; khung pháp lý Luật Kinh doanh bảo hiểm hợp nhất số 31/VBHN-VPQH, Nghị định 46/2023/NĐ-CP và Thông tư 67/2023/TT-BTC hợp nhất tại 44/VBHN-BTC).
- Mục tiêu học tập: xây dựng bộ hồ sơ nghiên cứu thực chiến kết nối trực tiếp với mô-đun bài giảng bảo hiểm ([`013-banks-insurers.md`](../../learning/lessons/013-banks-insurers.md), [`F8-vietnam-insurance-analysis.md`](../../learning/lessons/F8-vietnam-insurance-analysis.md), [`P4-personal-insurance-contracts-and-costs.md`](../../learning/lessons/P4-personal-insurance-contracts-and-costs.md)). Người học thực hành đọc Báo cáo tài chính hợp nhất năm 2025 đã kiểm toán của ba mô hình kinh doanh bảo hiểm khác hẳn nhau tại Việt Nam:
  1. **Tập đoàn Bảo Việt (`BVH` — HOSE):** Tập đoàn tài chính - bảo hiểm hỗn hợp (nhân thọ + phi nhân thọ), nơi dự phòng toán học nhân thọ dài hạn, dự phòng đảm bảo lãi suất cam kết tối thiểu và giao dịch mua bán lại (Repo) trái phiếu Chính phủ chi phối bảng cân đối kế toán.
  2. **CTCP PVI (`PVI` — HNX):** Doanh nghiệp đầu ngành bảo hiểm phi nhân thọ bán buôn công nghiệp - năng lượng và tái bảo hiểm (`PVI Insurance` + `Hanoi Re`), nơi tỷ lệ giữ lại thấp (~32,4%), tài sản tái bảo hiểm gấp 2,53 lần vốn chủ sở hữu và thu nhập hoa hồng nhượng tái / phí fronting quyết định biên lợi nhuận.
  3. **Tổng Công ty Bảo hiểm BIDV (`BIC` — HOSE):** Doanh nghiệp bảo hiểm phi nhân thọ bán lẻ qua ngân hàng mẹ (`Bancassurance` hệ thống BIDV), có tỷ lệ kết hợp (`Combined Ratio`) thuộc nhóm thấp nhất ngành nhưng chịu rủi ro tập trung kênh phân phối và tiền gửi tại ngân hàng mẹ cùng độ nhạy tổn thất thiên tai bão lũ.
- Câu hỏi quyết định được hỗ trợ: những giả định nào phải đúng để hiểu nguồn gốc lợi nhuận (khai thác bảo hiểm gốc, nhượng tái bảo hiểm hay đầu tư tài chính), chất lượng dự phòng kỹ thuật và biên an toàn vốn của từng doanh nghiệp. Không phải khuyến nghị mua/bán/nắm giữ cổ phiếu.

## Câu hỏi cốt lõi cho báo cáo ngành và từng hồ sơ

1. Chuỗi giá trị ngành bảo hiểm Việt Nam vận hành ra sao sau đợt tái cấu trúc pháp lý 2023–2025 (Luật Kinh doanh bảo hiểm 2022, Nghị định 46/2023/NĐ-CP, Thông tư 67/2023/TT-BTC)?
2. Doanh nghiệp tạo ra dòng tiền nổi (`Float`) từ đâu, chi phí của `Float` là âm (lãi khai thác) hay dương (lỗ khai thác), và danh mục đầu tư phân bổ vào tài sản nào?
3. Rủi ro tập trung (đối tác tái bảo hiểm, giao dịch bên liên quan với ngân hàng mẹ, lãi suất cam kết tối thiểu, nợ quá hạn tồn đọng) nằm ở đâu trong thuyết minh BCTC?
4. Ba kịch bản định giá (`Bất lợi`, `Cơ sở`, `Thuận lợi`) theo mô hình `P/B hợp lý` (`Justified P/B`) và `Thu nhập thặng dư` (`Residual Income`) đòi hỏi điều kiện gì, và điều kiện nào làm luận điểm mất hiệu lực?

## Kế hoạch tìm nguồn và kiểm chứng

- Nguồn pháp lý gốc: Công báo Chính phủ và Cổng Thông tin điện tử Chính phủ (`31/VBHN-VPQH`, `46/2023/NĐ-CP`, `44/VBHN-BTC`).
- Nguồn tài chính doanh nghiệp: BCTC hợp nhất năm 2025 đã kiểm toán của `BVH` (Ernst & Young Việt Nam ký 31/03/2026), `PVI` (PwC Việt Nam ký 15/02/2026) và `BIC` (Ernst & Young Việt Nam ký 20/03/2026), đối chiếu thêm BCTC hợp nhất Quý 4/2025 tự lập của `BIC` (ký 23/01/2026 kèm công văn giải trình 156/CV-KT) để phân tích điều chỉnh kiểm toán và điều chỉnh hồi tố năm 2024 theo Kiểm toán Nhà nước.
- Nguồn đối chiếu quốc tế: Báo cáo thường niên FY2025 của `Berkshire Hathaway Inc.` (mảng `GEICO` và `Berkshire Hathaway Reinsurance Group`).
- Toàn bộ phép tính được mã hóa và kiểm thử tự động trong [`research/companies/VN/calc_insurance_profiles.py`](../companies/VN/calc_insurance_profiles.py) và [`tests/test_insurance_profiles.py`](../../tests/test_insurance_profiles.py).

## Phân công agent

- `research_coordinator` lập phạm vi, tổng hợp bằng chứng và ghi báo cáo nháp cố định cùng sổ nguồn.
- `source_fact_checker` và `risk_bear_reviewer` chạy độc lập trên cùng bản nháp cố định của cả 4 báo cáo (`VN-insurance`, `BVH`, `PVI`, `BIC`) trước khi mở cổng xuất bản bằng `scripts/validate_report.py`.
