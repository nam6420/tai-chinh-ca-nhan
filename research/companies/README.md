# Hồ sơ doanh nghiệp

Lưu theo `research/companies/<thị-trường>/<mã>/`. Mỗi hồ sơ ghi đề bài, nguồn và kỳ, tài chính, quản trị, kịch bản, bằng chứng trái chiều, điều chưa biết và điều kiện bác bỏ. Dùng [mẫu báo cáo](../../templates/company-report.md) và [sổ nguồn](../../templates/source-register.md).

Báo cáo phải giữ nhãn nháp cho tới khi kiểm nguồn và phản biện độc lập trên cùng mã băm; việc có tệp hoặc điểm trong watchlist không là khuyến nghị. [Hồ sơ Apple mẫu](US/AAPL/report.md) dùng để học quy trình; kiểm mốc nguồn và trạng thái trong chính báo cáo.

## Hồ sơ Việt Nam (Đợt 2, đã qua hai nhánh kiểm duyệt)

Bốn hồ sơ học tập có hai biên bản ĐẠT khớp mã băm, chốt dữ liệu 31/10/2026, kiểm trực tuyến và chốt vòng 6–7 ngày 02/11/2026. Xem trạng thái, giới hạn và biên bản ngay trong từng báo cáo. Phép tính dùng chung [`calc_wave2.py`](VN/calc_wave2.py). Nhật ký: [vòng 1](VN/review-round-1.md), [vòng 2](VN/review-round-2.md), [vòng 3](VN/review-round-3.md), [vòng 4](VN/review-round-4.md), [vòng 5–7](VN/review-round-5.md). Đề bài: [Đợt 2](../briefs/vn-company-profiles-wave-2-2026-10-31.md). ĐẠT theo tiêu chí không còn lỗi nghiêm trọng/cao; các điểm trung bình/thấp và điều chưa biết vẫn còn. Các công ty chỉ để học đọc báo cáo, không phải khuyến nghị.

| Mã | Công ty | Bài học chính | Hồ sơ |
|---|---|---|---|
| FPT | Công ty Cổ phần FPT (dịch vụ công nghệ) | Cơ sở hợp nhất đổi giữa hai kỳ; lợi nhuận liên kết chưa chắc thành tiền | [report](VN/FPT/report.md) |
| VNM | Vinamilk (tiêu dùng) | Tách thu nhập tài chính và lãi liên kết khỏi lợi nhuận; kịch bản Q4 so Q4 năm trước | [report](VN/VNM/report.md) |
| VCB | Vietcombank (ngân hàng) | Cách đọc ngân hàng; khoản một lần; dự phòng; đối chiếu nhóm nợ và cầu nối dự phòng với BCTC | [report](VN/VCB/report.md) |
| HPG | Tập đoàn Hòa Phát (công ty chu kỳ) | Không lấy lợi nhuận một năm làm mức bình thường; điều chỉnh giá theo cổ phiếu thưởng | [report](VN/HPG/report.md) |

## Hồ sơ Bảo hiểm Việt Nam (Đợt 3, đã qua hai nhánh kiểm duyệt)

Ba hồ sơ thực chiến ngành bảo hiểm có hai biên bản `ĐẠT` (`fact-check.md` và `risk-review.md`) khớp mã băm `SHA-256`, chốt dữ liệu ngày `05/11/2026` trên Báo cáo tài chính hợp nhất năm 2025 đã kiểm toán. Phép tính tái lập dùng chung mô-đun [`calc_insurance_profiles.py`](VN/calc_insurance_profiles.py) và bộ kiểm thử [`test_insurance_profiles.py`](../../tests/test_insurance_profiles.py). Đề bài: [Đợt 3](../briefs/vn-insurance-sector-and-profiles-2026-11-05.md); Báo cáo ngành đi kèm: [VN-insurance](../sectors/VN-insurance/report.md).

| Mã | Công ty | Bài học chính | Hồ sơ |
|---|---|---|---|
| BVH | Tập đoàn Bảo Việt (HOSE — Tập đoàn bảo hiểm Nhân thọ + Phi nhân thọ) | Dự phòng toán học nhân thọ, dự phòng đảm bảo lãi suất cam kết tối thiểu, đòn bẩy Repo TPCP (`53.229,07 tỷ VND`) và biên thanh toán nhân thọ (`107%`) | [report](VN/BVH/report.md) |
| PVI | Công ty Cổ phần PVI (HNX — Bảo hiểm công nghiệp & Tái bảo hiểm) | Kinh tế học nhượng tái bảo hiểm (tỷ lệ giữ lại `32,39%`), hoa hồng nhượng tái (`1.337,61 tỷ VND`) và rủi ro tập trung tài sản tái bảo hiểm (`2,70x` VCSH) | [report](VN/PVI/report.md) |
| BIC | Tổng Công ty Bảo hiểm BIDV (HOSE — Bảo hiểm phi nhân thọ Bancassurance) | Kinh tế đơn vị Bancassurance qua ngân hàng mẹ `BIDV`, rủi ro tập trung tiền gửi/hoa hồng bên liên quan, điều chỉnh kiểm toán và độ nhạy thiên tai bão lũ | [report](VN/BIC/report.md) |

