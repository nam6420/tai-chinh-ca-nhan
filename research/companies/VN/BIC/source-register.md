# Sổ nguồn — Tổng Công ty Cổ phần Bảo hiểm Ngân hàng Đầu tư và Phát triển Việt Nam (BIC)

- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Mục đích: lưu vết nguồn cho hồ sơ học tập [report.md](report.md).
- Danh mục payload và mã băm SHA-256: xem [`data/raw/insurance-review-sources-2026-11-05.json`](../../../../data/raw/insurance-review-sources-2026-11-05.json).

| Mã | Nguồn và URL | Ngày công bố | Kỳ dữ liệu | Đơn vị / phạm vi | Loại | Giới hạn |
|---|---|---|---|---|---|---|
| S1 | [BCTC hợp nhất năm 2025 đã kiểm toán của Tổng Công ty Bảo hiểm BIDV (BIC)](https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/NAM/BIC_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf) | Ký ngày 20/03/2026 | Năm tài chính kết thúc 31/12/2025 (so sánh 2024 điều chỉnh lại) | VND; hợp nhất | Bản sao BCTC kiểm toán độc lập (Ernst & Young Việt Nam, số 12237572/E-68669225-HN) lưu trên CDN Vietstock | 86 trang, 4.964.127 byte; SHA-256 `c3cb5c109c0aa3ebe695476b7a6c90133885ccb65d88685797a066e10d1d45e2`; đọc trực tiếp ảnh trang PDF 1–86; chưa khớp byte trực tiếp với miền bic.vn/HOSE |
| S2 | [BCTC hợp nhất Quý 4/2025 và công văn giải trình 156/CV-KT của BIC](https://static2.vietstock.vn/vietstock/2026/1/30/20260130___bic___bao_cao_tai_chinh_hop_nhat_q4_2025_signed.pdf) | Ký ngày 23/01/2026 & 30/01/2026 | Quý 4/2025 và lũy kế năm 2025 trước kiểm toán | VND; hợp nhất | Bản sao BCTC Quý 4/2025 có chữ ký và con dấu lưu trên CDN Vietstock | 22 trang, 2.826.711 byte; SHA-256 `27d4788f34794923cd3c1989bfd30d72f8229a115ee3f2f86a9dd70e4e34f5d8`; dùng để đối chiếu chênh lệch trước/sau kiểm toán và giải trình bão lũ Q4/2025 |
| S3 | [Văn bản hợp nhất Luật Kinh doanh bảo hiểm số 31/VBHN-VPQH](https://congbao.chinhphu.vn/tai-ve-van-ban-so-31-vbhn-vpqh-46722-51065) | 2025 | Hiệu lực hiện hành | Văn bản luật | Gốc, Công báo Chính phủ | Quy định đại lý bảo hiểm qua tổ chức tín dụng và lộ trình vốn RBC 01/01/2028 |
| S4 | [Nghị định 46/2023/NĐ-CP](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/7/46-cp.signed.pdf) | 01/07/2023 | Hiệu lực hiện hành | Tỷ VND / % | Gốc, Chính phủ (PDF ký số) | Quy định dự phòng nghiệp vụ phi nhân thọ và biên khả năng thanh toán |
| S5 | [Văn bản hợp nhất số 44/VBHN-BTC hợp nhất Thông tư 67/2023/TT-BTC](https://congbao.chinhphu.vn/tai-ve-van-ban-so-44-vbhn-btc-46909-51525) | 2025 | Hiệu lực hiện hành | % | Gốc, Bộ Tài chính (Công báo Chính phủ) | Quy định hoạt động đại lý bảo hiểm của tổ chức tín dụng (Bancassurance) |
| S6 | Thống kê toàn ngành bảo hiểm Việt Nam năm 2025 dẫn theo Cục Quản lý, giám sát bảo hiểm — Bộ Tài chính (`mof.gov.vn`, `tapchikinhtetaichinh.vn`, `pjico.com.vn`) | 2026 | FY2025 | Tỷ VND | Thứ cấp (bản tin tổng hợp dẫn nguồn Cục QLBH) | Doanh thu phí phi nhân thọ toàn ngành ước ~88.705–91.771 tỷ VND; chỉ dùng để ước tính khoảng thị phần |
| S7 | [Berkshire Hathaway Inc. 2025 Annual Report](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) | 2026 | FY2025 | Triệu USD; US GAAP | Gốc, công ty công bố | Dùng làm mốc đối chiếu quốc tế về kỷ luật khai thác bảo hiểm bán lẻ |

## Mâu thuẫn và mục chưa giải quyết

| Mục | Bằng chứng mâu thuẫn | Cách xử lý |
|---|---|---|
| Chênh lệch lợi nhuận gộp kinh doanh bảo hiểm (`-31,75 tỷ VND`) và lợi nhuận sau thuế (`-1,36 tỷ VND`) giữa BCTC Q4/2025 tự lập và BCTC 2025 đã kiểm toán | Trên BCTC Q4/2025 tự lập [S2], lợi nhuận gộp KDBH năm 2025 là `994,94 tỷ VND`, chi phí QLDN là `831,08 tỷ VND`, `NPAT` là `551,89 tỷ VND`. Trên BCTC 2025 đã kiểm toán [S1], kiểm toán viên EY tái phân loại `+31,53 tỷ VND` từ chi phí QLDN sang chi phí trực tiếp KDBH, đưa lợi nhuận gộp KDBH về `963,19 tỷ VND`, chi phí QLDN về `800,17 tỷ VND` và `NPAT` về `550,53 tỷ VND` | Sử dụng số liệu đã kiểm toán [S1] làm số chính thức và phân tích rõ khoản tái phân loại `-31,75 tỷ VND` như một bài học thực chiến về kiểm toán chi phí bảo hiểm |
| Điều chỉnh hồi tố số liệu năm 2024 theo Kết luận Kiểm toán Nhà nước (`380/TB-KTNN`) | Thuyết minh 43 (trang 80–81 BCTC / trang PDF 83–84) trình bày điều chỉnh hồi tố Bảng CĐKT tại `31/12/2024` theo Thông báo `380/TB-KTNN` ngày `09/10/2025` (giảm dự phòng nghiệp vụ ngắn hạn `-5,92 tỷ VND` về `3.798,68 tỷ VND`, tăng phải thu ngắn hạn `+3,16 tỷ VND`, tăng lợi nhuận sau thuế chưa phân phối thêm `+2,18 tỷ VND` lên `586,58 tỷ VND`) | Sử dụng cột số liệu cuối năm 2024 đã trình bày lại trên BCTC kiểm toán 2025 và ghi rõ nguồn điều chỉnh từ Thông báo `380/TB-KTNN` |
