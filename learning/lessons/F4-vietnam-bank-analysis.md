# Bài F4 — Đọc ngân hàng Việt Nam: biên lãi, nợ xấu và vốn

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:58 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính NIM, CIR, tỷ lệ nợ xấu và độ bao phủ trong ví dụ; phân biệt dự phòng, nợ xấu và an toàn vốn.
- Bài trước liên quan: [013](013-banks-insurers.md), [005](005-debt-liquidity-survival.md), [M1](M1-monetary-policy-rates-fx-credit.md).
- Câu hỏi cốt lõi: Ngân hàng kiếm lãi từ đâu, khoản vay có thể tổn thất bao nhiêu và vốn đệm được đo như thế nào?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F4-fact-check.md), [phản biện](../reviews/F4-risk-review.md).

## Hiểu bài trong một phút

Ngân hàng huy động và phân bổ vốn; thu nhập lãi thuần là lãi thu được trừ chi phí lãi, nhưng lợi nhuận còn phụ thuộc chi phí hoạt động và tổn thất tín dụng. Nợ xấu thấp, dự phòng cao và vốn cao là các câu hỏi khác nhau; một tỷ lệ riêng không chứng minh ngân hàng an toàn.

## 1. NIM và CIR

`KỊCH_BẢN` Ngân hàng hư cấu có thu nhập lãi thuần cả năm 40 tỷ VND, tài sản sinh lãi bình quân 1.000 tỷ. `PHÉP_TÍNH` NIM (*net interest margin*, biên lãi ròng) minh họa = `40/1.000 = 4%/năm`. Không lấy dư nợ cuối kỳ thay số bình quân mà không ghi thay đổi phương pháp. Cơ cấu tài sản, lãi huy động và lịch tái định giá đều có thể ảnh hưởng NIM.

CIR (*cost-to-income ratio*, chi phí hoạt động trên thu nhập hoạt động) phụ thuộc định nghĩa tử và mẫu. `KỊCH_BẢN` Chi phí hoạt động 30 tỷ, tổng thu nhập hoạt động 100 tỷ: `PHÉP_TÍNH` CIR = `30/100 = 30%`. Chi phí dự phòng tín dụng giả định chưa nằm trong tử; đọc công thức ngân hàng thực tế trước khi so sánh.

## 2. Nhóm nợ, dự phòng và độ bao phủ

