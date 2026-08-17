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


w('Ứng dụng', 'Linh Quy Bát Pháp',
  fm(['LQBP', 'Kỳ kinh nạp quái pháp', 'Phi đằng châm'],
     ['kinh-dịch/ứng-dụng', 'y-học-cổ-truyền', 'châm-cứu']) + """
# Linh Quy Bát Pháp

**Linh Quy Bát Pháp** (LQBP) còn gọi là **kỳ kinh nạp quái pháp** (phép quy nạp kỳ kinh vào bát quái), hay **linh quy thủ pháp phi đằng châm** — ý nói tác dụng nhanh như tên bay.

Đây là **phương pháp thời châm cứu**: lấy 8 huyệt của bát mạch kỳ kinh làm chủ, phối hợp với [[Bát quái]], cửu cung, thiên can, địa chi để **xác định huyệt mở theo giờ**.

- *Linh quy* nghĩa là **con rùa thiêng** — xem [[Lạc Thư]].
- *Bát pháp* là phép vận dụng tám huyệt giao hội với bát mạch kỳ kinh, bát quái, cửu cung, [[Hà Đồ]], [[Lạc Thư]] và hệ can chi.

## 1. Bát mạch kỳ kinh
| Mạch | Đường đi | Phối với kinh | Qua huyệt | Chức năng |
|---|---|---|---|---|
| **Đốc** | Từ tầng sinh môn qua cột sống lên huyệt Phong phủ, qua đỉnh đầu, trán, chân răng hàm trên tại huyệt Ngân giao | Thủ Thái Dương Tiểu trường | **Hậu khê** | Phụ trách kinh dương, đưa dương khí lên não |
| **Nhâm** | Từ tầng sinh môn theo đường giữa bụng lên mặt và mắt | Thủ Thái Âm Phế | **Liệt khuyết** | Chủ bào cung |
| **Xung** | Từ tử cung vào cột sống, qua rốn đến ngực và tỏa ra | Túc Thái Âm Tỳ | **Công tôn** | Vào bể huyết, điều hòa huyết |
| **Đới** | Vòng qua lưng như cái đai | Túc Thiếu Dương Đởm | **Túc lâm khấp** | Giữ cho kinh âm dương không rối loạn |
| **Dương kiểu** | Từ mắt cá ngoài dọc mặt ngoài đùi đi lên | Túc Thái Dương Bàng quang | **Thân mạch** | Quản lý chức năng vận động |
| **Âm kiểu** | Từ Chiếu hải đi lên mặt trong đùi | Túc Thiếu Âm Thận | **Chiếu hải** | Quản lý chức năng vận động |
| **Dương duy** | Từ mắt cá ngoài dọc mé đùi ngoài, gần Dương kiểu | Thủ Thiếu Dương Tam tiêu | **Ngoại quan** | Thăng bằng, điều hòa các kinh dương |
| **Âm duy** | Từ mặt trong cẳng chân dọc mặt trong đùi, bám theo Âm kiểu | Thủ Quyết Âm Tâm bào | **Nội quan** | Thăng bằng, điều hòa các kinh âm |

Hai mạch **Âm kiểu, Dương kiểu** chuyên trách về âm dương tả hữu, có nhiệm vụ **đóng mở mắt**.

## 2. Bảng phối bát quái – số – huyệt – kinh – mạch
| Quẻ | Số ([[Lạc Thư]]) | Huyệt | Thuộc kinh | Biểu lý với | Thông với mạch |
|---|---|---|---|---|---|
| [[Khảm]] | 1 | Thân mạch (VII-62) | Bàng quang | Thận | Dương kiểu |
| [[Khôn]] | 2 | Chiếu hải (VIII-6) | Thận | Bàng quang | Âm kiểu |
| [[Chấn]] | 3 | Ngoại quan (X-5) | Tam tiêu | Tâm bào | Dương duy |
| [[Tốn]] | 4 | Túc lâm khấp (XI-41) | Đởm | Can | Đới |
| Trung cung | 5 | Chiếu hải (VIII-6) | Thận | Bàng quang | Âm kiểu |
| [[Càn]] | 6 | Công tôn (IV-4) | Tỳ | Vị | Xung |
| [[Đoài]] | 7 | Hậu khê (VI-3) | Tiểu trường | Tâm | Đốc |
| [[Cấn]] | 8 | Nội quan (IX-6) | Tâm bào | Tam tiêu | Âm duy |
| [[Ly]] | 9 | Liệt khuyết (I-7) | Phế | Đại trường | Nhâm |

### Vị trí huyệt
| Huyệt | Vị trí |
|---|---|
| **Thân mạch** | Từ mỏm mắt cá ngoài đo xuống 0,5 tấc |
| **Liệt khuyết** | Từ lằn chỉ cổ tay đo lên 1,5 tấc theo kinh Phế |
| **Ngoại quan** | Từ lằn chỉ cổ tay đo lên 2 tấc theo kinh Tam tiêu |
| **Hậu khê** | Giữa đốt 1 ngón út và xương đốt bàn tay 5 |
| **Công tôn** | Sau khớp gốc ngón chân cái 1,5 tấc |
| **Chiếu hải** | Đỉnh mắt cá trong đo xuống 0,5 tấc |
| **Túc lâm khấp** | Kẽ ngón chân 4 và 5 đo lên 1,5 tấc |
| **Nội quan** | Lằn chỉ cổ tay đo lên 2 tấc, đối diện huyệt Ngoại quan |

## 3. Bốn cặp huyệt phối hợp
| Quẻ | Mã | Huyệt khóa | Vai | Cặp với | Hợp ở vùng |
|---|---|---|---|---|---|
| [[Càn]] | 6 | **Công tôn** | Cha | Nội quan | Ngực, Tâm vị |
| [[Cấn]] | 8 | **Nội quan** | Mẹ | Công tôn | |
| [[Đoài]] | 7 | **Hậu khê** | Chồng | Thân mạch | Khóe mắt trong, cổ |
| [[Khảm]] | 1 | **Thân mạch** | Vợ | Hậu khê | |
| [[Tốn]] | 4 | **Túc lâm khấp** | Nữ | Ngoại quan | Khóe mắt ngoài, sau tai |
| [[Chấn]] | 3 | **Ngoại quan** | Nam | Túc lâm khấp | |
| [[Ly]] | 9 | **Liệt khuyết** | Chủ | Chiếu hải | Yết hầu, ngực |
| [[Khôn]] | 2 | **Chiếu hải** | Khách | Liệt khuyết | |

**Vì sao đặt vai như vậy:**
- Công tôn thuộc [[Càn]] (trời) nên gọi là **cha**; Nội quan thuộc kinh Tâm bào là **mẹ** âm huyết, ứng [[Cấn]] số 8 — số âm là mẹ.
- Hậu khê thuộc kinh Tiểu trường (hỏa) ví là **chồng**; Thân mạch thuộc kinh Bàng quang (thủy) ví là **vợ**.
- Ngoại quan ứng [[Chấn]] (số 3) thuộc dương là **nam**; Túc lâm khấp ứng [[Tốn]] (số 4) thuộc âm là **nữ**.
- Liệt khuyết ứng số 9 quẻ [[Ly]] thuộc dương là **chủ**; Chiếu hải ứng số 2 quẻ [[Khôn]] thuộc âm là **khách**.

> **Ứng dụng lâm sàng:** khi tính được số huyệt mở, có thể **châm thêm huyệt đôi** để tăng tác dụng. Ví dụ được số 3 (Ngoại quan) thì châm thêm Túc lâm khấp — quan hệ *nam nữ*; được số 6 (Công tôn) thì châm thêm Nội quan — quan hệ *cha mẹ*.

## 4. Thiên can và Địa chi phối số
**Thiên can (10 can):** Giáp 1, Ất 2, Bính 3, Đinh 4, Mậu 5, Kỷ 6, Canh 7, Tân 8, Nhâm 9, Quý 10.
**Địa chi (12 chi):** Tý 1, Sửu 2, Dần 3, Mão 4, Thìn 5, Tỵ 6, Ngọ 7, Mùi 8, Thân 9, Dậu 10, Tuất 11, Hợi 12.
Trong đó **số lẻ thuộc dương, số chẵn thuộc âm**.

### Bảng phối số can chi NGÀY
Dựa vào **số thành của các hành trong [[Hà Đồ]]**.

| Thiên can | Địa chi | Phối số |
|---|---|---|
| Giáp (1), Kỷ (6) | Thìn (5), Tuất (11), Sửu (2), Mùi (8) | **10** |
| Ất (2), Canh (7) | Thân (9), Dậu (10) | **9** |
| Đinh (4), Nhâm (9) | Dần (3), Mão (4) | **8** |
| Mậu (5), Quý (10) | Tý (1), Ngọ (7), Tỵ (6), Hợi (12) | **7** |
| Bính (3), Tân (8) | | **7** — vì quan hệ với thủy, hỏa |

### Bảng phối số can chi GIỜ
Lý do phối số dựa vào **số thứ tự**: từ Giáp tới Nhâm có 9 số; từ Tý đến Thân cũng có 9 số, do đó Nhâm và Thân cùng thuộc số 9.

| Thiên can | Phối số | | Địa chi | Phối số |
|---|---|---|---|---|
| Giáp (1), Kỷ (6) | **9** | | Tý (1), Ngọ (7) | **9** |
| Ất (2), Canh (7) | **8** | | Sửu (2), Mùi (8) | **8** |
| Bính (3), Tân (8) | **7** | | Dần (3), Thân (9) | **7** |
| Đinh (4), Nhâm (9) | **6** | | Mão (4), Dậu (10) | **6** |
| Mậu (5), Quý (10) | **5** | | Thìn (5), Tuất (11) | **5** |
| | | | Tỵ (6), Hợi (12) | **4** |

*Riêng Tỵ Hợi (tương xung) đếm đến Thân có 4 số.*

## 5. Công thức tính huyệt mở theo giờ

> **Mã số = (số phối can ngày + số phối chi ngày + số phối can giờ + số phối chi giờ) ÷ 9** *(ngày dương)* **hoặc ÷ 6** *(ngày âm)* — **lấy số dư**.

- **Ngày dương**: Giáp, Bính, Mậu, Canh, Nhâm → chia cho **9**
- **Ngày âm**: Ất, Đinh, Kỷ, Tân, Quý → chia cho **6**
- Nếu **không còn dư**: ngày dương huyệt mở là **9**, ngày âm huyệt mở là **6**.

Lấy số dư đối chiếu với **bảng phối bát quái – Lạc Thư – bát huyệt** ở mục 2.

### Ví dụ 1 — giờ Ất Sửu ngày Giáp Tý
- Can chi **ngày**: Giáp = 10, Tý = 7
- Can chi **giờ**: Ất = 8, Sửu = 8
- Ngày Giáp là **ngày dương** → chia 9

(10 + 7 + 8 + 8) ÷ 9 = 3, **dư 6** → số 6 thuộc quẻ [[Càn]] → huyệt **Công tôn**.

Trên lâm sàng: châm huyệt mở này trước, sau đó phối hợp với công thức điều trị bệnh; nếu kết quả chưa vừa ý thì châm thêm huyệt đôi **Nội quan** (quan hệ cha – mẹ).

### Ví dụ 2 — giờ Kỷ Mão ngày Ất Sửu
- Can chi **ngày**: Ất = 9, Sửu = 10
- Can chi **giờ**: Kỷ = 9, Mão = 6
- Ngày Ất là **ngày âm** → chia 6

(9 + 10 + 9 + 6) ÷ 6 = 5, **dư 4** → số 4 là huyệt **Túc lâm khấp**, ứng quẻ [[Tốn]]. Muốn tăng hiệu quả nên châm thêm **Ngoại quan** (quan hệ nam – nữ).

## 6. Nguyên tắc bổ trợ
- *"Bệnh bên phải châm bên trái và ngược lại."*
- Phép **nghinh tùy bổ tả**: **xuôi đường kinh là bổ, ngược đường kinh là tả**.

## 7. Dùng bảng tra sẵn
Chỉ cần có quyển lịch ghi can chi ngày và giờ khởi là tra ra được mã số huyệt mở. Cách tra: **tìm ngày, rồi đọc từ ngoài vào trong theo thứ tự Tý, Sửu, Dần, Mão, Thìn…**

- **Ví dụ:** bệnh nhân hen phế quản lúc 8h sáng thứ hai 5-6-2006 (tức 10-5 âm lịch), **ngày Ất Sửu giờ Thìn**. Đếm Tý, Sửu, Dần, Mão, Thìn → được **số 2** = huyệt **Chiếu hải**.
  - *Huyệt mở*: Chiếu hải + Liệt khuyết
  - *Huyệt điều trị*: Thái uyên, Phế du, Xích trạch, Khổng tối, Chiên trung…
- **Ví dụ:** bệnh nhân viêm loét dạ dày tá tràng đau lúc 14h thứ bảy 12-8-2006 (19-7 âm lịch), **ngày Quý Dậu giờ Mùi**. Đếm Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi → được **số 3** = huyệt **Ngoại quan**.
  - *Huyệt mở*: Ngoại quan + Túc lâm khấp
  - *Huyệt điều trị*: Túc tam lý, Trung quản, Thiên khu, điểm dạ dày trên loa tai…

## Kết luận của tác giả
> Cách tính của Linh Quy Bát Pháp phức tạp nhưng **chỉ cần nhớ 8 huyệt** và có bảng tra sẵn; còn **Tý Ngọ Lưu Chú cần nhớ 66 huyệt ngũ du**. Vì vậy **Linh Quy Bát Pháp dễ sử dụng và có hiệu quả cao**.

> [!warning] Lưu ý
> Đây là ghi chép hệ thống hóa nội dung sách, **không phải hướng dẫn điều trị**. Việc châm cứu cần được thực hiện bởi người có chuyên môn.

## Liên quan
[[Lạc Thư]] · [[Hà Đồ]] · [[Hậu Thiên Bát Quái]] · [[Bát quái]] · [[Kinh Dịch với Y lý]]

""" + SRC)

