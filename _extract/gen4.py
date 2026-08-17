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

w(K, 'Hà Đồ', fm(['Long mã', 'Số sinh số thành'], ['kinh-dịch/khái-niệm', 'kinh-dịch/đồ-hình']) + """
# Hà Đồ

> *Hà xuất Đồ, Lạc xuất Thư, thánh nhân tắc chi* — sông Hà xuất hiện Đồ, sông Lạc xuất hiện Thư, thánh nhân nhìn vào đó mà bắt chước theo. (Khổng Tử)

Đời vua **Phục Hy** (4477–4363 TCN), có con **long mã** xuất hiện trên sông Hà, trên lưng có **55 khoáy** đen và trắng như một bức họa đồ. Nhà vua bắt chước những chấm ấy vẽ nên Hà Đồ.

## Các số trong Hà Đồ
| Phương | Số dương (khoáy trắng, lẻ) | Số âm (khoáy đen, chẵn) |
|---|---|---|
| Bắc | 1 | 6 |
| Nam | 7 | 2 |
| Tả (Đông) | 3 | 8 |
| Hữu (Tây) | 9 | 4 |
| Trung ương | 5 | 10 |

- **1 hợp 6 · 2 hợp 7 · 3 hợp 8 · 4 hợp 9 · 5 hợp 10.**
- Vòng trong 1–5 là **số sinh**; 6–10 là **số thành**. **Số thành = số sinh + 5** (số của thổ ở giữa).
- Tổng 5 số trời (1,3,5,7,9) = **25**; tổng 5 số đất (2,4,6,8,10) = **30**; tổng cộng = **55** khoáy.

## Hà Đồ sinh ngũ hành
> *"Thiên nhất sinh thủy, địa lục thành chi. Địa nhị sinh hỏa, thiên thất thành chi. Thiên tam sinh mộc, địa bát thành chi. Địa tứ sinh kim, thiên cửu thành chi. Thiên ngũ sinh thổ, địa thập thành chi."* — Chu Hy

**Trời sinh thì đất thành, đất sinh thì trời thành** — đó là lẽ sinh thành của tạo hóa.

| Thứ tự | Hành | Số sinh | Số thành | Phương |
|---|---|---|---|---|
| 1 | **Thủy** | 1 (trời) | 6 (đất) | Bắc |
| 2 | **Hỏa** | 2 (đất) | 7 (trời) | Nam |
| 3 | **Mộc** | 3 (trời) | 8 (đất) | Đông |
| 4 | **Kim** | 4 (đất) | 9 (trời) | Tây |
| 5 | **Thổ** | 5 (trời) | 10 (đất) | Trung ương |

Nhờ Hà Đồ mới giải thích được **phương vị** của ngũ hành, và biết quy luật **tương sinh** không phải như hình ngôi sao 5 cánh.

## Vì sao thủy sinh ra trước
Khi trời đất định ngôi, càn khôn xác lập thì hành đầu tiên phải là **nước**. Thủy là gốc của con người và vũ trụ, cũng là **thiên thủy / thiên quý** — nước của trời cho, mang số 1 của trời, ứng với thiên can nhâm quý. Xem [[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]].

## Ứng dụng trong y học
- **Thai nhi 9 tháng 10 ngày**: số 9 là số thành của **kim** (phế) — phế hoàn thành thì thở được; số 10 là số thành của **thổ** (tỳ vị) — bộ máy tiêu hóa làm việc được. Tự ăn được, tự thở được là điều kiện cần và đủ để đứa trẻ ra đời. (Số sinh là nguyên thể / tiên thiên; **số thành mới phát sinh công dụng** / hậu thiên.)
- **Bài Lục vị** bổ thận âm có 6 vị — số 6 chính là số của thủy thận.
- **Tam thất**: tam là 3 vào can mộc, thất là 7 vào tâm hỏa, theo lý *đồng thanh tương ứng, đồng khí tương cầu*; lá xanh gân hồng nên bổ tâm huyết và can huyết.
- Vì sao **nước có màu đen, vị mặn**: thủy không phải nước ao hồ mà là **nước biển** — biển mênh mông nên mặn, càng xa bờ càng sâu càng sẫm tới màu đen; nước bốc hơi thành mây đen vần vũ. Còn nước ngọt lấy từ lòng đất, mà **ngọt là vị của hành thổ**.

Hậu Thiên Bát Quái dựa theo **vị trí 10 số của Hà Đồ**.

## Liên quan
[[Lạc Thư]] · [[Ngũ hành]] · [[Hậu Thiên Bát Quái]] · [[Hào]] · [[Linh Quy Bát Pháp]]

""" + SRC)

