# -*- coding: utf-8 -*-
import os
W = r'D:\claude\claude-source\wiki'


def w(folder, name, body):
    open(os.path.join(W, folder, name + '.md'), 'w', encoding='utf-8').write(body.strip() + '\n')


NTT = 'Nguồn: [[Kinh Dịch Trọn Bộ — Ngô Tất Tố]]'


def fm(aliases, tags):
    a = '\n'.join('  - "%s"' % x for x in aliases)
    t = '\n'.join('  - %s' % x for x in tags)
    return '---\naliases:\n%s\ntags:\n%s\n---\n\n' % (a, t)


w('Nguồn', 'Kinh Dịch Trọn Bộ — Ngô Tất Tố',
  fm(['Kinh Dịch Trọn Bộ', 'Ngô Tất Tố', 'Chu Dịch đại toàn'], ['nguồn', 'kinh-dịch']) + """
# Kinh Dịch Trọn Bộ — Ngô Tất Tố (dịch và chú giải)

| | |
|---|---|
| **Dịch giả** | **Ngô Tất Tố** |
| **Nhà xuất bản** | NXB Văn học · nộp lưu chiểu quý I năm **2004** (in 700 cuốn) |
| **Độ dài** | 938 trang |
| **Nguyên bản** | ***Chu Dịch đại toàn*** của bọn **Hồ Quảng** và **Kim Âu Tư**, vâng mệnh Thành Tổ nhà Minh mà soạn |
| **File gốc** | `nguồn thô/Kinh Dịch Trọn Bộ (Ngô Tất Tố).pdf` |

Đây là **bản dịch mà [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] trích thoán từ nguyên văn**, nên hai nguồn trong wiki này khớp nhau về phần kinh văn.

## Vì sao chọn Chu Dịch đại toàn
Từ Hán đến Thanh có hàng trăm học giả chú thích Kinh Dịch. Ngô Tất Tố chọn *Chu Dịch đại toàn* vì nó **gom góp hầu khắp lời chú giải của Tiên nho** — đầy đủ hơn hết trong các bản lưu hành.

Nhưng ông nói thẳng sự dè dặt của mình:

> Soạn giả lấy **Dịch truyện của Trình Di** và **Chu Dịch bản nghĩa của Chu Hy** làm phần chính… Họ Trình họ Chu là hai cự phách trong Tống nho, sự khảo cứu của các ông ấy **không khỏi có chỗ vũ đoán và khiên cưỡng**. Như vậy thì chữ "đầy đủ" chỉ nói được về phần **lượng**, không nói được về phần **phẩm** — nghĩa là bộ sách ấy chỉ là **sách dày, không phải là sách chú giải thật đúng**.
>
> Song thế nào là đúng? Thế nào là không đúng? Đối với chính văn Kinh Dịch, những câu hỏi đó **có lẽ loài người tiêu diệt vẫn chưa giải quyết**.

## Nguyên tắc dịch
Trình Di và Chu Hy nhiều chỗ **không đồng ý với nhau**, có chỗ họ Chu công nhiên phản đối ý họ Trình. Gặp trường hợp ấy, dịch giả tự đặt một cái lệ:

> Lấy **văn pháp chữ Nho** làm bằng — hễ lời chua của ai hợp văn pháp chữ Nho hơn thì lời dịch theo ý của người ấy, bất kỳ của họ Chu hay họ Trình. Nhưng **dù theo, dù không theo, dịch giả chỉ căn cứ ở văn pháp chữ Nho, chứ không hề cho thế này là đúng, thế kia là sai.**

Khi cả hai không đồng ý mà một nhà khác có ý kiến lạ hơn thì được trích vào làm **"Lời bàn của tiên nho"**.

## Vì sao lời dịch nghe "gàn"
Ngô Tất Tố cố ý dùng tiếng cổ — *thửa, chưng, hay, khá* — xem [[Từ cổ trong bản dịch Ngô Tất Tố]]. Lý do ông tự biện hộ:

> Cái khó hiểu của Kinh Dịch **không tại ý tứ sâu xa, chỉ tại lời văn chủng chẳng rời rã, ngớ ngẩn đột ngột**, giống như lời nói của bọn đồng cốt, không đầu đuôi, không mạch lạc, có chỗ lại không đúng với văn pháp nữa… **Tinh thần của Kinh Dịch, một phần là ở chỗ đó.**
>
> Nay nếu đem những đoạn văn ấy mà dịch ra những lời trôi chảy, dễ nghe, dễ hiểu, thì là **làm cho độc giả phải theo ý kiến của mình** — đó là mất tinh thần của Kinh Dịch. Dịch giả không muốn như thế… **để độc giả muốn hiểu thế nào thì hiểu.**

Đây là một lựa chọn dịch thuật có ý thức, không phải sự vụng về — và là lý do wiki này giữ nguyên văn phong ấy trong phần hào từ.

## Cấu trúc sách
| Phần | Nội dung | Wiki |
|---|---|---|
| **Những điều nên biết** (lời người dịch) | Lai lịch Kinh Dịch · Khái luật của Kinh Dịch · Vài lời phân giải về việc dịch | [[Ngôi hào — trung, chính, ứng, thời]], [[Tượng và Chiêm]], [[Từ cổ trong bản dịch Ngô Tất Tố]] |
| **Tựa của Trình Di** | | [[Quan điểm Nho gia về Kinh Dịch]] |
| **Đồ thuyết của Chu Hy** | 9 đồ hình + [[Phép bói bằng cỏ thi]] | [[Đồ thuyết của Chu Hy]] |
| **Dịch thuyết cương lĩnh** | Lời bàn của Trình Di, Chu Hy về cách đọc Dịch | [[Lý — Tượng — Số]] |
| **Chu Dịch Thượng Kinh** | 30 quẻ, mỗi quẻ: Lời Kinh → Giải nghĩa (Truyện của Trình Di / Bản nghĩa của Chu Hy / Lời bàn của tiên nho) | [[Chu Dịch Thượng Kinh]] |
| **Chu Dịch Hạ Kinh** | 34 quẻ | [[Chu Dịch Hạ Kinh]] |

## Đóng góp cho wiki này
- **Toàn bộ 384 hào từ** (Hán–Việt + dịch nghĩa) cho cả 64 quẻ — trước đó wiki chỉ có hào từ của quẻ [[01 Bát Thuần Càn|Càn]] và [[02 Bát Thuần Khôn|Khôn]].
- [[Phép bói bằng cỏ thi]] — nghi thức bói cổ 18 lần biến.
- [[Tượng và Chiêm]] · [[Lý — Tượng — Số]] · [[Đồ thuyết của Chu Hy]] · [[Từ cổ trong bản dịch Ngô Tất Tố]].

> [!note] Về chất lượng bản số hoá
> Bản ebook có khá nhiều lỗi nhận dạng: nhãn hỏng (*Dịch âni*, *Dịchnghĩa*), tên hào sai (*Lạc Tứ* thay *Lục Tứ*), và **15 chỗ ghi sai tên hào âm/dương**. Khi đưa vào wiki, tên hào được **suy lại từ cấu tạo quẻ** chứ không lấy theo nhãn — chi tiết ở [[Trạng thái số hóa nguồn thô]].

## Liên quan
[[Kinh Dịch]] · [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] · [[Trạng thái số hóa nguồn thô]]
""")

