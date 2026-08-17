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

w(K, 'Chu Dịch Thượng Kinh', fm(['Thượng Kinh'], ['kinh-dịch/khái-niệm']) + """
# Chu Dịch Thượng Kinh

Quyển một của Chu Dịch, gồm **30 quẻ** từ Càn tới Ly.

Mở đầu bằng hai quẻ **Càn – Khôn** là trời và đất: nói về vũ trụ, là giai đoạn **tiên thiên**, là *hình nhi thượng học nghiên cứu về thiên lý*. Có trời có đất rồi mới có vạn vật, có vạn vật rồi mới có nam nữ, vợ chồng, cha con, vua tôi, trên dưới, lễ nghĩa — và đó là lúc chuyển sang [[Chu Dịch Hạ Kinh]].

## Danh sách
[[01 Bát Thuần Càn]] · [[02 Bát Thuần Khôn]] · [[03 Thủy Lôi Truân]] · [[04 Sơn Thủy Mông]] · [[05 Thủy Thiên Nhu]] · [[06 Thiên Thủy Tụng]] · [[07 Địa Thủy Sư]] · [[08 Thủy Địa Tỷ]] · [[09 Phong Thiên Tiểu Súc]] · [[10 Thiên Trạch Lý]] · [[11 Địa Thiên Thái]] · [[12 Thiên Địa Bĩ]] · [[13 Thiên Hỏa Đồng Nhân]] · [[14 Hỏa Thiên Đại Hữu]] · [[15 Địa Sơn Khiêm]] · [[16 Lôi Địa Dự]] · [[17 Trạch Lôi Tùy]] · [[18 Sơn Phong Cổ]] · [[19 Địa Trạch Lâm]] · [[20 Phong Địa Quán]] · [[21 Hỏa Lôi Phệ Hạp]] · [[22 Sơn Hỏa Bí]] · [[23 Sơn Địa Bác]] · [[24 Địa Lôi Phục]] · [[25 Thiên Lôi Vô Vọng]] · [[26 Sơn Thiên Đại Súc]] · [[27 Sơn Lôi Di]] · [[28 Trạch Phong Đại Quá]] · [[29 Tập Khảm]] · [[30 Bát Thuần Ly]]

## Liên quan
[[Bố cục Kinh Dịch]] · [[Lục thập tứ quái]]

""" + SRC)

w(K, 'Chu Dịch Hạ Kinh', fm(['Hạ Kinh'], ['kinh-dịch/khái-niệm']) + """
# Chu Dịch Hạ Kinh

Quyển hai của Chu Dịch, gồm **34 quẻ** từ Hàm tới Vị Tế.

Là *hình nhi hạ học nghiên cứu về nhân sự* — giai đoạn thứ hai, nói về con người, về nam nữ:
- **Hàm** là đạo chồng, là trai gái cảm nhau: *"thiên địa cảm nhi vạn vật hóa sinh"*.
- **Hằng** là đạo vợ, đầu bạc răng long thủy chung không đổi: *"tứ thời biến hóa nhi năng cửu thành"*.

## Danh sách
[[31 Trạch Sơn Hàm]] · [[32 Lôi Phong Hằng]] · [[33 Thiên Sơn Độn]] · [[34 Lôi Thiên Đại Tráng]] · [[35 Hỏa Địa Tấn]] · [[36 Địa Hỏa Minh Di]] · [[37 Phong Hỏa Gia Nhân]] · [[38 Hỏa Trạch Khuê]] · [[39 Thủy Sơn Kiển]] · [[40 Lôi Thủy Giải]] · [[41 Sơn Trạch Tổn]] · [[42 Phong Lôi Ích]] · [[43 Trạch Thiên Quải]] · [[44 Thiên Phong Cấu]] · [[45 Trạch Địa Tụy]] · [[46 Địa Phong Thăng]] · [[47 Trạch Thủy Khốn]] · [[48 Thủy Phong Tỉnh]] · [[49 Trạch Hỏa Cách]] · [[50 Hỏa Phong Đỉnh]] · [[51 Bát Thuần Chấn]] · [[52 Bát Thuần Cấn]] · [[53 Phong Sơn Tiệm]] · [[54 Lôi Trạch Quy Muội]] · [[55 Lôi Hỏa Phong]] · [[56 Hỏa Sơn Lữ]] · [[57 Bát Thuần Tốn]] · [[58 Bát Thuần Đoài]] · [[59 Phong Thủy Hoán]] · [[60 Thủy Trạch Tiết]] · [[61 Phong Trạch Trung Phu]] · [[62 Lôi Sơn Tiểu Quá]] · [[63 Thủy Hỏa Ký Tế]] · [[64 Hỏa Thủy Vị Tế]]

## Liên quan
[[Bố cục Kinh Dịch]] · [[Chu Dịch Thượng Kinh]]

""" + SRC)

