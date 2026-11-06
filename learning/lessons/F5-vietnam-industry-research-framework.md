# Bài F5 — Khung nghiên cứu sáu ngành Việt Nam: Thép, Chứng khoán, Bán lẻ, Dầu khí, Điện và Thủy sản

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:05 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Xây dựng bản đồ kinh tế đơn vị (`Unit Economics`), cấu trúc chi phí, đòn bẩy hoạt động, chu kỳ vốn lưu động và biến số phá vỡ luận điểm cho 6 ngành trụ cột trên thị trường chứng khoán Việt Nam (`Thép`, `Chứng khoán`, `Bán lẻ chuỗi`, `Dầu khí thượng - trung - hạ nguồn`, `Điện phát điện`, và `Thủy sản xuất khẩu`).
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Ngành Thép (`BOF` vs. `EAF`, chênh lệch giá `HRC` – quặng – than) và Ngành Điện (`PPA`, $Q_c$, thị trường `CGM`).
  - **Buổi 2 (90 phút):** Ngành Dầu khí (thượng – trung – hạ nguồn) và Ngành Thủy sản (chu kỳ nuôi, giá thức ăn, thuế `POR`).
  - **Buổi 3 (90 phút):** Ngành Bán lẻ chuỗi (`SSSG` vs. mở mới) và Công ty Chứng khoán (Môi giới, `Margin`, Tự doanh).
- Bài trước liên quan: [Bài F4 — Đọc ngân hàng Việt Nam](F4-vietnam-bank-analysis.md), [Bài 014 — Chu kỳ ngành và chu kỳ vốn](014-industry-capital-cycle.md), [Bài F1 — Mô hình ba báo cáo](F1-three-statement-model-sensitivity.md).
- Học tiếp: [Bài F6 — Quản trị, bên liên quan và kiểm toán](F6-governance-related-party-audit.md).
- Mô hình thực hành và hồ sơ đi kèm: [`../practice/models/cyclical.py`](../practice/models/cyclical.py), [`../practice/models/hpg_cycle_inputs.csv`](../practice/models/hpg_cycle_inputs.csv), [`../practice/models/earnings_quality.py`](../practice/models/earnings_quality.py), và hai hồ sơ thực chiến [`../../research/companies/VN/HPG/report.md`](../../research/companies/VN/HPG/report.md), [`../../research/companies/VN/VNM/report.md`](../../research/companies/VN/VNM/report.md).
- Câu hỏi cốt lõi: Vì sao áp dụng cùng một bội số `P/E = 10x` cho một nhà máy thép ở đỉnh chu kỳ, một công ty chứng khoán lúc thanh khoản kỷ lục và một chuỗi bán lẻ đang mở rộng cửa hàng lại dẫn tới những sai lầm định giá đắt giá nhất?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F5-fact-check.md), [phản biện](../reviews/F5-risk-review.md).

---

## Hiểu bài trong một phút

Mỗi ngành có một **"đơn vị kinh tế hạt nhân" (`Core Unit Economics`)** riêng:
- **Thép**: Đơn vị kinh tế là `1 tấn thép tiêu thụ`; biên lợi nhuận phụ thuộc vào **chênh lệch giá (`Spread`)** giữa giá thép thành phẩm (`Thép xây dựng`, `HRC`) với nguyên liệu đầu vào (`Quặng sắt + Than cốc` đối với lò cao `BOF`, hoặc `Thép phế + Điện` đối với lò điện `EAF`), nhân với hiệu suất vận hành nhà máy (`SUY_LUẬN`).
- **Điện**: Đơn vị kinh tế là `1 kWh điện thương phẩm`. Lợi nhuận phụ thuộc vào **tỷ lệ sản lượng điện hợp đồng ($Q_c$, thường `80%–90%`)** thanh toán theo giá `PPA` để bù chi phí cố định và trả nợ vay, đối lập với phần bán trên thị trường phát điện cạnh tranh (`CGM`) (`SUY_LUẬN`).
- **Bán lẻ chuỗi**: Đơn vị kinh tế là **1 cửa hàng hiện hữu**. Mở thêm cửa hàng làm tổng doanh thu tăng không có nghĩa là công ty khỏe lên nếu **Tăng trưởng doanh thu cùng cửa hàng (`SSSG`)** âm (`SUY_LUẬN`).
- **Công ty Chứng khoán**: Kết hợp 3 động cơ nhạy cảm với thanh khoản (`ADTV`) và chỉ số thị trường: (1) Môi giới (`Brokerage`), (2) Cho vay ký quỹ (`Margin` — trần `200%` Vốn chủ sở hữu), và (3) Tự doanh (`FVTPL/AFS/HTM`) (`SỰ_THẬT`).

---

## Ôn bài cũ

- Sau khi phân tích bất động sản ở [Bài F3](F3-vietnam-property-developers.md), ngân hàng ở [Bài F4 — Đọc ngân hàng Việt Nam](F4-vietnam-bank-analysis.md) và chu kỳ vốn ở [Bài 014 — Chu kỳ ngành và chu kỳ vốn](014-industry-capital-cycle.md), Bài F5 xây dựng khung kinh tế đơn vị cho 6 ngành trụ cột khác trên sàn chứng khoán Việt Nam.

---

## Buổi 1 — Ngành Hàng hóa & Tài sản cố định nặng: Thép và Điện

### 1.1. Ngành Thép Việt Nam: Công nghệ Lò cao (`BOF`) vs. Lò điện (`EAF`) và Chu kỳ CapEx

Để phân tích một doanh nghiệp thép (như Tập đoàn Hòa Phát — `HPG`, Hoa Sen — `HSG`, Nam Kim — `NKG`), trước hết bạn phải xác định doanh nghiệp đó nằm ở khâu nào của chuỗi giá trị:

| Khâu trong chuỗi giá trị | Công nghệ & Đầu vào chính | Đầu ra chính | Đặc tính biên lợi nhuận & Rủi ro tồn kho |
|---|---|---|---|
| **1. Luyện thép thượng nguồn từ quặng (`BOF` — Lò cao luyện gang thép liên hợp)** | Quặng sắt (`Iron Ore`, khoảng `1,6 tấn/tấn thép`) + Than mỡ luyện cốc (`Coking Coal`, khoảng `0,5–0,6 tấn/tấn thép`). | Phôi thép, Thép xây dựng, Thép cuộn cán nóng (`HRC`). | Vốn đầu tư tài sản cố định (`CapEx`) khổng lồ (hàng tỷ USD), thời gian xây dựng 3–4 năm; đổi lại có **biên lợi nhuận gộp vượt trội** khi chạy tối đa công suất. Rủi ro lớn nhất là khi vừa hoàn thành đại dự án `CapEx` bằng nợ vay thì nhu cầu bất động sản suy thoái và giá quặng/than biến động ngược chiều. |
| **2. Luyện thép từ phế liệu (`EAF` — Lò điện hồ quang)** | Thép phế liệu (`Scrap Steel`) + Điện năng tiêu thụ lớn. | Phôi thép và Thép xây dựng. | Chi phí đầu tư ban đầu thấp hơn `BOF`, linh hoạt đóng/mở theo mùa vụ xây dựng, nhưng chi phí biến đổi trên mỗi tấn cao hơn nên biên lợi nhuận mỏng hơn. |
| **3. Cán nguội & Tôn mạ hạ nguồn (`Flat Steel Rollers / Coaters`)** | Mua cuộn cán nóng (`HRC`) làm nguyên liệu đầu vào (chiếm `75%–85%` giá vốn) + Kẽm, nhôm, sơn. | Tôn mạ kẽm, tôn lạnh, tôn màu, ống thép hàn. | Bản chất là **nhà gia công và thương mại tồn kho `HRC`**. Khi giá `HRC` thế giới tăng, doanh nghiệp hưởng lợi từ tồn kho giá rẻ; khi giá `HRC` đảo chiều giảm `20%–30%`, doanh nghiệp lập tức bị lỗ nặng do phải trích lập **Dự phòng giảm giá hàng tồn kho** và phụ thuộc nặng vào các vụ kiện phòng vệ thương mại tại thị trường xuất khẩu (`Mỹ`, `EU`). |

Công thức tính **Biên chênh lệch kim loại thô (`Raw Material Spread`)** trên mỗi tấn thép sản xuất theo công nghệ lò cao `BOF`:

$$\text{Spread}_{\text{BOF}} = P_{\text{Thép (HRC/XD)}} - \left(1,6 \times P_{\text{Quặng sắt}} + 0,55 \times P_{\text{Than cốc}}\right)$$

Như đã chứng minh trong mô-đun [`../practice/models/cyclical.py`](../practice/models/cyclical.py) và bộ dữ liệu thực tế [`../practice/models/hpg_cycle_inputs.csv`](../practice/models/hpg_cycle_inputs.csv), khi định giá cổ phiếu ngành thép, **tuyệt đối không lấy lợi nhuận năm đỉnh chu kỳ (`Peak Earnings`) để nhân `P/E`**, mà phải tính **Lợi nhuận chuẩn hóa qua trọn một chu kỳ 5–7 năm (`Normalized Mid-Cycle Earnings`)**!

### 1.2. Ngành Điện Việt Nam: Thủy điện, Nhiệt điện Khí/Than và Năng lượng tái tạo

Doanh thu của một nhà máy phát điện độc lập (`IPP`) tại Việt Nam (như `PV Power — POW`, `Nhiệt điện Quảng Ninh — QTP`, `Thủy điện Vĩnh Sơn Sông Hinh — VSH`) được tách thành hai phần theo cơ chế thị trường phát điện cạnh tranh:

$$\text{Doanh thu điện} = \underbrace{Q_c \times P_{\text{PPA}}}_{\text{Sản lượng hợp đồng (cố định biên thu hồi vốn)}} + \underbrace{(Q_{\text{thực phát}} - Q_c) \times P_{\text{CGM}}}_{\text{Phần chênh lệch bán theo giá thị trường giao ngay}}$$

Trong đó:
- $Q_{\text{thực phát}}$: Sản lượng điện thương phẩm thực tế phát lên lưới trong kỳ (đơn vị: `kWh` hoặc `triệu kWh`).
- $Q_c$: Sản lượng điện hợp đồng được giao theo tháng/năm (thường bằng `80%–90%` sản lượng dự kiến). Với phần $Q_c$, nhà máy được thanh toán theo giá hợp đồng $P_{\text{PPA}}$ (gồm Giá cố định $FC$ để thu hồi chi phí khấu hao + trả nợ vay, và Giá biến đổi $VC$ chuyển ngang chi phí nhiên liệu than/khí định mức sang bên mua điện).
- $P_{\text{CGM}}$: Giá thị trường phát điện cạnh tranh giao ngay. Nếu nhà máy vận hành khả dụng tốt và phát vượt $Q_c$ ($Q_{\text{thực phát}} > Q_c$) vào mùa khô khi $P_{\text{CGM}}$ cao hơn chi phí biến đổi, phần vượt đó tạo ra biên lợi nhuận đột biến; ngược lại, nếu nhà máy gặp sự cố kỹ thuật hoặc thiếu khí/nước khiến $Q_{\text{thực phát}} < Q_c$, nhà máy có thể phải mua lại phần thiếu hụt theo giá thị trường (`SUY_LUẬN`).

---

## Buổi 2 — Ngành Dầu khí và Thủy sản xuất khẩu

### 2.1. Ngành Dầu khí Việt Nam: Tách Thượng nguồn, Trung nguồn và Hạ nguồn

Chuỗi giá trị dầu khí Việt Nam gồm 3 khâu có độ nhạy giá dầu hoàn toàn khác nhau:
1. **Thượng nguồn (`Upstream` — `PVD`, `PVS`):** Phụ thuộc vào ngân sách chi tiêu vốn thăm dò khai thác (`E&P CapEx`) của `Petrovietnam` tại các đại dự án (như `Lô B – Ô Môn`). Biến số cốt lõi của `PVD` là giá thuê giàn khoan (`Day Rate`, `USD/ngày`) và hiệu suất sử dụng giàn; của `PVS` là giá trị hợp đồng chưa thực hiện (`Backlog M&C`) và biên gộp hợp đồng `EPC` (`SUY_LUẬN`).
2. **Trung nguồn (`Midstream` — `GAS`, `PVG`):** Phụ thuộc vào sản lượng khí dẫn qua đường ống và giá bán khí neo theo dầu `FO` cộng cước đường ống (`Tariff`). Rủi ro dài hạn là mỏ khí nội địa giá rẻ suy giảm trữ lượng, phải chuyển dần sang nhập khẩu `LNG` giá cao (`SUY_LUẬN`).
3. **Hạ nguồn (`Downstream` — Lọc dầu `BSR`, Phân phối `PLX`, `OIL`):** Lợi nhuận của `BSR` phụ thuộc vào **Biên lọc dầu (`Crack Spread`)** (chênh lệch giá xăng/diesel Singapore với giá dầu thô `Brent`). Khi giá dầu thô giảm đột ngột cuối quý, nhà máy lọc dầu và doanh nghiệp đầu mối xăng dầu phải gánh lỗ trích lập dự phòng giảm giá tồn kho bắt buộc.

