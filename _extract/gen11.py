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


w('Ứng dụng', 'Phép bói bằng cỏ thi', fm(
  ['Thi pháp', 'Bói cỏ thi', 'Mười tám lần biến'], ['kinh-dịch/ứng-dụng']) + """
# Phép bói bằng cỏ thi

Nghi thức bói cổ chép trong **Đồ thuyết của Chu Hy**, phần cuối. Đây là phép bói **chính thống** của Chu Dịch — khác với phép gieo ba đồng tiền và phép bấm độn trong [[Gieo quẻ và bấm độn]], vốn là những lối giản tiện đời sau.

## 1. Sắp đặt nơi bói
- Chọn **chỗ đất sạch** làm nhà chứa cỏ thi, **cửa ngoảnh về Nam**. Giữa nhà kê một chiếc giường (dài chừng 5 thước, rộng chừng 3 thước, đừng để gần vách quá).
- **Cỏ thi 50 cây**, bọc bằng **lụa màu đỏ nhạt**, đựng trong **túi màu đen**, cho vào hộp, đặt ở **phía bắc** chiếc giường.
  - *Hộp bằng ống tre hoặc gỗ rắn hay vải sơn, hình tròn, đường kính độ 3 tấc, dài bằng cỏ thi; một nửa làm đáy, một nửa làm nắp.*
- Đặt **chiếc khay** ở phía nam cái hộp. Trong khay chia **hai ô lớn** cách nhau một thước; phía tây ô lớn làm **ba ô nhỏ**, mỗi ô cách nhau năm tấc.
- Đặt **lò hương** ở phía nam chiếc khay, **hộp hương** ở phía nam cái lò. Hằng ngày thắp hương cung kính; sắp bói thì quét rửa lau chùi.
- Chuẩn bị nghiên có rót nước, một cây bút, một thoi mực, **một miếng ván sơn vàng** (để vạch quẻ).
- Người bói **trai khiết, đội mũ mặc áo, ngoảnh mặt về bắc**, rửa tay đốt hương cúng lễ.

## 2. Lời khấn
Cầm cả 50 cây bằng hai tay, hơ trên lò hương, khấn:

> *Giả nhĩ Thái phệ hữu thường, giả nhĩ Thái phệ hữu thường! Mỗ (quan tính danh) kim dĩ mỗ sự vị tri khả phủ, viên chất sở nghi vu thần vu linh, cát hung đắc thất, hối lận ưu ngu, duy nhĩ hữu thần, thượng minh cáo chi.*
>
> **Nghĩa:** Mượn mày, đồ bói lớn, tính không thay đổi. Mỗ (quan tước — hoặc chức nghiệp — họ và tên) vì việc (kể rõ) chưa biết nên chăng, phải đem điều nghi ngờ ấy hỏi đấng thần linh. **Lành hay dữ, được hay mất, hối tiếc hay lo sợ — người có thiêng hãy bảo cho rõ.**

## 3. Bốn "dinh" — một lần biến
Trước hết dùng tay phải **nhặt một thẻ trả lại trong hộp** → chỉ còn **49 thẻ** dùng để bói.

| Dinh | Thao tác | Hình dung |
|---:|---|---|
| **1** | Hai tay **chia đôi** 49 thẻ vào hai ô lớn tả và hữu | **hai Nghi** |
| **2** | Tay trái cầm thẻ ô tả; tay phải nhặt **một thẻ** ở ô hữu, cài vào khe **ngón út** tay trái | **tam tài** |
| **3** | Tay phải đếm thẻ ở tay trái theo **"bốn chiếc một"** | **tứ thời** |
| **4** | Thẻ còn thừa (1, 2, 3 hoặc 4) kẹp vào khe **ngón vô danh** tay trái | **tháng nhuận** |

Rồi lặp lại với **ô hữu**: trả thẻ đã đếm về ô tả, cầm thẻ ô hữu đếm "bốn chiếc một" bằng tay trái, thẻ thừa giắt vào khe **ngón giữa** tay trái (*hai lần nhuận*).

Cuối cùng gom số thẻ **một lần cài + hai lần kẹp** đặt vào **ô nhỏ thứ nhất**. **Đó là một lần biến.**

### Quy luật số thẻ
| Lần biến | Còn lại trước khi biến | Tổng thẻ cài kẹp |
|---|---|---|
| **1** | 49 | **5 hoặc 9** |
| **2** | 44 hoặc 40 | **4 hoặc 8** |
| **3** | 40, 36 hoặc 32 | **4 hoặc 8** |

Trong lần biến thứ nhất: tay tả 1 thì tay hữu 3; tả 2 thì hữu 2; tả 3 thì hữu 1; tả 4 thì hữu 4. **Năm thẻ được một lần bốn là số lẻ; chín thẻ được hai lần bốn là số chẵn** — lẻ thì ba mà chẵn thì một.

## 4. Ba lần biến thành một hào
**Số thẻ cài kẹp: 5 và 4 là *lẻ*; 9 và 8 là *chẵn*.**

| Cài kẹp | Tổng thẻ | Số đếm qua còn | Hào | Dấu | Tên gọi |
|---|---:|---:|---|---|---|
| **ba số lẻ** | 13 | 26 | **Lão Dương** | ▮ | **trùng** |
| hai lẻ một chẵn | 17 | 32 | **Thiếu Âm** | ▬ ▬ | **triết** |
| hai chẵn một lẻ | 21 | 28 | **Thiếu Dương** | ▬▬ | **đạo** |
| **ba số chẵn** | 25 | 24 | **Lão Âm** | ✕ | **giao** |

Số đếm qua chia cho 4 cho ra chính các số của [[Tứ tượng]]: 26/4 ≈ **9** (lão dương), 32/4 = **8** (thiếu âm), 28/4 = **7** (thiếu dương), 24/4 = **6** (lão âm) — xem [[Hào]].

**Lão Dương và Lão Âm là hào động, sẽ biến** thành hào ngược lại; Thiếu Dương và Thiếu Âm không biến. *Già thì biến đổi, trẻ thì chưa biến đổi.*

## 5. Mười tám lần biến thành một quẻ
> **Cứ ba lần biến thì thành một hào. Tất cả mười tám lần biến thì thành một quẻ.** Xét sự biến đổi trong quẻ để xem việc dữ hay lành.

Chỉ **khấn ở hai lần biến đầu**; từ lần thứ ba trở đi không khấn nữa, chỉ dùng 49 thẻ mà làm. Các lần 1, 4, 7, 10, 13, 16 giống nhau; các lần 2, 5, 8, 11, 14, 17 giống nhau; các lần 3, 6, 9, 12, 15, 18 giống nhau.

Bói xong: bọc lại cỏ thi, đựng vào túi, cho vào hộp, đậy nắp, thu xếp bút nghiên mực ván, rồi **thắp hương cúng lễ lần nữa**.

*Nếu nhờ người bói hộ thì chủ nhân thuật thẳng việc mình định xem, kẻ bói vâng lời; bói xong chủ nhân thắp hương, vái kẻ bói giúp rồi lui.*

## Đọc quẻ ra sao
Sau khi có quẻ, đọc theo [[Ngôi hào — trung, chính, ứng, thời|thì – ngôi – người]], [[Tượng và Chiêm]] và phần **Hào từ** của quẻ tương ứng. Nhớ lời răn ở [[Triệu]]: Kinh Dịch tuyệt nhiên không mê tín; lời chiêm chỉ nói về **xu thế**.

## Liên quan
[[Gieo quẻ và bấm độn]] · [[Tứ tượng]] · [[Hào]] · [[Đồ thuyết của Chu Hy]] · [[Lục thập tứ quái]]

""" + NTT)

