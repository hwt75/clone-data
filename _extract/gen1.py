# -*- coding: utf-8 -*-
import os
W = r'D:\claude\claude-source\wiki'
for d in ['Khái niệm', 'Bát quái', '64 quẻ', 'Ứng dụng', 'Nguồn']:
    os.makedirs(os.path.join(W, d), exist_ok=True)


def w(folder, name, body):
    p = os.path.join(W, folder, name + '.md')
    open(p, 'w', encoding='utf-8').write(body.strip() + '\n')


SRC = 'Nguồn: [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]]'


def fm(aliases, tags):
    a = '\n'.join('  - "%s"' % x for x in aliases)
    t = '\n'.join('  - %s' % x for x in tags)
    return '---\naliases:\n%s\ntags:\n%s\n---\n\n' % (a, t)


w('Khái niệm', 'Kinh Dịch', fm(['Chu Dịch', 'Dịch'], ['kinh-dịch/khái-niệm']) + """
# Kinh Dịch

**Kinh** là quyển sách. **Dịch** là chuyển dịch, là biến đổi. Kinh Dịch là quyển sách nói về **các quy luật biến đổi** của toàn bộ thế giới quanh ta.

Kinh Dịch không kể sự kiện như Kinh Thi, Kinh Thư hay Kinh Xuân Thu; nó "từ sự hư không mà làm ra", chỉ gồm những vạch liền vạch đứt xếp theo quy luật, rồi mượn **tượng** để tỏ **lý**. Chính vì nói bằng tượng nên một quẻ ứng được vào rất nhiều việc — nếu nói thẳng ra thì chỉ được một việc mà thôi.

## Ba tầng nghĩa
Xem [[Ba nghĩa của chữ Dịch]]: Bất Dịch — Giao Dịch — Biến Dịch, trong đó **biến dịch là quan trọng nhất**, như triết học vẫn nói: vận động chính là phương thức của tồn tại.

## Bộ khung tri thức
- **Vũ trụ luận**: [[Thái cực]] → [[Lưỡng nghi]] → [[Tứ tượng]] → [[Bát quái]] → [[Lục thập tứ quái]] gồm 384 hào.
- **Đồ hình gốc**: [[Hà Đồ]] (số sinh thành, ngũ hành tương sinh) và [[Lạc Thư]] (cửu cung, ngũ hành tương khắc).
- **Hai cách sắp bát quái**: [[Tiên Thiên Bát Quái]] nghiên cứu thiên lý, [[Hậu Thiên Bát Quái]] nghiên cứu nhân sự.
- **Văn bản**: thoán từ (Văn Vương) + hào từ (Chu Công Đán) + [[Thập Dực]] (Khổng Tử).

## Ba bậc học Dịch
Theo Chu Hy, nên chia làm ba bậc mà xem:
1. **Dịch của Phục Hy** — chỉ có hào dương hào âm, vạch liền vạch đứt, cốt dùng vào việc bói toán, chưa có văn tự ngôn ngữ.
2. **Dịch của Văn Vương – Chu Công Đán** — chia thành 64 quẻ, chú lời quẻ lời hào, vẫn mang màu sắc bói toán.
3. **Dịch của Khổng Tử** — [[Thập Dực]], chú giải lời thoán và tượng số, chú trọng **tu thân xử thế** trong đạo làm người quân tử.

## Tinh thần
- *"Xem Kinh Dịch phải biết **thời**."* Cả sáu hào ai ai cũng dùng được: thánh nhân có chỗ dùng của thánh nhân, người thường có chỗ dùng của người thường, không đâu là không thông suốt.
- Trong 64 quẻ có tới **34 quẻ khuyên giữ đạo chính** thì sẽ bền tốt. Vì vậy tiên nho nói: *"Kinh Dịch chỉ mưu tính cho người quân tử, không mưu tính cho tiểu nhân."*
- Quẻ tốt mà không phấn đấu, không chớp thời cơ thì quẻ tốt cũng chẳng làm gì; quẻ xấu mà vững lòng tin, bình tĩnh tìm giải pháp thì cũng vượt qua được — *"xưa nay nhân định thắng thiên cũng nhiều"* (Nguyễn Du).
- Kinh Dịch khó xem vì nói về vật nào mà không phải thật là vật ấy: nói rồng mà chẳng ai thấy rồng, cũng như y học cổ truyền nói thận mà chẳng phải là quả thận.

## Liên quan
[[Nguồn gốc và năm tác giả Kinh Dịch]] · [[Ba loại Dịch]] · [[Bố cục Kinh Dịch]] · [[Quan điểm Nho gia về Kinh Dịch]] · [[Kinh Dịch trong văn minh phương Đông]] · [[Kinh Dịch với Y lý]]

""" + SRC)

