# Bắt đầu học tại đây

> **Cập nhật học phần Bảo hiểm, Ngân hàng, Vĩ mô, Tài sản & Kế toán bậc S (05/11/2026):** Đã nâng cấp [Bài 013 — Ngân hàng và bảo hiểm](lessons/013-banks-insurers.md), bổ sung 2 bài bậc S mới về bảo hiểm tại Việt Nam ([Bài F8 — Phân tích doanh nghiệp bảo hiểm Việt Nam (`BVH`, `PVI`, `BIC`)](lessons/F8-vietnam-insurance-analysis.md), [Bài P4 — Đọc hợp đồng bảo hiểm cá nhân (`Term Life`, `UL`, `ILP`)](lessons/P4-personal-insurance-contracts-and-costs.md) kèm [`practice/models/insurance.py`](practice/models/insurance.py)), đồng thời nâng cấp toàn bộ 13 bài thuộc cụm chuyên ngành – tài sản – vĩ mô – chu kỳ (`F3–F7`, `A1–A4`, `M1–M3`, `014`) và 2 bài nền kế toán (`N2`, `N3`) lên chuẩn bậc S. Tổng hiện có **33/67 bài đạt chuẩn cấu trúc bậc S**.
>
> **Nâng chiều sâu 02/11/2026, nhóm H3–H5:** ba bài đạt bậc S, có 10 bài tập/đáp án mỗi bài, mô hình Python và hai nhánh kiểm duyệt độc lập cùng phiên bản. Xem [nhật ký nhóm 2](reviews/wave4-group2-2026-11-02.md) và [sổ kiểm duyệt](reviews/README.md) để đọc các hạn chế còn mở.

- Cập nhật cấu trúc: `2026-11-05`.
- Hiện có **67 mã bài đã soạn**: 001–016, N1–N8, 39 bài Đợt 1–6 (bổ sung `P4`, `F8`) và Q1–Q4. Mã là địa chỉ, không phải thứ tự đọc; trạng thái kiểm duyệt từng bài xem tại sổ kiểm duyệt.
- Trạng thái từng bài mới và biên bản đúng phiên bản: [sổ kiểm duyệt](reviews/README.md). Bài đã soạn không tự đồng nghĩa đã kiểm duyệt.
- [Lộ trình và chuẩn học](roadmap.md), [đối chiếu 51 mục](coverage-51.md), [thuật ngữ](glossary.md), [bảng thực hành](practice/research-and-model-worksheets.md), [review gốc và nhật ký triển khai](review-and-expansion-plan-2026-10-26.md).

Nâng chiều sâu Đợt4: N1, N4, N5 đã đạt bậcS và qua hai nhánh trên bản chốt02/11/2026; xem [nhật ký](reviews/wave4-group1-2026-11-02.md), [mô hình](practice/models/market_returns.py). ĐẠT không thay việc học thử với người thật.

## Nhánh 1 — Hiểu doanh nghiệp và phân tích cổ phiếu