w('Khái niệm', 'Đồ thuyết của Chu Hy', fm(
  ['Chín đồ hình', 'Quái biến đồ'], ['kinh-dịch/khái-niệm', 'kinh-dịch/đồ-hình']) + """
# Đồ thuyết của Chu Hy

Phần đầu *Chu Dịch đại toàn* mà [[Kinh Dịch Trọn Bộ — Ngô Tất Tố|Ngô Tất Tố]] dịch gồm **chín đồ hình** kèm lời bàn của tiên nho, rồi kết bằng [[Phép bói bằng cỏ thi]].

| # | Đồ hình | Note trong wiki |
|---:|---|---|
| 1 | **Hà Đồ** | [[Hà Đồ]] |
| 2 | **Lạc Thư** | [[Lạc Thư]] |
| 3 | **Thứ tự tám quẻ của Phục Hy** | [[Bát quái]] — thái cực → lưỡng nghi → tứ tượng → bát quái |
| 4 | **Phương vị tám quái của Phục Hy** | [[Tiên Thiên Bát Quái]] |
| 5 | **Thứ tự 64 quẻ của Phục Hy** | [[Lục thập tứ quái]] |
| 6 | **Phương vị 64 quẻ của Phục Hy** | [[Lục thập tứ quái]] — Viên đồ và Phương đồ |
| 7 | **Thứ tự tám quẻ của Văn Vương** | [[Thuyết Lục Tử]] |
| 8 | **Phương vị tám quẻ của Văn Vương** | [[Hậu Thiên Bát Quái]] |
| 9 | **Hình vẽ sự biến đổi của các quẻ** (quái biến đồ) | dưới đây |

## Hà Đồ và Lạc Thư — vài chú giải đáng chú ý
**Chu Hy**: *"Sinh số của trời đất chỉ có đến năm là hết. Năm đối một, hai, ba, bốn thì thành sáu, bảy, tám, chín; cuối cùng lại đối với năm thành mười."* — cơ sở của quy tắc **số thành = số sinh + 5** ở [[Hà Đồ]].

**Hoàng Miễn Trai** giải thích vì sao 1 sinh Thủy mà 3 sinh Mộc, 2 sinh Hỏa mà 4 sinh Kim:
> Dùng **một cạnh vặn cho tròn thì thành ba cạnh** — thế là số một cùng cực thì thành số ba. Dùng **hai cạnh bẻ cho vuông thì thành bốn cạnh** — thế là số hai cùng cực thì thành số bốn.

Và nối số thành với tượng quẻ:
> Số **sáu** hoàn thành hành Thủy cũng giống tượng quẻ [[Khảm]]: một hào Dương ở giữa (số một của trời sinh Thủy), số sáu của đất bao bọc ở ngoài — **Dương ít Âm nhiều thì Thủy mới thịnh**. Số **bảy** hoàn thành hành Hỏa cũng giống tượng quẻ [[Ly]]: một hào Âm ở giữa (số hai của đất sinh Hỏa), số bảy của trời bao bọc ở ngoài — **Âm ít Dương nhiều thì Hỏa mới thịnh**.

**So sánh hai đồ** (Chu Hy chua):
| | Hà Đồ | Lạc Thư |
|---|---|---|
| Cân đối | **chẵn thừa mà lẻ thiếu** | **lẻ thừa mà chẵn thiếu** |
| Số trời | 25 (5 × 5) | 25 (5 × 5) |
| Số đất | 30 (5 × 6) | 20 (5 × 4) |
| Để trống ở giữa | số **mười lăm** | số **năm** |

## Hình vẽ sự biến đổi của các quẻ (quái biến đồ)
Đồ hình thứ chín mô tả **một quẻ biến sang quẻ khác** khi hào động đổi âm dương — đây chính là cơ sở của việc đọc **quẻ chính** và **quẻ biến** trong [[Gieo quẻ và bấm độn]] và [[Phép bói bằng cỏ thi]].

## Liên quan
[[Hà Đồ]] · [[Lạc Thư]] · [[Tiên Thiên Bát Quái]] · [[Hậu Thiên Bát Quái]] · [[Lục thập tứ quái]] · [[Phép bói bằng cỏ thi]]

""" + NTT)