### 2.2. Ngành Thủy sản xuất khẩu (Cá tra & Tôm): Chu kỳ sinh học và Thuế POR

Doanh nghiệp xuất khẩu cá tra (`VHC`, `ANV`) hoặc tôm (`MPC`, `FMC`) chịu sự chi phối của 4 biến số:
1. **Tỷ lệ tự chủ vùng nuôi (`Self-sufficiency Rate`):** Nuôi cá tra mất 6–8 tháng; tự chủ `60%–70%` vùng nuôi giúp ổn định biên gộp hơn mua cá nguyên liệu ngoài chợ.
2. **Chi phí thức ăn (`Feed Cost`):** Chiếm **`65%–75%` giá thành nuôi**, phụ thuộc giá khô đậu tương, ngô và bột cá nhập khẩu bằng `USD`.
3. **Thuế chống bán phá giá (`POR` của Bộ Thương mại Mỹ `DOC`):** Doanh nghiệp hưởng mức thuế `0,00 USD/kg` hoặc thấp giữ được thị phần biên cao tại Mỹ; doanh nghiệp chịu thuế cao phải dồn hàng sang thị trường biên thấp hơn (`SUY_LUẬN`).
4. **Sản phẩm phụ (`Collagen & Gelatin`, dầu cá, bột cá):** Nâng biên gộp hợp nhất thêm `3–5 điểm phần trăm`.

---

## Buổi 3 — Ngành Bán lẻ chuỗi và Công ty Chứng khoán

### 3.1. Ngành Bán lẻ chuỗi (`MWG`, `FRT`, `PNJ`): Phân rã Tăng trưởng Mở mới và `SSSG`

Khi đọc báo cáo của một chuỗi bán lẻ hàng công nghệ, dược phẩm, bách hóa hay trang sức, phương trình tăng trưởng doanh thu luôn phải tách thành hai vế:

$$\Delta \text{Doanh thu} = \underbrace{\text{Doanh thu từ các cửa hàng cũ mở đủ trên 12 tháng} \times \text{SSSG}}_{\text{Tăng trưởng nội tại (Organic Same-Store Growth)}} + \underbrace{\Delta N_{\text{cửa hàng mới}} \times \text{Doanh thu bình quân cửa hàng mới}}_{\text{Tăng trưởng nhờ mở rộng quy mô (Expansion Growth)}}$$

Bốn câu hỏi kiểm toán chất lượng tăng trưởng bán lẻ:
1. **`SSSG` (`Same-Store Sales Growth`) là dương hay âm?** Nếu tổng doanh thu tăng `+15%` nhưng số lượng cửa hàng tăng `+30%`, điều đó có nghĩa là doanh thu bình quân mỗi cửa hàng đang sụt giảm (`SSSG < 0`) hoặc cửa hàng mới đang "ăn thịt" (`Cannibalize`) doanh số của cửa hàng cũ đứng cạnh!
2. **Kinh tế đơn vị cấp cửa hàng (`Store-Level EBITDA`) và Thời gian hoàn vốn (`Payback Period`):** Một cửa hàng mới cần bao nhiêu tháng để đạt điểm hòa vốn chi phí thuê mặt bằng + nhân viên tại chỗ (`Store-Level Breakeven`), và mất bao nhiêu năm để thu hồi vốn đầu tư nội thất + tồn kho ban đầu (`CapEx + Working Capital per store`)?
3. **Vòng quay hàng tồn kho (`Inventory Days`) và Quyền lực chiếm dụng vốn nhà cung cấp (`Payable Days`):** Chuỗi bán lẻ hàng đầu có sức mạnh đàm phán để trả chậm tiền cho nhà cung cấp (`Payables`) lâu hơn số ngày nằm kho của hàng hóa (`Inventory`), tạo ra **Chu kỳ chuyển đổi tiền mặt (`CCC`) thấp hoặc âm** (tương tự cơ chế trong Bài [004](004-cash-flow-and-earnings-quality.md)).
4. **Rủi ro đóng cửa hàng loạt (`Store Closure Write-off`):** Khi một chuỗi mở rộng quá nhanh vào mặt bằng giá thuê cao không đạt điểm hòa vốn, việc đóng cửa 200–300 cửa hàng sẽ làm phát sinh chi phí thanh lý tài sản cố định và mất cọc thuê nhà một lần rất lớn trên Báo cáo KQKD (`SUY_LUẬN`).

### 3.2. Ngành Công ty Chứng khoán (`SSI`, `VND`, `VCI`, `HCM`): Ba động cơ lợi nhuận và Rủi ro bảng cân đối

Một công ty chứng khoán (`CTCK`) không phải là một doanh nghiệp dịch vụ thuần túy, mà là một **định chế tài chính có đòn bẩy cao**. Khi đọc BCTC của một CTCK (lập theo Thông tư `210/2014/TT-BTC` và Thông tư `334/2016/TT-BTC`), bạn phải bóc tách riêng 3 mảng kinh doanh:

| Động cơ lợi nhuận | Công thức doanh thu & Chi phí trực tiếp | Chỉ tiêu Bảng cân đối kế toán đi kèm | Rủi ro cốt lõi cần kiểm tra |
|---|---|---|---|
| **1. Môi giới chứng khoán (`Brokerage`)** | $\text{Doanh thu môi giới} = \text{ADTV toàn thị trường} \times \text{Số phiên} \times \text{Thị phần} \times 2 \times \text{Phí môi giới thuần bình quân}$ | Không đòi hỏi vốn bảng cân đối lớn, nhưng đòi hỏi chi phí công nghệ và hoa hồng môi giới. | Cuộc chiến "Zero-fee" ép biên lợi nhuận môi giới thuần xuống sát `0%`; môi giới biến thành phễu thu hút khách vay `Margin`. |
| **2. Cho vay ký quỹ (`Margin Lending`)** | $\text{Lãi thuần Margin} = \text{Dư nợ Margin bình quân} \times (\text{Lãi suất cho vay Margin} - \text{Chi phí vốn vay ngân hàng/trái phiếu})$ | **Các khoản cho vay (`Loans`)** bên phần Tài sản tài chính; bị khống chế bởi trần pháp lý: **Tổng dư nợ cho vay ký quỹ không được vượt quá `200%` (`2,0 lần`) Vốn chủ sở hữu** của CTCK (`SỰ_THẬT`). | Rủi ro cho vay cầm cố bằng cổ phiếu thanh khoản thấp của một nhóm cổ đông lớn/bất động sản: khi cổ phiếu mất thanh khoản giảm sàn nhiều phiên liên tiếp, CTCK không thể bán giải chấp (`Force-sell`) để thu hồi nợ gốc! |
| **3. Tự doanh và Bảo lãnh phát hành (`FVTPL`, `HTM`, `AFS`)** | Lãi/lỗ bán tài sản tài chính `FVTPL` + **Chênh lệch đánh giá lại theo giá thị trường (`Mark-to-Market`)** + Cổ tức/trái tức nhận được. | Tài sản tài chính ghi nhận thông qua lãi/lỗ (`FVTPL`), Nắm giữ đến ngày đáo hạn (`HTM`), và Sẵn sàng để bán (`AFS`). | Lãi đánh giá lại `FVTPL` là lãi chưa thu tiền mặt; đặc biệt cảnh giác khi danh mục `FVTPL`/`AFS` chứa hàng nghìn tỷ đồng **trái phiếu doanh nghiệp chưa niêm yết** kèm cam kết mua lại ngoại bảng. |

---

## 4. Ví dụ từ nguồn thật: Đối chiếu Hòa Phát (HPG — Ngành Thép) và PV Power (POW — Ngành Điện)