w(K, 'Quan điểm Nho gia về Kinh Dịch', fm(
    ['Trình Di', 'Chu Hy'], ['kinh-dịch/khái-niệm']) + """
# Quan điểm Nho gia về Kinh Dịch

Tổng hợp lời bàn của **Trình Di**, **Chu Hy** và tiên nho (lược khảo Ngô Tất Tố và Phan Bội Châu).

## Trình Di
- *"Gọi là Dịch mới có lý; nếu xếp đặt nhất định thì có cái lý gì?"* Cuộc biến đổi của trời đất âm dương cũng như **hai thớt cối xay**: lên xuống đầy vơi, cứng mềm chưa từng dừng nghỉ. **Dương thường hữu dư, âm thường bất túc**, cho nên không đều nhau; đã không bằng nhau thì sinh ra hàng vạn sự biến đổi.
- Kinh Dịch chỉ nói về lẽ **tráo trở, đi lại, lên xuống**. Từ trời đất tối sáng cho đến cây cỏ sâu bọ nhỏ nhặt, không cái nào không thích hợp.
- **Lý luận là vô hình**, cho nên người ta mượn **tượng** để tỏ rõ **lý**; lý hiện ở lời thì có thể do lời mà biết tượng. *"Hiểu được ý nghĩa của nó thì số sẽ ở bên trong."*
- Xem Kinh Dịch phải biết **thời**.

## Chu Hy
- Thánh nhân làm ra Dịch chỉ là ngửa xem cúi xét, thấy đầy khoảng trời đất không có cái gì không phải là lẽ **một âm một dương**. Có lẽ ấy thì có tượng ấy, có tượng ấy thì số tự ở bên trong.
- Vạch một vạch lẻ hình dung khí dương, một vạch chẵn hình dung khí âm; có hai thì liền có bốn, có bốn thì liền có tám, lần lượt tới **64 quẻ với 384 hào**.
- *"Trong khoảng trời đất này chỉ là hai chữ âm dương mà thôi."* Mở mắt ra: chẳng âm thì dương, chẳng nhân thì nghĩa, chẳng cứng thì mềm. Muốn thẳng lên là dương, thu lại lùi lại là âm.

## Sách của người quân tử
- *"Kinh Dịch chỉ mưu tính cho người quân tử, không mưu tính cho tiểu nhân."* Kẻ tiểu nhân lấy bụng tiểu nhân mà xét đoán thì không làm sao hiểu được.
- Quy ước đọc hào: **hào dương là quân tử / đàn ông**, **hào âm là tiểu nhân / đàn bà**. Chi tiết ở [[Ngôi hào — trung, chính, ứng, thời]].
- Kinh Lễ chép: *"khiết tĩnh tinh vi là giáo hóa của Kinh Dịch."* Khi chưa vạch quẻ, các hào vẫn im lặng, mừng giận buồn vui chưa phát tiết, chỉ là cái rất rỗng rất tĩnh; đến khi vạch quẻ, tượng số hiện ra mới nói lên rất nhiều đạo lý lành dữ.

## Bốn điều thuộc về đạo thánh nhân trong Dịch
1. Để **nói** thì chuộng lời.
2. Để **hành động** thì chuộng sự biến đổi.
3. Để **chế đồ đạc** thì chuộng hình tượng.
4. Để **bói toán** thì chuộng lời chiêm đoán của nó.

Người quân tử khi ở yên thì coi hình tượng mà ngẫm lời lẽ; khi hành động thì coi sự biến đổi mà suy đoán. Đó là lẽ *"dĩ bất biến ứng vạn biến"*.

## Vì sao Kinh Dịch khó hiểu
Cái khó không phải ở ý tứ sâu xa mà **tại lời văn** — chủng chẳng, rã rời, không đầu đuôi, có chỗ không đúng văn pháp; một câu có thể hiểu theo mấy nghĩa mà chẳng thể bảo nghĩa nào đúng sai. Tinh thần của Kinh Dịch chính là ở chỗ đó. Nên đọc lúc **trong lòng yên tĩnh** và **không giữ ý kiến riêng**; người từng trải càng lĩnh hội được nhiều.

## Liên quan
[[Kinh Dịch]] · [[Âm dương]] · [[Ngôi hào — trung, chính, ứng, thời]]

""" + SRC)