w(K, 'Lạc Thư', fm(['Cửu cung', 'Linh quy'], ['kinh-dịch/khái-niệm', 'kinh-dịch/đồ-hình']) + """
# Lạc Thư

**Lạc** là sông Lạc, **thư** là một thông điệp mà trời đất gửi đến trên lưng một con rùa. Vua **Hạ Vũ** (2205–2167 TCN) nhân đi trị thủy ở sông Lạc nhìn thấy, chép lại rồi xếp theo thứ tự làm nên thiên [[Cửu Trù Hồng Phạm]].

> Chu Hy: *"Lạc Thư lấy tượng của rùa nên số của nó thì trên đầu đội số 9, dưới chân đạp số 1, sườn trái mang số 3, hông phải mang số 7, vai mang số 2 và số 4, chân đi số 6 và số 8, nằm giữa bụng là số 5 (ngũ trung)."*

## Ma phương
```
4  9  2
3  5  7
8  1  6
```
Cộng theo hàng dọc, hàng ngang hay đường chéo đều được **15**, trong đó 15 = 9 + 6 (lão dương + lão âm).

## Các con số
- Lạc Thư có **9 số** (1→9), tổng = **45**. Số lẻ (dương/thiên số) 1+3+5+7+9 = **25**; số chẵn (âm/địa số) 2+4+6+8 = **20**.
- Tổng Lạc Thư + [[Hà Đồ]] = 45 + 55 = **100**.
- Bỏ số 5 ở giữa thì mỗi cặp đối xứng có tổng = **10** — số lớn của trời đất, *trời bắt đầu ở 1 (thỉ) mà toàn vẹn ở 10 (chung)*. Từ đó ra số của [[Tứ tượng]]: 10−1=9, 10−2=8, 10−3=7, 10−4=6.
- Số **5** là số giữa của số dương, số **6** là số giữa của số âm → cho nên hay gặp **ngũ** và **lục**: ngũ vị, ngũ sắc, ngũ tạng, ngũ hành, 5 ngón tay chân… và lục hợp, lục khí, lục phủ.
- **Số 5 ở giữa** (ngũ trung) là biểu tượng ngũ hành nằm giữa, có tượng [[Thái cực]].

## Lạc Thư sinh ngũ hành tương khắc
So với Hà Đồ, các số đổi chỗ: 1 từ bắc sang tây bắc, 7 từ tây sang tây nam, 9 từ nam sang đông nam, 3 từ đông xuống đông bắc. **Số 2 và 7 của Hỏa đổi chỗ cho số 4 và 9 của Kim.**

Do đó trên Lạc Thư khởi từ **Thủy khắc Hỏa → Hỏa khắc Kim → Kim khắc Mộc → Mộc khắc Thổ → Thổ khắc Thủy**.

## Ứng dụng
1. **[[Cửu Trù Hồng Phạm]]** — 9 phạm trù đạo đức xã hội.
2. **Phép tỉnh điền nhà Chu** — 900 mẫu chia 9 ô, 8 nhà mỗi nhà 100 mẫu tư điền không phải nộp thuế, 100 mẫu công điền ở giữa mọi người cùng cày và nộp toàn bộ thu hoạch.
3. **Phép xây dựng kinh thành** — chia 9 khu: giữa là cung vua, trước là triều đình, sau là chợ, kèm đàn tế trời đất và miếu thờ tổ tiên, 6 khu còn lại dân ở. **Cung đình Huế cũng dựa theo Lạc Thư mà xây.**
4. **Bản đồ phối bát quái – ngũ hành – tiết khí** (dùng trong [[Linh Quy Bát Pháp]]):

| Phương | Số | Quẻ | Hành | Tiết khí |
|---|---|---|---|---|
| Bắc | 1 | [[Khảm]] | Thủy | Đông chí |
| Tây Nam | 2 | [[Khôn]] | Thổ | Lập thu |
| Đông | 3 | [[Chấn]] | Mộc | Xuân phân |
| Đông Nam | 4 | [[Tốn]] | Mộc | Lập hạ |
| Trung ương | 5 | | | |
| Tây Bắc | 6 | [[Càn]] | Kim | Lập đông |
| Tây | 7 | [[Đoài]] | Kim | Thu phân |
| Đông Bắc | 8 | [[Cấn]] | Thổ | Lập xuân |
| Nam | 9 | [[Ly]] | Hỏa | Hạ chí |

Tiên Thiên Bát Quái dựa theo **số 9 của Lạc Thư**; Hậu Thiên Bát Quái dựa theo **10 số của Hà Đồ**.

## Liên quan
[[Hà Đồ]] · [[Cửu Trù Hồng Phạm]] · [[Ngũ hành]] · [[Hậu Thiên Bát Quái]] · [[Linh Quy Bát Pháp]]

""" + SRC)

