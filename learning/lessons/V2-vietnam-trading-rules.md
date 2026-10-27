# BẢN NHÁP - CHƯA KIỂM DUYỆT: Bài V2 — Quy tắc giao dịch cổ phiếu Việt Nam: phiên, lệnh, lô, biên độ, thanh toán và cảnh báo

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 09:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc đúng giá trần, giá sàn và bước giá từ giá tham chiếu; phân biệt lô chẵn với lô lẻ và các loại lệnh chính; tính ngày cổ phiếu về tài khoản theo T+2; nhận ra tín hiệu cảnh báo, kiểm soát, hạn chế của một cổ phiếu.
- Bài trước liên quan: [V1](V1-vietnam-market-structure.md), [N1](N1-market-basics.md). Học tiếp bài B1 (phí, thuế, lưu ký) ở Đợt 2, chưa soạn.
- Thời lượng: Hai phiên; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Với một lệnh tôi định đặt, giá nào hợp lệ, khi nào khớp, và khi nào cổ phiếu về tài khoản để bán lại?**
- Kiểm nguồn: `CHƯA CHẠY` trên bản này (bản trước `ĐẠT`)
- Phản biện rủi ro: `CHƯA CHẠY` trên bản này (bản trước `ĐẠT`)
- Hạn kiểm lại dữ kiện: trước 23/12/2026 (HNX chuyển sang HOSE, biên độ và giờ có thể đổi) và sau mọi thông báo mới của UBCKNN/VSDC về chu kỳ thanh toán

## Hiểu bài này trong 1 phút