`SỰ_THẬT` [Thông tư 31/2024/TT-NHNN](https://vanban.chinhphu.vn/?classid=1&docid=210625&pageid=27160) quy định phân loại tài sản có, được sửa đổi bởi [Thông tư 37/2025/TT-NHNN](https://vanban.chinhphu.vn/?classid=1&docid=215867&pageid=27160&typegroupid=6). `CHƯA_BIẾT` Bài chưa đối chiếu toàn văn mọi sửa đổi và quy tắc tính của từng báo cáo để tái lập con số pháp lý cụ thể; cần kiểm bản hiện hành, nhóm nợ, kỳ và phạm vi.

Trong thực hành phân tích, *NPL* là nợ xấu và thường được mô tả theo nhóm nợ không đạt chuẩn, nhưng chỉ tiêu công bố có thể khác phạm vi: số dư trên bảng, sau điều chỉnh hay kèm nghĩa vụ ngoại bảng. `KỊCH_BẢN` Nợ xấu theo định nghĩa giả định 20 tỷ, tổng dư nợ tương ứng 1.000 tỷ: `PHÉP_TÍNH` tỷ lệ = 2%. Không coi số này là kết luận tuân thủ pháp luật.

Độ bao phủ nợ xấu có thể minh họa bằng `số dư dự phòng xác định theo phương pháp / số dư nợ xấu cùng phạm vi`. `KỊCH_BẢN` Dự phòng 15 tỷ, nợ xấu 20 tỷ: 15/20 = 75%. Cần kiểm ngân hàng bao gồm dự phòng chung/cụ thể, phạm vi hợp nhất và kỳ ra sao. Chi phí trích lập trong kỳ, số dư dự phòng và nợ đã xử lý là các đại lượng khác nhau; không cộng hoặc so mà bỏ qua định nghĩa.

## 3. CAR và ví dụ công bố

CAR (*capital adequacy ratio*, tỷ lệ an toàn vốn) là thước đo vốn theo khuôn khổ rủi ro; mẫu số và vốn đủ điều kiện phụ thuộc quy tắc cụ thể. Không thay bằng vốn chủ kế toán/tổng tài sản hoặc coi CAR là bảo đảm thanh khoản.

`SỰ_THẬT` [Techcombank — báo cáo kết quả năm 2025](https://techcombank.com/content/dam/techcombank/public-site/documents/bao-cao-ket-qua-kinh-doanh-2025-ke-hoach-2026-eng.pdf), ngày 03/04/2026, công bố tỷ lệ nợ xấu sau CIC cuối kỳ 2025 là 1,13% và trước CIC là 0,98%. Hai số có phạm vi điều chỉnh khác nhau theo báo cáo; không tự suy cả ngành hay dùng số này để đánh giá khoản nợ riêng. `CHƯA_BIẾT` Bài chưa tái lập tỷ lệ từ bảng nhóm nợ gốc và chưa xác định toàn bộ phương pháp điều chỉnh CIC của ngân hàng.

## Năm câu hỏi khi đọc

1. NIM dùng thu nhập nào, tài sản bình quân theo ngày hay số dư cuối kỳ?
2. CIR bao gồm chi phí nào, thu nhập có khoản bất thường không?
3. Nợ xấu, nhóm 2 và nghĩa vụ ngoại bảng được phân loại thế nào theo kỳ?
4. Chi phí dự phòng trong kỳ khác số dư dự phòng và khoản đã xử lý thế nào?
5. CAR theo khuôn khổ nào, mẫu số và vốn đủ điều kiện được xác định ra sao?

## Bài tập

1. Thu nhập lãi thuần 50 tỷ trên tài sản sinh lãi bình quân 1.000 tỷ: NIM giả định?
2. Chi phí hoạt động 40, thu nhập hoạt động 100 tỷ: CIR giả định?
3. Nợ xấu 10, dư nợ cùng phạm vi 500 tỷ: tỷ lệ?
4. Dự phòng 12, nợ xấu 10 tỷ: độ bao phủ minh họa?
5. Dự phòng là số dư và chi phí trích lập trong kỳ có tự bằng nhau không?
6. Vốn chủ/tổng tài sản có tự là CAR theo quy định không?

## Đáp án

1. 50/1.000 = 5%/năm trong giả định cùng kỳ.
2. 40/100 = 40%.
3. 10/500 = 2%.
4. 12/10 = 120% theo định nghĩa giả định, không bảo đảm thu hồi nợ.
5. Không; còn phụ thuộc sử dụng, hoàn nhập, chuyển nhóm và các điều chỉnh khác.
6. Không; CAR dùng khuôn khổ vốn đủ điều kiện và tài sản/rủi ro tương ứng.

## Lỗi thường gặp và ranh giới an toàn

So NIM khác cách tính, coi nhóm nợ và dự phòng là một, hoặc kết luận CAR cao loại bỏ rủi ro. Số Techcombank chỉ minh họa đọc công bố, không là khuyến nghị hay đánh giá toàn ngành.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Công thức chính xác, số dư nhóm nợ và dự phòng của từng ngân hàng/kỳ; tỷ lệ trích lập chi tiết và mọi sửa đổi hiện hành. Đọc báo cáo kiểm toán, thuyết minh và nguồn quản lý trước áp dụng.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [Techcombank — báo cáo năm 2025](https://techcombank.com/content/dam/techcombank/public-site/documents/bao-cao-ket-qua-kinh-doanh-2025-ke-hoach-2026-eng.pdf), 03/04/2026; [TT31/2024](https://vanban.chinhphu.vn/?classid=1&docid=210625&pageid=27160) và [TT37/2025](https://vanban.chinhphu.vn/?classid=1&docid=215867&pageid=27160&typegroupid=6). Ví dụ tỷ lệ còn lại là hư cấu.