w('Khái niệm', 'Tượng và Chiêm', fm(
  ['Tượng', 'Chiêm', 'Lời đoán', 'Thang lời chiêm'], ['kinh-dịch/khái-niệm']) + """
# Tượng và Chiêm

Theo **Chu Hy**, lời một hào thường làm hai việc:

- **Tượng** (象) là **hình tượng**.
- **Chiêm** (占) là **lời đoán**.

> Ví như hào Chín Đầu quẻ [[01 Bát Thuần Càn|Kiền]] có câu *"rồng lặn chớ dùng"*: **"rồng lặn" là Tượng** — vì Kiền là tượng con rồng, mà ngôi Đầu là chỗ rất thấp, tức là tượng của sự lặn; **"chớ dùng" là Chiêm** — vì nó là lời khuyên bảo người ta.

**Tượng** thì tùy quẻ tùy hào mà hình dung ra, **không có nhất định**.

> Trong 64 quẻ, 384 hào: **nhiều hào có Tượng mà không có Chiêm, cũng nhiều hào có Chiêm mà không có Tượng** — không phải hào nào cũng đủ cả hai thứ đó.

## Thang bậc của lời Chiêm
Đây là một trong những đóng góp thực dụng nhất của [[Kinh Dịch Trọn Bộ — Ngô Tất Tố|bản Ngô Tất Tố]]: phân tích tính chất **nặng nhẹ** của lời chiêm thành hai thang.

### Về mặt hay — từ tốt nhất xuống
| Bậc | Lời chiêm | Nghĩa |
|---:|---|---|
| 1 | **nguyên cát** 元吉 | cả tốt |
| 2 | **cát hanh** 吉亨 | tốt và hanh thông |
| 3 | **cát** 吉 | tốt |
| 4 | **hanh** 亨 | hanh thông |
| 5 | **lợi** 利 | lợi về sự gì |
| 6 | **vô hối** 無悔 | không ăn năn |
| 7 | **vô cữu** 無咎 | không lỗi |

### Về mặt dở — từ xấu nhất xuống
| Bậc | Lời chiêm | Nghĩa |
|---:|---|---|
| 1 | **hung** 凶 | dữ |
| 2 | **lệ** 厲 | nguy |
| 3 | **vô du lợi** 無攸利 | không lợi về sự gì |
| 4 | **lận** 吝 | đáng thẹn tiếc |
| 5 | **hữu cữu** 有咎 | có lỗi |
| 6 | **hữu hối** 有悔 | có ăn năn |

Nắm thang này thì đọc phần **Hào từ** trong 64 note quẻ sẽ định lượng được ngay mức độ lành dữ của từng hào.

## Phân biệt với Triệu
[[Triệu]] (lời chiêm bốn chữ như *"khốn long đắc thủy"*) là lớp **về sau**, do các sách Dịch học đời sau thêm vào — trong wiki này lấy theo [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] tham khảo *Dịch học* của Lê Gia. Còn **Chiêm** nói ở đây là lời đoán **nằm ngay trong kinh văn** của Văn Vương và Chu Công.

## Liên quan
[[Hào]] · [[Ngôi hào — trung, chính, ứng, thời]] · [[Lý — Tượng — Số]] · [[Triệu]] · [[Lục thập tứ quái]]

""" + NTT)

