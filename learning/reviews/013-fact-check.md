# Biên bản kiểm nguồn — Bài 013

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-05 10:52 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-05 09:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; tìm kiếm/mở nguồn trọng yếu (JPMorgan Chase FY2025 10-K, Berkshire Hathaway FY2025 10-K, IFRS 17, FASB ASU 2018-12 LDTI, Thông tư 232/2012/TT-BTC); tái tính ví dụ và toàn bộ 10 bài tập cùng hàm trong learning/practice/models/insurance.py.`
- Báo cáo đích: `learning/lessons/013-banks-insurers.md`
- SHA-256 nội dung đích: `e3dd723f16ce65b3f20c751b4aecd2f139a80acf97772382cc797eb95abcf7f2`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập `source-fact-checker` (Vòng 1 và Vòng 2) ngày 05/11/2026 trên bản nháp cố định (`shasum -a 256`: `0ce17d31bca8685f53733e6e4dd34843ba3ce08a2dc8233b145b59e14387841f`); người kiểm không sửa bài.

## Các nguồn Internet và hồ sơ gốc đã đối chiếu trong lượt kiểm duyệt

| Nguồn / URL | Ngày xuất bản / kỳ / phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [JPMorgan Chase & Co. — FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/19617/000001961726000289/jpm-20251231.htm) | Nộp 13/02/2026; kỳ 31/12/2025; Hoa Kỳ; US GAAP; triệu USD | 2026-11-05 | Đối chiếu số liệu kết quả kinh doanh, bảng cân đối, dự phòng `LLR`/`ACL` và vốn `CET1` |
| [Berkshire Hathaway Inc. — FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1067983/000106798326000009/brka-20251231.htm) | Nộp 02/03/2026; kỳ 31/12/2025; Hoa Kỳ; US GAAP; triệu USD | 2026-11-05 | Đối chiếu số liệu `GEICO` (`GWP`, `NEP`, `Losses & LAE`, `UW Expenses`, `Combined Ratio`) và `Float` hợp nhất |
| [IFRS Foundation — IFRS 17 Insurance Contracts](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/) | Ban hành 05/2017, sửa đổi 06/2020, hiệu lực 01/01/2023; toàn cầu | 2026-11-05 | Đối chiếu cơ chế `CSM`, `GMM`/`VFA`/`PAA` và `Onerous Contracts` |

## Phát hiện và kiểm tra

1. **Ngân hàng (`JPMorgan Chase FY2024–FY2025`):**
   - `SỰ_THẬT` & `PHÉP_TÍNH`: `NII` Reported GAAP = `$95.443M` (`FY2024`: `$92.583M`; Managed FTE = `$95.868M`, `NIM` = `2,54%`, tr. 47, 59, 165); `Noninterest Revenue` = `$87.004M` (`FY2024`: `$84.973M`); `TOI` = `95.443 + 87.004 = $182.447M`; `Noninterest Expense` = `$95.640M` (`CIR` = `52,42%`); `PPOP` = `$86.807M`; `Provision for Credit Losses` = `$14.212M` (`16,37%` `PPOP`); `EBT` = `$72.595M`; `Net Income` = `$57.048M`.
   - Bảng cân đối & vốn (tr. 44, 61, 94, 111, 167): `Total Assets` = `$4.424.900M`, `Loans` = `$1.493.429M`, `Deposits` = `$2.559.320M`, `LLR` nội bảng = `$25.765M`, tổng `ACL` = `$31.230M`, `NPA` = `$10.359M`, `CET1 Capital` = `$288.469M`, `RWA Standardized` = `$1.981.692M` (`14,56%`, báo cáo `14,6%`), `RWA Advanced` = `$2.045.249M` (`14,10%`, báo cáo `14,1%`).
2. **Bảo hiểm (`GEICO` & `Berkshire Hathaway Insurance FY2023–FY2025`):**
   - `SỰ_THẬT` & `PHÉP_TÍNH`: `GEICO` `Premiums Written` = `$45.193M` (`FY2024`: `$42.916M`, `FY2023`: `$39.837M`), `NEP` = `$44.481M` ($\Delta\text{UPR} = +712\text{M}$), `Losses & LAE` = `$32.144M` (`Loss Ratio` = `72,2646%`, báo cáo `72,3%`), `UW Expenses` = `$5.513M` (`Expense Ratio` = `12,3941%`, báo cáo `12,4%`), `Combined Ratio` = `84,6586%` (báo cáo `84,7%`), `Pre-tax UW Gain` = `$6.824M` (`FY2024`: `$7.813M`, `FY2023`: `$3.635M`, `FY2022` lỗ `-$1.880M`, `CR` = `104,8%`).
   - Hợp nhất bảo hiểm `Berkshire`: `Pre-tax UW Gain` = `6.824 + 785 + 1.851 = $9.460M` (sau thuế `$7.258M`), `Pre-tax Investment Income` = `$15.261M` (sau thuế `$12.513M`), `Float` cuối 2025 = `$176.000M` (2024: `$171.000M`, 2023: `$169.000M`), `Cost of Float` trên `Float` bình quân (`$173.500M`) = `-9.460 / 173.500 = -5,4524%`.
3. **Chuẩn mực kế toán & khớp mô hình thực hành:**
   - Khớp 100% tên hàm và đầu ra trong [`learning/practice/models/insurance.py`](../practice/models/insurance.py): `bank_operating_bridge()`, `pc_underwriting_bridge()`, `ifrs17_csm_rollforward()`, `reserve_understatement_adjustment()`. Toàn bộ 10 bài tập tính tay và bài tập làm sạch dữ liệu bẩn khớp số học.

## Hạn chế của lần kiểm duyệt

Không đo hiệu quả học thực tế; các ví dụ định giá `Justified P/B` và `RIM` là phép tính mô hình trên giả định đầu vào (`SUY_LUẬN` / `KỊCH_BẢN`), không phải khuyến nghị mua/bán cổ phiếu `JPM` hay `BRK`.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả.
