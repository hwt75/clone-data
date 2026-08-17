---
aliases:
  - "Cấu trúc Hà Lạc"
  - "Lập quẻ Hà Lạc"
  - "Quẻ Tiên Thiên Hậu Thiên"
  - "Hào Nguyên Đường"
tags:
  - hà-lạc
  - kinh-dịch/ứng-dụng
  - dự-đoán-học
---


# Lập cấu trúc Hà Lạc — mười bước

Thuật toán biến **tám chữ Can Chi** của một người thành **bốn quẻ Dịch và mười hai đại vận** phủ kín cuộc đời. Rút từ **Bài Ba** của [[Tám chữ Hà Lạc và quỹ đạo đời người — Xuân Cang]] (tr. 28–40).

> Đề toán ra là **bài toán Hà Lạc gồm có tám chữ Can Chi** phản ánh Năm, Tháng, Ngày, Giờ sinh của một con người.

Điểm phân biệt với các môn khác: **không gieo quẻ**. Quẻ được **tính ra** từ ngày sinh, nên mỗi người chỉ có một cấu trúc duy nhất, cố định — gần với [[Tử Vi Đẩu Số — thiên hạ đệ nhất thần số|lá số Tử Vi]] hơn là với [[Gieo quẻ và bấm độn|phép gieo quẻ]].

## Đề toán — dữ liệu đầu vào
| Mục | Nội dung |
|---|---|
| 1 | Họ tên, nghề nghiệp |
| 2 | Ngày giờ sinh **dương lịch** và **âm lịch** + **mã số ngày** |
| 3 | Các **tiết khí** liên quan: tiết lệnh tháng sinh, Xuân Phân / Hạ Chí / Thu Phân / Đông Chí |
| 4 | **Giờ khí Dương** hay **Giờ khí Âm** |
| 5 | **Dương Nam / Âm Nam / Dương Nữ / Âm Nữ** — theo Can Chi *năm* sinh |
| 6 | **Mệnh** = nạp âm của năm sinh |
| 7 | **Nguyên** — Thượng / Trung / Hạ nguyên |

**Giờ khí** khác **giờ âm dương**: giờ khí Dương là **Tý, Sửu, Dần, Mão, Thìn, Tị**; giờ khí Âm là **Ngọ, Mùi, Thân, Dậu, Tuất, Hợi** (nửa vòng, không so le). Sách nhắc riêng: *"Người làm toán Hà Lạc cần phân biệt Giờ Âm với Giờ khí Âm."*

**Tam nguyên** — mỗi nguyên 60 năm, một vòng [[Thiên Can và Địa Chi|giáp tý]]:

| Nguyên | Khoảng năm |
|---|---|
| Thượng nguyên | **1864 – 1923** (Giáp Tý – Quý Hợi) |
| Trung nguyên | **1924 – 1983** |
| Hạ nguyên | **1984 – 2043** |

## Bước 1 — Xác định Can Chi bốn trụ
Theo **tiết lệnh**, không theo lịch:

- **Năm**: lấy mốc **Lập Xuân**. Sinh sau Lập Xuân là năm mới dù còn trong niên lịch năm cũ, và ngược lại.
- **Tháng**: lấy mốc **tiết lệnh của tháng** (Lập Xuân → tháng Dần, Kinh Trập → Mão, Thanh Minh → Thìn, Lập Hạ → Tị, Mang Chủng → Ngọ, Tiểu Thử → Mùi, Lập Thu → Thân, Bạch Lộ → Dậu, Hàn Lộ → Tuất, Lập Đông → Hợi, Đại Tuyết → Tý, Tiểu Hàn → Sửu).
- **Ngày**: tra mã số Can Chi trong lịch; **không phụ thuộc năm và tháng sinh**, chỉ phụ thuộc vòng giáp tý 60 ngày.
- **Giờ**: phụ thuộc **Can của ngày sinh**. Ngày âm lịch bắt đầu từ **23 giờ** hôm trước.