w('Nguồn', 'Kinh Dịch Diễn Giảng — Kiều Xuân Dũng',
  fm(['Kinh Dịch Diễn Giảng', 'Kiều Xuân Dũng'], ['nguồn', 'kinh-dịch']) + """
# Kinh Dịch Diễn Giảng — Ths.BS Kiều Xuân Dũng

| | |
|---|---|
| **Tác giả** | Ths.BS **Kiều Xuân Dũng** — Học viện Y Dược học Cổ truyền Việt Nam |
| **Nhà xuất bản** | NXB Y học, Hà Nội — **2006** |
| **Độ dài** | 118 trang |
| **Giới thiệu** | GS.TS **Lê Ngọc Trọng**, Thứ trưởng Bộ Y tế, Giám đốc Học viện YDHCT Việt Nam |
| **File gốc** | `nguồn thô/Kinh Dịch Diễn Giảng Ths BS Kiều Xuân Dũng…pdf` |

## Vì sao một bác sĩ viết sách về Kinh Dịch
Trong *Lời nói đầu*, tác giả kể: sau khi thi đỗ nội trú khóa IX Trường Đại học Y khoa Hà Nội, ông xin vào học nội trú chuyên ngành Y học cổ truyền. Tốt nghiệp thành giảng viên mà **vẫn chưa lý giải được nhiều vấn đề**: tại sao thận dương hư còn gọi là mệnh môn hỏa suy? Long lôi tướng hỏa là gì?

Khi được mời giảng về chương *Huyền Tẫn Phát Vi*, ông tìm sách của Hải Thượng để đọc mà cũng không hiểu gì nhiều, cho tới khi đọc được câu:

> **"Trước khi học thuốc thì hãy học Dịch; nếu người thầy thuốc mà không học Dịch thì chỉ là thầy thuốc tầm thường mà thôi."**

Ông tự nhận mình *"chỉ là người tập hợp lại những hiểu biết của người xưa và nay, có phân tích, bình giảng với các dẫn chứng để minh họa cho dễ hiểu, dễ nhớ"*, và nhấn mạnh: **"Kinh Dịch từ xưa tới nay chỉ thuộc về Phục Hy – Hạ Vũ – Văn Vương – Chu Công Đán và Khổng Tử."**

## Cấu trúc sách
| Phần | Nội dung | Wiki |
|---|---|---|
| **1** | Cơ sở của Kinh Dịch (10 chương: đại cương, Nho gia, vị trí trong văn minh phương Đông, khái niệm, bát quái & lục tử, Hà Đồ, Lạc Thư, TTBQ, HTBQ, lục thập tứ quái) | thư mục **Khái niệm**, **Bát quái** |
| **2** | Chu Dịch Thượng Kinh — 30 quẻ | [[Chu Dịch Thượng Kinh]] |
| **3** | Chu Dịch Hạ Kinh — 34 quẻ | [[Chu Dịch Hạ Kinh]] |
| **4** | Một số ứng dụng có tính minh họa (Y lý, dự đoán học, bộ vị mạch, thuyết Thủy Hỏa, Linh Quy Bát Pháp) | thư mục **Ứng dụng** |

## Nguồn thoán từ và cách diễn giải
- **Thoán từ và dịch nghĩa** trích nguyên văn từ *Kinh Dịch* do **Ngô Tất Tố** chú giải, biên dịch từ bản gốc Chu Dịch.
- Những chỗ khó diễn đạt vận dụng cách giải thích của **Phan Bội Châu**, **Nguyễn Hiến Lê**, **Nguyễn Hoàng Điệp**.
- Phần **[[Triệu|triệu / lời chiêm]]** tham khảo *Dịch học* của **Lê Gia**.

## Ký hiệu viết tắt trong sách
### 14 kinh mạch (số La Mã)
| # | Kinh | | # | Kinh |
|---|---|---|---|---|
| I | Thủ Thái âm Phế | | VIII | Túc Thiếu âm Thận |
| II | Thủ Dương minh Đại Trường | | IX | Thủ Quyết âm Tâm Bào |
| III | Túc Dương minh Vị | | X | Thủ Thiếu dương Tam Tiêu |
| IV | Túc Thái âm Tỳ | | XI | Túc Thiếu dương Đởm |
| V | Thủ Thiếu âm Tâm | | XII | Túc Quyết âm Can |
| VI | Thủ Thái Dương Tiểu Trường | | XIII | Mạch Đốc |
| VII | Túc Thái Dương Bàng Quang (hoặc BQ) | | XIV | Mạch Nhâm |

**Huyệt chính** dùng số La Mã tên kinh + số thứ tự Ả Rập: Trung phủ (Phế) = I-1, Ngoại quan (Tam Tiêu) = X-5, Chiếu hải (Thận) = VIII-6.

### Viết tắt khác
D = kinh dương · Â = kinh âm · TCN = trước công nguyên · ĐB/ĐN/TB/TN = đông bắc / đông nam / tây bắc / tây nam · **LQBP** = [[Linh Quy Bát Pháp]] · **HTLÔ** = Hải Thượng Lãn Ông · **TTBQ** = [[Tiên Thiên Bát Quái]] · **HTBQ** = [[Hậu Thiên Bát Quái]]

### Quy ước đọc hào
Xem [[Hào]] và [[Ngôi hào — trung, chính, ứng, thời]].

## Tài liệu tham khảo của sách
1. Ngô Tất Tố (1995), *Kinh Dịch*, NXB TP. Hồ Chí Minh
2. Phan Bội Châu toàn tập (1990), NXB Thuận Hóa – Huế
3. Nguyễn Hiến Lê (1994), *Kinh Dịch*, NXB Văn Học
4. Trần Thúy (1995), *Y Dịch*, NXB Y Học
5. Hải Thượng Lãn Ông (1995), *Hải Thượng Y Tông Tâm Lĩnh*, NXB Y Học
6. Nguyễn Hoàng Điệp (2002), *Bát Quái và Lịch Vạn Niên*, NXB Văn Hóa Thông Tin
7. Nguyễn Văn Thang (1991), *Lịch Thời Châm Cứu Học*, CLB YHCT TP.HCM
8. Trần Thúy – Thái Hà (1995), *Châm Cứu Giản Yếu*, NXB QĐND
9. Lê Gia (2000), *Dịch Học Giản Yếu*, NXB Văn Hóa Thông Tin
10. Nguyễn Tử Siêu (2001), *Hoàng Đế Nội Kinh Tố Vấn*, NXB Văn Hóa Thông Tin
11–12. Bộ môn YHCT, ĐH Y khoa Hà Nội (1993), *Bài Giảng YHCT* tập 1 & 2, NXB Y Học
13–14. Trần Thúy (2000), *Nạn Kinh* và *Nội Kinh*, NXB Y Học
15. Thiều Chửu (1999), *Hán Việt Tự Điển*, NXB Văn Hóa Thông Tin
16. Nguyễn Văn Đạm (1999–2000), *Từ Điển Tiếng Việt*, NXB Văn Hóa Thông Tin
17. Lê Quý Ngưu – Lương Tú Vân (1998), *Hướng dẫn viết đọc và dịch Hán Nôm trong Đông y*, NXB Thuận Hóa

## Lời kết của tác giả
> Kinh Dịch hay nói tới quân tử và tiểu nhân, thực ra khái niệm này **chỉ mang tính tương đối** — trong con người chúng ta thường xen kẽ hai trạng thái này. Khi chúng ta đấu tranh với thói hư tật xấu, xa lánh những dục vọng thấp hèn, phấn đấu đi lên, bảo vệ lẽ phải, thì lúc đó chúng ta là **người quân tử**; còn khi chúng ta lười biếng, ganh ghét với người tài giỏi, sống trong đố kỵ và hiềm khích, thì chúng ta trở thành **kẻ tiểu nhân**.
>
> Chính vì vậy mà hầu hết các thoán từ đều dặn rằng **cần phải giữ đạo chính thì mới bền vững**.

## Liên quan
[[Kinh Dịch]] · [[Trạng thái số hóa nguồn thô]]

""")