w('Khái niệm', 'Từ cổ trong bản dịch Ngô Tất Tố', fm(
  ['Thửa', 'Chưng', 'Từ cổ trong Kinh Dịch'], ['kinh-dịch/khái-niệm', 'ngôn-ngữ']) + """
# Từ cổ trong bản dịch Ngô Tất Tố

Toàn bộ **384 hào từ** trong wiki này dùng lối văn cổ của [[Kinh Dịch Trọn Bộ — Ngô Tất Tố|bản dịch Ngô Tất Tố]]. Ông cố ý làm vậy để **giữ cái "chủng chẳng rời rã" của nguyên văn**, không dịch trôi chảy vì như thế là ép độc giả theo ý mình.

Đây là bảng tra bốn từ hay gặp nhất, theo chính lời chua của dịch giả.

## Thửa
Có hai nghĩa, tùy vị trí:

| Đứng trước | Tương đương chữ Nho | Nghĩa | Thí dụ |
|---|---|---|---|
| **động từ** | 所 (sở) | *cái mà* (việc/vật), *kẻ mà* (người) | *Anh thửa làm* = cái mà anh làm · *không thửa lợi* = không cái gì mà lợi · *nó thửa ghét* = kẻ mà nó ghét |
| **danh từ** | 其 (kỳ) | *của nó, của người* (thường ngôi thứ ba) | *"thửa công đức ấy ai bằng"* = công đức ấy của nó, ai bằng |

Trong hào từ, dạng thứ hai rất phổ biến: *"Đậu **thửa** ngón chân"* ([[52 Bát Thuần Cấn]]) = đậu ở **ngón chân của nó**.

## Chưng
Là giới từ, dùng để nối tiếng nọ với tiếng kia. Hai nghĩa:

| Vị trí | Tương đương | Nghĩa | Thí dụ |
|---|---|---|---|
| đầu câu | 之 (chi) | làm cho lọn nghĩa tiếng đứng dưới nó (**ít dùng**) | *"chưng kiếp nhân sinh đã thỏa"* |
| dưới động từ | 於 (ư), 于 (vu) | **ở** | *Đi chưng đường* = đi ở đường · *ngủ chưng nhà* = ngủ ở nhà |

Ví dụ trong hào từ: *"Con sếu tiến **chưng** tảng đá"* ([[53 Phong Sơn Tiệm]]) = con sếu tiến **ở** tảng đá.

## Hay
- = **biết**: *Chẳng hay nàng ở nơi nao* = chẳng **biết** nàng ở nơi nào.
- = **được**: *chẳng hay giữ* = chẳng giữ **được**.

## Khá
- = **có thể**: *Việc này khá làm* = việc này **có thể** làm.
- = **đáng**: *chuyện đó khá tiếc* = chuyện đó **đáng** tiếc.

Ví dụ: *"Ngậm văn vẻ, **có thể** chính"* ([[02 Bát Thuần Khôn]], hào 3) dịch từ *hàm chương **khả** trinh*.

## Vài lối nói khác hay gặp
| Lối cổ | Nghĩa |
|---|---|
| *dường… vậy* | có vẻ như…, ra dáng… (dịch chữ 如 *như*) |
| *chớ* | đừng (勿 *vật*) |
| *cả tốt* | rất tốt (元吉 *nguyên cát*) |
| *không lỗi* | không có lỗi (無咎 *vô cữu*) |
| *thấy người lớn* | gặp được bậc đại nhân (利見大人 *lợi kiến đại nhân*) |
| *cuộc / thửa cổ* | công việc, sự đổ nát (蠱 *cổ*) |

## Liên quan
[[Kinh Dịch Trọn Bộ — Ngô Tất Tố]] · [[Hào]] · [[Tượng và Chiêm]] · [[Lục thập tứ quái]]

""" + NTT)

print('OK gen10')
