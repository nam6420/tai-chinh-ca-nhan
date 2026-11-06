# Bài M3 — Dòng vốn, thương mại và địa chính trị

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt chính xác cán cân thương mại hàng hóa, cán cân vãng lai (`Current Account`), dòng vốn đầu tư trực tiếp nước ngoài (`FDI` đăng ký so với giải ngân) và dòng vốn danh mục (`FII`); định lượng tác động của thuế quan, đứt gãy vận tải biển, quy tắc xuất xứ và giá trị gia tăng nội địa (`Domestic Value Added`) lên biên lợi nhuận cùng chu kỳ vốn lưu động của doanh nghiệp.
- Bài trước liên quan: [M1](M1-monetary-policy-rates-fx-credit.md), [M2](M2-credit-real-estate-cycle.md), [A5](A5-international-investing-currency-tax.md), [F5](F5-vietnam-industry-research-framework.md).
- Thời lượng: Ba phiên học có điểm dừng (mỗi phiên 45 phút) + thực hành trên mô hình [cyclical.py](../practice/models/cyclical.py) và [earnings_quality.py](../practice/models/earnings_quality.py).
- Câu hỏi cốt lõi: **Khi đọc tin xuất nhập khẩu kỷ lục, FDI đăng ký tăng mạnh hay một nước áp thuế phòng vệ thương mại mới, con số đó thực sự chảy vào dòng tiền của nền kinh tế và doanh nghiệp nội địa bao nhiêu phần trăm?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/M3-fact-check.md), [phản biện](../reviews/M3-risk-review.md).

---

## Hiểu bài trong một phút

Việt Nam là một trong những nền kinh tế có độ mở thương mại lớn nhất thế giới. Tuy nhiên, độ mở lớn cũng tạo ra ba ảo giác thống kê rất dễ đánh lừa nhà đầu tư chứng khoán:
1. **Nhập siêu hay xuất siêu hàng hóa không đồng nhất với toàn bộ Cán cân thanh toán quốc tế (`Balance of Payments — BOP`)**, vì chưa tính cán cân dịch vụ (vận tải, du lịch, bảo hiểm), thu nhập sơ cấp (lợi nhuận chuyển về nước của khối FDI), kiều hối và tài khoản tài chính.
2. **Vốn FDI đăng ký (`Registered FDI`) chỉ là ý định đầu tư trên giấy phép**, còn **Vốn FDI thực hiện/giải ngân (`Disbursed/Implemented FDI`)** mới là chi tiêu xây dựng nhà xưởng, mua máy móc thực tế trong kỳ.
3. **Kim ngạch xuất khẩu gộp (`Gross Exports`) khác xa giá trị gia tăng nội địa (`Domestic Value Added — DVA`)**: Một lô hàng xuất khẩu 100 triệu USD nhưng phải nhập khẩu 78 triệu USD linh kiện đầu vào thì thặng dư thương mại thực giữ lại trong nước chỉ là 22 triệu USD. Khi xảy ra cú sốc thuế quan hoặc cước vận tải biển tăng vọt, biên lợi nhuận của doanh nghiệp được quyết định bởi điều khoản giao hàng (`Incoterms`: `FOB` hay `CIF/DDP`), quyền định giá (`pricing power`) và tỷ lệ nội địa hóa chứ không phải quy mô doanh thu xuất khẩu gộp.

---

## Ôn bài cũ

- Trong [Bài M1 — Chính sách tiền tệ, lãi suất, tỷ giá và tín dụng](M1-monetary-policy-rates-fx-credit.md) và [Bài M2 — Chu kỳ tín dụng và bất động sản](M2-credit-real-estate-cycle.md), ta đã xét vĩ mô nội địa. Bài M3 khép lại **Tầng M** bằng cán cân thanh toán (`BOP`), thương mại quốc tế, dòng vốn `FDI / FII` và địa chính trị.

---

## Phiên 1 — Giải phẫu Cán cân thanh toán (`BOP`), Thương mại hàng hóa và Dòng vốn `FDI / FII`

### 1.1. Bốn mảnh ghép của Cán cân thanh toán quốc tế theo chuẩn IMF

Khi phân tích cung – cầu ngoại tệ quốc gia và áp lực tỷ giá (kết nối với bài [M1](M1-monetary-policy-rates-fx-credit.md)), bạn không thể chỉ nhìn vào con số xuất siêu hay nhập siêu hàng hóa hàng tháng.

