# Sổ kiểm duyệt bài học

> **Cập nhật 2026-11-02:** bốn bài Q1–Q4 (Đợt 3) đã qua hai nhánh độc lập (Q2, Q4 ở vòng 5; Q1, Q3 ở vòng 6) và qua cổng `validate_report.py`. Tiêu chí ĐẠT từ vòng 4: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; điểm trung bình và thấp còn mở được liệt kê trong biên bản. Nhật ký các vòng: [Q-round-1](Q-round-1.md), [Q-round-2](Q-round-2.md), [Q-round-3](Q-round-3.md), [Q-round-4](Q-round-4.md), [Q-round-5-6](Q-round-5-6.md); đây là tóm lược của điều phối viên, không phải biên bản ĐẠT.

> **Cập nhật 2026-10-31:** bài 010, 011, 012, F1, F2 đã viết lại theo [chuẩn chiều sâu](../../docs/LESSON_DEPTH_STANDARD.md), qua bốn vòng kiểm nguồn và phản biện độc lập, và **đã qua cổng xuất bản** (`validate_report.py`) với biên bản khớp mã băm ở bảng dưới. Biên bản ghi đè cùng tên tệp (bản cũ trong lịch sử git). Giữ các điểm Thấp còn mở trong biên bản: chưa có nguồn mở được cho Fisher dạng nhân, quan hệ sạch của RIM, thiểu số và chi phí trụ sở trong SOTP; giá AAPL 345 USD chỉ từ nguồn thứ cấp.

- Cập nhật: `2026-10-27`.
- **52 bài trong bảng** đã qua hai nhánh độc lập: kiểm nguồn và phản biện rủi ro; mỗi bài có hai biên bản khớp cùng phiên bản nội dung. Ngoài bảng, [hồ sơ Apple mẫu](../../research/companies/US/AAPL/report.md) có hai biên bản riêng.
- Đã chạy cổng cấu trúc cho 52 bài trong bảng với 104 biên bản và hồ sơ Apple với hai biên bản riêng. Cổng cấu trúc không thay kiểm nguồn và không chứng minh hiệu quả học thực tế.
- **N2 và N3** (soạn trong một phiên Claude Code cùng ngày) đã qua cả hai nhánh, nhiều vòng, trên đúng mã băm ở bảng dưới. **Bài 001** đạt kiểm nguồn cho phần đổi trong đợt này nhưng **chưa** qua phản biện rủi ro.
- **9 bài cũ còn lại** (002–009) không được tuyên bố kiểm duyệt toàn bộ trong đợt này. Thay đổi của chúng chủ yếu là điều hướng/chia phiên; xem trạng thái và mốc nguồn trong từng bài.
- **Đợt 6:** K1–K2 và hồ sơ Apple qua hai nhánh; K2 còn điểm phản biện trung bình về bối cảnh 8-K, hồ sơ Apple còn hai điểm trung bình về chuỗi cung ứng và App Store.
- **Đợt 5:** F1–F7 đã qua hai nhánh; F4 và F7 còn điểm phản biện mức trung bình, F5 còn giới hạn khung ngành.
- **Đợt 4:** M1–M3, H1–H6 đã qua hai nhánh; phản biện M2, M3, H1 còn điểm trung bình và M1, H3, H6 còn điểm thấp, xem biên bản.
- **Đợt 3:** A1–A5 đã qua hai nhánh; A3, A4, A5 còn điểm phản biện chưa xử lý, xem biên bản.
- **Đợt 2:** V3–V5, B1–B2, L1–L3 đã qua hai nhánh. Phản biện V5 còn một điểm trung bình về quy mô ảnh hưởng của room; xem biên bản.
- **Đợt 1:** B3, P1–P3, V1–V2 đã qua hai nhánh trên phiên bản ở bảng. Các mục `CHƯA_BIẾT` vẫn là giới hạn nội dung, không được hiểu là đã xác minh.