w('Nguồn', 'Trạng thái số hóa nguồn thô', fm(
    ['Nguồn thô', 'Trạng thái PDF'], ['nguồn', 'meta']) + """
# Trạng thái số hóa nguồn thô

Ghi nhận tình trạng kỹ thuật của ba PDF trong thư mục `nguồn thô/`, tính đến **12-8-2026**.

| # | Tệp | Số trang | Lớp văn bản | Đã đưa vào wiki |
|---|---|---|---|---|
| 1 | **Chu dịch.pdf** — *Thiệu Vĩ Hoa*, "Chu Dịch với Dự Đoán Học", người dịch Mạnh Hà, NXB Văn Hóa, Hà Nội 1995 | 522 | ❌ **Chỉ có ảnh scan** — 1 ảnh/trang, không có lớp text (trừ vài dòng bìa) | Chưa |
| 2 | **Kinh Dịch Diễn Giảng** — *Ths.BS Kiều Xuân Dũng*, NXB Y học 2006 | 118 | ✅ **Có lớp text đầy đủ** (~263.000 ký tự) | ✅ **Toàn bộ** |
| 3 | **kinhdich-Sách tam-chu-ha-lac-va-quy-dao-doi-nguoi** | 608 | ❌ **Chỉ có ảnh scan**, không có lớp text | Chưa |

## Toàn bộ wiki hiện nay được rút từ nguồn số 2
Xem [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]].

## Ghi chú kỹ thuật
- Trích xuất bằng **PyMuPDF**. Lưu ý: `pdftotext -layout` **làm mất dấu tiếng Việt** trên tệp này (font nhúng thiếu ToUnicode CMap cho dấu phụ) — *"Kinh Dịch"* ra thành *"Kinh Dch"*. PyMuPDF cho ra Unicode đúng.
- Tên tệp có dấu tiếng Việt khiến các công cụ MinGW (`pdftotext`, `pdfinfo`) không mở được; phải sao chép sang tên ASCII trước.

## Để số hóa tiếp nguồn 1 và 3
Cần **OCR tiếng Việt**. Máy hiện chưa cài `tesseract`, `pdftoppm` hay `pytesseract`. Đường đi khả dĩ:
1. Cài Tesseract OCR kèm gói ngôn ngữ `vie`.
2. Render trang thành ảnh bằng PyMuPDF (`page.get_pixmap(dpi=300)`).
3. Chạy OCR, hiệu đính thủ công phần thuật ngữ Hán–Việt (dễ sai nhất ở tên quẻ, tên huyệt, tên nhân vật).

Với 1.130 trang scan, đây là một khối lượng công việc riêng — nên tách thành một đợt bổ sung, và khi có nội dung thì **so đối chiếu với các ghi chép hiện có** (Thiệu Vĩ Hoa thiên về dự đoán học, sẽ mở rộng đáng kể phần [[Gieo quẻ và bấm độn]]).

## Liên quan
[[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] · [[Kinh Dịch]]
""")

print('OK gen8')