`SỰ_THẬT` Theo khung phương pháp luận của Quỹ Tiền tệ Quốc tế tại [IMF — Balance of Payments and International Investment Position Statistics (BOP/IIP)](https://data.imf.org/Datasets/BOP), cán cân thanh toán quốc tế gồm các tài khoản hạch toán kép có phạm vi hoàn toàn khác nhau:

| Thành phần trong `BOP` | Đo lường dòng tiền/giao dịch gì? | Đặc thù cấu trúc tại Việt Nam | Sai lầm phổ biến cần tránh |
|---|---|---|---|
| **1. Cán cân hàng hóa (`Goods balance`)** | Xuất khẩu hàng hóa trừ Nhập khẩu hàng hóa. | Quy mô rất lớn; khu vực FDI thường xuất siêu lớn còn khu vực trong nước thường nhập siêu máy móc, nguyên liệu. | Đồng nhất cán cân hàng hóa với toàn bộ cán cân vãng lai hoặc dự trữ ngoại hối tăng thêm. |
| **2. Cán cân dịch vụ (`Services balance`)** | Xuất khẩu dịch vụ (du lịch quốc tế, vận tải, CNTT) trừ Nhập khẩu dịch vụ (cước tàu biển quốc tế, bảo hiểm hàng hải, du học). | Việt Nam thường nhập siêu dịch vụ vận tải biển và bảo hiểm quốc tế khi kim ngạch hàng hóa mở rộng. | Quên rằng khi nhập khẩu hàng theo giá `CIF`, phần cước tàu và bảo hiểm trả cho hãng ngoại là dòng chi ngoại tệ dịch vụ. |
| **3. Thu nhập sơ cấp (`Primary income`) & Thứ cấp (`Secondary income`)** | **Sơ cấp:** Lãi vay nợ nước ngoài và lợi nhuận khối FDI chuyển về công ty mẹ. **Thứ cấp:** Chuyển giao một chiều (kiều hối, viện trợ). | Khối FDI có lãi lớn sẽ ghi nhận dòng chi thu nhập sơ cấp lớn; ngược lại dòng kiều hối (`Secondary income`) luôn là nguồn thu ngoại tệ ròng ổn định. | Nhìn thấy khối FDI xuất siêu hàng chục tỷ USD mà quên phần lợi nhuận hợp pháp thuộc về công ty mẹ nước ngoài. |
| **4. Tài khoản tài chính (`Financial account`: `FDI`, `FII`, Vay nợ)** | Đầu tư trực tiếp (`FDI`), đầu tư danh mục chứng khoán (`FII`), vay và trả nợ nước ngoài, tiền gửi xuyên biên giới. | Dòng vốn `FDI` giải ngân có tính dài hạn; dòng vốn `FII` và tín dụng thương mại ngắn hạn nhạy cảm mạnh với chênh lệch lãi suất VND–USD (`M1`). | Lấy số `FDI đăng ký` cộng thẳng vào cung ngoại tệ trong năm hoặc đồng nhất bán ròng trên sàn chứng khoán (`FII`) với tổng dòng vốn quốc gia. |

### 1.2. Đọc đúng dữ liệu thực tế 9 tháng năm 2026: Hàng hóa và FDI

`SỰ_THẬT` Theo [Cục Thống kê — Báo cáo tình hình kinh tế - xã hội Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/):
1. **Về thương mại hàng hóa 9 tháng năm 2026:**
   - Kim ngạch xuất khẩu hàng hóa sơ bộ đạt `434,30 tỷ USD`; nhập khẩu hàng hóa sơ bộ đạt `453,72 tỷ USD`.
   - `PHÉP_TÍNH` Cán cân thương mại hàng hóa 9 tháng năm 2026:
     $$\text{Cán cân hàng hóa 9T2026} = 434{,}30 - 453{,}72 = -19{,}42\text{ tỷ USD (Nhập siêu hàng hóa 19,42 tỷ USD)}$$
2. **Về vốn đầu tư nước ngoài (`FDI`) 9 tháng năm 2026:**
   - Tổng vốn đầu tư nước ngoài **đăng ký (`Registered FDI`)** tính đến `30/09/2026` đạt `50,36 tỷ USD`.
   - Vốn đầu tư trực tiếp nước ngoài **thực hiện/giải ngân (`Implemented FDI`)** 9 tháng năm 2026 ước đạt `21,07 tỷ USD`.

`SUY_LUẬN` Đặt hai cặp số liệu này cạnh nhau giúp rút ra 3 nguyên tắc:
- **Không lấy `50,36 − 21,07 = 29,29 tỷ USD` làm "số ngoại tệ chắc chắn sẽ chảy vào Việt Nam trong quý IV":** Con số `50,36 tỷ USD` là cam kết cấp phép đa niên (giải ngân trong 2–5 năm, một phần bằng máy móc nhập khẩu hoặc vay tại chỗ), còn `21,07 tỷ USD` giải ngân bao gồm cả tiến độ của các dự án đã đăng ký từ những năm trước.
- **Nhập siêu hàng hóa `19,42 tỷ USD` cần bóc tách theo cấu trúc mặt hàng:** Nhập khẩu máy móc, linh kiện điện tử để lắp đặt cho lượng vốn FDI thực hiện `21,07 tỷ USD` và chuẩn bị đơn hàng xuất khẩu khác hoàn toàn với nhập siêu hàng tiêu dùng.
- **`CHƯA_BIẾT` cán cân thanh toán tổng thể (`Overall BOP`):** Báo cáo 9 tháng công bố sớm số hàng hóa và FDI, nhưng bảng `BOP` đầy đủ của NHNN có độ trễ theo quý, nên phải gắn nhãn `CHƯA_BIẾT` với cán cân vãng lai tại thời điểm đọc tin nhanh.

### 1.3. Giá trị gia tăng nội địa (`Domestic Value Added — DVA`) trong chuỗi cung ứng

Công thức tách **Xuất khẩu gộp (`Gross Exports`)** và **Giá trị gia tăng nội địa (`DVA`)**:
$$\text{DVA (USD)} = \text{Doanh thu xuất khẩu (USD)} - \text{Chi phí nguyên vật liệu, linh kiện & dịch vụ nhập khẩu trực tiếp (USD)}$$

`KỊCH_BẢN` So sánh hai doanh nghiệp cùng xuất khẩu `200 triệu USD/năm`:
- **Doanh nghiệp Lắp ráp Điện tử X (`CMT`):** Xuất khẩu `200 triệu USD`, nhập khẩu linh kiện từ nước ngoài `176 triệu USD` → `PHÉP_TÍNH` `DVA_X = 200 − 176 = 24 triệu USD` (`Tỷ lệ DVA = 12,0%`).
- **Doanh nghiệp Chế biến Thủy sản / Gỗ Y (Tích hợp nguyên liệu nội địa):** Xuất khẩu `200 triệu USD`, chỉ nhập khẩu `30 triệu USD` phụ liệu đặc chủng → `PHÉP_TÍNH` `DVA_Y = 200 − 30 = 170 triệu USD` (`Tỷ lệ DVA = 85,0%`).

`SUY_LUẬN` Dù cả hai cùng ghi nhận `200 triệu USD` xuất khẩu trên thống kê hải quan, doanh nghiệp Y tạo ra thặng dư ngoại tệ ròng gấp `170 / 24 ≈ 7,08 lần` doanh nghiệp X, nhưng Y lại nhạy cảm hơn trước các vụ kiện chống bán phá giá tại thị trường đích.

> **Điểm dừng phiên 1:** Liên hệ với bài [F5](F5-vietnam-industry-research-framework.md): Trong chuỗi giá trị dệt may (`CMT` vs `FOB` vs `ODM`), mắt xích nào có tỷ lệ `DVA` cao hơn và mắt xích nào phải gánh rủi ro tồn kho nguyên liệu khi đơn hàng toàn cầu giảm?

---

## Phiên 2 — Định lượng cú sốc Thuế quan (`Tariffs`), Cước vận tải (`Freight`) và Vốn lưu động (`Working Capital`)

### 2.1. Điều khoản `Incoterms` (`FOB` vs `CIF / DDP`) quyết định ai trả tiền cước và thuế

Khi xảy ra đứt gãy tuyến hàng hải hoặc áp thuế quan mới, câu hỏi đầu tiên là **"Doanh nghiệp bán hàng theo điều khoản Incoterms nào?"**:

| Điều khoản `Incoterms` | Nghĩa vụ của Nhà xuất khẩu (Việt Nam) | Nghĩa vụ của Nhà nhập khẩu (Mỹ / EU / Nhật) | Ai chịu thiệt hại trực tiếp ngay trên BCTC khi cước tàu / thuế tăng đột biến? |
|---|---|---|---|
| **`FOB` (`Free On Board`)** | Giao hàng qua lan can tàu tại cảng Việt Nam (Cát Lái, Cái Mép, Hải Phòng). | Thuê tàu biển quốc tế, trả cước (`ocean freight`), bảo hiểm và nộp thuế nhập khẩu tại nước đích. | **Nhà nhập khẩu chịu trực tiếp.** Nhà xuất khẩu Việt Nam không bị đội chi phí bán hàng trên lô đã chốt `FOB`, nhưng có thể bị ép giảm giá ở đơn hàng quý sau. |
| **`CIF` / `CFR`** | Phải thuê tàu và **trả tiền cước tàu biển + bảo hiểm** đến cảng đích nước ngoài. | Nhận hàng tại cảng đích và nộp thuế nhập khẩu. | **Nhà xuất khẩu Việt Nam chịu trực tiếp rủi ro giá cước tàu biển!** Nếu đã chốt giá `CIF` cố định mà cước tàu tăng vọt, biên lợi nhuận bị ăn mòn ngay. |
| **`DDP` (`Delivered Duty Paid`)** | Chịu toàn bộ cước tàu, bảo hiểm và **nộp luôn thuế nhập khẩu (`tariff`)** tận kho người mua. | Nhận hàng tại kho với giá trọn gói. | **Nhà xuất khẩu Việt Nam chịu toàn bộ cả rủi ro cước tàu lẫn rủi ro tăng thuế nhập khẩu** cho các hợp đồng đã chốt giá `DDP`. |

### 2.2. Kịch bản định lượng toàn diện: Cú sốc kép Thuế quan + Cước vận tải + Kéo dài vốn lưu động

`KỊCH_BẢN` Công ty Nội thất Gỗ Omega bán hàng sang Bắc Mỹ với doanh thu cơ sở `50,00 triệu USD/năm` (`2.500 container/năm`, giá bán `20.000 USD/container` theo điều khoản `CIF`):
- **Cấu trúc chi phí cơ sở:** Giá vốn sản xuất (`COGS`) = `15.600 USD/cont`; Cước tàu `CIF` do Omega trả = `2.000 USD/cont`; Chi phí `SG&A` khác = `1.000 USD/cont` → **`EBIT` cơ sở** = `20.000 − 15.600 − 2.000 − 1.000 = 1.400 USD/cont` (tổng `EBIT` = `2.500 × 1.400 = 3,50 triệu USD/năm`).
- **Ba cú sốc xảy ra đồng thời trong năm:**
  1. **Cước tàu biển tăng:** Từ `2.000 USD` lên `3.400 USD/cont` (`+1.400 USD/cont`).
  2. **Chia sẻ thuế quan và phụ phí cước:** Để giữ khách khi nước nhập khẩu áp thuế mới, Omega phải **giảm giá bán cơ sở `3,0%`** (`−600 USD/cont`), và chỉ đàm phán thu thêm được phụ phí cước từ khách hàng là `+800 USD/cont` (sản lượng giữ nguyên `2.500 cont`).
  3. **Tắc nghẽn vận tải làm phình Vốn lưu động:** Thời gian tàu chạy vòng và chờ cảng kéo dài làm vòng quay khoản phải thu + hàng trên biển tăng thêm **30 ngày** (tính trên doanh thu gốc `50,00 triệu USD/năm`, năm 360 ngày), phải vay vốn lưu động ngắn hạn lãi suất `6,0%/năm`.

`PHÉP_TÍNH` Tác động lên `EBIT`, Vốn lưu động và `EBT`:
1. **Biến động `EBIT`:**
   - Giá thu thực tế mới: `20.000 − 600 + 800 = 20.200 USD/cont`.
   - Trừ `COGS` (`15.600`), cước mới (`3.400`) và `SG&A` khác (`1.000`) → `EBIT` mới = `200 USD/cont`.
   - **Tổng `EBIT` cả năm mới:** `2.500 × 200 = 0,50 triệu USD/năm` (giảm `85,71%` so với mức `3,50 triệu USD` cơ sở!).
2. **Chi phí lãi vay vốn lưu động tăng thêm do tàu trễ 30 ngày:**
   - Vốn lưu động bị giam thêm: `50,00 triệu USD × (30 / 360) ≈ 4,1667 triệu USD`.
   - Lãi vay vốn lưu động phát sinh thêm: `4,1667 triệu USD × 6,0% = 0,25 triệu USD/năm`.
3. **Lợi nhuận trước thuế (`EBT`) mới:** `0,50 − 0,25 = 0,25 triệu USD/năm` (giảm `92,86%` so với mức `3,50 triệu USD` ban đầu dù sản lượng xuất khẩu giữ nguyên 2.500 container!). Bạn có thể kiểm chứng hiện tượng "doanh thu tăng nhẹ nhưng `CFO` âm do phình phải thu/tồn kho" qua [earnings_quality.py](../practice/models/earnings_quality.py).

> **Điểm dừng phiên 2:** Nếu Omega bán hàng theo điều khoản `FOB Cát Lái` thay vì `CIF`, khoản lỗ cước vận tải `600 USD/cont` sẽ dịch chuyển sang ai?

---

## Phiên 3 — Rủi ro địa chính trị, Quy tắc xuất xứ (`Rules of Origin`) và Bảng kiểm 5 bước

`SỰ_THẬT` Thông cáo [WTO — Global Trade Outlook and Statistics (08/10/2026)](https://www.wto.org/english/news_e/news26_e/stat_08oct26_510_e.htm) khi công bố dự báo thương mại hàng hóa toàn cầu 2026–2027 đã nhấn mạnh cả động lực hàng hóa công nghệ lẫn rủi ro phân mảnh chính sách thương mại và gián đoạn vận tải.

`SUY_LUẬN` Khi đánh giá một ngành xuất khẩu Việt Nam (thép HPG, gỗ, thủy sản, dệt may, lốp xe) trước rủi ro phòng vệ thương mại (thuế chống bán phá giá `AD`, chống trợ cấp `CVD`, chống lẩn tránh thuế `Anti-Circumvention`), cần kiểm tra **3 tiêu chí Quy tắc xuất xứ (`Rules of Origin — ROO`)** và **Bảng kiểm 5 bước**:
- **Ba tiêu chí xuất xứ:** (1) Tỷ lệ hàm lượng giá trị khu vực/nội địa (`Regional Value Content — RVC`), (2) Chuyển đổi mã số hàng hóa (`Change in Tariff Classification — CTC`), và (3) Truy xuất nguồn gốc nguyên liệu thượng nguồn (ví dụ tự luyện thép cuộn cán nóng `HRC` từ quặng sắt qua lò cao `BF/BOF` như HPG trong [cyclical.py](../practice/models/cyclical.py) giúp phòng vệ pháp lý tốt hơn hẳn việc nhập bán thành phẩm về cán lại).

| Bước kiểm tra | Câu hỏi phân tích bắt buộc | Nguồn dữ liệu cần mở |
|---|---|---|
| **1. Bản chất pháp lý** | Sắc lệnh đã có hiệu lực, quyết định sơ bộ, quyết định cuối cùng hay mới là đơn kiến nghị điều tra? | Công báo Bộ Thương mại nước nhập khẩu, Cục Phòng vệ thương mại (Bộ Công Thương). |
| **2. Tỷ trọng thị trường đích** | Thị trường bị áp thuế chiếm bao nhiêu `%` tổng doanh thu và lợi nhuận gộp của công ty? | Thuyết minh "Doanh thu theo khu vực địa lý" trên BCTC kiểm toán / Báo cáo thường niên. |
| **3. Xuất xứ đầu vào** | Tỷ lệ nguyên liệu nhập từ quốc gia bị điều tra là bao nhiêu? Có tự chủ thượng nguồn nội địa không? | Thuyết minh Hàng tồn kho, danh sách nhà cung cấp chính. |
| **4. Điều khoản `Incoterms`** | Xuất khẩu theo giá `FOB` hay `CIF/DDP`? Kỳ hạn chốt giá theo chuyến hay theo quý? | Tỷ trọng "Chi phí vận chuyển xuất khẩu" trong Thuyết minh Chi phí bán hàng. |
| **5. Chênh lệch thuế với đối thủ** | Mức thuế áp cho doanh nghiệp **cao hơn hay thấp hơn** các đối thủ cùng ngành trong và ngoài nước? | Bảng mức thuế riêng biệt (`separate rate`) trong phán quyết điều tra. |

`SUY_LUẬN` Lưu ý bước 5: Nếu đối thủ bị áp thuế `25%–50%` trong khi doanh nghiệp đầu ngành có hồ sơ kế toán minh bạch được hưởng thuế `0%`, vụ kiện lại giúp doanh nghiệp đầu ngành **chiếm thêm thị phần xuất khẩu**.

> **Điểm dừng phiên 3:** Kết nối `M1–M2–M3`: Một cú sốc thuế quan làm giảm xuất khẩu và thu hẹp FDI giải ngân (`M3`) sẽ truyền dẫn thế nào sang tỷ giá, thanh khoản ngân hàng (`M1`) và cầu thuê đất khu công nghiệp (`M2`)?

---

## Ví dụ từ nguồn thật

1. **Khung thống kê Cán cân thanh toán quốc tế của IMF:**
   `SỰ_THẬT` Mở trực tiếp [IMF — Balance of Payments and International Investment Position Statistics (BOP)](https://data.imf.org/Datasets/BOP): Tài liệu IMF tách bạch Tài khoản vãng lai (`Current Account` gồm hàng hóa, dịch vụ, thu nhập sơ cấp, thu nhập thứ cấp) với Tài khoản vốn và Tài khoản tài chính (`FDI`, `Portfolio Investment`, dự trữ ngoại hối).
2. **Dữ liệu thương mại hàng hóa và FDI 9 tháng năm 2026 tại Việt Nam:**
   `SỰ_THẬT` Mở [Cục Thống kê — Báo cáo tình hình kinh tế - xã hội Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/): Xuất khẩu hàng hóa 9 tháng đạt `434,30 tỷ USD`, nhập khẩu đạt `453,72 tỷ USD`, nhập siêu hàng hóa sơ bộ `19,42 tỷ USD`; vốn FDI đăng ký đến `30/09/2026` đạt `50,36 tỷ USD` và vốn FDI thực hiện ước đạt `21,07 tỷ USD`.
3. **Báo cáo Triển vọng Thương mại Toàn cầu của WTO:**
   `SỰ_THẬT` Mở [WTO — Global Trade Outlook and Statistics (08/10/2026)](https://www.wto.org/english/news_e/news26_e/stat_08oct26_510_e.htm): Công bố dự báo thương mại hàng hóa toàn cầu 2026–2027 kèm phân tích rủi ro gián đoạn địa chính trị và chính sách thương mại.

---

## Bài tập

Hãy tự giải 10 bài tập dưới đây trước khi mở phần Đáp án:

1. **Tính cán cân hàng hóa và phân biệt với cán cân vãng lai:** Trong 9 tháng năm 2026, xuất khẩu hàng hóa đạt `434,30 tỷ USD` và nhập khẩu đạt `453,72 tỷ USD` ([Cục Thống kê](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/)). Giả sử trong cùng kỳ (số giả định để luyện phương pháp IMF), cán cân dịch vụ thâm hụt `8,50 tỷ USD`, thu nhập sơ cấp ròng thâm hụt `14,00 tỷ USD` và thu nhập thứ cấp ròng (kiều hối) thặng dư `12,00 tỷ USD`. Tính: (a) Cán cân hàng hóa, và (b) Cán cân vãng lai (`Current Account`).
2. **Phân biệt FDI đăng ký và FDI thực hiện:** Đến `30/09/2026`, tổng vốn FDI đăng ký đạt `50,36 tỷ USD` và FDI thực hiện đạt `21,07 tỷ USD` ([Cục Thống kê](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/)). Tính tỷ lệ giữa FDI thực hiện và FDI đăng ký trong kỳ, và giải thích vì sao không được lấy hiệu `29,29 tỷ USD` làm vốn chắc chắn giải ngân cuối năm.
3. **Tính Giá trị gia tăng nội địa (`DVA`):** Công ty lốp xe xuất khẩu đạt doanh thu `300 triệu USD/năm`, mua cao su thiên nhiên trong nước `90 triệu USD` (bằng VND), nhập khẩu cao su tổng hợp và hóa chất từ nước ngoài `135 triệu USD`, trả cước tàu ngoại `15 triệu USD`. Tính: (a) Giá trị gia tăng nội địa gộp (`DVA`) giữ lại trong nước, và (b) Tỷ lệ `DVA / Doanh thu xuất khẩu`.
4. **Chia sẻ gánh nặng thuế quan (`Tariff pass-through`):** Doanh nghiệp xuất khẩu tôm sang thị trường A đạt doanh thu `60 triệu USD/năm`, biên `EBIT` ban đầu `8,0%`. Khi thị trường A áp thuế bổ sung `10,0%`, khách hàng chịu `6,0%` còn doanh nghiệp giảm giá bán `4,0%` (sản lượng và tổng chi phí USD không đổi). Tính `EBIT` trước và sau khi giảm giá bán `4,0%`.
5. **So sánh `FOB` và `CIF` khi cước tàu tăng:** Công ty X (bán `FOB`) và Công ty Y (bán `CIF`) cùng xuất `1.000 container` trong quý và cùng có `EBIT` dự kiến `1.200 USD/container`. Trước ngày giao hàng, cước tàu tăng thêm `+900 USD/container` và chưa kịp đổi giá bán. Tính `EBIT` thực tế trong quý của X và Y.
6. **Chi phí vốn lưu động khi tàu chạy chậm thêm 24 ngày:** Doanh nghiệp dệt may có doanh thu xuất khẩu `120 triệu USD/năm` (`360 ngày`). Do tàu đi vòng làm thời gian vận chuyển và thu tiền kéo dài thêm `24 ngày`, công ty phải vay thêm vốn lưu động USD lãi suất `6,5%/năm`. Tính vốn lưu động bị giam thêm và chi phí lãi vay phát sinh thêm trong 1 năm.
7. **Quy tắc hàm lượng giá trị khu vực (`RVC >= 40%`):** Hiệp định FTA quy định `RVC = (Giá FOB − Nguyên liệu ngoài khối) / Giá FOB >= 40%` để hưởng thuế `0%`. Sản phẩm có giá `FOB = 500 USD/chiếc`, đang dùng `320 USD` linh kiện ngoài khối. Sản phẩm đã đạt chuẩn chưa và cần chuyển tối thiểu bao nhiêu USD linh kiện sang nội khối?
8. **Lợi thế tương đối trong thuế chống bán phá giá:** Trong rà soát thuế chống bán phá giá cá tra, Doanh nghiệp P hưởng thuế `0,00 USD/kg`, còn đối thủ chịu thuế `1,35 USD/kg` trên giá bán cảng nhập `4,50 USD/kg`. Tính tỷ lệ thuế tương đương `%` giá bán mà đối thủ phải chịu và tác động lên thị phần của P.
9. **Độ nhạy đa thị trường (`Geographic diversification`):** Công ty Gỗ Q có doanh thu `4.000 tỷ VND` tại Mỹ (`55%`, biên gộp `22%`), Châu Âu (`25%`, biên gộp `18%`), Nhật Bản (`20%`, biên gộp `15%`). Nếu doanh thu tại Mỹ giảm `20%` và biên gộp tại Mỹ giảm xuống `16%` (hai thị trường kia giữ nguyên), tổng lợi nhuận gộp của Q giảm bao nhiêu tỷ VND và bao nhiêu phần trăm?
10. **Kiểm chứng chất lượng dòng tiền xuất khẩu qua [earnings_quality.py](../practice/models/earnings_quality.py):** Công ty nông sản báo doanh thu xuất khẩu sang một đối tác ở Hồng Kông tăng `+85%` (`2.400 tỷ VND`), lãi sau thuế `220 tỷ VND`, nhưng phải thu ngắn hạn từ đối tác này tăng `+1.100 tỷ VND`, `DSO` vọt từ `35` lên `195 ngày` và `CFO` âm `-650 tỷ VND`. Nêu 2 rủi ro trọng yếu.

---

## Đáp án

1. **Cán cân hàng hóa vs Cán cân vãng lai:**
   - `PHÉP_TÍNH` (a) Cán cân hàng hóa 9T2026: `434,30 − 453,72 = −19,42 tỷ USD` (nhập siêu hàng hóa `19,42 tỷ USD`).
   - `PHÉP_TÍNH` (b) Cán cân vãng lai giả định: `−19,42 − 8,50 − 14,00 + 12,00 = −29,92 tỷ USD`.
2. **FDI thực hiện so với FDI đăng ký:**
   - `PHÉP_TÍNH` Tỷ lệ `21,07 / 50,36 ≈ 41,84%`. Không lấy hiệu `29,29 tỷ USD` làm vốn giải ngân cuối năm vì vốn đăng ký giải ngân trong nhiều năm, còn số thực hiện gồm cả các dự án đăng ký từ những năm trước.
3. **Giá trị gia tăng nội địa (`DVA`):**
   - `PHÉP_TÍNH` Tổng chi ngoại tệ đầu vào và cước ngoại: `135 + 15 = 150 triệu USD`. (a) `DVA` giữ lại trong nước: `300 − 150 = 150 triệu USD`. (b) Tỷ lệ `DVA`: `150 / 300 = 50,00%`.
4. **Chia sẻ gánh nặng thuế quan:**
   - `PHÉP_TÍNH` `EBIT` ban đầu = `60 × 8,0% = 4,80 triệu USD` (chi phí = `55,20 triệu USD`). Sau khi giảm giá `4,0%`, doanh thu mới = `57,60 triệu USD` → `EBIT` mới = `57,60 − 55,20 = 2,40 triệu USD` (giảm `50,0%`).
5. **So sánh `FOB` và `CIF`:**
   - `PHÉP_TÍNH` Công ty X (`FOB`): giữ nguyên `1.000 × 1.200 = 1,20 triệu USD`. Công ty Y (`CIF`): còn `1.000 × (1.200 − 900) = 0,30 triệu USD` (giảm `75%`).
6. **Chi phí vốn lưu động khi tàu trễ 24 ngày:**
   - `PHÉP_TÍNH` Vốn lưu động giam thêm: `120 × (24 / 360) = 8,00 triệu USD`. Lãi vay phát sinh thêm: `8,00 × 6,5% = 0,52 triệu USD/năm`.
7. **Quy tắc xuất xứ (`RVC >= 40%`):**
   - `PHÉP_TÍNH` `RVC` hiện tại = `(500 − 320) / 500 = 36,00% < 40%` (chưa đạt). Để đạt `40%` (`200 USD` nội khối), cần chuyển tối thiểu `320 − 300 = 20 USD/chiếc` linh kiện sang nội khối.
8. **Lợi thế tương đối trong thuế chống bán phá giá:**
   - `PHÉP_TÍNH` Thuế của đối thủ tương đương `1,35 / 4,50 = 30,00%` giá bán. Nhờ hưởng thuế `0%`, P vừa chiếm được đơn hàng từ đối thủ vừa có dư địa nâng giá bán `FOB`.
9. **Độ nhạy đa thị trường (Công ty Gỗ Q):**
   - `PHÉP_TÍNH` Lãi gộp ban đầu: Mỹ `2.200 × 22% = 484 tỷ`; EU `1.000 × 18% = 180 tỷ`; Nhật `800 × 15% = 120 tỷ` → Tổng = `784,00 tỷ VND`.
   - `PHÉP_TÍNH` Lãi gộp Mỹ mới (`1.760 × 16% = 281,60 tỷ`) → Tổng mới = `581,60 tỷ VND` (giảm `202,40 tỷ VND`, tức `−25,82%`).
10. **Chất lượng dòng tiền xuất khẩu:**
    - `SUY_LUẬN` Rủi ro ghi nhận doanh thu ảo/ký gửi hàng qua trung gian ở nước ngoài (`DSO = 195 ngày`, `CFO = −650 tỷ VND`) và rủi ro mất vốn không thu hồi được nợ xuyên biên giới.

---

## Bài làm với dữ liệu thiếu hoặc lệch

Trong nghiên cứu thương mại và dòng vốn tại Việt Nam, bạn thường gặp hai điểm khuyết dữ liệu:
1. **Lệch số liệu giữa báo cáo ước tính tháng của Cục Thống kê và số chốt sổ của Tổng cục Hải quan:** Số Cục Thống kê cuối tháng là số sơ bộ/ước tính, sau đó 10–15 ngày Hải quan mới chốt số chính thức theo tờ khai.
2. **Thiếu thuyết minh tỷ trọng thị trường xuất khẩu và điều khoản `Incoterms` trên BCTC:** Nhiều công ty chỉ ghi gộp "Doanh thu xuất khẩu".

**Quy trình xử lý chuẩn Bậc S:**
- **Bước 1 — Ghi rõ phiên bản dữ liệu (`Sơ bộ` hay `Chính thức`):** Luôn ghi rõ nhãn `sơ bộ` khi trích số 9 tháng năm 2026 (`xuất khẩu 434,30 tỷ USD, nhập khẩu 453,72 tỷ USD`).
- **Bước 2 — Ước lượng mức phơi nhiễm cước tàu từ Thuyết minh Chi phí bán hàng:** Tỷ trọng "Chi phí vận chuyển xuất khẩu / Doanh thu xuất khẩu" ở mức `1%–2%` gợi ý bán `FOB`, còn ở mức `8%–15%` gợi ý bán `CIF/CFR`.
- **Bước 3 — Gắn nhãn `CHƯA_BIẾT` và lập kịch bản thuế quan:** Không tự điền tỷ trọng thị trường từ tin đồn; gắn nhãn `CHƯA_BIẾT` và kiểm tra Báo cáo thường niên.

---

## Sai ở đâu

### Sai lầm 1: Lấy hiệu số `FDI đăng ký − FDI giải ngân` làm lượng ngoại tệ chắc chắn chảy vào trong quý tới
- **Bối cảnh:** Thấy FDI đăng ký 9 tháng là `50,36 tỷ USD` và thực hiện là `21,07 tỷ USD`, người viết suy ra quý IV sẽ có thêm đúng `29,29 tỷ USD` chảy vào hệ thống ngân hàng.
- **Sai ở đâu:** Nhầm **cam kết cấp phép đa niên** với **chi tiêu giải ngân trong kỳ**, và quên rằng một phần giải ngân bằng máy móc nhập khẩu tại chỗ.
- **Cách sửa:** Chỉ dùng số **FDI thực hiện (`Implemented FDI`)** và bảng `BOP` của NHNN.

### Sai lầm 2: Bán tháo hoặc mua đuổi cả ngành theo tin thuế quan mà không kiểm tra mức thuế riêng và xuất xứ nguyên liệu
- **Bối cảnh:** Nghe tin điều tra chống bán phá giá liền bán tháo cả doanh nghiệp đầu ngành tự chủ nguyên liệu thượng nguồn và hưởng thuế `0%`.
- **Sai ở đâu:** Bỏ qua tính phân hóa của biểu thuế riêng biệt (`separate rate`) và quy tắc xuất xứ (`ROO`).
- **Cách sửa:** Áp dụng Bảng kiểm 5 bước ở Phiên 3.

### Sai lầm 3: Nhìn doanh thu xuất khẩu tăng để mua cổ phiếu mà bỏ qua điều khoản `CIF` khi cước tàu tăng vọt
- **Bối cảnh:** Doanh thu xuất khẩu tăng `12%` nhờ cộng phụ phí vận tải một phần, nhưng công ty bán giá `CIF` phải tự gánh phần lớn đà tăng giá cước và bị giam vốn lưu động trên biển.
- **Cách sửa:** Kiểm tra biên lợi nhuận sau chi phí vận chuyển và số ngày phải thu (`DSO`) qua [earnings_quality.py](../practice/models/earnings_quality.py).

---

## Kiểm tra chuyển bài

Trước khi chuyển sang bài [014 — Kinh tế ngành và chu kỳ vốn](014-industry-capital-cycle.md), hãy trả lời 3 câu hỏi dưới đây:

1. **Tổng hợp `M3` → `M1`:** Khi cán cân hàng hóa 9 tháng 2026 nhập siêu sơ bộ `19,42 tỷ USD` trong khi FDI thực hiện đạt `21,07 tỷ USD`, vì sao dòng vốn FDI thực hiện và kiều hối lại đóng vai trò then chốt để giữ ổn định tỷ giá `VND/USD` ở bài `M1`?
2. **Tổng hợp `M3` → `M2`:** Phân biệt động lực dòng tiền của **Bất động sản Khu công nghiệp** (gắn với FDI thực hiện ở `M3`) và **Bất động sản Dân cư** (gắn với tín dụng mua nhà ở `M2`).
3. **Chuyển giao sang bài [014](014-industry-capital-cycle.md):** Khi một ngành xuất khẩu hưởng lợi từ thiếu hụt nguồn cung toàn cầu làm biên lợi nhuận tăng vọt, điều gì sẽ xảy ra tiếp theo với quyết định mở rộng nhà máy (`CapEx`) của toàn ngành?

---

## Nguồn Internet đã mở

- Truy cập `2026-10-27` và kiểm tra đối chiếu `2026-11-05`:
  1. [IMF — Balance of Payments and International Investment Position Statistics (BOP)](https://data.imf.org/Datasets/BOP) — phương pháp luận tách Tài khoản vãng lai, Tài khoản vốn và Tài khoản tài chính.
  2. [Cục Thống kê — Báo cáo tình hình kinh tế - xã hội Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/) — số sơ bộ 9 tháng 2026: xuất khẩu hàng hóa `434,30 tỷ USD`, nhập khẩu `453,72 tỷ USD` (nhập siêu `19,42 tỷ USD`); FDI đăng ký đến `30/09/2026` đạt `50,36 tỷ USD`, FDI thực hiện ước `21,07 tỷ USD`.
  3. [WTO — Global Trade Outlook and Statistics (08/10/2026)](https://www.wto.org/english/news_e/news26_e/stat_08oct26_510_e.htm) — dự báo thương mại hàng hóa toàn cầu 2026–2027 và rủi ro địa chính trị.
- Các ví dụ tính toán của doanh nghiệp X, Y, Omega, P, Q được gắn nhãn `KỊCH_BẢN`.