w(K, 'Kinh Dịch trong văn minh phương Đông', fm(
    ['Vị trí Kinh Dịch'], ['kinh-dịch/khái-niệm', 'kinh-dịch/lịch-sử']) + """
# Kinh Dịch trong văn minh phương Đông

## Trung Quốc
Từ **tam hoàng** (Phục Hy, Hoàng Đế, Thần Nông — có tài liệu thêm Nữ Oa, Chúc Dung, Toại Nhân) qua **ngũ đế** (Nghiêu, Thuấn, Hạ Vũ…), rồi Hạ → Thương–Ân → Chu → Tần → Hán → Tam Quốc → Ngụy, Tùy, Đường, Tống, Minh, Thanh.

Các vua thượng cổ rất gần dân và **nhìn tượng quẻ mà chế công cụ**:
| Quẻ | Công cụ |
|---|---|
| [[30 Bát Thuần Ly]] — nhiều lỗ rỗng như mắt lưới | Lưới bắt cá |
| [[59 Phong Thủy Hoán]] — gỗ ([[Tốn]]) đi trên nước ([[Khảm]]) | Thuyền |
| [[50 Hỏa Phong Đỉnh]] | Cái vạc nấu chín thức ăn |
| [[42 Phong Lôi Ích]] — trên âm mộc (Tốn) mềm, dưới dương mộc ([[Chấn]]) cứng | Cán cày và lưỡi cày |

Sau Khổng Tử có Mạnh Tử, Tuân Tử, Cáo Tử, **Trình Di**, **Chu Hy** tiếp tục xây dựng nho giáo và Kinh Dịch.

- **Tứ thư**: Luận Ngữ (chép lời Khổng Tử với học trò — quan trọng nhất), Đại Học (đạo làm quan), Mạnh Tử, Trung Dung (đạo làm người).
- **Ngũ kinh**: Kinh Thi, Kinh Thư, Kinh Lễ, Kinh Xuân Thu, **Kinh Dịch** — trong đó Kinh Dịch là cuốn khó xem nhất, tựa như một cuốn thiên thư.

**Đế đạo và Bá đạo**: triều đại nào gắn bó với dân, lấy dân làm gốc thì tồn tại lâu dài — đó là *Đế đạo*; triều đại nào tồn tại bởi đàn áp hà khắc thì sụp đổ nhanh chóng — đó là *Bá đạo*.

## Nhật Bản
Ngôn ngữ Nhật còn khoảng 2500–4000 từ gốc Hán cổ. Ảnh hưởng nho giáo còn thể hiện trong y học, võ học, hệ đường kinh và huyệt đạo; người Nhật chế tạo máy dò huyệt, máy dò loa tai, các loại kim châm cứu.

## Hàn Quốc
Sau khi Võ Vương lên ngôi có mời **Cơ Tử** (hoàng tử nhà Ân) ra giúp nước nhưng ông không chịu, nên được cho ra Triều Tiên lập một nước riêng — xem [[36 Địa Hỏa Minh Di]]. Điều này lý giải vì sao người Hàn rất chuộng Kinh Dịch: **cờ Hàn Quốc có thái cực đồ ở giữa, bốn bên là bốn quẻ [[Càn]], [[Khôn]], [[Ly]], [[Khảm]]**, và học thuyết [[Tứ tượng]] được đặc biệt coi trọng.

## Việt Nam
- Cung đình Huế được xây dựng theo [[Lạc Thư]]; thi cử theo chế độ trạng nguyên, bảng nhãn, thám hoa, tiến sĩ.
- Đại danh y Thiền sư **Tuệ Tĩnh** bị nhà Minh bắt về nước — *"ai có về Nam, cho tôi về với"*.
- **Hải Thượng Lãn Ông Lê Hữu Trác** là người tinh thông y lý, có công vận dụng Kinh Dịch vào y học, trình bày rõ trong bộ *Hải Thượng Y Tông Tâm Lĩnh* — xem [[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]].
- Kinh Dịch còn được ứng dụng trong thiên văn, lịch toán, kiến trúc và nông nghiệp.

## Ngôi cửu ngũ
Trong văn học Trung Hoa, **ngôi vua** gọi là *ngôi cửu ngũ chí tôn* hay *ngôi trời* — xem [[Ngôi hào — trung, chính, ứng, thời]]. Trong cung đình Huế có 9 đỉnh đồng xếp hai hàng bá quan văn võ, đỉnh thứ 9 ở giữa to nhất là biểu tượng nhà vua: *"quân bất hí ngôn, nhất ngôn cửu đỉnh, tứ mã nan truy"*.

## Liên quan
[[Kinh Dịch]] · [[Kinh Dịch với Y lý]]

""" + SRC)