| Bài | Nội dung | Kiểm nguồn | Phản biện | Phiên bản |
|---|---|---|---|---|
| [Q1](../lessons/Q1-earnings-quality-toolkit.md) | Đợt 3, kiểm duyệt 2026-11-02 | [ĐẠT](Q1-fact-check.md) | [ĐẠT](Q1-risk-review.md) | `24094d79412f…` |
| [Q3](../lessons/Q3-normalizing-earnings-cyclical.md) | Đợt 3, kiểm duyệt 2026-11-02 | [ĐẠT](Q3-fact-check.md) | [ĐẠT](Q3-risk-review.md) | `3b543db8af30…` |
| [Q2](../lessons/Q2-sbc-dilution-buybacks-dividends.md) | Đợt 3, kiểm duyệt 2026-11-02 | [ĐẠT](Q2-fact-check.md) | [ĐẠT](Q2-risk-review.md) | `e84b15a0bf43…` |
| [Q4](../lessons/Q4-getting-data-edgar-xbrl-vietnam.md) | Đợt 3, kiểm duyệt 2026-11-02 | [ĐẠT](Q4-fact-check.md) | [ĐẠT](Q4-risk-review.md) | `d08f14b282f9…` |
| [K1](../lessons/K1-screening-watchlist.md) | Đã soạn | [ĐẠT](K1-fact-check.md) | [ĐẠT](K1-risk-review.md) | `63a29010c308…` |
| [K2](../lessons/K2-failure-case-postmortem.md) | Đã soạn | [ĐẠT](K2-fact-check.md) | [ĐẠT](K2-risk-review.md) | `50c2292f7720…` |
| [F1](../lessons/F1-three-statement-model-sensitivity.md) | Viết lại 2026-10-31 | [ĐẠT](F1-fact-check.md) | [ĐẠT](F1-risk-review.md) | `3f2c5014c1bf…` |
| [F2](../lessons/F2-valuation-ddm-residual-sotp.md) | Viết lại 2026-10-31 | [ĐẠT](F2-fact-check.md) | [ĐẠT](F2-risk-review.md) | `60b77fa667db…` |
| [F3](../lessons/F3-vietnam-property-developers.md) | Đã soạn | [ĐẠT](F3-fact-check.md) | [ĐẠT](F3-risk-review.md) | `1956dcc04ee7…` |
| [F4](../lessons/F4-vietnam-bank-analysis.md) | Đã soạn | [ĐẠT](F4-fact-check.md) | [ĐẠT](F4-risk-review.md) | `4cbad2b67bbf…` |
| [F5](../lessons/F5-vietnam-industry-research-framework.md) | Đã soạn | [ĐẠT](F5-fact-check.md) | [ĐẠT](F5-risk-review.md) | `5da2dcecdeef…` |
| [F6](../lessons/F6-governance-related-party-audit.md) | Đã soạn | [ĐẠT](F6-fact-check.md) | [ĐẠT](F6-risk-review.md) | `a578a828fce3…` |
| [F7](../lessons/F7-special-situations-restructuring.md) | Đã soạn | [ĐẠT](F7-fact-check.md) | [ĐẠT](F7-risk-review.md) | `e79742eb0858…` |
| [M1](../lessons/M1-monetary-policy-rates-fx-credit.md) | Đã soạn | [ĐẠT](M1-fact-check.md) | [ĐẠT](M1-risk-review.md) | `96d43e00bc57…` |
| [M2](../lessons/M2-credit-real-estate-cycle.md) | Đã soạn | [ĐẠT](M2-fact-check.md) | [ĐẠT](M2-risk-review.md) | `593cf2be2e8c…` |
| [M3](../lessons/M3-capital-trade-geopolitics.md) | Đã soạn | [ĐẠT](M3-fact-check.md) | [ĐẠT](M3-risk-review.md) | `7c95dae89eee…` |
| [H1](../lessons/H1-behavioral-biases.md) | Đã soạn | [ĐẠT](H1-fact-check.md) | [ĐẠT](H1-risk-review.md) | `e7fbb0af3df1…` |
| [H2](../lessons/H2-decisions-stress-position-size.md) | Đã soạn | [ĐẠT](H2-fact-check.md) | [ĐẠT](H2-risk-review.md) | `9ffcffd48e3b…` |
| [H3](../lessons/H3-risk-volatility-drawdown-liquidity.md) | Đã soạn | [ĐẠT](H3-fact-check.md) | [ĐẠT](H3-risk-review.md) | `7dac5d06fd65…` |
| [H4](../lessons/H4-twr-mwr-benchmark.md) | Đã soạn | [ĐẠT](H4-fact-check.md) | [ĐẠT](H4-risk-review.md) | `bb8e025a413b…` |
| [H5](../lessons/H5-statistics-backtest-overfitting.md) | Đã soạn | [ĐẠT](H5-fact-check.md) | [ĐẠT](H5-risk-review.md) | `cd1cac9443a0…` |
| [H6](../lessons/H6-technical-analysis-market-microstructure.md) | Đã soạn | [ĐẠT](H6-fact-check.md) | [ĐẠT](H6-risk-review.md) | `7892d145a3d7…` |
| [A1](../lessons/A1-deposits-government-corporate-bonds.md) | Đã soạn | [ĐẠT](A1-fact-check.md) | [ĐẠT](A1-risk-review.md) | `bd4073d72bbd…` |
| [A2](../lessons/A2-mutual-funds-etfs-fees.md) | Đã soạn | [ĐẠT](A2-fact-check.md) | [ĐẠT](A2-risk-review.md) | `c0c31fbe6257…` |
| [A3](../lessons/A3-gold-currency-property-crypto.md) | Đã soạn | [ĐẠT](A3-fact-check.md) | [ĐẠT](A3-risk-review.md) | `afabf7d47089…` |
| [A4](../lessons/A4-allocation-correlation-rebalancing.md) | Đã soạn | [ĐẠT](A4-fact-check.md) | [ĐẠT](A4-risk-review.md) | `0d49859d4b92…` |
| [A5](../lessons/A5-international-investing-currency-tax.md) | Đã soạn | [ĐẠT](A5-fact-check.md) | [ĐẠT](A5-risk-review.md) | `fbe8247a3637…` |
| [V3](../lessons/V3-corporate-actions.md) | Đã soạn | [ĐẠT](V3-fact-check.md) | [ĐẠT](V3-risk-review.md) | `407eff684ca5…` |
| [V4](../lessons/V4-disclosure-and-source-tracing.md) | Đã soạn | [ĐẠT](V4-fact-check.md) | [ĐẠT](V4-risk-review.md) | `7d65b22c73c8…` |
| [V5](../lessons/V5-index-foreign-room-upgrade.md) | Đã soạn | [ĐẠT](V5-fact-check.md) | [ĐẠT](V5-risk-review.md) | `2d3bfe38c78f…` |
| [B1](../lessons/B1-broker-fees-custody.md) | Đã soạn | [ĐẠT](B1-fact-check.md) | [ĐẠT](B1-risk-review.md) | `f749dce8337f…` |
| [B2](../lessons/B2-margin-leverage.md) | Đã soạn | [ĐẠT](B2-fact-check.md) | [ĐẠT](B2-risk-review.md) | `42338ff511e4…` |
| [L1](../lessons/L1-insider-trading-manipulation-disclosure.md) | Đã soạn | [ĐẠT](L1-fact-check.md) | [ĐẠT](L1-risk-review.md) | `1d77c6d7fbbd…` |
| [L2](../lessons/L2-minority-shareholder-rights.md) | Đã soạn | [ĐẠT](L2-fact-check.md) | [ĐẠT](L2-risk-review.md) | `a45f281c9ad9…` |
| [L3](../lessons/L3-personal-income-tax-reporting.md) | Đã soạn | [ĐẠT](L3-fact-check.md) | [ĐẠT](L3-risk-review.md) | `1ae218402b9a…` |
| [B3](../lessons/B3-account-security-scams.md) | Đã soạn | [ĐẠT](B3-fact-check.md) | [ĐẠT](B3-risk-review.md) | `6e63d8d9fae5…` |
| [P1](../lessons/P1-budget-emergency-fund-insurance.md) | Đã soạn | [ĐẠT](P1-fact-check.md) | [ĐẠT](P1-risk-review.md) | `089cda636e1e…` |
| [P2](../lessons/P2-personal-debt.md) | Đã soạn | [ĐẠT](P2-fact-check.md) | [ĐẠT](P2-risk-review.md) | `e9675a0e3d88…` |
| [P3](../lessons/P3-goals-risk-ips.md) | Đã soạn | [ĐẠT](P3-fact-check.md) | [ĐẠT](P3-risk-review.md) | `19cec10b2058…` |
| [V1](../lessons/V1-vietnam-market-structure.md) | Đã soạn | [ĐẠT](V1-fact-check.md) | [ĐẠT](V1-risk-review.md) | `17e384b64beb…` |
| [V2](../lessons/V2-vietnam-trading-rules.md) | Đã soạn | [ĐẠT](V2-fact-check.md) | [ĐẠT](V2-risk-review.md) | `f7e01717e1a8…` |
| [010](../lessons/010-cost-of-capital.md) | Viết lại 2026-10-31 | [ĐẠT](010-fact-check.md) | [ĐẠT](010-risk-review.md) | `fe0471055e63…` |
| [011](../lessons/011-dcf-reverse-dcf.md) | Viết lại 2026-10-31 | [ĐẠT](011-fact-check.md) | [ĐẠT](011-risk-review.md) | `7ab38cae7ce6…` |
| [012](../lessons/012-scenarios-margin-of-safety.md) | Viết lại 2026-10-31 | [ĐẠT](012-fact-check.md) | [ĐẠT](012-risk-review.md) | `9ea42a6923c5…` |
| [013](../lessons/013-banks-insurers.md) | Đã soạn | [ĐẠT](013-fact-check.md) | [ĐẠT](013-risk-review.md) | `1754fcda84e8…` |
| [014](../lessons/014-industry-capital-cycle.md) | Đã soạn | [ĐẠT](014-fact-check.md) | [ĐẠT](014-risk-review.md) | `29cd0d6544ba…` |
| [015](../lessons/015-behavior-decision-journal.md) | Đã soạn | [ĐẠT](015-fact-check.md) | [ĐẠT](015-risk-review.md) | `0a5126787c5b…` |
| [016](../lessons/016-company-research-capstone.md) | Đã soạn | [ĐẠT](016-fact-check.md) | [ĐẠT](016-risk-review.md) | `5e3299c48e83…` |
| [N1](../lessons/N1-market-basics.md) | Đã soạn | [ĐẠT](N1-fact-check.md) | [ĐẠT](N1-risk-review.md) | `17f84bb54a24…` |
| [N4](../lessons/N4-time-value-returns.md) | Đã soạn | [ĐẠT](N4-fact-check.md) | [ĐẠT](N4-risk-review.md) | `b6eae1288f29…` |
| [N5](../lessons/N5-portfolio-index-investing.md) | Đã soạn | [ĐẠT](N5-fact-check.md) | [ĐẠT](N5-risk-review.md) | `19614c988878…` |
| [N6](../lessons/N6-business-model-unit-economics.md) | Đã soạn | [ĐẠT](N6-fact-check.md) | [ĐẠT](N6-risk-review.md) | `525824d368db…` |
| [N7](../lessons/N7-data-probability-uncertainty.md) | Đã soạn | [ĐẠT](N7-fact-check.md) | [ĐẠT](N7-risk-review.md) | `99cb2d79cc25…` |
| [N8](../lessons/N8-finding-verifying-sources.md) | Đã soạn | [ĐẠT](N8-fact-check.md) | [ĐẠT](N8-risk-review.md) | `3ad1116c84ff…` |
| [N2](../lessons/N2-statement-line-items.md) | Đã soạn | [ĐẠT](N2-fact-check.md) | [ĐẠT](N2-risk-review.md) | `a9d024fae646…` |
| [N3](../lessons/N3-vietnam-vas-statements.md) | Đã soạn (A/B) | [ĐẠT](N3-fact-check.md) | [ĐẠT](N3-risk-review.md) | `4a9358fa8819…` |
| [001](../lessons/001-business-financial-statements.md) | Sửa cấu trúc | [ĐẠT](001-fact-check.md) — phần đổi | Chưa chạy | `45eb073f910d…` |

