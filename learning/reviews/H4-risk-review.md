# Biên bản phản biện rủi ro: H4 — Đợt 4, nhóm 2, vòng 2

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 15:46 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Phạm vi: toàn bản chụp H4-v2, bài tập/đáp án, đọc risk_performance.py và test liên quan; không chạy test.
- Báo cáo đích: `learning/lessons/H4-twr-mwr-benchmark.md`
- SHA-256 nội dung đích: `7b20b19c335a4a3d1eca6e9af51913b06badde7b54efff00987a3de044168999`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Điều phối ghi kết quả nhánh độc lập mới `h4_risk_v2`, không đổi kết luận. Nhánh đọc mới bản chụp `data/raw/payloads/learning-wave4-group2-snapshot-2026-11-02-1541/H4-v2-twr-mwr-benchmark.md`, xác nhận hash chuẩn; không đọc bài khác, bản H4 cũ, learning/reviews hay kết quả nhánh kiểm nguồn. Toàn văn trả trong cuộc trao đổi02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [GIPS Handbook](https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/) | Sổ tay11/2020; bản trực tuyến | 02/11/2026 | Phân kỳ, MWR/benchmark, tuân thủ |
| [CFA Rates and Returns](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/rates-and-returns) | Chương trình2026; không ghi ngày riêng | 02/11/2026 | Phạm vi so sánh TWR/MWR |
| [Berkshire thư2024](https://www.berkshirehathaway.com/letters/2024ltr.pdf) | 22/02/2025; PDF15; S&P2022–2023,%có cổ tức | 02/11/2026 | Đầu vào lịch sử và ghép |
| [CFA Research Foundation — Benchmarks](https://rpc.cfainstitute.org/sites/default/files/-/media/documents/book/rf-publication/2003/rf-v2003-n1-3922-pdf.pdf) |08/2003; khái niệm | 02/11/2026 | Alpha khác chênh lệch thô |

## Phát hiện

| Mức | Phần | Phát hiện / tác động | Bằng chứng | Khắc phục / trạng thái |
|---|---|---|---|---|
| Trung bình | Benchmark | Đã yêu cầu kỳ/tiền tệ/cổ tức/phí/thuế nhưng nhánh đề nghị nói rõ hơn cơ sở gộp/ròng của benchmark và chi phí sản phẩm mô phỏng; tránh diễn giải quá mức chênh lệch không cùng phí | GIPS5.A.1 và ví dụ+8%sau phí so+6%chỉ giá | Ghi cơ sở gộp/ròng cả hai; nếu dùng sản phẩm, ghi chi phí/thuế/sai lệch bám. MỞ, không chặn |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

`PHÉP_TÍNH` Berkshire S&P−18,1%,+26,3%có cổ tức khớp; ghép0,819×1,263−1=3,4397%; năm hóa≈1,7053%. Có góp giả định100 cuối2022:cuối229,7397USD,IRR≈9,61%theo2kỳ năm. Ca chính TWR18,8%,IRR3,98249%,XIRR5,59966%ACT/365 đúng. Ba đoạn10%,−10%,20%; ví dụ nhiều nghiệm có cả10%/20%, test có hai khoảng riêng.

GIPS2.A.24 đòi phân kỳ và ghép, định giá phù hợp; bài công khai giả định định giá quanh dòng tiền. GIPS5.A.1 cảnh báo TWRchỉ số không so trực tiếp MWRcomposite, có thể tạo MWRđối chứng cùng dòng tiền; bài đã nêu cách dựng đối chứng. CFA Research Foundation chỉ ra phép trừ thô chưa điều chỉnh beta/phong cách; định nghĩa alpha bảnv2 phù hợp. GIPS1.A.8–1.A.9 không chứng nhận tuân thủ bằng phương pháp riêng; bài không tự nhận tuân thủ.

Không thấy sai lệch trọng yếu giữa đáp án và mã/test; không suy MWR thấp là quản lý kém hoặc TWR/MWR là kỹ năng.

## Hạn chế của lần kiểm duyệt

Chỉ bảnv2 được giao; đọc tĩnh mã, không chạy test. Không dữ liệu danh mục thật để kiểm phí/thuế/thanh khoản/đòn bẩy/pháp lý. Nguồn2003 dùng cho khái niệm, không cho hiệu quả hiện tại. Điều phối giữ nguyên nội dung chuẩn sau kiểm; chỉ bỏ nháp và đổi hai trạng thái vòng đời khi đủ biên bản.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không nghiêm trọng/cao; giữ điểm trung bình về làm rõ chi phí benchmark, không chặn.
