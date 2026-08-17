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

w(K, 'Tiên Thiên Bát Quái', fm(['TTBQ', 'Bát Quái Tiên Thiên Đồ'],
                               ['kinh-dịch/khái-niệm', 'kinh-dịch/đồ-hình']) + """
# Tiên Thiên Bát Quái

Do **Phục Hy** sắp xếp 8 hiện tượng thiên nhiên theo **đúng quy luật của trời đất sinh ra nó** — bởi vậy mới gọi là *tiên thiên*.

> **Tiên Thiên Bát Quái là hình nhi thượng học nghiên cứu về thiên lý** — môn học đầu tiên nghiên cứu về lý lẽ của trời đất.

## Thuyết tam tài trong ba vạch
Trong quẻ [[Càn]] có 3 vạch: **vạch trên là đạo trời, vạch giữa là đạo người, vạch dưới là đạo đất**. Đạo trời diễn tả bằng **âm – dương**, đạo đất bằng **nhu – cương**, đạo người bằng **nhân – nghĩa**.

## Thứ tự sinh thành
| Số | Quẻ | Lý do sinh ra |
|---|---|---|
| 1 | [[Càn]] | Trời, tức khí có đầu tiên |
| 2 | [[Đoài]] | Có khí thì có hơi nước |
| 3 | [[Ly]] | Có hơi nước thì có khí nóng (khí nóng nước mới bốc hơi) |
| 4 | [[Chấn]] | Có Ly hỏa thì có phát động |
| 5 | [[Tốn]] | Sự phát động tạo nên gió |
| 6 | [[Khảm]] | Có gió thì nước lưu chuyển |
| 7 | [[Cấn]] | Nước lưu chuyển làm đất lồi lõm tạo đồi núi |
| 8 | [[Khôn]] | Đã có tất cả rồi thì thổ khí hoàn thành |

## Phương vị
| Quẻ | Phương | Lý do Phục Hy quan sát |
|---|---|---|
| [[Càn]] | Nam | Trời trên, thiên cầu ở phương nam |
| [[Khôn]] | Bắc | Đất dưới, địa cầu đối với thiên cầu |
| [[Ly]] | Đông | Mặt trời thường mọc ở phương đông |
| [[Khảm]] | Tây | Nước chảy từ tây sang đông |
| [[Tốn]] | Tây Nam | Gió nhiều ở tây nam |
| [[Chấn]] | Đông Bắc | Sấm nhiều ở đông bắc |
| [[Cấn]] | Tây Bắc | Núi nhiều ở tây bắc |
| [[Đoài]] | Đông Nam | Sông suối và đầm nhiều ở đông nam |

## Động tĩnh, cương nhu
**Trời sinh ra 4 cái động, đất sinh ra 4 cái tĩnh.**
- **Dương nghi** gồm Càn, Đoài, Ly, Chấn — thuộc **bên trái**, từ 0h tới 12h.
- **Âm nghi** gồm Tốn, Khảm, Cấn, Khôn — thuộc **bên phải**, theo chiều đi xuống từ 13h tới 0h.

Trong tiên thiên: **âm chủ giáng, dương chủ thăng; âm bên phải, dương bên trái** — xem [[Âm dương]].

## Bào thai người theo tiên thiên
Mệnh môn có đầu tiên, tương đương vạch dương của quẻ Càn:

| Tháng | Quẻ | Diễn biến |
|---|---|---|
| 1 | Càn | Mới thụ thai, có một khí dương |
| 2 | Đoài | Thai có chất nước |
| 3 | Ly | Khí dương làm sôi nước tạo sức nóng |
| 4 | Chấn | Thai có cử động |
| 5 | Tốn | Thai có hô hấp |
| 6 | Khảm | Nhiều nước bao quanh mình |
| 7 | Cấn | Bộ máy tiêu hóa hình thành |
| 8 | Khôn | Da thịt đầy đủ |
| 9 tháng 10 ngày | | Phế kim đầy đủ (số 9), thổ khí hoàn thành (số 10) → đứa trẻ ra đời |

## Vì sao loài người sinh ra ở hội Dần
Hải Thượng Lãn Ông nói *loài người sinh ra ở hội Dần* mà không giải thích. **Mão** (5h–7h) là lúc mặt trời mọc, bắt đầu ngày mới — nhưng ngày mới ấy đã có mầm mống từ **Dần** (3h–5h) trước đó, cũng như đứa trẻ chào đời đã được sinh ra từ 9 tháng 10 ngày trước. Dần cũng tương ứng tháng 1 âm lịch. Trong châm cứu, kinh **Thủ Thái Âm Phế** là kinh số I và khởi vào **giờ Dần**.

## Liên quan
[[Hậu Thiên Bát Quái]] · [[Bát quái]] · [[Lạc Thư]] · [[Ba nghĩa của chữ Dịch]]

""" + SRC)