w('Khái niệm', 'Lý — Tượng — Số', fm(
  ['Lý Tượng Số', 'Dịch thuyết cương lĩnh'], ['kinh-dịch/khái-niệm']) + """
# Lý — Tượng — Số

Trích từ **Dịch thuyết cương lĩnh**, phần Trình Di và Chu Hy bàn về cách đọc Dịch.

## Thứ tự phát sinh
Trương Hoành Trung hỏi: *có phải nghĩa của Kinh Dịch vốn khởi ở **Số** hay không?* **Trình Di** đáp:

> **Bảo nghĩa khởi ra tự Số thì sai. Có Lý rồi mới có Tượng, có Tượng rồi mới có Số.**
>
> Kinh Dịch nhân **Tượng** để biết **Số**; hễ hiểu được nghĩa của nó thì **Số sẽ ở bên trong**.

Vì **Lý và vật vô hình**, cho nên phải **nhân Tượng để tỏ Lý**; Lý hiện ở Lời, thì có thể **do Lời mà biết Tượng**.

```
Lý  ──→  Tượng  ──→  Số
(vô hình)  (hình dung)  (chừng mực)
```

## Lời cảnh báo với người mê thuật số
Đây là chỗ Trình Di phân ranh giới rất dứt khoát:

> Ai muốn **xét cho cùng cực sự tinh vi của Tượng, biết cho hết từng hào hốt của Số** — đó là **tìm dòng theo ngọn**. Cách đó chỉ có những **nhà thuật số** vẫn chuộng, **không phải là việc mà kẻ nho giả nên cần**. Nó là cái học của bọn **Quản Lộ, Quách Phác** vậy.

Đây đồng điệu với lời răn ở [[Triệu]] và [[Gieo quẻ và bấm độn]]: **đừng biến Dịch thành bói toán nhảm nhí**.

## Ba định nghĩa của Trình Di
> Việc của đấng thượng thiên, không tiếng không hơi:
> - cái **thể** của nó gọi là **Dịch**
> - cái **lý** của nó gọi là **Đạo**
> - cái **dụng** của nó thì gọi là **Thần**

Và: ***Âm Dương khép ngỏ tức là Dịch; một khép một ngỏ gọi là biến.*** — xem [[Ba nghĩa của chữ Dịch]].

## Cách xem quẻ
> **Xem Dịch cần phải biết *thời*.** Tất cả sáu hào ai ai cũng có thể dùng: ông thánh có chỗ dùng của ông thánh, ông hiền có chỗ dùng của ông hiền, người thường có chỗ dùng của người thường, vua có chỗ dùng của vua, tôi có chỗ dùng của tôi — **không đâu không thông**.
>
> **Xem Dịch hãy xem nên *thời*, rồi mới xem đến *tài* của từng hào.** Trong một hào thường bao hàm mấy ý, thánh nhân thường lấy những ý trọng hơn mà làm ra lời… **Phải trước xem quẻ, rồi mới xem được lời hệ.**

## Từ vạch đến lành dữ — Chu Hy
> Lúc mới chỉ là vạch một vạch lẻ để hình dung khí Dương, vạch một vạch chẵn để hình dung khí Âm mà thôi. **Nhưng hễ có hai thì liền có bốn, hễ có bốn thì liền có tám**, lại theo đó mà gấp hai lên liền thành mười sáu… **không đợi xếp đặt mà thế vẫn không thể thôi.**
>
> Quẻ vạch đã lập liền có lành dữ, vì là Âm Dương đi lại giao thác ở trong. Thời của nó thì có **tiêu đi, lớn lên** khác nhau: **cái lớn lên là chủ, cái tiêu đi là khách**; việc của nó hoặc có nên chăng khác nhau: **cái nên là thiện, cái chăng là ác**. Theo chỗ chủ khách thiện ác mà phân biệt thì sự lành dữ sẽ rõ.

## Vì sao quẻ có tên như thế
Chu Hy phân biệt hai lối đặt tên quẻ:
- Theo **sự tiến lui của hào** — như [[23 Sơn Địa Bác|Bác]], [[24 Địa Lôi Phục|Phục]].
- Theo **sự hệt giống của hình** — như [[50 Hỏa Phong Đỉnh|Đỉnh]], [[48 Thủy Phong Tỉnh|Tỉnh]].

*Phục Hy theo chỗ hoàn toàn của hình thể các quẻ mà lập tên; Văn Vương coi hình tượng của quái thể mà làm Thoán từ; Chu Công coi sự biến đổi của quái hào mà làm hào từ.*

## Liên quan
[[Quan điểm Nho gia về Kinh Dịch]] · [[Tượng và Chiêm]] · [[Ba nghĩa của chữ Dịch]] · [[Ngôi hào — trung, chính, ứng, thời]] · [[Triệu]]

""" + NTT)

print('OK gen11')