> [!warning] Hai cái bẫy tác giả nhắc riêng
> - **Lịch Vạn niên** dịch từ NXB Thẩm Dương (Trung Quốc): giờ Trung Quốc **sớm hơn giờ Việt Nam một giờ**, nên mọi **giờ giao tiết lệnh trong sách đó phải trừ đi một giờ**.
> - Người sinh **1946–1975 từ Quảng Trị đến Cà Mau**: chính quyền địa phương đổi lịch nhiều lần, phải đối chiếu bảng tham khảo riêng (Bảng 4b).
>
> *"Không có chuyện sai một ly đi một dặm đâu. **Sai một ly là đi đứt luôn cả bài toán** đấy."*

## Bước 2 — Đổi Can Chi thành mã số
Đây là chỗ [[Hà Đồ]] và [[Lạc Thư]] đi vào thuật toán:

> **Mã số của Thiên Can bắt nguồn từ Lạc Thư. Mã số của Địa Chi bắt nguồn từ Hà Đồ.**

**Bảng mã số Can** (Bảng 9) — tám mã cho mười can, hai cặp dùng chung:

| Can | Nhâm · Giáp | Mậu | Bính | Canh | Tân | Kỷ | Ất · Quý | Đinh |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Mã số** | **6** | **1** | **8** | **3** | **4** | **9** | **2** | **7** |

Không can nào mang số **5** — đúng như [[Lạc Thư]], nơi số 5 là ngôi giữa để trống. (Chỗ trống này về sau thành **luật Tam nguyên** ở bước 4.)

**Bảng mã số Chi** (Bảng 10) — mỗi chi mang **hai số**, đúng cặp sinh–thành của [[Hà Đồ]]:

| Chi | Hợi · Tý | Tị · Ngọ | Dần · Mão | Thân · Dậu | Thìn · Tuất · Sửu · Mùi |
|---|---|---|---|---|---|
| **Mã số** | **1 – 6** | **2 – 7** | **3 – 8** | **4 – 9** | **5 – 10** |

Liệt kê mã số của cả tám chữ rồi **tách thành hai hệ: số lẻ (Dương) và số chẵn (Âm)** — mỗi hệ đúng **6 con số**, tổng cộng 12. Đây là bước kiểm tra: *"Xem lại cho đủ 12 con số."*

## Bước 3 — Tính trị số Âm Dương
> Trị số Âm Dương là **hai con số quy tụ của Tám chữ Can Chi**, mở đầu cho toàn bộ hành lang số mệnh của một đời người.

| Chủ thể | Hàng trên | Hàng dưới | Ký hiệu |
|---|---|---|---|
| **Dương Nam** · **Âm Nữ** | hệ số **lẻ** (Dương) | hệ số **chẵn** (Âm) | Dương / Âm |
| **Âm Nam** · **Dương Nữ** | hệ số **chẵn** (Âm) | hệ số **lẻ** (Dương) | Âm / Dương |

Cộng từng hàng → được **trị số Dương** và **trị số Âm**.

## Bước 4 — Tìm mã số quẻ, xác định quẻ Tiên Thiên
**Mã số 8 quẻ đơn trùng khít với mã số Can** (Bảng 11):

| Quẻ | [[Càn]] | [[Khảm]] | [[Cấn]] | [[Chấn]] | [[Tốn]] | [[Ly]] | [[Khôn]] | [[Đoài]] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Mã số** | 6 | 1 | 8 | 3 | 4 | 9 | 2 | 7 |
| **Can** | Giáp·Nhâm | Mậu | Bính | Canh | Tân | Kỷ | Ất·Quý | Đinh |

Quy tắc xử lý:

1. **Hàng trên trước** → cho **quẻ Thượng (Ngoại)**; hàng dưới → **quẻ Hạ (Nội)**.
2. **Modulo**: trị số Dương > 25 thì **trừ 25** (M25); trị số Âm > 30 thì **trừ 30** (M30) — *trừ một lần*.
3. Kết quả:
   - dưới 10 → chính là mã số quẻ;
   - là 10 hoặc bội số của 10 → **bỏ số không** (10→1, 20→2, 40→4);
   - trên hàng chục → **bỏ hàng chục** (17→7, 22→2, 36→6).
4. Nếu con số giữ lại là **5** → xử lý theo **luật Tam nguyên**:

| Sinh vào | Nam | Nữ |
|---|---|---|
| **Thượng nguyên** (không kể tuổi âm dương) | [[Cấn]] | [[Khôn]] |
| **Hạ nguyên** (không kể tuổi âm dương) | [[Ly]] | [[Đoài]] |
| **Trung nguyên** | Dương Nam · Âm Nữ → **[[Cấn]]** | Dương Nữ · Âm Nam → **[[Khôn]]** |

> [!tip] Vì sao lại là 25 và 30
> Đây chính là hai tổng của [[Hà Đồ]]: **tổng năm số trời (1+3+5+7+9) = 25**, **tổng năm số đất (2+4+6+8+10) = 30**. Hệ Dương lấy modulo theo số trời, hệ Âm lấy modulo theo số đất — thuật toán khép kín trong chính bộ số Hà Đồ mà nó vay mượn.

Ghép quẻ Thượng + quẻ Hạ → **quẻ Tiên Thiên**, ứng với **tiền vận**.

## Bước 5 — Xác định hào Nguyên Đường
> Hào Nguyên Đường là hào chỉ mệnh của Tiền vận (gắn với quẻ Tiên Thiên) hoặc Hậu vận (quẻ Hậu Thiên). **Nguyên đường của Hà Lạc cũng giống như cung Mệnh, cung Thân trong thuật Tử Vi** — xem [[Mười hai cung (Tử Vi)]]. Nguyên đường **quyết định vận hạn đời người bắt đầu từ đâu**.

Xác định từ **giờ sinh**:

- Sinh **giờ khí Dương** → đếm bắt đầu từ **Tý**, chỉ đếm **hào Dương**, từ dưới lên.
- Sinh **giờ khí Âm** → đếm bắt đầu từ **Ngọ**, chỉ đếm **hào Âm**, từ dưới lên.
- Đếm đến hào nào **trùng với chi giờ sinh** thì hào ấy là Nguyên Đường.

Số lượt đếm tùy số hào cùng loại trong quẻ (Bảng 12):

| Quẻ có | Đếm 1 lần | Đếm 2 lần | Rồi tiếp sang hào loại kia |
|---|:---:|:---:|:---:|
| **1–2 hào** cùng loại | không | **có** | **có** |
| **3 hào** cùng loại | không | **có** | không |
| **4–5 hào** cùng loại | **có** | không | **có** |

**Quẻ [[01 Bát Thuần Càn|Thuần Càn]] và [[02 Bát Thuần Khôn|Thuần Khôn]]** (6 hào cùng loại) phải tra **bảng riêng** (Bảng 13a/b/c, 12 trường hợp), vì còn phụ thuộc sinh **trước hay sau Đông Chí / Hạ Chí**. Sách dẫn ba bảng này từ *Tích hợp đa văn hóa Đông Tây* của **Nguyễn Hoàng Phương**.

## Bước 6 — Biến quẻ Tiên Thiên ra quẻ Hậu Thiên
> Nếu quẻ Tiên Thiên là quẻ nguyên thủy thuộc về số Trời cho, thì **quẻ Hậu Thiên biểu hiện sự thăng trầm của con người trải qua một cuộc biến đổi bể dâu trong môi trường cuộc sống**.

Hai thao tác:

1. **Đảo trong ngoài**: quẻ Nội Tiên Thiên → quẻ Ngoại Hậu Thiên; quẻ Ngoại Tiên Thiên → quẻ Nội Hậu Thiên.
2. **Hào Nguyên Đường đi theo sang** (dời 3 ngôi cùng với quái của nó) và **đổi tính**: âm thành dương, dương thành âm.