1. **Ngành Điện — Tổng công ty Điện lực Dầu khí Việt Nam (`PV Power — POW`):**
   - `SỰ_THẬT`: Theo tài liệu công bố thông tin [PV Power — Nội dung trình Đại hội đồng cổ đông ngày 20/05/2026](https://pvpower.vn/vi/post/pv-power-vuot-ke-hoach-loi-nhuan-nam-thu-7-lien-tiep--dat-muc-tieu-doanh-thu-gan-50-000-ty-dong-trong-nam-2026-6909.htm), tổng sản lượng điện toàn tổng công ty năm 2025 đạt **`18,6 tỷ kWh`** (`18.600 triệu kWh`), tổng doanh thu đạt **`35.364 tỷ VND`** và lợi nhuận trước thuế đạt **`3.234,3 tỷ VND`**.
   - `PHÉP_TÍNH`: Từ ba con số công bố này, nhà phân tích tính được ngay hai chỉ số kinh tế đơn vị sơ bộ của toàn tổ hợp phát điện năm 2025:
     - Doanh thu bình quân trên mỗi kWh điện (`Implicit Revenue per kWh`) $\approx \frac{35.364.000.000.000\text{ VND}}{18.600.000.000\text{ kWh}} \approx 1.901,29\text{ VND/kWh}$.
     - Tỷ suất lợi nhuận trước thuế trên doanh thu (`EBT Margin`) $= \frac{3.234,3}{35.364} = 9,1457\%\; (\approx 9,15\%)$.
   - **Giới hạn kiểm chứng (`SUY_LUẬN` & `CHƯA_BIẾT`):** Hai tỷ số trên là con số gộp cấp tổng công ty từ thông cáo ĐHĐCĐ; để định giá chính xác, nhà phân tích không dừng ở đây mà phải mở **BCTC hợp nhất kiểm toán năm 2025 của `POW`** để tách riêng: (a) khoản bồi thường bảo hiểm gián đoạn kinh doanh hoặc chênh lệch tỷ giá một lần (nếu có), (b) dòng tiền chi đầu tư xây dựng cơ bản (`CapEx`) và lịch trả nợ vay ngoại tệ của đại dự án nhà máy điện khí `LNG Nhơn Trạch 3 & 4`, và (c) số dư phải thu tiền điện từ Công ty Mua bán điện (`EPTC/EVN`).

2. **Ngành Thép — Tập đoàn Hòa Phát (`HPG`) từ Hồ sơ thực chiến đã kiểm duyệt:**
   - `SỰ_THẬT`: Theo BCTC hợp nhất của Tập đoàn Hòa Phát (`HPG`) đã được kiểm nguồn độc lập trong [`../../research/companies/VN/HPG/report.md`](../../research/companies/VN/HPG/report.md) và bộ dữ liệu [`../practice/models/hpg_cycle_inputs.csv`](../practice/models/hpg_cycle_inputs.csv), lợi nhuận sau thuế của `HPG` biến động cực mạnh theo chu kỳ thép: đạt đỉnh kỷ lục `34.521 tỷ VND` năm 2021, rơi xuống `8.444 tỷ VND` năm 2022 và `6.800 tỷ VND` năm 2023 khi giá thép giảm và chi phí than/tỷ giá tăng, trước khi phục hồi lên `12.020 tỷ VND` năm 2024 và tiếp tục tăng trong năm 2025 khi dự án Khu liên hợp gang thép Dung Quất 2 đi vào vận hành thương mại.
   - `SUY_LUẬN`: Dữ liệu lịch sử của `HPG` là minh chứng điển hình nhất cho quy tắc của Bài `F5`: đối với ngành chu kỳ thâm dụng vốn, nhìn `P/E` một năm đơn lẻ mà không đặt vào vị trí của chu kỳ công suất và chu kỳ biên lợi nhuận (`Spread`) chắc chắn dẫn đến định giá sai.

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Một báo cáo phân tích ngắn trên mạng xã hội so sánh ngang 3 cổ phiếu thuộc 3 ngành khác nhau (`Thép`, `Chứng khoán`, `Bán lẻ`) vào cuối năm 2025 dựa trên một bảng duy nhất:

| Mã cổ phiếu (Giả định) | Ngành | P/E trượt 12 tháng | Tỷ lệ Nợ vay / Vốn chủ sở hữu (D/E) | Nhận định của tác giả bài viết |
|---|---|---:|---:|---|
| **Cổ phiếu S** | Công ty Chứng khoán | `8,5x` | `1,40x` | *"P/E chỉ 8,5 lần sau một năm lợi nhuận kỷ lục — cổ phiếu tăng trưởng giá rẻ!"* |
| **Cổ phiếu R** | Chuỗi Bán lẻ điện máy & bách hóa | `28,0x` | `0,90x` | *"Doanh thu tăng +18% nhờ mở mới 250 cửa hàng, nhưng P/E 28 lần là quá đắt!"* |
| **Cổ phiếu T** | Thương mại & Tôn mạ thép | `6,0x` | `1,80x` | *"P/E 6 lần là món hời lớn nhất thị trường, nợ vay cao chỉ vì nhập hàng tồn kho!"* |

Khi mở BCTC kiểm toán của cả 3 công ty, bạn phát hiện các dữ kiện bị che khuất (`KỊCH_BẢN`):
1. **Tại Công ty Chứng khoán S:** Trong `2.400 tỷ VND` lợi nhuận trước thuế năm 2025, có tới **`1.350 tỷ VND` là lãi đánh giá lại chưa thực hiện (`Unrealized FVTPL Gain`)** của 2 mã cổ phiếu vốn hóa trung bình do chính công ty tự doanh nắm giữ ở vùng giá đỉnh lịch sử; đồng thời dư nợ cho vay `Margin` đã chạm kịch trần `195%` Vốn chủ sở hữu, trong đó `35%` dư nợ là cho vay cầm cố cổ phiếu của các doanh nghiệp bất động sản có liên quan.
2. **Tại Chuỗi Bán lẻ R:** Dù tổng doanh thu tăng `+18%` nhờ mở thêm 250 cửa hàng mới, nhưng doanh thu trên các cửa hàng cũ đã mở trên 12 tháng giảm **`SSSG = -7,5%`**. Ngược lại, lợi nhuận ròng năm 2025 bị kéo thấp tạm thời do công ty trích một lần `420 tỷ VND` chi phí xóa sổ các cửa hàng thuốc/phụ kiện kém hiệu quả để dồn nguồn lực cho chuỗi bách hóa đã vượt điểm hòa vốn toàn chuỗi.
3. **Tại Công ty Tôn mạ T:** Lợi nhuận năm 2025 đạt đỉnh nhờ nhập được lô nguyên liệu `HRC` giá rẻ đầu năm trước khi giá `HRC` tăng vọt. Tuy nhiên, vào cuối Quý 4/2025, công ty vừa vay ngắn hạn ngân hàng nhập thêm `9.000 tỷ VND` tồn kho `HRC` đúng ở vùng đỉnh giá, trong khi thị trường xuất khẩu chủ lực vừa thông báo khởi xướng điều tra thuế chống bán phá giá với biên độ dự kiến `25%–35%`.

### Quy trình làm sạch và sửa sai khung phân tích
1. **Không bao giờ so ngang `P/E` và `D/E` giữa 3 ngành khác bản chất:**
   - Với **Chứng khoán S**: Phải loại bỏ `1.350 tỷ VND` lãi tự doanh chưa thực hiện khỏi lợi nhuận bền vững. Lợi nhuận cốt lõi trước thuế từ môi giới và `Margin` chỉ là $2.400 - 1.350 = 1.050\text{ tỷ VND}$ (`PHÉP_TÍNH`), làm `P/E` cốt lõi vọt lên gần `19,4x` ngay tại đỉnh thanh khoản và kịch trần `Margin`! Thay vì nhìn `P/E`, phải định giá Công ty S bằng **`P/B` điều chỉnh chất lượng danh mục `FVTPL` và dư nợ `Margin`**.
   - Với **Bán lẻ R**: Phải cộng trả lại khoản chi phí đóng cửa hàng một lần (`420 tỷ VND` trước thuế, tức `336 tỷ VND` sau thuế) để tìm lợi nhuận hoạt động chuẩn hóa, đồng thời theo dõi sát xem `SSSG = -7,5%` của chuỗi cũ đã tạo đáy chưa và biên `EBITDA` của chuỗi bách hóa mới mở rộng như thế nào (`SUY_LUẬN`).
   - Với **Tôn mạ T**: Con số `P/E = 6,0x` ở đỉnh chu kỳ tồn kho `HRC` là một **"Bẫy giá trị chu kỳ" (`Cyclical Value Trap`)** kinh điển. Nếu giá `HRC` thế giới điều chỉnh giảm `15%` trên `9.000 tỷ VND` hàng tồn kho cuối kỳ, công ty sẽ bay mất tới `1.350 tỷ VND` vì trích lập dự phòng giảm giá hàng tồn kho, biến `P/E = 6,0x` thành thua lỗ ngay trong 2 quý tới (`PHÉP_TÍNH`)!

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai trong nhận định sau về ngành Dầu khí và Điện:

> *"Giá dầu thế giới và giá khí thiên nhiên tăng vọt +40% chắc chắn là tin đại cát cho tất cả các doanh nghiệp có chữ Dầu khí trong tên gọi — từ tổng công ty khoan dầu (PVD), công ty phân phối khí (GAS) cho tới nhà máy điện khí (POW) và nhà máy đạm khí (DPM, DCM) đều sẽ tăng mạnh biên lợi nhuận!"*

### Phân tích chỗ sai
1. **Đánh đồng đầu ra của khâu này với đầu vào của khâu kia trong chuỗi giá trị năng lượng:**
   - Với **Thượng nguồn (`PVD`) và Trung nguồn (`GAS`)**: Giá dầu và giá dầu `FO` tăng giúp thúc đẩy nhu cầu thuê giàn khoan và làm tăng giá bán khí neo theo dầu `FO`, nên thường hưởng lợi (`SUY_LUẬN`).
   - Nhưng với **Nhà máy nhiệt điện chạy khí (`POW`)** và **Nhà máy sản xuất phân đạm urê từ khí thiên nhiên (`DPM`, `DCM`)**: Khí thiên nhiên không phải là sản phẩm bán ra của họ, mà là **nguyên nhiên liệu đầu vào chiếm tỷ trọng lớn nhất trong giá vốn sản xuất**!
2. **Cơ chế truyền dẫn thực tế:**
   - Tại nhà máy sản xuất phân đạm (`DPM`, `DCM`), khi giá dầu `FO` tăng `+40%`, giá khí đầu vào tăng mạnh sẽ trực tiếp đẩy giá vốn sản xuất urê tăng lên; nếu giá bán phân urê trên thị trường nông nghiệp không tăng kịp, **biên lợi nhuận gộp của nhà máy đạm sẽ bị thu hẹp mạnh** (`SUY_LUẬN`).
   - Tại nhà máy nhiệt điện khí (`POW`), dù phần sản lượng hợp đồng $Q_c$ được chuyển ngang giá khí vào giá bán điện theo `PPA`, nhưng giá khí tăng cao làm chi phí biến đổi phát điện mỗi kWh của điện khí đắt đỏ hơn so với điện than và thủy điện. Hệ quả là trên thị trường phát điện cạnh tranh (`CGM`), Trung tâm Điều độ Hệ thống điện Quốc gia sẽ ưu tiên huy động thủy điện và điện than giá rẻ trước, làm **sản lượng huy động vượt $Q_c$ của nhà máy điện khí sụt giảm** (`SUY_LUẬN`).

---

## 7. Bài tập (10 câu)

1. Liệt kê "đơn vị kinh tế hạt nhân" (`Core Unit`) và 2 biến số chi phí/giá quan trọng nhất của từng ngành trong 6 ngành: `Thép`, `Chứng khoán`, `Bán lẻ chuỗi`, `Dầu khí`, `Điện` và `Thủy sản xuất khẩu`.
2. Một nhà máy luyện thép lò cao (`BOF`) cần `1,60 tấn` quặng sắt và `0,55 tấn` than mỡ luyện cốc để sản xuất `1 tấn` thép cuộn cán nóng (`HRC`). Đầu năm, giá quặng sắt là `105 USD/tấn`, giá than cốc là `220 USD/tấn` và giá bán `HRC` là `560 USD/tấn`. Cuối năm, giá `HRC` giảm xuống `510 USD/tấn`, trong khi giá quặng sắt chỉ giảm nhẹ xuống `100 USD/tấn` và than cốc tăng lên `240 USD/tấn`. Tính `Raw Material Spread` (`USD/tấn HRC`) đầu năm và cuối năm, cùng mức sụt giảm tuyệt đối và phần trăm của `Spread`.
3. Theo số liệu công bố của `PV Power (POW)` trong Mục 4: năm 2025 tổng sản lượng điện đạt `18,6 tỷ kWh`, doanh thu đạt `35.364 tỷ VND`, lợi nhuận trước thuế đạt `3.234,3 tỷ VND`. Hãy tính doanh thu bình quân mỗi kWh, lợi nhuận trước thuế bình quân mỗi kWh và tỷ suất lợi nhuận trước thuế trên doanh thu (`EBT Margin`).
4. Một nhà máy nhiệt điện có sản lượng điện thực phát trong quý là $Q_{\text{thực phát}} = 1.200\text{ triệu kWh}$. Sản lượng điện hợp đồng được giao là $Q_c = 1.000\text{ triệu kWh}$ với giá hợp đồng $P_{\text{PPA}} = 1.850\text{ VND/kWh}$. Phần sản lượng phát vượt $Q_c$ được bán trên thị trường phát điện cạnh tranh với giá bình quân $P_{\text{CGM}} = 2.150\text{ VND/kWh}$. Tổng chi phí nhiên liệu, vận hành, khấu hao và lãi vay trong quý của nhà máy là `2.020 tỷ VND`. Tính tổng doanh thu tiền điện và lợi nhuận trước thuế của nhà máy trong quý.
5. Một chuỗi bán lẻ dược phẩm đầu năm 2025 có `1.000` cửa hàng đã hoạt động ổn định với doanh thu bình quân `12,0 tỷ VND/cửa hàng/năm` (tổng doanh thu năm trước = `12.000 tỷ VND`). Trong năm 2025, các cửa hàng cũ này đạt mức tăng trưởng doanh thu cùng cửa hàng là `SSSG = +6,0%`; đồng thời chuỗi mở thêm `300` cửa hàng mới (do mở rải rác trong năm nên mỗi cửa hàng mới đóng góp bình quân `5,5 tỷ VND` doanh thu trong năm 2025). Tính tổng doanh thu năm 2025 của chuỗi, tốc độ tăng trưởng tổng doanh thu, và tỷ trọng đóng góp của tăng trưởng nội tại (`SSSG`) so với mở mới cửa hàng trong mức tăng trưởng doanh thu đó.
6. Một Công ty Chứng khoán có Vốn chủ sở hữu cuối kỳ là `8.000 tỷ VND`. Theo quy định trần cho vay ký quỹ của pháp luật chứng khoán Việt Nam (`tối đa 200% Vốn chủ sở hữu`), dư nợ cho vay `Margin` tối đa mà công ty được phép cấp là bao nhiêu? Nếu công ty đang cho vay bình quân `14.000 tỷ VND` dư nợ `Margin` với lãi suất cho vay trung bình `11,2%/năm` và nguồn vốn tài trợ gồm `6.000 tỷ VND` vốn tự có (chi phí lãi vay `0%`) cộng `8.000 tỷ VND` vốn vay ngân hàng (lãi suất `6,5%/năm`), hãy tính Thu nhập lãi thuần từ mảng `Margin` trong năm.
7. Một doanh nghiệp xuất khẩu cá tra có doanh thu năm 2025 là `120 triệu USD` (tỷ giá bình quân `25.000 VND/USD`, tương đương `3.000 tỷ VND`). Chi phí cá nguyên liệu chiếm `60%` doanh thu, trong đó chi phí thức ăn thủy sản chiếm `70%` chi phí cá nguyên liệu. Nếu giá khô đậu tương nhập khẩu tăng làm chi phí thức ăn tăng thêm `+15%` mà doanh nghiệp không tăng được giá bán xuất khẩu, biên lợi nhuận gộp của doanh nghiệp sẽ bị co hẹp bao nhiêu điểm phần trăm và mất bao nhiêu tỷ VND lợi nhuận gộp?
8. Giải thích sự khác biệt về rủi ro tồn kho giữa một doanh nghiệp luyện thép thượng nguồn từ quặng (`HPG`) với một doanh nghiệp cán tôn mạ hạ nguồn mua `HRC` thương mại khi giá thép thế giới đột ngột giảm `-20%` trong 1 quý.
9. Sử dụng mô-đun [`../practice/models/cyclical.py`](../practice/models/cyclical.py) và tệp [`../practice/models/hpg_cycle_inputs.csv`](../practice/models/hpg_cycle_inputs.csv): Nếu lợi nhuận sau thuế qua 5 năm của một doanh nghiệp chu kỳ lần lượt là `34.521`, `8.444`, `6.800`, `12.020` và `15.500 tỷ VND`, hãy tính lợi nhuận bình quân chu kỳ 5 năm (`5-Year Normalized Earnings`). Nếu vốn hóa thị trường hiện tại là `180.000 tỷ VND`, hãy so sánh `P/E` tính trên năm đỉnh (`34.521 tỷ`), năm đáy (`6.800 tỷ`) và `P/E` chuẩn hóa 5 năm.
10. Khi thiết lập một hồ sơ ngành mới trong thư mục `research/sectors/`, bạn cần tối thiểu những nguồn dữ liệu gốc nào và những bước kiểm chứng nào trước khi được phép gỡ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT`?

---

## 8. Đáp án chi tiết

1. **Bản đồ đơn vị kinh tế hạt nhân của 6 ngành:**
   - `Thép`: 1 tấn thép tiêu thụ; biến số: `Spread` giá thép trừ (`1,6 × quặng + 0,55 × than cốc`) và hiệu suất chạy lò.
   - `Chứng khoán`: 1 đồng vốn chủ sở hữu & thị phần giao dịch; biến số: thanh khoản thị trường (`ADTV`), dư nợ & chênh lệch lãi suất `Margin`, và danh mục tự doanh `FVTPL`.
   - `Bán lẻ`: 1 cửa hàng hiện hữu; biến số: `SSSG`, biên `EBITDA` cấp cửa hàng và vòng quay tồn kho.
   - `Dầu khí`: Tách Thượng nguồn (`Day rate` giàn khoan, `Backlog EPC`), Trung nguồn (sản lượng khí và cước đường ống), Hạ nguồn (`Crack Spread` lọc dầu).
   - `Điện`: 1 kWh điện thương phẩm; biến số: tỷ lệ sản lượng hợp đồng $Q_c$, giá thị trường `CGM` và chi phí nhiên liệu/thủy văn.
   - `Thủy sản`: 1 kg cá/tôm xuất khẩu; biến số: tỷ lệ tự chủ vùng nuôi, giá thức ăn và thuế chống bán phá giá `POR`.
2. **Tính `Raw Material Spread` của lò cao `BOF`:**
   - Đầu năm: Chi phí kim loại thô = $1,60 \times 105 + 0,55 \times 220 = 168 + 121 = 289\text{ USD/tấn}$;
     $$\text{Spread}_{\text{đầu năm}} = 560 - 289 = 271\text{ USD/tấn HRC}$$
   - Cuối năm: Chi phí kim loại thô = $1,60 \times 100 + 0,55 \times 240 = 160 + 132 = 292\text{ USD/tấn}$;
     $$\text{Spread}_{\text{cuối năm}} = 510 - 292 = 218\text{ USD/tấn HRC}$$
   - Mức sụt giảm của `Spread`: giảm $271 - 218 = 53\text{ USD/tấn}$ (tức giảm **`-19,56%`**), mạnh hơn nhiều so với mức giảm `-8,93%` của giá bán `HRC` (`PHÉP_TÍNH`)!
3. **Chỉ số đơn vị năm 2025 của `PV Power (POW)`:**
   - Doanh thu bình quân mỗi kWh = $35.364\text{ tỷ VND} / 18,6\text{ tỷ kWh} = 1.901,29\text{ VND/kWh}$.
   - Lợi nhuận trước thuế bình quân mỗi kWh = $3.234,3\text{ tỷ VND} / 18,6\text{ tỷ kWh} = 173,89\text{ VND/kWh}$.
   - `EBT Margin` = $3.234,3 / 35.364 = 9,15\%$ (`PHÉP_TÍNH`).
4. **Tính doanh thu và lợi nhuận nhà máy điện theo $Q_c$ và `CGM`:**
   - Doanh thu phần sản lượng hợp đồng $Q_c$: $1.000\text{ triệu kWh} \times 1.850\text{ VND} = 1.850\text{ tỷ VND}$.
   - Doanh thu phần phát vượt bán trên thị trường `CGM` ($1.200 - 1.000 = 200\text{ triệu kWh}$): $200\text{ triệu kWh} \times 2.150\text{ VND} = 430\text{ tỷ VND}$.
   - Tổng doanh thu tiền điện = $1.850 + 430 = 2.280\text{ tỷ VND}$.
   - Lợi nhuận trước thuế trong quý = $2.280 - 2.020 = 260\text{ tỷ VND}$ (`PHÉP_TÍNH`).
5. **Phân rã tăng trưởng chuỗi bán lẻ (`SSSG` vs. Mở mới):**
   - Doanh thu năm 2025 từ 1.000 cửa hàng cũ = $12.000 \times (1 + 6,0\%) = 12.720\text{ tỷ VND}$ (tăng thêm **`+720 tỷ VND`**).
   - Doanh thu năm 2025 từ 300 cửa hàng mở mới = $300 \times 5,5 = 1.650\text{ tỷ VND}$ (tăng thêm **`+1.650 tỷ VND`**).
   - Tổng doanh thu năm 2025 = $12.720 + 1.650 = 14.370\text{ tỷ VND}$ (tăng trưởng tổng = $+2.370 / 12.000 = +19,75\%$).
   - Trong `+2.370 tỷ VND` doanh thu tăng thêm, tăng trưởng nội tại `SSSG` đóng góp $720 / 2.370 = 30,38\%$, còn mở mới cửa hàng đóng góp $1.650 / 2.370 = 69,62\%$ (`PHÉP_TÍNH`).
6. **Trần `Margin` và Lãi thuần `Margin` của Công ty Chứng khoán:**
   - Dư nợ `Margin` tối đa được phép theo trần `200%` VCSH = $8.000 \times 200\% = 16.000\text{ tỷ VND}$.
   - Thu nhập lãi cho vay `Margin` = $14.000 \times 11,2\% = 1.568\text{ tỷ VND}$.
   - Chi phí lãi vay ngân hàng tài trợ `Margin` = $8.000 \times 6,5\% = 520\text{ tỷ VND}$.
   - Lãi thuần từ hoạt động cho vay `Margin` = $1.568 - 520 = 1.048\text{ tỷ VND}$ (`PHÉP_TÍNH`).
7. **Độ nhạy chi phí thức ăn thủy sản lên biên lợi nhuận gộp:**
   - Tỷ trọng chi phí thức ăn trên doanh thu ban đầu = $60\% \times 70\% = 42,0\%$ doanh thu (`1.260 tỷ VND`).
   - Khi chi phí thức ăn tăng thêm `+15%`, biên lợi nhuận gộp bị co hẹp trực tiếp: $42,0\% \times 15\% = 6,30\text{ điểm phần trăm}$, tương ứng mất $1.260 \times 15\% = 189\text{ tỷ VND}$ lợi nhuận gộp (`PHÉP_TÍNH`).
8. **Rủi ro tồn kho giữa Luyện thép thượng nguồn và Tôn mạ hạ nguồn:**
   - Doanh nghiệp tôn mạ hạ nguồn giữ phần lớn tồn kho dưới dạng cuộn `HRC` mua đắt (chiếm `80%` giá vốn) và thành phẩm tôn mạ, nên khi giá `HRC` sụt `-20%` sẽ lập tức bị lỗ nặng do trích lập dự phòng giảm giá hàng tồn kho. Ngược lại, nhà sản xuất thượng nguồn từ quặng có biên gộp đệm dày hơn và vòng quay nguyên liệu quặng/than theo hợp đồng dài hạn nên chịu sốc trích lập tồn kho nhẹ hơn (`SUY_LUẬN`).
9. **Tính lợi nhuận chuẩn hóa 5 năm (`Normalized Earnings`) và `P/E` chu kỳ:**
   - Lợi nhuận sau thuế bình quân 5 năm = $\frac{34.521 + 8.444 + 6.800 + 12.020 + 15.500}{5} = \frac{77.285}{5} = 15.457\text{ tỷ VND/năm}$.
   - Tại vốn hóa `180.000 tỷ VND`:
     - `P/E` tính trên năm đỉnh (`2021`): $180.000 / 34.521 = 5,21\text{ lần}$ (ảo giác cực rẻ ở đỉnh chu kỳ);
     - `P/E` tính trên năm đáy (`2023`): $180.000 / 6.800 = 26,47\text{ lần}$ (ảo giác cực đắt ở đáy chu kỳ);
     - `P/E` chuẩn hóa giữa chu kỳ (`Mid-cycle P/E`): $180.000 / 15.457 = 11,65\text{ lần}$ (`PHÉP_TÍNH`).
10. **Điều kiện xuất bản hồ sơ ngành trong `research/sectors/`:**
    - Phải có đề bài trong `research/briefs/`, sổ nguồn `source-register.md` dẫn ít nhất hai nguồn sơ cấp/có thẩm quyền độc lập cho các nhận định trọng yếu, tệp dữ liệu gốc lưu kèm mã băm `SHA-256` trong `data/raw/`, mô-đun tính toán tái lập có `unittest`, và phải vượt qua hai nhánh kiểm duyệt độc lập (`source-fact-checker` và `risk-bear-reviewer`) với `0` lỗi nghiêm trọng / `0` lỗi cao trên cùng mã băm `SHA-256` bằng `scripts/validate_report.py`.

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Trước khi chuyển sang Bài [F6 — Quản trị, bên liên quan và kiểm toán](F6-governance-related-party-audit.md), hãy tự kiểm tra 3 kỹ năng sau:
1. **Nhận diện đúng bội số theo ngành:** Khi bạn nhìn thấy một cổ phiếu có `P/E = 6,5x`, bạn đã có phản xạ tự hỏi ngay: *"Đây là công ty thuộc ngành nào? Lợi nhuận mẫu số `E` đang chứa lãi tự doanh cổ phiếu chưa thực hiện (Chứng khoán), lợi nhuận đỉnh chu kỳ `Spread` (Thép/Phân đạm/Hóa chất), hay lợi nhuận bàn giao dự án một lần (Bất động sản)?"* chưa?
2. **Kết nối từ Kinh tế đơn vị sang Quản trị (`F5 -> F6`):** Trong ngành Thép, Bán lẻ hay Chứng khoán, một doanh nghiệp có kinh tế đơn vị nhà máy/cửa hàng rất tốt nhưng vẫn có thể làm cổ đông thiểu số mất tiền nếu Ban lãnh đạo lập ra các công ty thương mại sân sau để mua nguyên liệu đầu vào giá cao hoặc bán thành phẩm giá thấp. Bạn đã sẵn sàng học cách kiểm toán giao dịch bên liên quan ở Bài [F6](F6-governance-related-party-audit.md) chưa?
3. **Kỷ luật thực hành Python:** Bạn đã chạy thử mô-đun [`../practice/models/cyclical.py`](../practice/models/cyclical.py) trên dữ liệu [`../practice/models/hpg_cycle_inputs.csv`](../practice/models/hpg_cycle_inputs.csv) để tái lập phép tính lợi nhuận chuẩn hóa chu kỳ chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Bốn lỗi phân tích phổ biến:** (1) Gộp chung các khâu Thượng – Trung – Hạ nguồn dầu khí; (2) Lấy một doanh nghiệp đơn lẻ để suy diễn cho toàn bộ ngành mà không kiểm tra công nghệ sản xuất hay cấu trúc hợp đồng; (3) Nhầm tăng trưởng doanh thu do mở ồ ạt cửa hàng mới bằng nợ vay với hiệu quả kinh tế đơn vị (`SSSG`); (4) Nhầm lãi đánh giá lại tự doanh (`FVTPL`) ở đỉnh thị trường của công ty chứng khoán với thu nhập lặp lại bền vững.
- **Ranh giới an toàn:** Bài học trang bị khung đặt câu hỏi và công thức kinh tế đơn vị cho 6 ngành tại Việt Nam; mọi số liệu của `PV Power (POW)` và `Hòa Phát (HPG)` chỉ phục vụ mục đích học tập, không phải khuyến nghị đầu tư.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:05 UTC+7`:
  1. [PV Power — Nội dung trình Đại hội đồng cổ đông ngày 20/05/2026](https://pvpower.vn/vi/post/pv-power-vuot-ke-hoach-loi-nhuan-nam-thu-7-lien-tiep--dat-muc-tieu-doanh-thu-gan-50-000-ty-dong-trong-nam-2026-6909.htm), công bố sản lượng điện (`18,6 tỷ kWh`), doanh thu (`35.364 tỷ VND`) và lợi nhuận trước thuế (`3.234,3 tỷ VND`) năm 2025.
  2. [Hồ sơ nghiên cứu đã kiểm duyệt — Tập đoàn Hòa Phát (HPG)](../../research/companies/VN/HPG/report.md) và [Công bố thông tin Hòa Phát](https://www.hoaphat.com.vn/investor-relations/information-disclosure).
  3. [CTCP Chứng khoán SSI — Báo cáo thường niên và Quan hệ nhà đầu tư](https://www.ssi.com.vn/quan-he-nha-dau-tu/bao-cao-thuong-nien).