w(K, 'Cửu Trù Hồng Phạm', fm(['Chín trù', 'Hồng Phạm'], ['kinh-dịch/khái-niệm']) + """
# Cửu Trù Hồng Phạm

Người xưa thấy [[Lạc Thư]] có 9 ô, mỗi ô mang một số, nên dựa theo đó đặt ra **9 phạm trù về đạo đức xã hội**.

```
4 Ngũ kỷ   9 Ngũ phúc lục cựu   2 Ngũ sự
3 Bát chính   5 Hoàng cực        7 Kê nghi
8 Thứ trưng   1 Ngũ hành         6 Tam đức
```

## Trù 1 — Ngũ hành gắn với Ngũ thường
| Hành | Đức | Lý do |
|---|---|---|
| Thủy | **Trí** | Trí tuệ là gốc của con người, mở mang dân trí, bao dung thiên hạ — nên ứng với hành sinh ra đầu tiên, mang số 1 của trời |
| Hỏa | **Lễ** | Hỏa bốc cao soi sáng, trên dưới rõ ràng; lễ phân biệt vua–tôi, bạn–thù, trên–dưới. *Muốn học văn trước phải học lễ* |
| Mộc | **Nhân** | Có thủy có hỏa thì mộc ra đời; có Càn Khôn thì quẻ [[03 Thủy Lôi Truân\\|Truân]] xuất hiện — muôn vật mới sinh, mà con người đứng đầu muôn vật, là *vạn vật chí linh* |
| Kim | **Nghĩa** | Kim loại ít thay đổi nhất, như sắt đá chẳng phai, là lời thề son sắt. *Đừng tham vàng bỏ nghĩa* |
| Thổ | **Tín** | Thổ là mẹ của vạn vật, bao dung, không bao giờ thay lòng đổi dạ — nên người xưa lấy đất đặt cho sự tín (nay vẫn cầm cố đất đai để làm tin) |

Người xưa nhận xét: nếu trời có gió mưa lụt lội (Thủy), nắng hạn khô cằn (Hỏa), cây cối khô héo (Mộc), khí độc bốc ra (Kim), nhân tâm ly tán (Thổ) — thì người làm vua nên **xem lại mình** có làm điều gì khiến trời đất và lòng người oán hận không.

## Chín trù
| # | Trù | Nội dung |
|---|---|---|
| 1 | **Ngũ hành** | Mộc, hỏa, thổ, kim, thủy — gắn với ngũ thường (bảng trên) |
| 2 | **Ngũ sự** | Thận trọng 5 việc lớn: ngôn ngữ (như Thủy), thị giác (như Hỏa), dung mạo (như Mộc), thính giác (như Kim), tư duy (như Thổ) |
| 3 | **Bát chính** | 8 chính sách: lương thực, của cải, tế tự, công chính, giáo dục, hình luật, tiếp tân, binh bị |
| 4 | **Ngũ kỷ** | Dùng thiên văn xác định 4 mùa, năm tháng, ngày sao và lịch pháp |
| 5 | **Hoàng cực** | Nội tộc nhà vua — **quan trọng nhất** vì nằm ở giữa mà bao dung tất cả. Minh quân thì xã hội an bình, hôn quân vô đạo thì nguy đổ tức thì |
| 6 | **Tam đức** | **Chính trực** (giữ lập trường), **cương khắc** (cứng rắn kiên quyết), **nhu khắc** (mềm dẻo quyền biến) |
| 7 | **Kê nghi** | Lý giải những điều hồ nghi — khi phân vân hòa hay chiến, tiến hay lui thì bói mai rùa hoặc cỏ thi |
| 8 | **Thứ trưng** | Dự đoán thời vận, suy mình xét người, luận thời tiết tốt xấu |
| 9 | **Ngũ phúc lục cựu** | 5 phúc: ham đức tốt, sống lâu, giàu có, mạnh khỏe, chết trọn đời. 6 họa: ác nghiệt, ốm yếu, chết non, bệnh tật, lo buồn, nghèo nàn. *Có cái họa mà là phúc, có cái tưởng phúc mà hóa họa* |

## Liên quan
[[Lạc Thư]] · [[Ngũ hành]] · [[Kinh Dịch trong văn minh phương Đông]]

""" + SRC)