## Bước 7 — Quẻ Hỗ
> Quẻ Hỗ là quẻ **nằm sẵn trong lòng** quẻ Tiên Thiên và Hậu Thiên; nó có vai trò **hỗ trợ, làm cho các tín hiệu phong phú thêm**.

**Bỏ hào 1 và hào 6.** Lấy hào **3-4-5** làm quẻ Ngoại, hào **2-3-4** làm quẻ Nội. Lập cả **Hỗ Tiên Thiên** và **Hỗ Hậu Thiên** → tổng cộng **bốn quẻ** trong một cấu trúc.

## Bước 8 — Hóa Công, Thiên/Địa Nguyên khí
Ba "ưu tiên của Trời Đất": chỉ cần **quẻ tương ứng có mặt trong bất kỳ quẻ nào** của bốn quẻ trên là **có**.

**Hóa Công** (Bảng 14) — theo **mùa sinh**:

| Sinh trong khoảng | Quẻ có Hóa Công |
|---|---|
| sau **Đông Chí**, trước **Xuân Phân** | [[Khảm]] |
| sau **Xuân Phân**, trước **Hạ Chí** | [[Chấn]] |
| sau **Hạ Chí**, trước **Thu Phân** | [[Ly]] |
| sau **Thu Phân**, trước **Đông Chí** | [[Đoài]] |

> Hóa Công hiểu nôm na là **công năng của tạo hóa**… là tín hiệu cho thấy có tiềm năng về **trí, đức, sức mạnh nhiều mặt**, do đó cũng là tín hiệu về **danh giá** — ân thưởng, vinh dự, đỗ đạt, thăng tiến.

**Thiên Nguyên khí / Địa Nguyên khí** (Bảng 14b) — **chỉ dùng Can Chi năm sinh**; Can cho TNK, Chi cho ĐNK:

| Quẻ | [[Càn]] | [[Khôn]] | [[Cấn]] | [[Đoài]] | [[Khảm]] | [[Ly]] | [[Chấn]] | [[Tốn]] | [[Càn]] | [[Khôn]] |
|---|---|---|---|---|---|---|---|---|---|---|
| **Can (TNK)** | Giáp | Ất | Bính | Đinh | Mậu | Kỷ | Canh | Tân | Nhâm | Quý |
| **Chi (ĐNK)** | Tuất | Mùi · Thân | Sửu · Dần | Dậu | Tý | Ngọ | Mão | Thìn · Tị | Hợi | — |

- **Thiên Nguyên khí** là nguyên khí của Trời, **chủ về sang trọng**.
- **Địa Nguyên khí** là nguyên khí của Đất, **chủ về giàu có**.
- Có cả hai là **Giàu Sang Phú Quý**.

> [!note] Tác giả không đồng ý với sách trước
> Có ý kiến cho rằng Hóa Công ở quẻ Hỗ Hậu Thiên thì phải đến chặng cuối đời mới phát huy. Xuân Cang cho biết **trắc nghiệm thực tế của ông thấy khác**: do tính thống nhất của cấu trúc, Hóa Công và Nguyên khí **dù ở Hỗ Hậu Thiên vẫn tác động mạnh ngay ở những chặng đầu cuộc đời**.

## Bước 9 — Xác định đại vận
- **Mỗi hào là một đại vận.** Sáu đại vận Tiên Thiên là **tiền vận**, sáu đại vận Hậu Thiên là **hậu vận** → **12 chặng phủ kín đời người**.
- **Hào Dương = 9 năm; hào Âm = 6 năm.**
- Bắt đầu từ **hào Nguyên Đường Tiên Thiên**, đi **lên**; đến hào 6 thì vòng xuống hào 1, cho đủ 6 đại vận khép kín. Hậu vận làm y như vậy, khởi từ hào Nguyên Đường Hậu Thiên.
- Tính bằng **tuổi**: đại vận đầu là **01–06** (hào âm) hoặc **01–09** (hào dương); các đại vận sau lấy tuổi bắt đầu **cộng 5** (hào âm) hoặc **cộng 8** (hào dương) ra tuổi kết thúc.

