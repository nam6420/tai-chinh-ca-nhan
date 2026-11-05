# Biên bản kiểm nguồn: H4 — Đợt 4, nhóm 2, vòng 2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 15:46 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Phạm vi: toàn thân bài H4-v2, 10 bài tập/đáp án, dữ liệu thiếu, nguồn và phép tính, phí/cổ tức/benchmark/GIPS, đọc mô hình/test.
- Báo cáo đích: `learning/lessons/H4-twr-mwr-benchmark.md`
- SHA-256 nội dung đích: `7b20b19c335a4a3d1eca6e9af51913b06badde7b54efff00987a3de044168999`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Điều phối ghi kết quả nhánh độc lập mới `h4_fact_v2` cùng phụ lục15:47, không đổi kết luận. Nhánh đọc mới bản chụp `data/raw/payloads/learning-wave4-group2-snapshot-2026-11-02-1541/H4-v2-twr-mwr-benchmark.md`, kiểm hash bằng validate_report.py; không đọc bản H4 khác, bài khác, learning/reviews hoặc kết quả phản biện. Toàn văn kết quả và phụ lục trả trong cuộc trao đổi02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày/kỳ/phạm vi | Truy cập | Mục đích |
|---|---|---|---|
| [GIPS Handbook](https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/) |11/2020; bản trực tuyến; không tiền tệ |02/11/2026| TWR/MWR/IRR, ghép, định giá, tuyên bố |
| [CFA Rates and Returns](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/rates-and-returns) |CFA LevelI2026; không ngày phát hành riêng; toàn văn cần quyền truy cập|02/11/2026| Chỉ xác nhận phạm vi học TWR/MWR/năm hóa |
| [Berkshire thư2024](https://www.berkshirehathaway.com/letters/2024ltr.pdf) |22/02/2025;PDF15;S&P2022–2023,%có cổ tức làm tròn|02/11/2026| −18,1%,+26,3%; bảng không ghi tiền USD |
| [CFA Research Foundation — Benchmarks](https://rpc.cfainstitute.org/sites/default/files/-/media/documents/book/rf-publication/2003/rf-v2003-n1-3922-pdf.pdf) |08/2003; nghiên cứu khái niệm|02/11/2026| Alpha điều chỉnh rủi ro khác trừ benchmark thô |

## Phát hiện

| Mức | Phần | Phát hiện ban đầu / bằng chứng | Khắc phục / trạng thái cuối |
|---|---|---|---|
| Trung bình, đã rút lại | Bài tập6 | Nhánh ban đầu nhận định câu6 không cho ngày/tiền, cho rằng chỉ có trong mã. Điều phối đọc lại và chỉ vị trí bảng4dòng ở mụcXIRR trong cùng bảnv2, quy ướcACT/365 và câu hỏi dẫn ca ngày không đều | Nhánh đọc lại, trả phụ lục15:47: rút nhận định thiếu dữ liệu, xác nhận tái lập được. Giữ góp ý nhẹ có thể chỉ rõ tên mục; không sửa nội dung |
| Thấp | Mô tả Berkshire | Số là %có cổ tức, bảng không trực tiếp ghi USD; “cơ sởUSD” có thể bị hiểu như đơn vị bảng | Có thể giải thích riêng khi biên tập sau; MỞ, không chặn |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

`PHÉP_TÍNH` Lãi tiền10−21+30=19triệu,kiểm180+39−100−100=19. TWR10%,−10%,20%,ghép18,8%,năm hóa3năm5,91045%.IRR[-100,−100,39,180]tại[0,1,2,3]≈3,98248913%,NPV≈0. NgàyACT/365:[0,181,547,731];XIRR5,59966054%,NPV≈0;TWRnăm hóa731ngày8,98257%.

S&P(1−0,181)(1+0,263)−1=3,4397%,năm hóa1,70531%.Góp100cuối2022:cuối229,7397;IRR9,60567%. Chuỗi[-100,230,−132]có10%và20%đềuNPV≈0. Đã đối chiếu10đáp án và định nghĩa alpha bảnv2.

GIPS2.A.24 hỗ trợ phân kỳ/ghép và định giá phù hợp;2.A.29thảo luận MWRdòng tiền ngày. Phạm vi áp dụng là báo cáo tổ chức; bài không tuyên bố tuân thủ. CFAchỉ xác nhận phạm vi công khai, không dùng làm bằng chứng từng công thức chi tiết. Nguồn CFA2003cho thấy trừ benchmark đơn giản chưa điều chỉnh beta/phong cách. Phí/cổ tức được phân loại theo ranh giới, không tính trùng.

## Phụ lục điều chỉnh độc lập lúc 15:47

Nhánh xác nhận lại từ cùng bảnchụp: bảngXIRRghi−100ngày01/01/2023;−100ngày01/07/2023;+39ngày01/07/2024;+180ngày01/01/2025; số ngày0,181,547,731và quy ước365đủ tái lập5,59966%. Nguyên văn kết luận điều chỉnh: “Rút lại phát hiện ‘không thể tái lập, dữ liệu chỉ có trong mã’.” Kết luận tổng thể vẫnĐẠT,nghiêm trọng/cao0. Không thay bài hoặc hash sau phụ lục.

## Hạn chế của lần kiểm duyệt

CFAtoàn văn cần đăng nhập; công thức kiểm qua GIPSmở và số học. S&Pdựa trên một nguồn gốc chính đã làm tròn. Không chạy test,không xác nhận tài khoản thật. Điều phối đã tự kiểm phát hiện trọng yếu, giữ cả phát hiện gốc và việc rút lại thay vì âm thầm xóa. Chỉ đổi vòng đời sau khi đủ hai biên bản; sửa nội dung sau làm biên bản hết hiệu lực.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không nghiêm trọng/cao; phát hiện thiếu dữ liệu câu6 đã rút lại; còn chú giải tiền tệ mức thấp và góp ý dẫn chiếu nhẹ không chặn.
