# BẢN NHÁP - CHƯA KIỂM DUYỆT: Đánh giá chiều sâu 61 bài và kế hoạch bổ sung kiến thức

- Ngày: `2026-10-31`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`; đối tượng là tệp trong repo, không phải dữ liệu thị trường.
- Người ghi: phiên chính (vai `research-coordinator`). Chưa chạy `source_fact_checker` / `risk_bear_reviewer` trên tài liệu này.

## 0. Phạm vi và giới hạn của chính lượt review này

- `SỰ_THẬT — đo tệp` Đã đo cấu trúc **cả 61 bài**: số từ, mục, bảng, câu bài tập, nhãn, liên kết. `python3 scripts/verify.py` và 9 unit test đều ĐẠT; 0 liên kết nội bộ hỏng.
- `SỰ_THẬT — đọc kỹ` Đã đọc toàn văn 011 và F4, đọc phần đầu 004, xem mục lục và bài tập H3, A4, F2, L2, A1. Đã tái tính tay ví dụ DCF của 011 (EV 1.340,9091; vốn chủ 1.140,9091; TV chiếm 86,44% EV): **đúng**.
- `CHƯA_BIẾT` Chưa đọc từng chữ 208.000 từ; chưa kiểm lại nguồn Internet của từng bài (các bài đã có biên bản kiểm nguồn riêng). Đánh giá "sâu/nông" là `Ý_KIẾN` dựa trên số đo và các bài đã đọc.
- Phần "còn thiếu gì" là so với mục tiêu của dự án (người Việt tự học tới mức tự nghiên cứu cổ phiếu toàn cầu), dựa trên nội dung repo; chưa đối chiếu lại với khung ngoài (CFA, v.v.) trong lượt này.

## 1. Kết luận một đoạn

`Ý_KIẾN` Bộ bài **tốt về kỷ luật, trung thực và độ phủ chủ đề, nhưng không đồng đều về chiều sâu**. Khoảng 16 bài (001–009, N2, N3, P1–P3, B3, V1–V2) là bài học thật: 2.500–7.800 từ, nhiều ví dụ có số, nhiều phiên. Khoảng 45 bài còn lại dài 900–1.500 từ: đúng là **phiếu tóm tắt có kiểm nguồn** (khái niệm + một ví dụ hư cấu + 6 câu ngắn), chưa đủ để người mới tự làm được việc. Đáng lo nhất là phần cốt lõi của định giá (010–012) và mô hình (F1–F2) lại mỏng hơn hẳn phần nền (009 dài 5.090 từ, 011 chỉ 1.178 từ).

## 2. Chấm điểm theo nhóm

| Nhóm | Bài | Từ/bài | Chiều sâu | Chất lượng nội dung | Nhận xét chính |
|---|---|---|---|---|---|
| Nền kế toán, chất lượng DN | 001–009, N2, N3 | 5.000–7.800 | **8/10** | 8/10 | Có trực giác → số → phản ví dụ → ôn cũ → tự làm. Điểm mạnh của repo. Hơi nặng nhãn và chi tiết chuẩn mực (004 có 56 nhãn/5.9k từ). |
| Tài chính cá nhân, an toàn, thị trường VN | P1–P3, B3, V1–V2 | 2.800–4.100 | **7/10** | 8/10 | Phong phú, nhiều bảng và nguồn VN. Số nguồn nhiều (V1: 62 URL) nên nhanh cũ; cần lịch rà. |
| Định giá lõi | 010, 011, 012 | 1.200–1.330 | **4/10** | 7/10 | Đúng nhưng chỉ đủ biết công thức. Thiếu: tái đầu tư = g/ROIC, TV sanity check, SBC/pha loãng, lease, lập mô hình trên bảng tính, độ nhạy hai chiều. |
| Mô hình và định giá nâng cao | F1, F2 | ~1.200 | **3/10** | 7/10 | Mô hình ba báo cáo không có một mô hình cân đối hoàn chỉnh trong bài; DDM + RIM + SOTP gộp trong 1.200 từ. |
| Ngành và chuyên ngành | 013, 014, F3, F4, F5, F6, F7 | 1.000–1.550 | **3/10** | 7/10 | Khung tốt, không có phân tích một công ty thật đến cuối. F4: đáp án chỉ là phép chia. F5 là khung, chưa có hồ sơ ngành nào. |
| Danh mục, tài sản, quỹ | N5, A1–A5, H4 | 940–1.550 | **4/10** | 7/10 | Đủ khái niệm; thiếu toán thật (duration, YTM, spread, TWR/MWR nhiều kỳ, drag của phí qua 20–30 năm). |
| Rủi ro, thống kê, hành vi | H1–H6, N7 | 920–1.300 | **3/10** | 7/10 | H3: sáu câu đều dạng đúng/sai. H5 (backtest) quá ngắn so với độ khó. Không có dữ liệu thật để tự làm. |
| Vĩ mô | 008, M1–M3 | 1.000–5.750 | 008 **7/10**; M1–M3 **3/10** | 7/10 | Vĩ mô nhảy từ 5.7k xuống 1k từ. Bảng số 008 vẫn là "lịch sử chưa xác minh lại". |
| Pháp lý, thực thi, sự kiện | L1–L3, V3–V5, B1–B2, K1–K2 | 900–1.400 | **4/10** | 7/10 | Chính xác thận trọng nhưng ít tình huống ra quyết định cụ thể. |
| Capstone và mẫu | 015, 016, hồ sơ Apple | 1.300–1.500 | **4/10** | 7/10 | Chỉ **một** hồ sơ mẫu (Apple, Mỹ). Chưa có mẫu cho doanh nghiệp Việt, ngân hàng, bất động sản, chu kỳ. |

`PHÉP_TÍNH` Trung bình có trọng số ≈ **4,8/10 về chiều sâu**, **≈ 7,3/10 về độ cẩn trọng/chính xác**. Chênh lệch này là kết luận chính: quy trình kiểm duyệt đã bảo đảm "không bịa" nhưng chưa bảo đảm "đủ sâu để làm được".

## 3. Điểm mạnh cần giữ

1. Cấu trúc nhất quán (mục tiêu → 1 phút → ôn cũ → ví dụ → bài tập → đáp án → lỗi thường gặp → điều chưa biết).
2. Trung thực: `CHƯA_BIẾT`, ranh giới an toàn, không khuyến nghị cá nhân, số hư cấu có nhãn `KỊCH_BẢN`.
3. Phép tính kiểm được (011 đúng khi tái tính tay).
4. Phủ rộng: từ đời sống tài chính tới pháp lý, hành vi, nhiều thị trường.
5. Cổng kiểm duyệt có biên bản đúng phiên bản; test cấu trúc chạy xanh.

## 4. Vấn đề chiều sâu, xếp theo mức nghiêm trọng

| # | Vấn đề | Bằng chứng | Hệ quả |
|---|---|---|---|
| D1 | **Hai tốc độ**: ~16 bài sâu, ~45 bài "primer" | Số từ bảng §2; 47/61 bài đúng 6 câu bài tập | Người học tưởng đã học xong chủ đề nhưng chưa làm được |
| D2 | **Bài tập nhận biết là chủ yếu** | H3, F4: câu như "có tự bằng nhau không?", đáp án một dòng | Không rèn kỹ năng nhiều bước; thiếu bài "bẩn" với dữ liệu thiếu/mâu thuẫn |
| D3 | **Gần như toàn ví dụ hư cấu một bước** | 011, F4, H3 | Không nối được với báo cáo thật; thiếu cảm giác con số lộn xộn |
| D4 | **Ít trường hợp Việt Nam làm tới cùng** | Tên doanh nghiệp VN chỉ xuất hiện ở 9 bài, chủ yếu như ví dụ nguồn | Mục tiêu người Việt nhưng chưa có một phân tích doanh nghiệp Việt hoàn chỉnh |
| D5 | **Chỉ một hồ sơ mẫu (Apple)** | `research/companies/US/AAPL` là báo cáo duy nhất; `research/sectors` trống | Chưa có "mẫu đạt chuẩn" cho ngân hàng, bất động sản, chu kỳ, bán lẻ |
| D6 | **Không có tệp thực hành chạy được** | `practice/` chỉ có một tệp markdown; không thấy bảng tính/mã mẫu | Học DCF/mô hình mà không dựng được mô hình |
| D7 | **Gánh "siêu dữ liệu" nặng trong thân bài** | Nhãn dày, đầu bài 6–7 dòng trạng thái kiểm duyệt, bảng nguồn dài | Đọc nặng; trong 011 chỉ ~45% là nội dung dạy |
| D8 | **Dữ liệu có hạn dùng** | 008 bảng cũ chưa xác minh; V1/V2/L3/B1 nhiều quy định, phí, thuế | Cần lịch rà soát và cờ "hết hạn" |
| D9 | **Chưa thử với người học** | README tự ghi | Không biết bài nào quá khó/dễ, thời lượng thật |
| D10 | **Đường học dài** | Nhánh 1 có 23 lượt đọc | Dễ bỏ cuộc trước khi chạm 016 |

## 5. Kiến thức còn thiếu (so với mục tiêu "tự nghiên cứu cổ phiếu có bằng chứng")

`Ý_KIẾN` Xếp theo giá trị cho người học. Đã grep nội dung: các từ khóa gạch đầu dòng bên dưới xuất hiện **0 lần** trong 61 bài (hoặc chỉ như câu loại trừ).

**G1 — Phân tích chất lượng/gian lận có công cụ (cao):** Beneish M-score, Altman Z, Piotroski F-score, kiểm tra tuần tự doanh thu–phải thu–tồn kho, quality of earnings, điều chỉnh chuẩn hóa lợi nhuận. 007 mới dừng ở cờ đỏ định tính.

**G2 — Cơ chế cổ phần ảnh hưởng giá trị (cao):** SBC/ESOP và pha loãng, mua lại cổ phiếu (khi nào tạo giá trị), chính sách cổ tức, cổ tức bằng cổ phiếu, phát hành thêm, hợp nhất–goodwill–ghi giảm, IPO/sáp nhập. Có rải rác nhưng không có bài riêng.

**G3 — Kinh tế ngành cụ thể (cao):** F5 chỉ có khung. Thiếu bài/hồ sơ: bán lẻ, phần mềm/SaaS (ARR, NRR, CAC/LTV), thép/hàng hóa chu kỳ (chuẩn hóa lợi nhuận, định giá đỉnh–đáy), dầu khí/năng lượng, điện–tiện ích, bảo hiểm nhân thọ, công ty chứng khoán, thực phẩm tiêu dùng, dược/y tế, REIT/bất động sản cho thuê.

**G4 — Định giá thực hành (cao):** mô hình DCF trên bảng tính, tái đầu tư = g/ROIC, độ nhạy hai chiều, kiểm tra TV, xử lý SBC/lease/hưu trí, định giá công ty chu kỳ/âm lãi, kỳ vọng thị trường (expectations investing). Nay chỉ có công thức.

**G5 — Công cụ có rủi ro cao ở VN (trung bình, ưu tiên an toàn):** chứng quyền, hợp đồng tương lai VN30, quyền chọn: ít nhất bài **hiểu rủi ro** vì thị trường VN có các sản phẩm này (hiện chỉ nhắc để loại trừ).

**G6 — Toán danh mục và trái phiếu (trung bình):** YTM, duration, convexity ở mức trực giác, spread tín dụng, rủi ro trái phiếu doanh nghiệp VN, tác động phí 20–30 năm, TWR/MWR nhiều kỳ có dữ liệu, tương quan trong khủng hoảng.

**G7 — Bằng chứng về phong cách đầu tư (trung bình):** hiệu quả thị trường, quản lý chủ động so với thụ động, các yếu tố (giá trị/chất lượng/đà), net-net, Magic Formula; vì sao nhiều chiến lược biến mất khi hết thống kê (nối H5).

**G8 — Hưu trí, nhà ở, tài chính đời người (trung bình):** BHXH, hưu trí tự nguyện, vay mua nhà so với thuê, mục tiêu dài hạn; P1–P3 mới tới ngân sách, quỹ khẩn cấp, bảo hiểm, nợ.

**G9 — Vĩ mô nâng cao (thấp–trung bình):** đường cong lợi suất, chế độ lạm phát, chu kỳ toàn cầu, bảng cân đối ngân hàng trung ương. M1–M3 đang ~1.000 từ.

**G10 — Kỹ năng dữ liệu (cao):** truy xuất XBRL/EDGAR/HOSE–HNX, làm sạch dữ liệu, bảng tính/Python tối thiểu, tái lập phép tính, kiểm đơn vị và kỳ.

**G11 — Ca thất bại và thành công đối chứng (trung bình):** K2 chỉ có Enron. Nên bổ sung ca quốc tế (Wirecard, Lehman, LTCM, Luckin, Evergrande) và ca VN đã có phán quyết/kết luận công khai, **chỉ dùng văn bản gốc và phán quyết**, không suy diễn.

**G12 — Đánh giá thành thạo (trung bình):** chưa có bài kiểm cuối chặng, bộ thẻ ôn cách quãng, rubric chấm tự làm.

## 6. Chuẩn "bài đủ sâu" đề xuất (áp dụng cho mọi bài được nâng cấp)

`Ý_KIẾN` Con số để thử, không phải ngưỡng khoa học:

1. 2.500–4.000 từ thân bài, chia 2–3 phiên có điểm dừng. Siêu dữ liệu kiểm duyệt rút về một khối cuối bài.
2. **Hai ví dụ có số**: một hư cấu đủ dữ kiện, một lấy từ **báo cáo thật** (ghi kỳ, đơn vị, phạm vi, link mở được). Ít nhất một ví dụ liên quan thị trường Việt Nam khi chủ đề cho phép.
3. Bài tập: **3 nhận biết, 3 tính nhiều bước, 1 bài "bẩn"** (thiếu dữ kiện/đơn vị lệch), 1 tình huống chuyển giao; có rubric chấm câu mở.
4. Có bản làm trên bảng tính (CSV/XLSX hoặc công thức mẫu) cho mọi bài có tính toán.
5. Một mục "Sai ở đâu": một phân tích sai có chủ ý để người học tìm lỗi.
6. Cuối bài: kiểm tra chuyển bài (3 câu không nhìn mẫu).
7. Giữ cổng kiểm nguồn + phản biện cho **bản sau nâng cấp**, không dùng biên bản cũ.

## 7. Kế hoạch bổ sung theo đợt

| Đợt | Việc | Sản phẩm | Hoàn thành khi |
|---|---|---|---|
| **0 — Chuẩn hóa (nhỏ)** | Viết `docs/LESSON_DEPTH_STANDARD.md` từ §6; thêm kiểm tra tự động (số từ, số loại câu, có ví dụ thật, có tệp bảng tính); ghi cột "Chiều sâu" vào sổ kiểm duyệt; gom siêu dữ liệu xuống cuối bài | Chuẩn + test + bảng hiện trạng | Test chạy trên 61 bài, báo cáo bài nào chưa đạt |
| **1 — Vá chiều sâu lõi định giá** | Viết lại **010 → 011 → 012 → F1 → F2** theo chuẩn; thêm `practice/models/` với DCF, ba báo cáo, độ nhạy (XLSX hoặc CSV+công thức); dùng báo cáo thật của một DN phi tài chính | 5 bài ≈ 3k từ + 3–4 mô hình mẫu | Người học dựng lại DCF từ báo cáo thật, giải thích biến chi phối kết quả |
| **2 — Hồ sơ mẫu đa dạng (D4, D5, G3)** | Lập 4 hồ sơ mẫu: DN Việt phi tài chính, ngân hàng Việt, công ty chu kỳ, bán lẻ/phần mềm; chọn theo người học; dùng cùng mẫu `templates/company-report.md` | 4 hồ sơ nháp + 4 cặp biên bản | Mỗi hồ sơ có 3 kịch bản, rủi ro, điều làm luận điểm mất hiệu lực |
| **3 — Lấp khoảng trống cao (G1, G2, G4, G10)** | Bài mới: **Q1 Chất lượng lợi nhuận có công cụ** (Beneish/Altman/Piotroski), **Q2 SBC, pha loãng, mua lại, cổ tức**, **Q3 Chuẩn hóa lợi nhuận và công ty chu kỳ**, **Q4 Lấy dữ liệu: EDGAR/XBRL/HOSE, bảng tính** | 4 bài + tệp mẫu | Làm được bài "bẩn" trên dữ liệu thật |
| **4 — Nâng cấp bài mỏng theo ưu tiên** | Nâng cấp **N1, N4, N5, H3–H5, A1–A4, M1–M3, F3–F7, 013, 014** (nhóm 3/10–4/10 trong §2) theo chuẩn; mỗi lần 3–4 bài | ~25 bài sâu hơn | Mỗi bài đạt chuẩn §6 và có biên bản mới |
| **5 — Chủ đề còn thiếu (G5–G9, G11)** | Bài mới: **chứng quyền & phái sinh VN (hiểu rủi ro)**, **trái phiếu: YTM/duration/spread**, **bằng chứng phong cách đầu tư**, **hưu trí & nhà ở**, **vĩ mô nâng cao**, **thêm 3–4 ca thất bại** | 8–10 bài | Có bài tập số và ca đối chứng |
| **6 — Đánh giá thành thạo (G12, D9)** | Kiểm tra cuối chặng, thẻ ôn cách quãng, rubric; chạy thử 3 phiên với một người học thật; đo phút thật, lỗi, câu chưa hiểu | Bộ kiểm tra + báo cáo phản hồi | Có dữ liệu học thật trước khi chốt lộ trình dài hạn |
| **Liên tục — Dữ liệu hết hạn (D8)** | Thêm trường `Hết hạn rà lúc` ở bài có quy định/phí/thuế/số liệu; danh sách rà 6 tháng/lần; thay bảng số 008 bằng mẫu cập nhật có nguồn | Bảng hạn dùng + lịch rà | Không bài nào dẫn quy định không có ngày rà |

### Thứ tự đề xuất và lý do

- **Đợt 0 → 1 trước.** Chuẩn xác định "đủ sâu" thế nào; Đợt 1 sửa chỗ lệch nặng nhất giữa độ khó và độ dài.
- **Đợt 2 song song Đợt 3** (hai việc độc lập về tệp), sau đó Đợt 4 chia theo cụm.
- **Đợt 6 nên chạy sớm** một lần nhỏ (sau Đợt 1) để biết chuẩn §6 có quá nặng không.

### Ước lượng khối lượng

`CHƯA_BIẾT` công sức thực tế. `Ý_KIẾN` đếm đầu việc: Đợt 1 (5 bài + mô hình), Đợt 2 (4 hồ sơ), Đợt 3 (4 bài), Đợt 4 (~25 bài), Đợt 5 (8–10 bài). Đợt 4 là khối lượng lớn nhất; có thể giảm nếu người học chỉ theo một nhánh (xem điều kiện đổi kế hoạch).

## 8. Rủi ro của kế hoạch này

- Nâng cấp ồ ạt có thể làm lệch liên kết và số từ trong 61 bài → mỗi đợt chạy `verify.py` + test và rà liên kết.
- Bài dài hơn có thể làm người học bỏ cuộc → giữ phiên có điểm dừng, thử ở Đợt 6 sớm.
- Hồ sơ doanh nghiệp thật dễ cũ và dễ bị hiểu thành khuyến nghị → luôn gắn nhãn học tập, ghi ngày dữ liệu, không kết luận mua/bán.
- Ca thất bại tại Việt Nam nhạy cảm pháp lý → chỉ dùng văn bản gốc, bản án/kết luận đã công bố, ghi rõ phạm vi.
- Công thức/chuẩn mực (IFRS 18, VAS, thông tư) đổi → bài chuẩn mực cần ngày rà.

## 9. Điều chưa biết

- Người học đã hiểu tới đâu và mục tiêu cuối (hiểu kinh doanh, đọc cổ phiếu, hay quỹ/danh mục).
- Bài nào thực sự quá khó hoặc quá dễ khi dùng.
- Mức độ chính xác của từng nguồn Internet trong ~45 bài chưa được đọc toàn văn lượt này (đã có biên bản riêng từng bài).
- Có nên giữ cả ba nhánh hay thu gọn theo mục tiêu người học.

## 10. Nhật ký triển khai Đợt 0–1 (2026-10-31)

- Đợt 0: đã thêm [chuẩn chiều sâu](../docs/LESSON_DEPTH_STANDARD.md), `scripts/check_lesson_depth.py` và test. Hiện **5/61 bài đạt bậc S** (010, 011, 012, F1, F2).
- Đợt 1: viết lại 010, 011, 012, F1, F2 (3 phiên mỗi bài, 10 câu bài tập, bài "bẩn", "sai ở đâu", kiểm tra chuyển bài); thêm [mô hình Python](practice/models/valuation.py) và số Apple FY2025 lấy từ 10-K; 18 test chạy xanh, gồm tái tính mọi số chính trong bài.
- Kiểm duyệt: bốn vòng kiểm nguồn + phản biện độc lập. Vòng 1 tìm 5 lỗi nghiêm trọng (F1 đòn bẩy vận hành, CCC Apple, RIM–Apple, FCF0 chưa chuẩn hóa thuế, lưới giá Apple xa thị trường); vòng 2 còn 2 lỗi trung bình; vòng 3–4 không còn lỗi nghiêm trọng hay trung bình. Cả năm bài **đã qua cổng xuất bản** `validate_report.py`, đã bỏ nhãn nháp.
- Chưa làm: bảng tính Excel; nguồn cho Fisher dạng nhân, quan hệ sạch của RIM, thiểu số/chi phí trụ sở của SOTP; đối chiếu giá AAPL với sàn.