| Thứ tự | Bài | Kết quả cần làm được |
|---|---|---|
| 1 | [N1 — Thị trường chứng khoán](lessons/N1-market-basics.md) | Phân biệt sở hữu, cấp vốn mới và mua bán lại |
| 2 | [N6 — Doanh nghiệp kiếm tiền thế nào](lessons/N6-business-model-unit-economics.md) | Giải thích khách hàng, sản phẩm, phần đóng góp, hòa vốn |
| 3 | [001 — Ba báo cáo tài chính](lessons/001-business-financial-statements.md) | Tách doanh thu, lợi nhuận, tiền |
| 4 | [N2 — Từng dòng báo cáo](lessons/N2-statement-line-items.md) | Học ba phiên: giao dịch → tầng lợi nhuận → tỷ số |
| 5 | [N8 — Tìm và kiểm nguồn](lessons/N8-finding-verifying-sources.md) | Truy đúng hồ sơ, kỳ, đơn vị và phạm vi |
| 6 | [N3 phần A — Tìm đường trên báo cáo Việt Nam](lessons/N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2) | Ghi đúng thông tin và tìm tên chỉ tiêu; dừng trước phần B |
| 7 | [002 — Ba câu hỏi trước khi gọi cổ phiếu rẻ](lessons/002-finding-a-cheap-stock.md) | Tách giá mỗi cổ phần với giá trị doanh nghiệp |
| 8 | [N4 — Thời gian và lợi suất](lessons/N4-time-value-returns.md) | Tính lãi kép, hiện tại/tương lai và sức mua |
| 9 | [003 — Lợi thế cạnh tranh và ROIC](lessons/003-business-quality-moat-and-roic.md) | Học ba phiên, chi phí vốn trước mắt là giả định cho sẵn |
| 10 | [004 — Dòng tiền và chất lượng lợi nhuận](lessons/004-cash-flow-and-earnings-quality.md) | Dựng cầu nối lợi nhuận–tiền |
| 11 | [005 — Nợ và thanh khoản](lessons/005-debt-liquidity-survival.md) | Phân biệt trả lãi với sống sót qua đáo hạn |
| 12 | [006 — Phân bổ vốn và quản trị](lessons/006-capital-allocation-governance.md) | Đọc doanh nghiệp dùng vốn ra sao |
| 13 | [007 — Thuyết minh và cờ đỏ](lessons/007-notes-and-accounting-red-flags.md) | Tìm chính sách, ước tính và dữ liệu cần kiểm |
| 14 | [008 — Vĩ mô truyền dẫn](lessons/008-macro-transmission.md) | Nối giá/lãi suất/tỷ giá với hoạt động |
| 15 | [009 — Bội số định giá](lessons/009-valuation-multiples.md) | Chọn tử/mẫu và nhóm so sánh phù hợp |
| 16 | [N3 phần B — Đối chiếu và điều chỉnh](lessons/N3-vietnam-vas-statements.md#phần-b--đối-chiếu-và-điều-chỉnh-chỉ-học-sau-bài-009) | Quay lại phần sâu sau 004–009 |
| 17 | [N7 — Dữ liệu và bất định](lessons/N7-data-probability-uncertainty.md) | Không nhầm mốc, mẫu số, kỳ vọng và bằng chứng |
| 18 | [N5 — Danh mục và quỹ chỉ số](lessons/N5-portfolio-index-investing.md) | A khái niệm, B đo kết quả/phí/tái cân bằng |
| 19 | [010 — Chi phí vốn](lessons/010-cost-of-capital.md) | Tính và kiểm giả định WACC |
| 20 | [011 — DCF và định giá ngược](lessons/011-dcf-reverse-dcf.md) | Đọc giả định sau khoảng giá trị |
| 21 | [012 — Kịch bản và biên an toàn](lessons/012-scenarios-margin-of-safety.md) | Tính chi phí và điều kiện bác bỏ |
| — | [Q4 — Lấy dữ liệu: EDGAR/XBRL, báo cáo Việt Nam, bảng tính](lessons/Q4-getting-data-edgar-xbrl-vietnam.md) | Đã kiểm duyệt (2026-11-02); học sau N8 và V4 |
| — | [Q2 — SBC, pha loãng, mua lại, cổ tức](lessons/Q2-sbc-dilution-buybacks-dividends.md) | Đã kiểm duyệt (2026-11-02); học sau 006 và 011 |
| — | [Q1 — Chất lượng lợi nhuận có công cụ](lessons/Q1-earnings-quality-toolkit.md) | Đã kiểm duyệt (2026-11-02); học sau 004, 005 và 007 |
| — | [Q3 — Chuẩn hóa lợi nhuận và công ty chu kỳ](lessons/Q3-normalizing-earnings-cyclical.md) | Đã kiểm duyệt (2026-11-02); học sau 009 và 011 |
| 22 | [015 — Tâm lý và nhật ký](lessons/015-behavior-decision-journal.md) | Tách quy trình với kết quả; có thể dùng nghi thức nhẹ từ đầu |
| 23 | [016 — Bài tổng kết](lessons/016-company-research-capstone.md) | Tạo hồ sơ nguồn và mô hình truy lại được |

N5A có thể đọc sớm sau N1, **không phải điều kiện học 001**. Bảng có 23 lượt đọc vì N3 quay lại hai lần; không phải 23 mã bài trong nhánh.

## Nhánh 2 — Danh mục và quỹ

**N1 → N5A → N4 → N7 → N5B → bài tổng kết nhánh quỹ ngay trong N5.** Không bắt buộc học kế toán và DCF. Ví dụ N7 tự đủ đầu vào. Không có quỹ hay tỷ trọng cá nhân nào được đề xuất.

## Nhánh 3 — Tài chính cá nhân, Việt Nam và thực thi

Sáu bài Đợt 1 đã qua hai nhánh kiểm duyệt; các mục chưa biết vẫn được ghi trong bài. Xem [sổ kiểm duyệt](reviews/README.md) trước khi dùng:

1. [P1 — Ngân sách, quỹ khẩn cấp, bảo hiểm](lessons/P1-budget-emergency-fund-insurance.md) → [P2 — Nợ cá nhân](lessons/P2-personal-debt.md) → [P3 — Mục tiêu và chính sách cá nhân](lessons/P3-goals-risk-ips.md) → [P4 — Đọc hợp đồng bảo hiểm cá nhân: cấu trúc phí, điều khoản loại trừ và ranh giới bảo vệ – đầu tư](lessons/P4-personal-insurance-contracts-and-costs.md) *(bậc S)*.
2. [B3 — Bảo mật tài khoản và lừa đảo](lessons/B3-account-security-scams.md): học trước khi chuyển tiền cho bên tự nhận là đơn vị đầu tư.
3. [V1 — Cấu trúc thị trường Việt Nam](lessons/V1-vietnam-market-structure.md) → [V2 — Quy tắc giao dịch](lessons/V2-vietnam-trading-rules.md). Quy tắc thay đổi theo thời gian; kiểm lại nguồn hiện hành trước khi áp dụng.

Đợt 2: [V3 — Sự kiện doanh nghiệp](lessons/V3-corporate-actions.md), [V4 — Công bố thông tin](lessons/V4-disclosure-and-source-tracing.md), [V5 — Chỉ số và room](lessons/V5-index-foreign-room-upgrade.md), [B1 — Phí và lưu ký](lessons/B1-broker-fees-custody.md), [B2 — Ký quỹ](lessons/B2-margin-leverage.md) đã qua hai nhánh; [L1 — Thông tin nội bộ](lessons/L1-insider-trading-manipulation-disclosure.md), [L2 — Quyền cổ đông](lessons/L2-minority-shareholder-rights.md), [L3 — Thuế và hồ sơ](lessons/L3-personal-income-tax-reporting.md) cũng đã qua hai nhánh.

Các bài khác của kế hoạch đang chờ biên soạn; có thể bắt đầu nhật ký học hoặc quyết định bằng [mẫu nhật ký](../templates/decision-journal.md).

## Loại tài sản và phân bổ — Đợt 3

[A1 — Tiền gửi và trái phiếu](lessons/A1-deposits-government-corporate-bonds.md) → [A2 — Quỹ mở và ETF](lessons/A2-mutual-funds-etfs-fees.md) → [A3 — Vàng, ngoại tệ, bất động sản và tài sản mã hóa](lessons/A3-gold-currency-property-crypto.md) → [A4 — Phân bổ và tái cân bằng](lessons/A4-allocation-correlation-rebalancing.md) → [A5 — Đầu tư nước ngoài](lessons/A5-international-investing-currency-tax.md). Năm bài đã qua hai nhánh, nhưng thông tin pháp lý cụ thể và các điểm còn mở cần xem [sổ kiểm duyệt](reviews/README.md).

## Vĩ mô, hành vi và rủi ro — Đợt 4

[M1 — Tiền tệ, lãi suất và tín dụng](lessons/M1-monetary-policy-rates-fx-credit.md) → [M2 — Chu kỳ tín dụng và bất động sản](lessons/M2-credit-real-estate-cycle.md) → [M3 — Dòng vốn và thương mại](lessons/M3-capital-trade-geopolitics.md).

[H1 — Thiên kiến hành vi](lessons/H1-behavioral-biases.md) → [H2 — Quyết định khi bất định](lessons/H2-decisions-stress-position-size.md) → [H3 — Đo rủi ro](lessons/H3-risk-volatility-drawdown-liquidity.md) → [H4 — TWR và MWR](lessons/H4-twr-mwr-benchmark.md) → [H5 — Thống kê và backtest](lessons/H5-statistics-backtest-overfitting.md) → [H6 — Phân tích kỹ thuật và vi cấu trúc](lessons/H6-technical-analysis-market-microstructure.md). Chín bài đã qua hai nhánh; xem [các giới hạn và phản biện](reviews/README.md) trước khi dùng.

## Phân tích nâng cao — Đợt 5

[F1 — Mô hình ba báo cáo](lessons/F1-three-statement-model-sensitivity.md) → [F2 — Định giá nâng cao](lessons/F2-valuation-ddm-residual-sotp.md) → [F3 — Bất động sản](lessons/F3-vietnam-property-developers.md) → [F4 — Ngân hàng](lessons/F4-vietnam-bank-analysis.md) → [F8 — Bảo hiểm Việt Nam: dự phòng nghiệp vụ, tái bảo hiểm, đầu tư tài chính và vốn `RBC`](lessons/F8-vietnam-insurance-analysis.md) *(bậc S)* → [F5 — Khung sáu ngành](lessons/F5-vietnam-industry-research-framework.md) → [F6 — Quản trị](lessons/F6-governance-related-party-audit.md) → [F7 — Sự kiện đặc biệt](lessons/F7-special-situations-restructuring.md). Các bài qua hai nhánh; các hạn chế nguồn và điểm mở được giữ trong [sổ kiểm duyệt](reviews/README.md).

## Thực hành — Đợt 6

[K1 — Sàng lọc và watchlist](lessons/K1-screening-watchlist.md) → [K2 — Hậu kiểm Enron](lessons/K2-failure-case-postmortem.md); [danh sách đọc](reading-list.md), [mẫu watchlist](../watchlists/template.md), [hướng dẫn nhật ký](../journal/README.md) và [hồ sơ Apple mẫu](../research/companies/US/AAPL/report.md). K1–K2 và hồ sơ Apple có hai biên bản độc lập; các điểm còn mở xem trong từng biên bản. Khung ngành tại F5 chưa thay thế sáu hồ sơ ngành riêng.

## Nhánh chuyên ngành — chọn khi cần

- [013 — Ngân hàng và bảo hiểm: hai mô hình bảng cân đối ngược cần đọc riêng](lessons/013-banks-insurers.md) *(bậc S)*: ba buổi học (Ngân hàng `JPMorgan FY2025`, Phi nhân thọ & `Float` `Berkshire/GEICO FY2025`, Nhân thọ `IFRS 17` & Định giá `RIM`), dẫn tiếp sang [F8 — Bảo hiểm Việt Nam](lessons/F8-vietnam-insurance-analysis.md) và [P4 — Hợp đồng bảo hiểm cá nhân](lessons/P4-personal-insurance-contracts-and-costs.md).
- [014 — Kinh tế ngành và chu kỳ](lessons/014-industry-capital-cycle.md): học trước bài tổng kết khi cần phân tích công suất, cung/cầu và nhóm so sánh.

## Cách học một phiên

1. Nói lại câu hỏi của bài bằng lời mình.
2. Đọc một khối, tự làm trước khi xem đáp án.
3. Làm phần cốt lõi; phần luyện thêm dùng để đào sâu và chuyển tình huống.
4. Nếu chưa giải thích được kết quả, quay lại đúng chỗ vướng và thử một câu tương tự.
5. Ghi điều chưa hiểu; ôn lại ở phiên sau và sau một khoảng nghỉ.

Thử ba phiên đầu để quan sát nền tảng, thời gian và lỗi; chưa coi đó là chuẩn thời lượng cho cả khóa. Giáo trình chưa được thử nghiệm học thực tế với người dùng. Nội dung tài chính cũ giữ mốc dữ liệu và giới hạn kiểm duyệt riêng; khi áp dụng lại phải xác minh trực tuyến.