## Phạm vi và giới hạn còn lại

- N1: đã thêm nguồn thanh khoản; N5: đã thêm tái cân bằng và nguồn phân biệt lợi suất giá/tổng lợi suất.
- 013: định nghĩa chính dùng Fed và NAIC; nhánh kiểm nguồn không mở trực tiếp được PDF OCC/Allstate gốc, đã ghi giới hạn và nguồn đối chiếu bổ sung trong biên bản.
- 015/016: đã bổ sung ngày công bố/ngày nộp hồ sơ; 016 có bảng thực hành và giữ riêng dữ kiện Apple với kịch bản hư cấu.
- Mọi tỷ lệ thuế/phí giả định chỉ là đầu vào bài tập. Chưa xác minh mức áp dụng cho một cá nhân/thị trường cụ thể.
- N3: văn bản gốc TT 43 (Công báo) và phụ lục mẫu biểu TT 99 vẫn chưa mở được; mã mới đối chiếu trên báo cáo thật của VNM và bản sao LuatVietnam. Ghi chú thấp N3-9 đến N3-12 đã xử lý ở bản cuối.
- N2: ghi chú thấp N2-6 đã xử lý ở bản cuối.
- Nguồn AERO có bất đồng metadata ở review trước, vẫn giữ ngày chưa xác minh; không dùng ngày ấy làm luận cứ.
- Chưa có dữ liệu người học thực tế. Thời lượng và khả năng chuyển kiến thức cần tiếp tục quan sát.

## Khi sửa nội dung

Tính lại mã băm, kiểm lại nguồn/phản biện khi nội dung trọng yếu đổi. Không sửa biên bản để khớp một bài chưa được người kiểm đọc. Trạng thái hai dòng vòng đời được chuẩn hóa theo script; thay nội dung bài không được chuẩn hóa bỏ qua.
