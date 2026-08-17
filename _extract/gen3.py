# -*- coding: utf-8 -*-
import os
W = r'D:\claude\claude-source\wiki'


def w(folder, name, body):
    open(os.path.join(W, folder, name + '.md'), 'w', encoding='utf-8').write(body.strip() + '\n')


SRC = 'Nguồn: [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]]'


def fm(aliases, tags):
    a = '\n'.join('  - "%s"' % x for x in aliases)
    t = '\n'.join('  - %s' % x for x in tags)
    return '---\naliases:\n%s\ntags:\n%s\n---\n\n' % (a, t)


K = 'Khái niệm'

w(K, 'Hào', fm(['Hào cửu', 'Hào lục'], ['kinh-dịch/khái-niệm']) + """
# Hào

**Hào** là từng vạch trong quẻ.

| | Hào dương | Hào âm |
|---|---|---|
| Hình | vạch **liền** ▬▬ | vạch **đứt** ▬ ▬ |
| Tên | hào **cửu** (lão dương) | hào **lục** (lão âm) |
| Số | **9** | **6** |

## Vì sao dương là 9 và âm là 6
Theo [[Hà Đồ]] có 5 số sinh 1, 2, 3, 4, 5:
- Tổng các số dương: 1 + 3 + 5 = **9**
- Tổng các số âm: 2 + 4 = **6**

Đồng thời trong [[Tứ tượng]], 9 là lão dương và 6 là lão âm — **già thì biến, trẻ thì không biến**, nên quẻ chỉ dùng số cửu và số lục.

## Quy ước đọc số
- Viết **"hào 6"** có hai nghĩa: (a) hào âm / hào lục, (b) hào ở ngôi thứ 6, ngôi trên cùng.
- Viết **"hào 1, hào 2… hào 6"** là chỉ hào số mấy ở ngôi ấy.
- Viết **"hào 6 ngôi 5"** phải hiểu là *hào lục ngũ*, tức hào âm ở ngôi 5.
- Viết **"hào 9 ngôi 2"** phải hiểu là *hào cửu nhị*, tức hào dương ở ngôi 2.

## Nguyên tắc vạch quẻ
**Vạch từ dưới lên trên và từ trong ra ngoài.**

## Liên quan
[[Ngôi hào — trung, chính, ứng, thời]] · [[Quẻ]] · [[Tứ tượng]] · [[Hà Đồ]]

""" + SRC)

