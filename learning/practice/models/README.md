# Mô hình thực hành

Chỉ dùng thư viện chuẩn Python 3. Chạy `python3 valuation.py`; kiểm bằng `python3 -m unittest discover tests` ở thư mục gốc.

- `apple_fy2025_inputs.csv`: số lịch sử từ Form 10-K Apple FY2025 (triệu USD), mở 2026-10-31.
- `valuation.py`: chi phí vốn (010), DCF và định giá ngược (011), kịch bản (012), ba báo cáo hư cấu (F1), DDM/RIM/SOTP (F2).
- Mọi giả định tương lai là giả định bài học, không phải dự báo. Chưa có bảng tính Excel: người học dựng lại công thức theo hàm trong tệp.
- `hpg_cycle_inputs.csv`: doanh thu, lợi nhuận, vốn chủ HPG FY2021–FY2025 (tỷ VND; trộn báo cáo thường niên 2023 và BCTC kiểm toán FY2025), mở 2026-11-01.
- `cyclical.py`: chuẩn hóa lợi nhuận công ty chu kỳ (bài Q3): trung bình tuyệt đối, biên, trung vị, bỏ năm cực đoan, ROE, chiết khấu lùi.
- `hpg_fy2025_statements.csv`: số báo cáo tài chính hợp nhất kiểm toán FY2025 và cột năm trước của HPG (tỷ VND), mở 2026-11-01.
- `earnings_quality.py`: Beneish M-score, Altman Z'', Piotroski F-score (bài Q1). Hệ số Beneish/Altman từ nguồn thứ cấp, chưa đối chiếu bài gốc.
- `apple_capital_return_inputs.csv`: SBC, mua lại, cổ tức, số cổ phiếu và EPS của Apple FY2023–FY2025 (triệu USD; cổ phiếu nghìn), mở 2026-11-01.
- `capital_return.py`: SBC, pha loãng, mua lại (EPS và giá trị mỗi cổ phiếu), cổ tức, cổ phiếu thưởng (bài Q2).
- `apple_xbrl_subset.json`: tập con 14 tag của companyfacts Apple (SEC), tải 2026-11-01, giữ nguyên giá trị, để chạy offline.
- `hpg_fy2025_transcription.csv`: bản chép 14 chỉ tiêu báo cáo HPG FY2025/FY2024 (tỷ VND) cho các phép kiểm đẳng thức.
- `data_pull.py`: gọi companyfacts (cần User-Agent của bạn), lọc kỳ, chọn tag, quý 4 suy ra, kiểm đẳng thức (bài Q4).

- `market_returns.py`: N1/N4/N5 — luồng tiền phát hành, vốn hóa/EV giản lược, sổ lệnh hư cấu, PV/FV, quy đổi tỷ lệ, lạm phát, CAGR, góp đầu/cuối tháng, trọng số và tái cân bằng. Chạy từ gốc: `python3 learning/practice/models/market_returns.py`. Không tra dữ liệu thị trường hay chọn tỷ trọng. Kiểm thử ở `tests/test_market_returns.py`; đầu vào thật AppleFY2025 và VOO30/09/2026 ghi nguồn trong các bài.

- `risk_performance.py`: H3/H4 — chuỗi lợi suất, độ lệch chuẩn mẫu, drawdown, hồi phục, sổ mua tĩnh, TWR, NPV, IRR có kẹp và XIRR ngày thực/365. Bộ giải trả một nghiệm trong khoảng đổi dấu, không chứng minh nghiệm duy nhất. Chạy `python3 learning/practice/models/risk_performance.py`; kiểm ở `tests/test_risk_performance.py`.
- `evidence_lab.py`: H5 — dữ liệu A/B/C hư cấu để kiểm chọn mẫu, ngoài mẫu và chi phí; lịch ngày công bố để phát hiện nhìn trước; xác suất dương giả chỉ trong mô hình độc lập đã nêu. Chạy `python3 learning/practice/models/evidence_lab.py`; kiểm ở `tests/test_evidence_lab.py`. Không tìm quy tắc sinh lời, không gửi lệnh.
- Nguồn nhóm H3–H5: `data/raw/learning-wave4-group2-sources-2026-11-02.json`; bản nguồn lớn đã Git ignore, có checksum trong manifest. Số S&P là số năm làm tròn trong thư Berkshire2024, không phải dữ liệu hiện hành hay lợi suất quỹ sau phí.
- `geico_berkshire_fy2025_inputs.csv`: số lịch sử từ Form 10-K FY2025 của JPMorgan Chase và Berkshire Hathaway/GEICO (triệu USD), BCTC hợp nhất kiểm toán FY2025 của Tập đoàn Bảo Việt (`BVH`) và BCTC hợp nhất Q4/2025 của Bảo hiểm BIDV (`BIC`, triệu VND), mở 2026-11-05.
- `insurance.py`: bài 013, F8, P4 — cầu nối thu nhập và dự phòng ngân hàng, cầu nối phí bảo hiểm phi nhân thọ (`GWP`/`NWP`/`UPR`/`NEP`, tỷ lệ bồi thường, tỷ lệ chi phí, tỷ lệ kết hợp, chi phí `float`), các phương pháp dự phòng phí chưa được hưởng (`25%/50%`, `1/8`, `1/24`, theo ngày), tam giác phát triển bồi thường `Chain-Ladder` (tái lập bảng mẫu Điều 36 Văn bản hợp nhất `44/2026/VBHN-TT-BTC`), cuộn số dư `CSM` theo `IFRS 17`, trần lãi suất kỹ thuật bảo hiểm nhân thọ (`80%` lợi suất TPCP $\ge 10$ năm), biên khả năng thanh toán và tỷ lệ loại trừ tài sản (Mẫu biểu `7-PNT`), và mô hình so sánh dòng tiền bảo hiểm liên kết đầu tư (`UL`/`ILP`) với phương án mua bảo hiểm tử kỳ thuần túy cộng tự đầu tư phần chênh lệch. Chạy `python3 learning/practice/models/insurance.py`; kiểm ở `tests/test_insurance_models.py`.