Quy tắc giao dịch là các thông số do cơ quan và sở giao dịch đặt, có thể đổi: biên độ giá, bước giá, giờ phiên, loại lệnh, chu kỳ thanh toán. Bài này dạy cách **tính và đọc** chúng từ một giá tham chiếu, và cách kiểm tra thông số hiện hành thay vì tin vào bài viết cũ. Quy chế niêm yết và giao dịch theo [Quyết định 22/QĐ-HĐTV ngày 16/03/2026](https://stream.vnx.vn/VNX//Legal/2026031816145088VNX.Quy-che-niem-yet_QD22.pdf) thay thế quyết định cùng số ngày 18/04/2025; [Quyết định 23/QĐ-HĐTV ngày 18/03/2026](https://stream.vnx.vn/VNX//Legal/20260324164637497VNX.-Quy-che-CK-CNY_QD23....pdf) quy định giao dịch chứng khoán chưa niêm yết. Từng thông số còn cần đối chiếu thông báo sở và các thay đổi sau ngày chốt. Đọc nhãn nguồn.

## Ôn bài cũ hoặc kiểm tra đầu vào

Đầu vào: từ N1, giá chào mua cao nhất, giá chào bán thấp nhất và giá khớp gần nhất là ba thứ khác nhau; lệnh thị trường không bảo đảm giá khớp. Bài này áp vào quy tắc Việt Nam.

## Bài này làm gì và chưa làm gì

Dạy cách đọc và tính quy tắc ở mức cơ bản. Không dạy phí, thuế (xem bài B1), không dạy ký quỹ (bài B2), không hướng dẫn thao tác trên ứng dụng của công ty chứng khoán cụ thể. Không chọn thời điểm hay giá để mua/bán.

## Thay đổi sắp tới (đọc trước)

`SỰ_THẬT (thứ cấp)` Cổ phiếu niêm yết HNX dự kiến chuyển sang HOSE: HNX giao dịch lần cuối 23/12/2026, tạm ngừng 24–25/12, HOSE từ 28/12/2026 (xem [V1](V1-vietnam-market-structure.md); mốc ngày được VietnamPlus đăng lại ngày 30/09/2026 từ thông báo của VNX [VietnamPlus](https://www.vietnamplus.vn/2312-ngay-giao-dich-cuoi-cung-cua-cac-co-phieu-tai-hnx-post1139250.vnp)). Một bài báo ngày 06/10/2026 cho biết cơ quan quản lý còn *nghiên cứu* giao dịch xuyên trưa, nới biên độ và rút ngắn chu kỳ thanh toán (phần tóm tắt bài còn nêu bỏ phiên khớp lệnh định kỳ), **chưa quyết định**. Biên độ và giá tham chiếu ngày 28/12/2026 của mã chuyển sàn chưa có công bố (`CHƯA_BIẾT`). [Thời báo Tài chính, 06/10/2026](https://thoibaotaichinhvietnam.vn/chuyen-toan-bo-co-phieu-hnx-sang-hose-trong-nam-2026-nghien-cuu-giao-dich-xuyen-trua-va-noi-bien-do-204943.html). Vì vậy biên độ ±10% của HNX, giờ phiên và chu kỳ thanh toán trong bài này có thể đổi; kiểm lại sau 28/12/2026.

## 1. Giá tham chiếu, biên độ và bước giá

`SỰ_THẬT (thứ cấp)` Thông tư 120/2020/TT-BTC (toàn văn trên trang thứ cấp, hiệu lực 15/02/2021, thay Thông tư 203/2015): biên độ giao động giá do Sở Giao dịch quyết định sau khi UBCKNN chấp thuận; Thông tư không ghi tỷ lệ phần trăm cụ thể. [ketoananpha.vn](https://ketoananpha.vn/thong-tu-120-2020-tt-btc). Thông tư này được sửa bởi Thông tư 68/2024 và 08/2026; `CHƯA_BIẾT` bản trên trang đã cập nhật chưa.

`SỰ_THẬT` (tài liệu hướng dẫn của HOSE, tệp ghi tháng 02/2026, dẫn Quy chế 22/QĐ-HĐTV) Biên độ HOSE ±7% so với giá tham chiếu; ngày đầu niêm yết và ngày giao dịch lại từ khi tạm ngừng hoặc đình chỉ **từ 25 ngày giao dịch liên tiếp trở lên**: ±20%. Bước giá HOSE: 10 đồng (giá dưới 10.000), 50 đồng (từ 10.000 đến 49.950), 100 đồng (từ 50.000). [HOSE — Quy định cần biết](https://staticfile.hsx.vn/Uploads/UploadDocuments/2453338/HTGD_Quy%20dinh%20can%20biet%20khi%20GDCK%20tren%20HOSE_T2.2026.pdf). `SỰ_THẬT (thứ cấp)` Bài giải thích của một công ty chứng khoán (DSC, không ghi ngày) khớp các số HOSE trên và ghi thêm: HNX ±10% và UPCoM ±15%; ngày đầu HNX ±30%, UPCoM ±40%; bước giá HNX và UPCoM 100 đồng; giá tham chiếu HOSE/HNX là giá đóng cửa phiên trước, UPCoM là giá bình quân gia quyền. [DSC](https://www.dsc.com.vn/kien-thuc/bien-do-giao-dong-gia-co-phieu-la-gi).

`SỰ_THẬT` Với UPCoM, Điều 18–19 [Quy chế 23/QĐ-HĐTV ngày 18/03/2026](https://stream.vnx.vn/VNX//Legal/20260324164637497VNX.-Quy-che-CK-CNY_QD23....pdf) nêu bước giá khớp liên tục 100 đồng, biên độ thông thường ±15% và ±40% cho một số trường hợp đặc biệt. `CHƯA_BIẾT` HNX niêm yết vẫn cần đối chiếu thông báo gốc của sở; các con số HOSE từ tài liệu 02/2026 cần kiểm có thông báo mới hơn hay không.

`SỰ_THẬT` Điều 32 Quy chế 22/QĐ-HĐTV ngày 16/03/2026 quy định giá trần làm tròn xuống và giá sàn làm tròn lên theo đơn vị yết giá; có điều chỉnh riêng khi giá trần hoặc sàn bằng giá tham chiếu và các trường hợp giá rất thấp. [Quy chế VNX](https://stream.vnx.vn/VNX//Legal/2026031816145088VNX.Quy-che-niem-yet_QD22.pdf). `CHƯA_BIẾT` Điều 32 dẫn Điều 30 về đơn vị yết giá nhưng bài chưa xác minh cách áp dụng khi trần hoặc sàn rơi sang vùng giá khác; ví dụ dùng *bước giá của vùng giá kết quả* như giả định, không phải quy tắc đã xác nhận. Bài tập dưới đây chỉ xét cổ phiếu; công cụ khác có quy định riêng.

`PHÉP_TÍNH` Công thức: `trần lý thuyết = tham chiếu × (1 + biên độ)`, làm tròn **xuống** về bội số của bước giá; `sàn lý thuyết = tham chiếu × (1 − biên độ)`, làm tròn **lên** về bội số của bước giá.

`KỊCH_BẢN` (giá tham chiếu giả định) Tham chiếu 23.450 đồng, HOSE ±7%, bước 50 đồng: trần lý thuyết `23.450 × 1,07 = 25.091,5` → làm tròn xuống **25.050**; sàn lý thuyết `23.450 × 0,93 = 21.808,5` → làm tròn lên **21.850**.

`KỊCH_BẢN` (tham chiếu giả định 20.000 đồng, biên độ theo nguồn nêu ở trên) HOSE ±7%: trần 21.400, sàn 18.600; HNX ±10%: 22.000 và 18.000; UPCoM ±15%: 23.000 và 17.000. Cùng đợt tăng +8%: chạm trần ở HOSE nhưng chưa chạm trần ở hai sàn kia. Điểm dừng: tự tính thêm cho tham chiếu 8.700 đồng với bước 10 đồng, biên độ 7%.

## 2. Phiên giao dịch, loại lệnh và lô

`SỰ_THẬT` (HOSE, tài liệu 2025 và 2026) Giờ giao dịch HOSE: khớp lệnh định kỳ mở cửa ATO 9h00–9h15, khớp lệnh liên tục 9h15–11h30 và 13h00–14h30, khớp lệnh định kỳ đóng cửa ATC 14h30–14h45; giao dịch thỏa thuận 9h00–11h30 và 13h00–15h00. [HOSE — Thời gian giao dịch](https://staticfile.hsx.vn/Uploads/UploadDocuments/2372196/2.Thoi%20gian%20giao%20dich.pdf). `SỰ_THẬT (thứ cấp)` Bảng của DSC ("tính đến 9/2026") chỉ liệt kê khung thỏa thuận 14h45–15h00 và có chỗ không nhất quán nội bộ (câu mở đầu so với bảng; mục HOSE thiếu khung ATC); bài không dùng bảng đó cho HOSE. `CHƯA_BIẾT` Giờ HNX/UPCoM từ nguồn gốc. `SỰ_THẬT` Trong khớp lệnh liên tục, HOSE nêu ưu tiên giá rồi thời gian: mua giá cao hơn hoặc bán giá thấp hơn được ưu tiên; cùng giá thì lệnh nhập trước được ưu tiên. [HOSE — Quy định giao dịch](https://staticfile.hsx.vn/Uploads/News/437a3bc734a845fc853283b0c627a593/20250429_20250429%20-%20HOSE%20-%20Quy%20dinh%20giao%20dich%20dang%20website%20HOSE.pdf).

`SỰ_THẬT` Tài liệu HOSE liệt kê **LO** (giới hạn giá), **ATO** và **ATC** (phiên định kỳ), **MTL** (thị trường, chỉ nhập trong phiên liên tục; phần chưa khớp chuyển thành LO theo quy tắc giá và giới hạn trần/sàn). [HOSE — Các loại lệnh](https://staticfile.hsx.vn/Uploads/UploadDocuments/2372203/6.Cac%20loai%20lenh%20.pdf). Quy chế VNX ngày 16/03/2026 cũng định nghĩa MOK và MAK trong danh sách chung; tài liệu HOSE này không liệt kê hai lệnh ấy. `CHƯA_BIẾT` Chưa đủ căn cứ kết luận MOK/MAK được triển khai hay không trên HOSE tại thời điểm sử dụng; kiểm thông báo chính thức theo từng sở.

`SỰ_THẬT` (HOSE, tài liệu 02/2026) Lệnh LO được sửa; giảm khối lượng giữ ưu tiên, tăng khối lượng hoặc sửa giá thì mất ưu tiên. Theo [HOSE — Các loại lệnh](https://staticfile.hsx.vn/Uploads/UploadDocuments/2372203/6.Cac%20loai%20lenh%20.pdf), lệnh ATO hoặc ATC không được ưu tiên trước lệnh LO mua giá trần hoặc LO bán giá sàn đã nhập vào hệ thống trước đó. [SGGP, 13/03/2025](https://www.sggp.org.vn/hose-cong-bo-nhung-thay-doi-quan-trong-trong-giao-dich-chung-khoan-khi-ap-dung-he-thong-giao-dich-moi-post785801.html) mô tả thay đổi dự kiến trước khi hệ thống vận hành, với cách diễn đạt rộng hơn.

`SỰ_THẬT` (HOSE) Tài liệu HOSE 02/2026 nêu lô chẵn 100 cổ phiếu (tối đa 500.000 cổ phiếu mỗi lệnh), lô lẻ 1–99 cổ phiếu mỗi lệnh; mã bị hạn chế chỉ giao dịch lô chẵn. Điều 34 Quy chế 22/QĐ-HĐTV ngày 16/03/2026 quy định giao dịch lô lẻ chỉ nhập lệnh LO. [Quy chế VNX](https://stream.vnx.vn/VNX//Legal/2026031816145088VNX.Quy-che-niem-yet_QD22.pdf). `CHƯA_BIẾT` Các thông số trong tài liệu HOSE tháng 02 có thay đổi bởi thông báo sau tháng 03/2026 hay không; kiểm nguồn sở và nền tảng công ty chứng khoán trước khi dùng. `KỊCH_BẢN` Cổ phiếu 25.000 đồng: một lô chẵn `100 × 25.000 = 2.500.000` đồng (chưa phí); mua 137 cổ phiếu thường phải tách một lệnh 100 và một lệnh 37 (suy luận, cần kiểm trên nền tảng của bạn).

### Các lỗi đặt lệnh phổ biến (không phải khuyến nghị giao dịch)

- Đặt giá lệch bước giá có thể bị hệ thống từ chối (DSC).
- Lệnh ATO, ATC, MTL **không bảo đảm giá khớp**; giá ATC chưa biết trước khi phiên kết thúc.
- Sửa lệnh: tăng khối lượng hoặc sửa giá mất ưu tiên hàng đợi (HOSE).
- Phần dư của lệnh MTL chuyển thành LO ở giá gần nhất cộng hoặc trừ một bước, có thể nằm hàng chờ chứ không khớp tiếp.
- Mã bị hạn chế chỉ giao dịch lô chẵn và theo phương thức riêng; kiểm tín hiệu của mã trước khi đặt lệnh.

## 3. Thanh toán T+2 và điều chưa có

`SỰ_THẬT` (HOSE) Chu kỳ thanh toán hiện là T+2: người mua nhận cổ phiếu vào chiều ngày T+2 (tài liệu HOSE). `SỰ_THẬT (thứ cấp)` Sự cố 27/02/2026 xác nhận: lệnh mua ngày 25/2 dự kiến về tài khoản trong phiên 27/2. [Nhà đầu tư](https://nhadautu.vn/lanh-dao-vsdc-xac-nhan-nha-dau-tu-chua-duoc-nhan-thanh-toan-chung-khoan-t2-trong-chieu-27-2-d103155.html). `CHƯA_BIẾT` Giờ cụ thể cổ phiếu và tiền khả dụng để bán lại có thể khác nhau theo công ty chứng khoán; kiểm với công ty của bạn. Chưa mở được thông báo gốc của UBCKNN/VSDC; chưa thấy văn bản nào rút ngắn chu kỳ đến ngày chốt (bài 06/10/2026 chỉ nêu *nghiên cứu*).

`SỰ_THẬT (thứ cấp)` Giao dịch T+0 và bán chứng khoán chờ về chưa vận hành như sản phẩm chuẩn. Chủ tịch HĐTV VSDC nói (11/06/2026) có thể sớm nhất nửa cuối 2026, khả thi hơn là nửa cuối 2027 hoặc 2028. [Người Quan Sát, 11/06/2026](https://nguoiquansat.vn/lanh-dao-vsdc-tiet-lo-thoi-diem-trien-khai-t-0-va-ban-khong-297283.html); [24hmoney, 11/06/2026](https://24hmoney.vn/news/khi-nao-trien-khai-t-0-va-ban-khong-c1a2793712.html). Bài của Người Quan Sát ngày 06/01/2026 là phát biểu của UBCKNN, chỉ nói đối tác bù trừ trung tâm (CCP) dự kiến 2026–2027, không nêu mốc T+0. [Người Quan Sát, 06/01/2026](https://nguoiquansat.vn/lanh-dao-ubcknn-thong-tin-lo-trinh-trien-khai-giao-dich-t-0-va-ban-chung-khoan-cho-ve-264784.html). Thông tư 120 Điều 7.3 chỉ cho đặt lệnh bán cổ phiếu đã có trên tài khoản lưu ký; "giao dịch trong ngày" ở Điều 10 cần hợp đồng riêng và chưa thấy vận hành (nguồn thứ cấp). Mọi bài viết hứa "T+0" cần đối chiếu thông báo mới nhất.

`PHÉP_TÍNH` Đếm T+2 theo ngày làm việc, bỏ thứ Bảy, Chủ Nhật và ngày nghỉ. `KỊCH_BẢN` Mua thứ Sáu 06/11/2026 (T+0): T+1 là thứ Hai 09/11, T+2 là thứ Ba 10/11/2026 (giả định không có ngày nghỉ lễ xen giữa; lịch nghỉ lễ cuối 2026 `CHƯA_BIẾT`). Kiểm với sự cố trên: mua thứ Tư 25/2, T+2 là thứ Sáu 27/2: khớp.

## 4. Diện cảnh báo, kiểm soát, hạn chế, tạm ngừng

`SỰ_THẬT` (HOSE) Tài liệu HOSE liệt kê ký hiệu trạng thái cổ phiếu (như cảnh báo, kiểm soát, hạn chế, tạm ngừng, đình chỉ) và nói mã bị hạn chế chỉ giao dịch lô chẵn theo phương thức riêng. Quy chế 22/QĐ-HĐTV ngày 16/03/2026 có các điều về trạng thái này; `CHƯA_BIẾT` bài chưa đối chiếu đầy đủ từng điều kiện với từng mã.

`SỰ_THẬT (thứ cấp)` Con số 120 tỷ đồng vốn điều lệ trong các bài cũ xuất phát từ Quyết định 85/QĐ-SGDHCM (LSVN dẫn các điều về kiểm soát; bài này không khẳng định số điều), một quy chế cũ của HOSE; quy chế 17/QĐ-HĐTV (31/03/2022) Điều 38 ghi ngưỡng vốn điều lệ kiểm soát là 30 tỷ đồng. [LSVN, 15/05/2022](https://lsvn.vn/khi-nao-co-phieu-bi-dua-vao-dien-kiem-soat1652583311-a118781.html); [Quy chế 17/QĐ-HĐTV](https://mbs.com.vn/files/uploads/2025/04/17_qd-hdtv_quy-che-niem-yet-va-giao-dich-ck-niem-yet.pdf). `CHƯA_BIẾT` Bài chưa đối chiếu đầy đủ điều kiện kiểm soát trong quy chế 2026; **đừng dùng 120 tỷ hay 30 tỷ như quy tắc hiện nay**.

`SỰ_THẬT (thứ cấp)` Ví dụ thực tế (báo chí về thông báo của sở): chậm báo cáo tài chính soát xét bán niên hơn 30 ngày dẫn tới diện kiểm soát (ITA, TNA, HOSE, công bố 18/10/2024, hiệu lực 24/10/2024); hơn 45 ngày dẫn tới hạn chế giao dịch (RDP, HOSE, công bố 18/10/2024, hiệu lực 24/10/2024). [24hmoney](https://24hmoney.vn/news/co-phieu-tan-tao-nhua-rang-dong-thien-nam-vao-dien-kiem-soat-han-che-giao-dich-c1a2411724.html). Ví dụ HBS (HNX): từ 08/10/2025 theo Quyết định 1218/QĐ/SGDHN chỉ giao dịch phiên thứ Sáu hằng tuần; cách này có thể đổi sau 28/12/2026. [Báo Pháp luật, 26/11/2025](https://doanhnhan.baophapluat.vn/chung-khoan-hoa-binh-hbs-bi-dinh-chi-mot-phan-hoat-dong-giao-dich-89201.html). Ý chính: mỗi nhãn là tín hiệu rủi ro về minh bạch hoặc tài chính, ảnh hưởng thanh khoản; hãy đọc thông báo của sở với từng mã.

## 5. Ngoại lệ đáng biết

`SỰ_THẬT (thứ cấp)` Thông tư 120 Điều 7.1.a yêu cầu đủ tiền khi mua; nhà đầu tư tổ chức nước ngoài được đặt lệnh mua không cần đủ tiền theo Thông tư 68/2024 và 08/2026 (mô hình giao dịch không cần đủ tiền). [LSVN](https://lsvn.vn/nhung-diem-moi-cua-thong-tu-08-2026-tt-btc-ve-chung-khoan-giao-dich-co-phieu-a169838.html). `CHƯA_BIẾT` Điều kiện margin; xem bài B2.

## Năm câu hỏi khi đọc

1. Giá tham chiếu, trần và sàn của mã này hôm nay là bao nhiêu, theo sàn nào?
2. Bước giá ở mức giá này là bao nhiêu?
3. Tôi đặt lệnh nào, và nếu không khớp hết thì phần còn lại thành gì?
4. Cổ phiếu mua hôm nay về tài khoản ngày nào theo lịch làm việc?
5. Mã này có đang bị cảnh báo, kiểm soát hay hạn chế không, theo thông báo của sở?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm. Dùng quy tắc của bài (nguồn thứ cấp) làm giả định.

1. HOSE, tham chiếu 8.700 đồng, bước 10, biên độ ±7%. Tính trần và sàn.
2. Tham chiếu 52.300 đồng, HOSE, bước 100, ±7%. Tính trần và sàn.
3. Mua thứ Hai 16/11/2026, giả định không có ngày nghỉ. Cổ phiếu về tài khoản ngày nào theo T+2?
4. Vì sao không nên dùng con số 120 tỷ (hay 30 tỷ) để dự đoán mã nào vào diện kiểm soát hôm nay?
5. Lệnh thị trường có đảm bảo giá khớp không? Sau KRX phần dư của MTL thành gì theo HOSE, và MTL nhập được trong phiên nào?
6. Mua 250 cổ phiếu giá 18.000 đồng: tách lô thế nào và giá trị lô chẵn bao nhiêu (chưa phí)?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` Trần `8.700 × 1,07 = 9.309` → làm tròn xuống bước 10 → **9.300**; sàn `8.700 × 0,93 = 8.091` → làm tròn lên → **8.100**.
2. `PHÉP_TÍNH` Trần `52.300 × 1,07 = 55.961` → xuống bước 100 → **55.900**; sàn `52.300 × 0,93 = 48.639` → lên bước 50 (vùng dưới 50.000) → **48.650**. Chú ý bước giá đổi theo vùng giá nên sàn rơi vào vùng 50 đồng. Đây là giả định bước giá của vùng giá kết quả; nếu dùng bước 100 của vùng giá tham chiếu thì sàn là 48.700. Kiểm quy tắc làm tròn thực tế trước khi dùng.
3. T+1 thứ Ba 17/11, T+2 thứ Tư 18/11/2026.
4. Các con số đó từ quy chế cũ (85/QĐ-SGDHCM và 17/QĐ-HĐTV); bài chưa đối chiếu đầy đủ điều kiện trong quy chế 2026, và còn nhiều tiêu chí khác.
5. Không đảm bảo. Theo HOSE phần dư sau MTL thành LO ở giá khớp cuối cùng cộng hoặc trừ một bước; MTL chỉ nhập trong phiên khớp lệnh liên tục.
6. 250 = 200 lô chẵn + 50 lô lẻ; `200 × 18.000 = 3.600.000` đồng cho lô chẵn (chưa phí).

</details>

## Lỗi thường gặp

- Dùng bài hướng dẫn trước khi KRX vận hành (05/05/2025, theo [SGGP](https://www.sggp.org.vn/hose-chinh-thuc-van-hanh-he-thong-krx-tu-hom-nay-5-5-2025-post793766.html)) cho quy tắc hiện nay, hoặc tự suy ra MOK/MAK đang được từng sở triển khai mà không kiểm thông báo sở.
- Coi biên độ ±7%/±10%/±15% là hằng số của luật.
- Tin rằng T+0 hay bán khống đã vận hành thông thường.
- Quên rằng bước giá đổi theo vùng giá nên làm tròn khác nhau.
- Bỏ qua thông báo cảnh báo, kiểm soát và hạn chế của mã.

## Ranh giới an toàn

- Đây là bài học tính và đọc quy tắc, không phải khuyến nghị mua/bán hay chọn giá đặt lệnh.
- Số liệu HOSE lấy từ tài liệu của chính HOSE, số liệu HNX/UPCoM từ nguồn thứ cấp; tất cả có thể đổi (đặc biệt sau 28/12/2026). Ví dụ số dùng giá tham chiếu giả định.
- Trước khi giao dịch thật, kiểm thông số hiện hành tại sở giao dịch và công ty chứng khoán của bạn.

## Điều tôi vẫn chưa hiểu

- Biên độ, bước giá, giờ phiên chính thức hiện hành là gì, trên văn bản nào?
- Chu kỳ thanh toán mới nhất theo thông báo của UBCKNN/VSDC là gì?
- Tín hiệu hạn chế/kiểm soát của mã tôi quan tâm là gì và dựa trên điều kiện nào?

## Nguồn Internet đã mở

Ngày truy cập tất cả: `2026-10-27`.

| Nguồn | Ngày / phạm vi | Dùng cho |
|---|---|---|
| [HOSE — Quy định cần biết](https://staticfile.hsx.vn/Uploads/UploadDocuments/2453338/HTGD_Quy%20dinh%20can%20biet%20khi%20GDCK%20tren%20HOSE_T2.2026.pdf) | Tệp 04/2026, nhãn T2.2026; nguồn gốc HOSE | Biên độ, bước giá, ký hiệu |
| [HOSE — Thời gian giao dịch](https://staticfile.hsx.vn/Uploads/UploadDocuments/2372196/2.Thoi%20gian%20giao%20dich.pdf) | Tệp 05/2025; nguồn gốc HOSE | Giờ phiên, thỏa thuận, lô lẻ |
| [HOSE — Các loại lệnh](https://staticfile.hsx.vn/Uploads/UploadDocuments/2372203/6.Cac%20loai%20lenh%20.pdf) | Sau KRX (2025); nguồn gốc HOSE | LO/ATO/ATC/MTL |
| [VNX — Quy chế 22/QĐ-HĐTV](https://stream.vnx.vn/VNX//Legal/2026031816145088VNX.Quy-che-niem-yet_QD22.pdf) | 16/03/2026; Việt Nam | Lệnh, làm tròn, giao dịch lô lẻ; bản quét |
| [VNX — Quy chế 23/QĐ-HĐTV](https://stream.vnx.vn/VNX//Legal/20260324164637497VNX.-Quy-che-CK-CNY_QD23....pdf) | 18/03/2026; Việt Nam | Bước giá và biên độ UPCoM; bản quét |
| [HOSE — Quy định giao dịch](https://staticfile.hsx.vn/Uploads/News/437a3bc734a845fc853283b0c627a593/20250429_20250429%20-%20HOSE%20-%20Quy%20dinh%20giao%20dich%20dang%20website%20HOSE.pdf) | 2025; nguồn gốc HOSE | Ưu tiên giá và thời gian trong khớp lệnh liên tục |
| [SGGP — KRX](https://www.sggp.org.vn/hose-chinh-thuc-van-hanh-he-thong-krx-tu-hom-nay-5-5-2025-post793766.html) | 05/05/2025; thứ cấp | Ngày vận hành hệ thống |
| [Quy chế 17/QĐ-HĐTV](https://mbs.com.vn/files/uploads/2025/04/17_qd-hdtv_quy-che-niem-yet-va-giao-dich-ck-niem-yet.pdf) | 31/03/2022; bản lưu trên MBS | Làm tròn trần/sàn, ngưỡng kiểm soát cũ |
| [Thời báo Tài chính, 06/10/2026](https://thoibaotaichinhvietnam.vn/chuyen-toan-bo-co-phieu-hnx-sang-hose-trong-nam-2026-nghien-cuu-giao-dich-xuyen-trua-va-noi-bien-do-204943.html) | 06/10/2026; thứ cấp | Thay đổi đang nghiên cứu |
| [Người Quan Sát, 11/06/2026](https://nguoiquansat.vn/lanh-dao-vsdc-tiet-lo-thoi-diem-trien-khai-t-0-va-ban-khong-297283.html) | 11/06/2026; thứ cấp | Lộ trình T+0 |
| [Thông tư 120/2020 trên ketoananpha.vn](https://ketoananpha.vn/thong-tu-120-2020-tt-btc) | Ban hành 31/12/2020, hiệu lực 15/02/2021; thứ cấp | Khung giao dịch, đủ tiền, giao dịch trong ngày |
| [DSC — biên độ](https://www.dsc.com.vn/kien-thuc/bien-do-giao-dong-gia-co-phieu-la-gi) | Không ghi ngày; thứ cấp | Biên độ, bước giá, tham chiếu |
| [DSC — giờ giao dịch](https://www.dsc.com.vn/kien-thuc/gio-giao-dich-chung-khoan-viet-nam) | "Tính đến 9/2026"; thứ cấp | Giờ phiên |
| [DNSE](https://hdsd.dnse.com.vn/master/nhung-thay-doi-quan-trong-cua-he-thong-krx/faq-krx-thi-truong-co-so) | Không ghi ngày; hướng dẫn công ty chứng khoán | Loại lệnh sau KRX |
| [SGGP](https://www.sggp.org.vn/hose-cong-bo-nhung-thay-doi-quan-trong-trong-giao-dich-chung-khoan-khi-ap-dung-he-thong-giao-dich-moi-post785801.html) | 13/03/2025; "dự kiến" | Thay đổi khi chuyển KRX |
| [Finhay](https://www.finhay.com.vn/lo-chan-lo-le-chung-khoan) | Không ghi ngày; có yếu tố quảng bá | Lô chẵn, lô lẻ |
| [Nhà đầu tư](https://nhadautu.vn/lanh-dao-vsdc-xac-nhan-nha-dau-tu-chua-duoc-nhan-thanh-toan-chung-khoan-t2-trong-chieu-27-2-d103155.html) | 27/02/2026 | T+2 qua sự cố |
| [24hmoney — T+0](https://24hmoney.vn/news/khi-nao-trien-khai-t-0-va-ban-khong-c1a2793712.html) | 11/06/2026 | T+0 và bán chờ về chưa vận hành |
| [Người Quan Sát](https://nguoiquansat.vn/lanh-dao-ubcknn-thong-tin-lo-trinh-trien-khai-giao-dich-t-0-va-ban-chung-khoan-cho-ve-264784.html) | 06/01/2026 | Lộ trình T+0 |
| [LSVN — diện kiểm soát](https://lsvn.vn/khi-nao-co-phieu-bi-dua-vao-dien-kiem-soat1652583311-a118781.html) | 15/05/2022; quy chế cũ | Điều kiện kiểm soát (cũ) |
| [24hmoney — RDP/TNA](https://24hmoney.vn/news/co-phieu-tan-tao-nhua-rang-dong-thien-nam-vao-dien-kiem-soat-han-che-giao-dich-c1a2411724.html) | 18/10/2024 | Ví dụ kiểm soát và hạn chế |
| [Báo Pháp luật — HBS](https://doanhnhan.baophapluat.vn/chung-khoan-hoa-binh-hbs-bi-dinh-chi-mot-phan-hoat-dong-giao-dich-89201.html) | 26/11/2025 | Ví dụ hạn chế giao dịch |
| [LSVN — TT 08/2026](https://lsvn.vn/nhung-diem-moi-cua-thong-tu-08-2026-tt-btc-ve-chung-khoan-giao-dich-co-phieu-a169838.html) | TT ký 03/02/2026; hiệu lực không nêu | Giao dịch không cần đủ tiền |

Không mở được: hnx.vn (lỗi chứng chỉ), ssc.gov.vn, thuvienphapluat.vn. Bản quét quy chế VNX 2026 đã được trích nhận dạng chữ để tìm điều khoản và đối chiếu ảnh các trang trọng yếu; bài chưa kiểm hết từng điều và thông báo sở sau ngày ban hành. Ví dụ số được điều phối viên tính lại bằng tay; câu 2 của bài tập là cách làm tròn theo giả định. `CHƯA_BIẾT` hiệu quả học thực tế.