w(K, 'Hậu Thiên Bát Quái', fm(['HTBQ'], ['kinh-dịch/khái-niệm', 'kinh-dịch/đồ-hình']) + """
# Hậu Thiên Bát Quái

Do **Văn Vương** sắp xếp trong 7 năm bị Trụ Vương giam ở ngục Dữu Lý (xem [[09 Phong Thiên Tiểu Súc]]), theo **quy luật cuộc sống con người và xã hội**, theo quan điểm thực tế hơn.

> **Hậu Thiên Bát Quái là hình nhi hạ học nghiên cứu về nhân sự** — môn học sau này nghiên cứu về việc của con người.

## Cặp đối lập tiên thiên – hậu thiên
| Tiên thiên | Hậu thiên |
|---|---|
| Nguyên thể | Công dụng |
| Bất dịch | Giao dịch và biến dịch |
| Vô hình | Hữu hình |
| [[Âm dương]] | [[Ngũ hành]] |
| Dựa theo **số 9 của [[Lạc Thư]]** | Dựa theo **vị trí 10 số của [[Hà Đồ]]** |

Trên thực tế, Hậu Thiên Bát Quái được vận dụng trong **châm cứu, làm lịch, nông nghiệp** — người ta thường dùng HTBQ hơn TTBQ.

## Phương vị và lý do sắp đặt
| Quẻ | Phương | Lý do |
|---|---|---|
| [[Ly]] | **Nam** | Ly hỏa ở phương đông thì độ nóng cực tiểu, không phơi thóc được; chỉ ở phương nam nắng vàng rực rỡ mới phát huy công dụng. Ly lấy số lão dương **9**, vì *già thì biến* mới sinh công dụng. Ly thay Càn ở phía nam **như con thay bố mẹ** |
| [[Khảm]] | **Bắc** | Khảm thủy là nước, là mặt trăng, phải ở phương bắc đối diện với Ly theo lẽ âm dương |
| [[Chấn]] | **Đông** | Chấn từ đông bắc dồn lên thế chỗ cho Ly. Chấn là động, là nhất dương sinh, bắt đầu một ngày mới. Đông là vị trí hành **Mộc**, cũng là vị trí của **can** — can ứng quẻ Chấn, có **lôi hỏa** dữ dội nhất trong các tướng hỏa |
| [[Đoài]] | **Tây** | Phương tây là chính giữa thu; thu phân thì vạn vật vui vẻ, mà vui vẻ là tính của Đoài. Đây là nơi ở của **phế kim** |
| [[Càn]] | **Tây Bắc** | Càn nhường chỗ cho Ly mà về tây bắc trông coi 3 con trai Chấn, Khảm, Cấn |
| [[Khôn]] | **Tây Nam** | Khôn tiến về tây nam chăm sóc 3 con gái Tốn, Ly, Đoài |
| [[Tốn]] | **Đông Nam** | Tốn thay mẹ làm việc và trưởng dưỡng |
| [[Cấn]] | **Đông Bắc** | Tốn và Cấn không giao nhau, âm dương còn lẫn lộn chưa có chỗ dùng nên tạm ở đông nam và đông bắc |

Dịch nói: Chấn và Đoài là cuộc bắt đầu giao nhau nên nằm vào **ngôi sớm tối** (Mão 6h sáng, Dậu 18h tối); Khảm và Ly là cuộc giao nhau trót lọt nên nhằm vào **ngôi Tý Ngọ**.

## Ngũ hành trong Hậu Thiên Bát Quái
Xem bảng đầy đủ tại [[Ngũ hành]]: Khảm–Thủy, Ly–Hỏa, Càn/Đoài–Kim, Cấn/Khôn–Thổ, Chấn/Tốn–Mộc.

## Thứ tự bát quái theo địa chi
- **Dương** bắt đầu ở **Hợi**, sinh ra ở **Tý**, hình thành ở **Sửu**.
- **Âm** bắt đầu ở **Tỵ**, sinh ra ở **Ngọ**, hình thành ở **Mùi**.

Khí trời khí đất là **thể** của âm dương; lửa nước là **công dụng** của âm dương — đó là từ vô hình đến hữu hình. Vì vậy Hậu Thiên Bát Quái nói về ngũ hành, dựa vào 10 số của Hà Đồ mà ra.

## Ứng dụng
- Đọc quẻ [[39 Thủy Sơn Kiển]]: *lợi tây nam, bất lợi đông bắc* — vì tây nam là phương [[Khôn]], miền đồng bằng xuôi thuận; đông bắc là phương [[Cấn]], rừng núi hiểm trở.
- Nền tảng của [[Linh Quy Bát Pháp]] và phép [[Gieo quẻ và bấm độn|bấm độn trên bàn tay]].

## Liên quan
[[Tiên Thiên Bát Quái]] · [[Hà Đồ]] · [[Lạc Thư]] · [[Ngũ hành]] · [[Bát quái]]

""" + SRC)