w(K, 'Ngôi hào — trung, chính, ứng, thời', fm(
    ['Ngôi hào', 'Cửu ngũ', 'Đắc trung', 'Đắc chính', 'Trung chính'],
    ['kinh-dịch/khái-niệm']) + """
# Ngôi hào — trung, chính, ứng, thời

Một quẻ kép có **6 hào**, đánh số **từ dưới lên trên**: hào sơ, hào nhị, hào tam, hào tứ, hào ngũ, hào thượng.

## Cách gọi tên
| Ngôi | Quẻ [[01 Bát Thuần Càn\\|Càn]] (toàn dương) | Quẻ [[02 Bát Thuần Khôn\\|Khôn]] (toàn âm) |
|---|---|---|
| 1 | sơ cửu | sơ lục |
| 2 | cửu nhị | lục nhị |
| 3 | cửu tam | lục tam |
| 4 | cửu tứ | lục tứ |
| 5 | cửu ngũ | lục ngũ |
| 6 | thượng cửu | thượng lục |

## Ngôi ứng với địa vị xã hội
| Ngôi | Địa vị |
|---|---|
| 1 — sơ cửu | thứ dân |
| 2 — cửu nhị | bậc trung phu, tư mục |
| 3 — cửu tam | quan khanh, đại phu |
| 4 — cửu tứ | các vị đại thần |
| **5 — cửu ngũ** | **ngôi vua** — *cửu ngũ chí tôn*, ngôi trời |
| 6 — thượng cửu | trời, các bậc nguyên lão, cố vấn |

Theo [[Lục thập tứ quái|thuyết tam tài]]: hai hào dưới (1–2) là **Địa**, hai hào giữa (3–4) là **Nhân**, hai hào trên (5–6) là **Thiên**.

## Trung
- Hào **2** ở giữa nội quái, hào **5** ở giữa ngoại quái → **đắc trung**.

## Chính
- Ngôi 1, 3, 5 là **vị trí dương**; ngôi 2, 4 là **vị trí âm**.
- Hào dương ở ngôi dương, hào âm ở ngôi âm → **đắc chính**.
- Hào dương ở ngôi âm, hào âm ở ngôi dương → **bất chính**.
- Hào vừa trung vừa chính → **trung chính**, rất tốt, như hào **cửu ngũ**.

## Đọc theo quân tử – tiểu nhân
| Hào | Ngôi | Ý nghĩa |
|---|---|---|
| dương | lẻ | **quân tử được ngôi** (sơ cửu, cửu tam, cửu ngũ) |
| dương | chẵn | quân tử **không ngôi**, chưa gặp thời vận (cửu nhị, cửu tứ, thượng cửu) |
| âm | chẵn | **tiểu nhân biết điều** (lục nhị, lục tứ, thượng lục) |
| âm | lẻ | **tiểu nhân làm bậy** (sơ lục, lục tam, lục ngũ) |

## Ứng
**Ứng** là hào này viện trợ cho hào kia: sơ ứng tứ, nhị ứng ngũ, tam ứng thượng — **với điều kiện hai hào phải khác nhau** (hào này dương thì hào kia phải âm và ngược lại).

Khi trên dưới ứng nhau thì là quẻ tốt. Ví dụ hào 5 dương cương ứng với các hào âm ([[08 Thủy Địa Tỷ]]), hoặc hào 5 âm mềm ứng với các hào dương ([[14 Hỏa Thiên Đại Hữu]]) — ứng với ngôi tôn mà mềm mỏng, trên dưới ứng nhau thì dù chỉ trung mà không chính cũng tốt.

## Thì (thời) và người
- **Thì** là thời kỳ: quẻ [[11 Địa Thiên Thái|Thái]] là thời hanh thái, quẻ [[12 Thiên Địa Bĩ|Bĩ]] là thời bế tắc; hào sơ là thời kỳ đầu, hào thượng là thời kỳ cuối.
- **Người** là bản thân kẻ xem bói ở địa vị nào, thời kỳ nào — ví dụ *hào sơ quẻ Bĩ* là thứ dân trong thời bĩ tắc, *hào ngũ quẻ Thái* là ông vua trong thời hanh thái.

## Quy luật hào thượng
Các quẻ **tốt** thì hào trên cùng thường **không tốt** (Càn: *kháng long hữu hối*; Thái: *thành phục vu hoàng*), các quẻ **xấu** thì hào trên cùng thường **tốt** (Bĩ: *khuynh bĩ, hậu hỷ*; Khốn: khốn cực thì phải thay đổi). Riêng [[48 Thủy Phong Tỉnh]] và [[50 Hỏa Phong Đỉnh]] hào trên cùng vẫn tốt, vì nước đã múc lên rồi, thức ăn đã nấu chín rồi — tức là lúc đã thành công.

## Liên quan
[[Hào]] · [[Quẻ]] · [[Lục thập tứ quái]] · [[Quan điểm Nho gia về Kinh Dịch]]

""" + SRC)