w(K, 'Thái cực', fm(['Vô cực', 'Đạo'], ['kinh-dịch/khái-niệm']) + """
# Thái cực

## Định nghĩa
Trên bờ sông Hoàng Hà, Khổng Tử hỏi Lão Tử: *thưa thầy, thái cực là gì?* Lão Tử đáp:

> *"Có một vật do hỗn hợp mà thành, nó sinh ra trước trời đất, vừa trống không vừa yên lặng, đứng một mình mà không biến cải, có thể làm mẹ đẻ của thiên hạ. Ta không biết tên nó là gì, phải đặt tên chữ cho nó là **Đạo**; chỉ có biến động là thuộc tính của nó."*

Khổng Tử không dùng chữ **Đạo** mà dùng chữ **Thái cực** để chỉ cái bắt đầu của vũ trụ. Do đó **Đạo cũng chính là Thái cực**, và trong lòng chữ Đạo ấy đã mang sẵn hai mặt đối kháng là âm và dương.

## Chuỗi sinh thành
> *Vô cực sinh thái cực, thái cực sinh [[Lưỡng nghi\\|lưỡng nghi]], lưỡng nghi sinh [[Tứ tượng\\|tứ tượng]], tứ tượng sinh [[Bát quái\\|bát quái]], bát quái lay động thành [[Lục thập tứ quái\\|lục thập tứ quái]] gồm 384 hào.*
> — Hệ Từ Thượng Truyện, [[Thập Dực]]

**Vô cực** là lúc vũ trụ còn trong cõi hư vô, đã chứa sẵn thái cực rồi. **Thái cực động thành dương, thái cực tĩnh thành âm.**

## Thái cực trong thân người
Trong y học, Hải Thượng Lãn Ông cho rằng **hai quả thận họp lại thành một hình thái cực**: quả trái là âm thủy, quả phải là dương thủy, mệnh môn nằm ở giữa. Xem [[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]].

Trong [[Lạc Thư]], **số 5 ở giữa bụng (ngũ trung)** là biểu tượng ngũ hành nằm giữa, có tượng thái cực.

## Liên quan
[[Kinh Dịch]] · [[Âm dương]] · [[Lưỡng nghi]]

""" + SRC)

w(K, 'Lưỡng nghi', fm(['Dương nghi', 'Âm nghi'], ['kinh-dịch/khái-niệm']) + """
# Lưỡng nghi

Từ [[Thái cực]] mà ra hai nghi: **dương nghi** và **âm nghi**.

| | Dương nghi | Âm nghi |
|---|---|---|
| Ký hiệu | Một vạch **liền** ▬▬ | Một vạch **đứt** ▬ ▬ |
| Tính chất | động, nóng, sáng, trong, nhẹ | tĩnh, lạnh, đục, tối, nặng |
| Vận động | nổi lên thành **trời** | chìm xuống thành **đất** |
| Phương sinh | phương **bắc** | phương **nam** |
| Bên chủ | bên **trái** chủ dương | bên **phải** chủ âm |

Nguyên tắc này chi phối cả [[Tiên Thiên Bát Quái]] (dương đi lên bên trái, âm đi xuống bên phải) và cả sinh lý học trong y học cổ truyền — xem [[Âm dương]].

Chồng hai vạch lên nhau thì thành **tượng**: đó là [[Tứ tượng]].

## Liên quan
[[Thái cực]] · [[Tứ tượng]] · [[Hào]] · [[Âm dương]]

""" + SRC)