w(K, 'Lục thập tứ quái', fm(['64 quẻ', 'Viên đồ'], ['kinh-dịch/khái-niệm']) + """
# Lục thập tứ quái (64 quẻ)

Chồng lần lượt 8 lần [[Bát quái]] lên từng quái một, từ quái số 1 đến quái số 8: **8 × 8 = 64 quái kép**, gồm **384 hào**.

## Cấu trúc quẻ kép
- 3 hào dưới = **nội quái**; 3 hào trên = **ngoại quái**.
- Theo **thuyết tam tài**: hai hào trên là **Thiên**, hai hào giữa là **Nhân**, hai hào dưới là **Địa** — vì đạo trời có âm dương, đạo người có nhân nghĩa, đạo đất có cứng mềm.
- Xem [[Ngôi hào — trung, chính, ứng, thời]] cho các khái niệm đắc trung, đắc chính, ứng.

## Quy luật Viên đồ
64 quẻ trình bày theo **đồ tròn (Viên Đồ)** tượng trưng cho trời, hình vuông nội tiếp tượng trưng cho đất — *trời tròn đất vuông, trời chứa đất*.

Xuất phát từ 2 quẻ Càn và tận cùng bằng 2 quẻ Khôn:

**Bên trái chủ dương** (dương lớn dần, đi lên):
| Số vạch dương | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Quẻ | [[24 Địa Lôi Phục\\|Phục]] | [[19 Địa Trạch Lâm\\|Lâm]] | [[11 Địa Thiên Thái\\|Thái]] | [[34 Lôi Thiên Đại Tráng\\|Đại Tráng]] | [[43 Trạch Thiên Quải\\|Quải]] | [[01 Bát Thuần Càn\\|Càn]] |

**Bên phải chủ âm** (âm lớn dần, đi xuống):
| Số vạch âm | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Quẻ | [[44 Thiên Phong Cấu\\|Cấu]] | [[33 Thiên Sơn Độn\\|Độn]] | [[12 Thiên Địa Bĩ\\|Bĩ]] | [[20 Phong Địa Quán\\|Quán]] | [[23 Sơn Địa Bác\\|Bác]] | [[02 Bát Thuần Khôn\\|Khôn]] |

Theo quy luật **dương cực âm sinh, âm cực dương sinh**; trong âm có dương, trong dương có âm. Từ [[24 Địa Lôi Phục|Phục]] (tháng 11) tới [[44 Thiên Phong Cấu|Cấu]] (tháng 5) là **7 quẻ, 7 tháng** — đúng chu kỳ *"thất nhật lai phục"*.

## Ứng dụng 64 quẻ
1. **Chế công cụ** — thời tam hoàng ngũ đế: [[30 Bát Thuần Ly|Ly]] → lưới đánh cá, [[59 Phong Thủy Hoán|Hoán]] → thuyền, [[50 Hỏa Phong Đỉnh|Đỉnh]] → cái vạc, [[42 Phong Lôi Ích|Ích]] → cày.
2. **Tu thân xử thế** — Kinh Dịch của Khổng Tử.
3. **24 tiết khí trong năm** — phục vụ làm lịch, nông nghiệp và học thuyết vận khí (ví dụ lập đông đầu tháng 10 ứng [[15 Địa Sơn Khiêm|Khiêm]], [[12 Thiên Địa Bĩ|Bĩ]]).
4. **[[Gieo quẻ và bấm độn|Dự đoán học]]**.

## Danh sách đầy đủ
[[Chu Dịch Thượng Kinh]] (quẻ 1–30) · [[Chu Dịch Hạ Kinh]] (quẻ 31–64)

## Liên quan
[[Quẻ]] · [[Hào]] · [[Bát quái]] · [[Bố cục Kinh Dịch]] · [[Triệu]]

""" + SRC)