w(K, 'Quẻ', fm(['Quái', 'Đơn quái', 'Trùng quái', 'Nội quái', 'Ngoại quái'],
               ['kinh-dịch/khái-niệm']) + """
# Quẻ (quái)

Có hai loại quẻ:
- **Quẻ đơn** — quẻ 3 vạch, *đơn quái*. Có 8 quẻ đơn, gọi là [[Bát quái]].
- **Quẻ kép** — quẻ 6 vạch, *trùng quái*. Có 64 quẻ kép, gọi là [[Lục thập tứ quái]].

Trong quẻ kép: **3 hào dưới là nội quái**, **3 hào trên là ngoại quái**.

## Cách gọi tên quẻ kép
Đọc tên **ngoại quái trước**, rồi **nội quái**, cuối cùng là **tên quẻ**.

- *Địa Thủy Sư*: **Sư** là tên quẻ, *thủy* là [[Khảm]] làm nội quái, *địa* là [[Khôn]] làm ngoại quái.
- *Thiên Phong Cấu*: thiên là ngoại quái [[Càn]], phong là nội quái [[Tốn]], **Cấu** là tên quẻ.

Nếu hai quái nội ngoại giống nhau thì thêm chữ **thuần** (Bát Thuần Càn, Bát Thuần Ly). Riêng quẻ Khảm gọi là **Tập Khảm** để nhấn mạnh tính hiểm và dày đặc.

## Số của 8 quẻ đơn
| Quẻ | [[Càn]] | [[Đoài]] | [[Ly]] | [[Chấn]] | [[Tốn]] | [[Khảm]] | [[Cấn]] | [[Khôn]] |
|---|---|---|---|---|---|---|---|---|
| Số | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

## Quẻ âm và quẻ dương
Ngoài [[Càn]] là quẻ dương và [[Khôn]] là quẻ âm:
- **[[Tốn]], [[Ly]], [[Đoài]] là quẻ âm** — vì dương × âm × dương = âm.
- **[[Chấn]], [[Khảm]], [[Cấn]] là quẻ dương** — vì dương × âm × âm = dương.

Đây là cơ sở của [[Thuyết Lục Tử]]: quẻ âm thành **nữ**, quẻ dương thành **nam**.

## Liên quan
[[Hào]] · [[Bát quái]] · [[Lục thập tứ quái]] · [[Ngôi hào — trung, chính, ứng, thời]]

""" + SRC)

w(K, 'Bát quái', fm(['Tám quẻ đơn'], ['kinh-dịch/khái-niệm', 'kinh-dịch/bát-quái']) + """
# Bát quái

Tám quẻ đơn, mỗi quẻ 3 vạch, sinh ra từ [[Tứ tượng]] bằng cách chồng thêm một vạch âm hoặc dương.

| Tứ tượng | + vạch dương | + vạch âm |
|---|---|---|
| Thái dương | [[Càn]] ☰ | [[Đoài]] ☱ |
| Thiếu âm | [[Ly]] ☲ | [[Chấn]] ☳ |
| Thiếu dương | [[Tốn]] ☴ | [[Khảm]] ☵ |
| Thái âm | [[Cấn]] ☶ | [[Khôn]] ☷ |

## Bảng tổng hợp
| Số | Quẻ | Ký hiệu | Tên khác | Tượng | Tính | Vai trong gia đình | Bộ phận cơ thể |
|---|---|---|---|---|---|---|---|
| 1 | [[Càn]] — Càn tam liên | ☰ | thiên | trời, con rồng | mãnh liệt, cương quyết | cha | đầu |
| 2 | [[Đoài]] — Đoài thượng khuyết | ☱ | trạch | đầm lầy, sông, suối | vui vẻ, hòa duyệt | thiếu nữ | mồm miệng |
| 3 | [[Ly]] — Ly trung hư | ☲ | hỏa | lửa, mặt trời | sáng, rỗng | trung nữ | tim, mắt |
| 4 | [[Chấn]] — Chấn ngưỡng vu | ☳ | lôi | sấm | động | trưởng nam | thân động ở dưới |
| 5 | [[Tốn]] — Tốn hạ đoạn | ☴ | phong | gió, gỗ, cây cỏ thảo mộc | vào, nhún nhường | trưởng nữ | hai đùi |
| 6 | [[Khảm]] — Khảm trung mãn | ☵ | thủy | nước, mây, mưa | hiểm, dày đặc | trung nam | thận, hai lỗ tai |
| 7 | [[Cấn]] — Cấn phúc uyển | ☶ | sơn | núi, đồi | đậu lại, dừng lại | thiếu nam | hai tay phía trước |
| 8 | [[Khôn]] — Khôn lục đoạn | ☷ | địa | đất, con trâu | thuận, hòa, hiền lành | mẹ | bụng, tỳ vị |

## Hai cách sắp xếp
- [[Tiên Thiên Bát Quái]] — của Phục Hy, theo lý lẽ trời đất (*hình nhi thượng học*).
- [[Hậu Thiên Bát Quái]] — của Văn Vương, theo công dụng và việc người (*hình nhi hạ học*).

## Liên quan
[[Quẻ]] · [[Thuyết Lục Tử]] · [[Lục thập tứ quái]] · [[Ngũ hành]]

""" + SRC)