w('Khái niệm', 'Ba nghĩa của chữ Dịch', fm(['Bất Dịch', 'Giao Dịch', 'Biến Dịch'], ['kinh-dịch/khái-niệm']) + """
# Ba nghĩa của chữ Dịch

Chữ **Dịch** gồm ba nghĩa, hợp thành một chu trình khép kín.

| Nghĩa | Nội dung | Trong Dịch |
|---|---|---|
| **Bất Dịch** | Chẳng có gì thay đổi cả. Âm dương, trai gái gặp nhau mà không giao nhau thì không có kết quả gì. | [[Càn]] vẫn là Càn, [[Khôn]] vẫn là Khôn |
| **Giao Dịch** | Sự trao đổi, thảo luận giữa các sự vật và hiện tượng. | Càn giao Khôn thì ra [[Tốn]], [[Ly]], [[Đoài]]; Khôn giao Càn thì ra [[Chấn]], [[Khảm]], [[Cấn]] — xem [[Thuyết Lục Tử]] |
| **Biến Dịch** | Kết quả của giao dịch; sinh ra một trạng thái *bất dịch mới*. | Vòng [[63 Thủy Hỏa Ký Tế]] → [[64 Hỏa Thủy Vị Tế]] rồi lại bắt đầu |

**Biến dịch là quan trọng nhất.**

> Ví dụ mua bán nhà: người mua không muốn mua, người bán không muốn bán, nhà vẫn của người bán, tiền vẫn của người mua — đó là *bất dịch*. Hai ý định bán mua gặp nhau, mặc cả — đó là *giao dịch*. Cuộc giao dịch xong, người mua thành chủ sở hữu ngôi nhà, người bán thành chủ sở hữu món tiền — đó là *biến dịch*, và cũng là một trạng thái bất dịch mới.

Ngoài ra còn có cách giải thích khác: con thằn lằn thay đổi màu sắc 12 lần trong một ngày, hoặc sự dịch chuyển của mặt trời và mặt trăng.

## Ánh xạ sang cặp tiên thiên – hậu thiên
- **Tiên thiên là bất dịch**, vô hình, là nguyên thể → [[Tiên Thiên Bát Quái]], [[Âm dương]].
- **Hậu thiên là giao dịch và biến dịch**, hữu hình, là công dụng → [[Hậu Thiên Bát Quái]], [[Ngũ hành]].

## Liên quan
[[Kinh Dịch]] · [[Thái cực]]

""" + SRC)