w(K, 'Tứ tượng', fm(
    ['Thái dương', 'Thiếu âm', 'Thiếu dương', 'Thái âm'], ['kinh-dịch/khái-niệm']) + """
# Tứ tượng

Trên [[Lưỡng nghi|dương nghi và âm nghi]] chồng thêm một vạch nữa thì thành bốn **tượng**.

| Tượng | Cấu tạo | Ngôi | Số (10 − ngôi) | Khung giờ trong ngày |
|---|---|---|---|---|
| **Thái dương** (lão dương) | trên vạch dương thêm vạch dương | 1 | **9** | 6h – 12h: dương trùng dương, dương khí dày đặc trùm khắp |
| **Thiếu âm** | trên vạch dương thêm vạch âm | 2 | **8** | 12h – 18h: âm sinh trong dương, âm còn non yếu |
| **Thiếu dương** | trên vạch âm thêm vạch dương | 3 | **7** | 0h – 6h: khí nhất dương phát sinh, dương sinh trong âm |
| **Thái âm** (lão âm) | trên vạch âm thêm vạch âm | 4 | **6** | 18h – 0h: âm trong âm, âm khí dày đặc |

- Lão dương **9**, thiếu dương **7** — đều là số **lẻ**.
- Lão âm **6**, thiếu âm **8** — đều là số **chẵn**.

## Vì sao quẻ chỉ dùng số 9 và số 6
Vì đó là **lão dương và lão âm**. *Già thì biến, trẻ thì không biến* — lão âm lão dương là âm dương phát triển tới cực độ nên dễ biến hơn thiếu âm thiếu dương. Đây chính là lý do [[Hào]] dương gọi là **hào cửu** và hào âm gọi là **hào lục**.

## Ý nghĩa rộng
Một năm cũng vậy, một ngày cũng vậy, một đời người cũng vậy: sáng – trưa – chiều – tối, sinh – trưởng – thu – tàng, sinh – lão – bệnh – tử. Đó chính là tứ tượng.

Học thuyết Tứ Tượng được người Hàn Quốc đặc biệt coi trọng — xem [[Kinh Dịch trong văn minh phương Đông]].

## Liên quan
[[Lưỡng nghi]] · [[Bát quái]] · [[Hào]] · [[Lạc Thư]]

""" + SRC)

w(K, 'Âm dương', fm(['Lẽ âm dương'], ['kinh-dịch/khái-niệm']) + """
# Âm dương

*"Trong khoảng trời đất này chỉ là hai chữ âm dương mà thôi."* — Chu Hy

## Nguyên tắc nền
- **Âm dương là tiên thiên** vì âm dương vô hình; **[[Ngũ hành]] là hậu thiên** vì ngũ hành hữu hình.
- **Dương thường hữu dư, âm thường bất túc** (Trình Di) — vì không đều nhau nên mới sinh ra hàng vạn biến đổi.
- **Dương cực âm sinh, âm cực dương sinh**; trong âm có dương, trong dương có âm.
- **Vật cùng tắc biến, biến tắc thông, thông tắc cửu.**
- Âm dương giao nhau thì hanh thái ([[11 Địa Thiên Thái]]); không giao nhau thì bế tắc ([[12 Thiên Địa Bĩ]]).

## Hướng vận động
| | Dương | Âm |
|---|---|---|
| Vận động | thăng, đi lên, đi ra | giáng, đi xuống, đi vào |
| Bên | trái | phải |
| Số | lẻ (1, 3, 5, 7, 9) — số **trời** | chẵn (2, 4, 6, 8, 10) — số **đất** |

## Ứng dụng trong thân người
Từ đồ hình [[Tiên Thiên Bát Quái]] rút ra: dương đi lên chủ về bên trái, âm đi xuống chủ về bên phải. Do đó:
- Đầu là nơi **hội tụ của khí dương**; bên trái cơ thể thuộc dương, tinh khí theo dương khí dồn lên tai và mắt → **tai mắt bên trái sáng suốt hơn bên phải**.
- Bên phải thuộc âm, tinh khí theo âm khí đi xuống → **tay chân bên phải mạnh hơn bên trái**.
- Thân người từ nhất âm nhất dương sinh ra tam âm tam dương: tay có lục kinh, chân có lục kinh, tổng cộng **12 kinh**.

## Cân bằng
Trong thực tế âm dương phải quân bình. Đừng bao giờ nghĩ phải tiêu diệt hết cái ác, cái xấu, rằng chỉ có dương hoàn toàn mới tốt — xem [[11 Địa Thiên Thái]] và [[60 Thủy Trạch Tiết]]. *Thái quá hoặc bất cập đều xấu cả.*

## Liên quan
[[Thái cực]] · [[Lưỡng nghi]] · [[Ngũ hành]] · [[Quan điểm Nho gia về Kinh Dịch]]

""" + SRC)

print('OK gen2')