w(K, 'Thuyết Lục Tử', fm(['Lục tử', 'Thuyết Lục Tử của Văn Vương'],
                         ['kinh-dịch/khái-niệm', 'kinh-dịch/bát-quái']) + """
# Thuyết Lục Tử của Văn Vương

Văn Vương xếp thứ tự các quẻ nhưng chưa nói rõ ý; sau này **Thiệu Tử** mới bàn thêm.

[[Càn]] và [[Khôn]] là trời đất mà cũng là **cha mẹ**. Bát quái chính là **một gia đình thu nhỏ** có đầy đủ bố mẹ, ba con trai và ba con gái.

| Giao | Lần | Kết quả | Vai |
|---|---|---|---|
| **Khôn tìm Càn** | 1 | [[Chấn]] | trưởng nam |
| | 2 | [[Khảm]] | trung nam |
| | 3 | [[Cấn]] | thiếu nam |
| **Càn tìm Khôn** | 1 | [[Tốn]] | trưởng nữ |
| | 2 | [[Ly]] | trung nữ |
| | 3 | [[Đoài]] | thiếu nữ |

## Vì sao Tốn, Ly, Đoài là nữ
Vì **Tốn, Ly, Đoài là quẻ âm** (dương × âm × dương = âm); còn **Chấn, Khảm, Cấn là quẻ dương** (dương × âm × âm = dương). Dịch nói: *được dương thì tiến, được âm thì lùi*, cho nên thuộc càn đạo thì thành nam, thuộc khôn đạo thì thành nữ.

## Câu hỏi để ngỏ
Tác giả nêu: tại sao **mẹ tìm bố thì ra con trai, bố tìm mẹ thì ra con gái**? Phải chăng đó là tính chủ động của từng cá thể bố và mẹ? Văn Vương không bàn luận gì thêm.

## Ứng dụng đọc quẻ kép
Thuyết Lục Tử là chìa khóa đọc nhiều quẻ trong [[Chu Dịch Hạ Kinh]]:
- [[31 Trạch Sơn Hàm]]: thiếu nữ (Đoài) trên, thiếu nam (Cấn) dưới → trai trẻ gái trẻ cảm nhau, trai hạ mình cầu gái → **tốt**.
- [[32 Lôi Phong Hằng]]: trưởng nam (Chấn) trên, trưởng nữ (Tốn) dưới → trai lớn gái lớn đứng đắn, tôn ty hợp lẽ → **lâu dài**.
- [[54 Lôi Trạch Quy Muội]]: trưởng nam trên, thiếu nữ dưới → **không cân xứng**, gái trẻ quyến rũ trai lớn → **xấu**.
- [[18 Sơn Phong Cổ]]: trưởng nữ (Tốn) chịu dưới thiếu nam (Cấn) → *loạn về tình*, dễ đổ nát.
- [[38 Hỏa Trạch Khuê]]: trung nữ (Ly) và thiếu nữ (Đoài) — chị em rồi cũng mỗi người một ngả → **chia lìa**.

## Liên quan
[[Bát quái]] · [[Quẻ]] · [[Tiên Thiên Bát Quái]]

""" + SRC)

print('OK gen3')