w('Khái niệm', 'Nguồn gốc và năm tác giả Kinh Dịch', fm(
    ['Phục Hy', 'Hạ Vũ', 'Văn Vương', 'Chu Công Đán', 'Khổng Tử'],
    ['kinh-dịch/khái-niệm', 'kinh-dịch/lịch-sử']) + """
# Nguồn gốc và năm tác giả Kinh Dịch

Kinh Dịch do **năm người** xây dựng nên, trải hơn ba nghìn năm.

| # | Người | Niên đại | Đóng góp |
|---|---|---|---|
| 1 | **Phục Hy** (Đào Hy, Thái Cao, Thái Hạo) | 4477–4363 TCN | Thấy con long mã nổi trên sông Hoàng Hà, ghi lại 55 khoáy trên lưng nó → [[Hà Đồ]]; vạch quẻ, lập [[Tiên Thiên Bát Quái]] |
| 2 | **Hạ Vũ** | 2205–1766 TCN | Đi trị thủy sông Lạc, thấy đồ hình trên lưng rùa → [[Lạc Thư]]; từ đó lập [[Cửu Trù Hồng Phạm]] |
| 3 | **Chu Văn Vương** (Tây Bá Hầu Cơ Xương) | ~1144 TCN | Bị giam ở ngục Dữu Lý 7 năm; xếp lại quẻ Dịch của Phục Hy, viết **thoán từ**, lập [[Hậu Thiên Bát Quái]] |
| 4 | **Chu Công Đán** | | Con thứ tư của Văn Vương; đặt lời cho từng vạch — **hào từ** của 384 hào trong 64 quẻ |
| 5 | **Khổng Tử** | 551–479 TCN | Viết [[Thập Dực]]; chia thành [[Chu Dịch Thượng Kinh]] 30 quẻ và [[Chu Dịch Hạ Kinh]] 34 quẻ |

## Ghi chú
- Phục Hy tìm Hà Đồ trước Lạc Thư hơn 2000 năm, nhưng phải đến **Văn Vương** — người có sẵn cả Hà Đồ lẫn Lạc Thư trong tay — mới đủ cơ sở dựng nên Hậu Thiên Bát Quái.
- Văn Vương có tới 100 người con: con đầu **Bá Ấp Khảo** (bị Trụ Vương giết, làm mắm gửi cho cha — xem [[36 Địa Hỏa Minh Di]]), con thứ hai **Chu Võ Vương** (diệt Thương–Ân, lập nhà Chu), con thứ tư **Chu Công Đán**, con thứ 100 là **Lôi Chấn Tử** — đứa trẻ Văn Vương nhặt được và đặt tên nghĩa là "sinh ra sau tiếng sấm nổ".
- Sách viết về Kinh Dịch có tới **150 bộ, 1761 quyển, của 158 tác giả**, nhưng tất cả đều xoay quanh nội dung của năm người trên.
- Tác giả sách nguồn nhấn mạnh: *"Kinh Dịch từ xưa tới nay chỉ thuộc về Phục Hy – Hạ Vũ – Văn Vương – Chu Công Đán và Khổng Tử."*

## Một cách đọc khác về truyền thuyết
Tác giả nêu giả thuyết: phải chăng có nhà bác học tài năng nào đó tìm ra quy luật âm dương nhưng chưa đủ uy tín thuyết phục, nên **mượn cớ chuyện thánh thần** mà truyền bá học thuyết của mình? Tương tự Võ Mỵ Nương mượn cớ nhặt được ngọc để lên ngôi, hay Nguyễn Trãi chấm mật vào lá cây *"Lê Lợi vi quân, Nguyễn Trãi vi thần"* để dân tin vào mệnh trời mà kéo về đầu quân.

## Liên quan
[[Kinh Dịch]] · [[Ba loại Dịch]] · [[Kinh Dịch trong văn minh phương Đông]]

""" + SRC)

w('Khái niệm', 'Thập Dực', fm(['Mười cánh', 'Dực Truyện'], ['kinh-dịch/khái-niệm']) + """
# Thập Dực (mười cánh)

Thoán từ của Văn Vương và hào từ của Chu Công quá vắn tắt, nhiều câu lơ lửng khó hiểu, nên **Khổng Tử** viết Thập Dực để giải thích. Tiên nho ví Thập Dực như mười cánh chim bay bổng: đến đây Kinh Dịch đã hoàn tất và phát huy được hết ý nghĩa của nó.

## Mười thiên
| | |
|---|---|
| 1. Thoán Thượng Truyện | 6. Hệ Từ Hạ Truyện |
| 2. Thoán Hạ Truyện | 7. Văn Ngôn Truyện |
| 3. Tượng Thượng Truyện | 8. Thuyết Quái Truyện |
| 4. Tượng Hạ Truyện | 9. Tự Quái Truyện |
| 5. Hệ Từ Thượng Truyện | 10. Tạp Quái Truyện |

## Mười thiên nhưng chỉ chia thành sáu thứ
| Truyện | Chức năng |
|---|---|
| **Thoán Truyện** | Chú thích lời quẻ của Văn Vương — những câu dưới chữ *"lời thoán nói rằng"* |
| **Tượng Truyện** | Chú thích hình tượng các quẻ và các hào. **Đại Tượng Truyện** chú chung cho cả quẻ; **Tiểu Tượng Truyện** chú riêng từng hào |
| **Văn Ngôn Truyện** | Chú thích riêng cho hai quẻ [[01 Bát Thuần Càn]] và [[02 Bát Thuần Khôn]] |
| **Hệ Từ Truyện** | Nói về công phu cũng như ý nghĩa trong việc làm Kinh Dịch của Văn Vương và Chu Công |
| **Thuyết Quái** | Nói về đức nghiệp và sự biến hóa của 8 quẻ |
| **Tự Quái Truyện** | Nói về **tại sao quẻ này lại nối tiếp quẻ kia** — cơ sở của mục *"Lý do tiếp nối"* trong mỗi quẻ |
| **Tạp Quái Truyện** | Nói về những ý nghĩa vụn vặt của quẻ |

## Câu then chốt
Hệ Từ Thượng Truyện (quyển 5) viết:

> *Dịch hữu thái cực, thị sinh lưỡng nghi, lưỡng nghi sinh tứ tượng, tứ tượng sinh bát quái.*

Bản mở rộng trong sách nguồn: *vô cực sinh thái cực, thái cực sinh lưỡng nghi, lưỡng nghi sinh tứ tượng, tứ tượng sinh bát quái, bát quái lay động thành lục thập tứ quái gồm 384 hào.* Xem [[Thái cực]].

## Liên quan
[[Kinh Dịch]] · [[Nguồn gốc và năm tác giả Kinh Dịch]] · [[Bố cục Kinh Dịch]]

""" + SRC)

