# Sổ nguồn — Tập đoàn Bảo Việt (BVH)

- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Mục đích: lưu vết nguồn cho hồ sơ học tập [report.md](report.md).
- Danh mục payload và mã băm SHA-256: xem [`data/raw/insurance-review-sources-2026-11-05.json`](../../../../data/raw/insurance-review-sources-2026-11-05.json).

| Mã | Nguồn và URL | Ngày công bố | Kỳ dữ liệu | Đơn vị / phạm vi | Loại | Giới hạn |
|---|---|---|---|---|---|---|
| S1 | [BCTC hợp nhất năm 2025 đã kiểm toán của Tập đoàn Bảo Việt (BVH)](https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/NAM/BVH_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf) | Ký ngày 31/03/2026 | Năm tài chính kết thúc 31/12/2025 (so sánh 2024) | VND; hợp nhất | Bản sao BCTC kiểm toán độc lập (Ernst & Young Việt Nam, số 11623354/E-68737085-HN) lưu trên CDN Vietstock | 115 trang PDF (111 trang BCTC), 9.746.450 byte; SHA-256 `9a2c25375016c62aaa0d14703c8b1eb79565761dc9a11a039ace27bf014dadde`; đọc trực tiếp ảnh trang PDF 1–115; chưa khớp byte trực tiếp với miền baoviet.com.vn/HOSE |
| S2 | [Văn bản hợp nhất Luật Kinh doanh bảo hiểm số 31/VBHN-VPQH](https://congbao.chinhphu.vn/tai-ve-van-ban-so-31-vbhn-vpqh-46722-51065) | 2025 | Hiệu lực hiện hành | Văn bản luật | Gốc, Công báo Chính phủ | Điều 63 (tách nhân thọ/phi nhân thọ), Điều 156 (lộ trình RBC 01/01/2028) |
| S3 | [Nghị định 46/2023/NĐ-CP](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/7/46-cp.signed.pdf) | 01/07/2023 | Hiệu lực hiện hành | Tỷ VND / % | Gốc, Chính phủ (PDF ký số) | Quy định vốn tối thiểu, dự phòng toán học, dự phòng đảm bảo lãi suất cam kết và biên khả năng thanh toán |
| S4 | [Văn bản hợp nhất số 44/VBHN-BTC hợp nhất Thông tư 67/2023/TT-BTC](https://congbao.chinhphu.vn/tai-ve-van-ban-so-44-vbhn-btc-46909-51525) | 2025 | Hiệu lực hiện hành | % | Gốc, Bộ Tài chính (Công báo Chính phủ) | Điều 51 (trần hoa hồng đại lý bảo hiểm nhân thọ UL năm đầu 30%) |
| S5 | Thống kê toàn ngành bảo hiểm Việt Nam năm 2025 dẫn theo Cục Quản lý, giám sát bảo hiểm — Bộ Tài chính (`mof.gov.vn`, `tapchikinhtetaichinh.vn`, `pjico.com.vn`) | 2026 | FY2025 | Tỷ VND | Thứ cấp (bản tin tổng hợp dẫn nguồn Cục QLBH) | Doanh thu phí nhân thọ toàn ngành ước ~145.085–148.786 tỷ VND; chỉ dùng để ước tính khoảng thị phần |
| S6 | [Berkshire Hathaway Inc. 2025 Annual Report](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) | 2026 | FY2025 | Triệu USD / Tỷ USD; US GAAP | Gốc, công ty công bố | Dùng làm mốc đối chiếu quốc tế về quản trị Float |

## Mâu thuẫn và mục chưa giải quyết

| Mục | Bằng chứng mâu thuẫn | Cách xử lý |
|---|---|---|
| Danh mục chi tiết 36.590,01 tỷ VND trái phiếu doanh nghiệp dài hạn | Thuyết minh 14.2 (trang 50 BCTC / trang PDF 54) công bố tổng giá trị ghi sổ `36.590.007.303.454 VND`, kỳ hạn 7–10 năm, lãi suất đến `8,90%/năm`, nhưng không liệt kê tên từng tổ chức phát hành | Ghi rõ `CHƯA_BIẾT` danh tính từng tổ chức phát hành và đưa vào mục rủi ro cần theo dõi |
| Chênh lệch nhỏ giữa EPS cơ bản trên báo cáo (`3.821 VND/CP`) và phép chia trực tiếp `NPAT mẹ / số cổ phiếu` (`3.821,27 VND/CP`) | Do làm tròn đến hàng đơn vị VND trên BCTC (`2.836.613.711.078 / 742.322.764 = 3.821,267 VND/CP`, Thuyết minh 36 trang 75 BCTC trình bày `3.821 VND/CP`; năm 2024 có trừ trích quỹ khen thưởng phúc lợi `42,93 tỷ VND` nên là `2.785 VND/CP`) | Trình bày rõ cả số làm tròn trên BCTC (`3.821 VND/CP`) và công thức tính trong mô-đun Python |
