# Sổ nguồn — Công ty Cổ phần PVI (PVI)

- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Mục đích: lưu vết nguồn cho hồ sơ học tập [report.md](report.md).
- Danh mục payload và mã băm SHA-256: xem [`data/raw/insurance-review-sources-2026-11-05.json`](../../../../data/raw/insurance-review-sources-2026-11-05.json).

| Mã | Nguồn và URL | Ngày công bố | Kỳ dữ liệu | Đơn vị / phạm vi | Loại | Giới hạn |
|---|---|---|---|---|---|---|
| S1 | [BCTC hợp nhất năm 2025 đã kiểm toán của CTCP PVI (PVI)](https://cafef1.mediacdn.vn/download/030326/pvi-bao-cao-tai-chinh-nam-2025-0-600196.pdf) | Ký ngày 15/02/2026 | Năm tài chính kết thúc 31/12/2025 (so sánh 2024 điều chỉnh lại) | VND; hợp nhất | Bản sao BCTC kiểm toán độc lập (Công ty TNHH PwC Việt Nam, số HAN 4235) lưu trên CDN CafeF | 65 trang, 22.514.367 byte; SHA-256 `2bc0badc1c60d2fdca5c6dbc0fd5e70ca31faf1e3bb0ce07f4fc6f4b8ebbf126`; đọc trực tiếp ảnh trang PDF 1–65; chưa khớp byte trực tiếp với miền pvi.com.vn/HNX |
| S2 | [Văn bản hợp nhất Luật Kinh doanh bảo hiểm số 31/VBHN-VPQH](https://congbao.chinhphu.vn/tai-ve-van-ban-so-31-vbhn-vpqh-46722-51065) | 2025 | Hiệu lực hiện hành | Văn bản luật | Gốc, Công báo Chính phủ | Quy định về đồng bảo hiểm, nhượng tái bảo hiểm và lộ trình vốn RBC 01/01/2028 |
| S3 | [Nghị định 46/2023/NĐ-CP](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/7/46-cp.signed.pdf) | 01/07/2023 | Hiệu lực hiện hành | Tỷ VND / % | Gốc, Chính phủ (PDF ký số) | Quy định dự phòng nghiệp vụ bảo hiểm phi nhân thọ, tái bảo hiểm và biên khả năng thanh toán |
| S4 | [Văn bản hợp nhất số 44/VBHN-BTC hợp nhất Thông tư 67/2023/TT-BTC](https://congbao.chinhphu.vn/tai-ve-van-ban-so-44-vbhn-btc-46909-51525) | 2025 | Hiệu lực hiện hành | % | Gốc, Bộ Tài chính (Công báo Chính phủ) | Quy định giới hạn đầu tư và phương pháp trích lập dự phòng nghiệp vụ |
| S5 | Thống kê toàn ngành bảo hiểm Việt Nam năm 2025 dẫn theo Cục Quản lý, giám sát bảo hiểm — Bộ Tài chính (`mof.gov.vn`, `tapchikinhtetaichinh.vn`, `pjico.com.vn`) | 2026 | FY2025 | Tỷ VND | Thứ cấp (bản tin tổng hợp dẫn nguồn Cục QLBH) | Doanh thu phí phi nhân thọ toàn ngành ước ~88.705–91.771 tỷ VND; chỉ dùng để ước tính khoảng thị phần |
| S6 | [Berkshire Hathaway Inc. 2025 Annual Report](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) | 2026 | FY2025 | Triệu USD; US GAAP | Gốc, công ty công bố | Dùng làm mốc đối chiếu quốc tế về bảo hiểm thương mại và tái bảo hiểm |

## Mâu thuẫn và mục chưa giải quyết

| Mục | Bằng chứng mâu thuẫn | Cách xử lý |
|---|---|---|
| Số liệu năm 2024 trên BCTC 2025 khác với BCTC 2024 công bố năm trước | Thuyết minh 35 (trang 58–62) công bố điều chỉnh hồi tố số liệu năm 2024 theo kiến nghị của Kiểm toán Nhà nước (`233/KTNN-TH` ngày `22/09/2025`) và phân loại lại doanh thu/chi phí tái bảo hiểm (`EBT` 2024 tăng từ `1.117,56 tỷ` lên `1.133,02 tỷ`, `NPAT` 2024 tăng từ `879,64 tỷ` lên `891,26 tỷ VND`) | Sử dụng nhất quán cột số liệu năm 2024 đã điều chỉnh lại trên BCTC kiểm toán năm 2025 và thuyết minh rõ nguyên nhân điều chỉnh hồi tố |
| Chênh lệch giữa EPS cơ bản trên báo cáo (`4.493 VND/CP`) và phép chia `NPAT mẹ / số cổ phiếu` (`4.708,50 VND/CP`) | Theo Thuyết minh 30 (trang 50), lợi nhuận phân bổ cho cổ đông sở hữu cổ phiếu phổ thông (`1.052,41 tỷ VND`) đã trừ khoản tạm trích quỹ khen thưởng, phúc lợi (`50,52 tỷ VND`) khỏi lợi nhuận sau thuế công ty mẹ (`1.102,93 tỷ VND`) | Ghi rõ cả EPS cơ bản sau trích quỹ khen thưởng phúc lợi (`4.493 VND/CP`) theo Thuyết minh 30 và lợi nhuận sau thuế công ty mẹ (`1.102,93 tỷ VND`) |