w(K, 'Triệu', fm(['Lời chiêm', 'Điềm báo'], ['kinh-dịch/khái-niệm']) + """
# Triệu (lời chiêm)

**Triệu** nghĩa là điềm báo, còn gọi là **lời chiêm**. Trong sách nguồn, mỗi quẻ đều kết bằng một câu triệu bốn chữ, kèm nghĩa và mục *chủ về sự*.

## Cách dùng đúng
Tác giả nhấn mạnh rất rõ:

> *"Các điềm, triệu chỉ mang tính tham khảo, nhằm giúp cho Kinh Dịch thêm phong phú chứ tuyệt nhiên không được làm cho Kinh Dịch trở thành bói toán nhảm nhí."*

Ví dụ triệu của quẻ [[01 Bát Thuần Càn|Càn]] là **"khốn long đắc thủy"** — *rồng bị nạn mà gặp nước*. Đó chỉ là điềm tốt giúp người xem có **ý chí và nghị lực để vươn lên**. Dù bói được quẻ Càn là quẻ tốt nhưng nếu không chính đính bền vững cũng không thể trọn vẹn về sau.

## Nguyên tắc đọc quẻ
- **Kinh Dịch tuyệt nhiên không mê tín.** Quẻ tốt trong hiện tại có thể không tốt trong tương lai gần vì **tính biến dịch**; quẻ không tốt hiện tại có thể tốt trong tương lai cũng vậy.
- Quẻ tốt mà không phấn đấu, không chớp thời cơ thì cũng chẳng làm gì.
- Quẻ xấu mà vững lòng tin, bình tĩnh tìm giải pháp thì vượt qua được.
- Suy đoán về Dịch **không nên cụ thể vào một việc nào đó**, chỉ nói về xu thế và những điểm chung nhất.

Tác giả tham khảo phần triệu từ *Dịch học* của **Lê Gia**; thoán từ và dịch nghĩa trích nguyên văn từ **Kinh Dịch do Ngô Tất Tố** chú giải, những chỗ khó diễn đạt vận dụng cách giải thích của **Phan Bội Châu**, **Nguyễn Hiến Lê** và **Nguyễn Hoàng Điệp**.

## Liên quan
[[Lục thập tứ quái]] · [[Gieo quẻ và bấm độn]] · [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]]

""" + SRC)

print('OK gen5')