w(K, 'Ngũ hành', fm(['Ngũ hành trong Dịch', 'Tương sinh tương khắc'],
                    ['kinh-dịch/khái-niệm']) + """
# Ngũ hành

**Ngũ hành là hậu thiên** vì ngũ hành hữu hình; [[Âm dương]] là tiên thiên vì vô hình.

Khi học ngũ hành mà chưa học qua [[Hà Đồ]], người đọc chỉ chấp nhận sự xếp đặt một cách máy móc mà không giải thích được tại sao lại quy nạp sự vật vào ngũ hành như vậy.

## Số và phương vị (theo Hà Đồ)
| Hành | Số sinh | Số thành | Phương | Ngũ thường | Tạng |
|---|---|---|---|---|---|
| Thủy | 1 | 6 | Bắc | Trí | Thận |
| Hỏa | 2 | 7 | Nam | Lễ | Tâm |
| Mộc | 3 | 8 | Đông | Nhân | Can |
| Kim | 4 | 9 | Tây | Nghĩa | Phế |
| Thổ | 5 | 10 | Trung ương | Tín | Tỳ |

- **Tương sinh** đọc theo [[Hà Đồ]] — không phải theo hình ngôi sao 5 cánh.
- **Tương khắc** đọc theo [[Lạc Thư]]: Thủy khắc Hỏa → Hỏa khắc Kim → Kim khắc Mộc → Mộc khắc Thổ → Thổ khắc Thủy.

## Ngũ hành trong Hậu Thiên Bát Quái
| Hành | Quẻ dương | Quẻ âm | Lý do |
|---|---|---|---|
| Thủy | [[Khảm]] | | |
| Hỏa | [[Ly]] | | |
| Kim | [[Càn]] | [[Đoài]] | Càn cương kiện nên dương kim; Đoài mềm mại nên âm kim |
| Thổ | [[Cấn]] | [[Khôn]] | Cấn là đá cứng hơn đất nên dương thổ; Khôn thuận hòa nên âm thổ |
| Mộc | [[Chấn]] | [[Tốn]] | Chấn là cây cứng rắn (đinh, lim — cọc Ngô Quyền) nên dương mộc; Tốn là hoa lá cỏ mềm nên âm mộc |

## Ngũ thường
Thứ tự bát quái đã lập thì ngũ hành, lục khí biến thành **ngũ thường**: Nhân, Lễ, Nghĩa, Trí, Tín. *Đạo người hưng ở Nhân, lập ở Lễ, lý ở Nghĩa, định ở Tín và thành ở Trí.* Xem [[Cửu Trù Hồng Phạm]].

## Liên quan
[[Hà Đồ]] · [[Lạc Thư]] · [[Hậu Thiên Bát Quái]] · [[Kinh Dịch với Y lý]]

""" + SRC)

print('OK gen4')