## Bước 10 — Ví dụ đã dựng đủ
Ví dụ của sách, dùng xuyên suốt cả bài toán:

**Đề toán** — Hoàng Hoa Cúc, nhà báo. Sinh **18-6-1955** lúc 08:05, tức **28-4 Ất Mùi**, giờ Thìn (mã số ngày 47). Tiết khí: Lập Hạ 15-3, **Mang Chủng 16-4**, Xuân Phân 28-2, Hạ Chí 3-5. **Giờ khí Dương** · **Âm Nữ** · Mệnh **Kim** (Trong cát) · **Trung nguyên**.

**Bốn trụ** — sinh *sau* tiết Mang Chủng nên tháng sinh tính là **tháng Năm**:
**Ất Mùi · Nhâm Ngọ · Canh Tuất · Canh Thìn**

**Mã số**: 2 · 5-10 · 6 · 2-7 · 3 · 5-10 · 3 · 5-10

| | Phép tính | Modulo | Mã | Quẻ |
|---|---|---|---:|---|
| **Trị số Dương** (hàng trên, vì Âm Nữ) | 5+7+3+5+3+5 = **28** | M25 → 3 | 3 | **[[Chấn]]** (Lôi) → quẻ Thượng |
| **Trị số Âm** | 2+10+6+2+10+10 = **40** | M30 → 10 → 1 | 1 | **[[Khảm]]** (Thủy) → quẻ Hạ |

→ **Quẻ Tiên Thiên = [[40 Lôi Thủy Giải|Lôi Thủy Giải]]**, hào Nguyên Đường ở **hào 1**.

Đảo trong ngoài rồi biến hào Nguyên Đường (từ hào 1 dời lên **hào 4**, âm → dương):
→ **Quẻ Hậu Thiên = [[17 Trạch Lôi Tùy|Trạch Lôi Tùy]]**, Nguyên Đường ở **hào 4**.

Lấy hào 2-3-4 và 3-4-5:
→ **Hỗ Tiên Thiên = [[63 Thủy Hỏa Ký Tế|Thủy Hỏa Ký Tế]]** · **Hỗ Hậu Thiên = [[53 Phong Sơn Tiệm|Phong Sơn Tiệm]]**

| Tiền vận (Giải) | Tuổi | | Hậu vận (Tùy) | Tuổi |
|---|---|---|---|---|
| hào 1 âm **(nđ)** | 01–06 | | hào 4 dương **(nđ)** | 43–51 |
| hào 2 dương | 07–15 | | hào 5 dương | 52–60 |
| hào 3 âm | 16–21 | | hào 6 âm | 61–66 |
| hào 4 dương | 22–30 | | hào 1 dương | 67–75 |
| hào 5 âm | 31–36 | | hào 2 âm | 76–81 |
| hào 6 âm | 37–42 | | hào 3 âm | 82–87 |

**Hóa Công**: sinh sau Xuân Phân trước Hạ Chí → quẻ [[Chấn]]; Chấn có mặt ở cả Tiên Thiên và Hậu Thiên → **có Hóa Công**.
**Thiên / Địa Nguyên khí**: Ất → [[Khôn]], Mùi → [[Khôn]]; không quẻ nào trong bốn quẻ có Khôn → **không**.

## Liên quan
[[Tám chữ Hà Lạc và quỹ đạo đời người — Xuân Cang]] · [[Hà Đồ]] · [[Lạc Thư]] · [[Thiên Can và Địa Chi]] · [[Lục thập tứ quái]] · [[Gieo quẻ và bấm độn]] · [[Hào]]

Nguồn: [[Tám chữ Hà Lạc và quỹ đạo đời người — Xuân Cang]], Bài Ba (tr. 28–40)