w('Khái niệm', 'Ba loại Dịch', fm(
    ['Liên Sơn Dịch', 'Quy Tàng Dịch'], ['kinh-dịch/khái-niệm', 'kinh-dịch/lịch-sử']) + """
# Ba loại Dịch

| Loại | Triều đại | Chủ quẻ | Ghi chú |
|---|---|---|---|
| **Liên Sơn Dịch** | Nhà Hạ, có từ thời Phục Hy | | Thời cổ, người xưa vạch quẻ xong treo lủng lẳng để trấn ma quỷ |
| **Quy Tàng Dịch** | Nhà Thương, có từ thời vua Thần Nông | Lấy quẻ [[Khôn]] làm chủ | Vì nông nghiệp phát triển nên coi trọng đất |
| **Chu Dịch** | Nhà Chu — thời Văn Vương, Võ Vương khởi nghiệp | Lấy [[Càn]] và [[Khôn]] làm chủ | Lúc này đã hiểu rõ vai trò trời đất. **Sách Dịch cổ duy nhất còn tồn tại** |

Ngày nay trong các y văn không còn nhắc tới Liên Sơn Dịch và Quy Tàng Dịch nữa; tất cả sách về Dịch chỉ nói về **Chu Dịch** mà thôi.

Trong *Tứ Khố Toàn Thư Liên Minh Mục Lục* có 4 bộ **Kinh – Tử – Tập – Sử**; Kinh Dịch được xếp vào bộ **Kinh**.

## Liên quan
[[Kinh Dịch]] · [[Bố cục Kinh Dịch]] · [[Nguồn gốc và năm tác giả Kinh Dịch]]

""" + SRC)

w('Khái niệm', 'Bố cục Kinh Dịch', fm(['Bố cục Chu Dịch'], ['kinh-dịch/khái-niệm']) + """
# Bố cục Kinh Dịch

## 1. Bố cục theo cổ truyền
- **Chính kinh**
  - [[Chu Dịch Thượng Kinh]]: 30 quẻ, từ quẻ Càn tới quẻ Ly
  - [[Chu Dịch Hạ Kinh]]: 34 quẻ, từ quẻ Hàm tới quẻ Vị Tế
- **Dực Truyện**: [[Thập Dực]] của Khổng Tử

## 2. Bố cục theo lẽ thiên – nhân – địa
| Giai đoạn | Quẻ | Ý nghĩa |
|---|---|---|
| **Càn Khôn** | 1–2 | Trời đất, cha mẹ muôn loài — giai đoạn **tiên thiên**, nguyên thể của vạn vật |
| **Hàm Hằng** | 31–32 | Giai đoạn **hậu thiên** thuộc con người, tiêu biểu là quan hệ nam nữ vợ chồng. Nhờ Hàm mà *"thiên địa cảm nhi vạn vật hóa sinh"*, nhờ Hằng mà *"tứ thời biến hóa nhi năng cửu thành"* — công dụng của vạn vật |
| **Ký Tế – Vị Tế** | 63–64 | Đã xong rồi mà lại chưa xong, nối tiếp một vòng Dịch mới, tuần hoàn *"chu nhi phục thỉ, như hoàn vô đoan"* — như chiếc vòng ngọc không có điểm nối |

Đây chính là lý do Thượng Kinh được gọi là **hình nhi thượng học** nghiên cứu thiên lý, còn Hạ Kinh là **hình nhi hạ học** nghiên cứu nhân sự — song song với cặp [[Tiên Thiên Bát Quái]] / [[Hậu Thiên Bát Quái]].

## Liên quan
[[Kinh Dịch]] · [[Lục thập tứ quái]] · [[Thập Dực]]

""" + SRC)

print('OK gen1')
