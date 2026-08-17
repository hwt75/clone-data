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


U = 'Ứng dụng'

w(U, 'Kinh Dịch với Y lý', fm(['Y Dịch', 'Bất tri Dịch bất khả tri Y'],
                              ['kinh-dịch/ứng-dụng', 'y-học-cổ-truyền']) + """
# Kinh Dịch với Y lý

> ***Bất tri Dịch, bất khả tri Y*** — không học về Kinh Dịch thì không sao hiểu được y lý.

Hải Thượng Lãn Ông trong *Huyền Tẫn Phát Vi*: **"Trước khi học thuốc thì hãy học qua Dịch đã; làm nghề thuốc mà không biết Dịch thì chỉ là thầy thuốc tầm thường mà thôi."**

*Đá chứa ngọc mà núi sáng, nước chứa ngọc trai mà sông đẹp — Kinh Dịch chính là ngọc quý của nghề Y vậy.*

## Vì sao một mớ vạch liền vạch đứt lại gắn với nghề Y
Bản thân Kinh Dịch không nói tới phủ tạng, không nói tới thuốc. Nhưng từ lý luận **con người là vũ trụ nhỏ, con người và trời đất là một**, người xưa cho rằng **các định luật chi phối vũ trụ cũng đồng thời chi phối con người** — mà con người lại là đối tượng chính và duy nhất của y học.

### Giai thoại
Dương Quý Sơn đến nhà Thiềm Quý Lỗ ở Hoàng Đình; Quý Lỗ hỏi về Kinh Dịch, **Quý Sơn lấy tờ giấy vẽ vòng tròn, lấy mực bôi đen một nửa và nói: đó là Dịch.**

> Dịch chỉ là **một không một có, một trắng một đen, một trong một ngoài**; phức tạp thì như con người, như vũ trụ, mà xét đến tận cùng thì Dịch chỉ là một âm một dương xoay xỏa với nhau mà thôi.

## Chuỗi sinh thành từ Dịch sang ngũ tạng
1. Từ **vô cực** chuyển sang [[Thái cực]], từ thái cực sang [[Lưỡng nghi]].
2. Có trời có đất thì muôn vật được sinh ra: sau [[01 Bát Thuần Càn|Càn]], [[02 Bát Thuần Khôn|Khôn]] thì [[03 Thủy Lôi Truân|Truân]] tiếp nối — *truân là muôn vật mới sinh*, mà đứng đầu muôn vật là con người, **vạn vật chí linh**.
3. **Trời sinh ngũ hành, ngũ hành vận động thì sinh ngũ tạng.**
4. Đầu tiên là **hào dương trong quẻ [[Khảm]] — tức mệnh môn hỏa** có trước, rồi theo thứ tự trong [[Hà Đồ]] mà **tâm, can, phế, tỳ** lần lượt sinh ra.
5. Loài người sinh ra ở **hội Dần**, ở **đốt sống thứ 14** — xem [[Tiên Thiên Bát Quái]].
6. Nhờ bẩm thụ hai khí của trời đất mà con người **sử dụng dược vật thiên về một khí để điều chỉnh âm dương trong cơ thể** nhằm chữa bệnh.

## Bài học từ quẻ Ký Tế
Quẻ [[63 Thủy Hỏa Ký Tế|Ký Tế]] có [[Ly]] bên dưới, [[Khảm]] bên trên. Cứ tưởng lửa phải ở trên, nước phải ở dưới mới đúng lẽ thường — **đâu biết rằng khi trên dưới xa cách thì bao giờ mới có sự hòa hợp**.

> **Lửa ở dưới nước mới làm nước sôi**, và vì vậy công cuộc sinh hóa mới thành. Còn nước dưới lửa trên ([[64 Hỏa Thủy Vị Tế|Vị Tế]]) thì chẳng có gì xảy ra cả.

Lấy cái cao siêu tinh diệu trong Dịch để soi sáng lý luận y học cổ truyền, vận dụng các quy luật biến dịch vào chẩn đoán và điều trị, **mới làm người thầy thuốc bớt đi được sai lầm và nâng cao hiệu quả chữa bệnh**.

## Liên quan
[[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]] · [[Lục bộ mạch trên cổ tay]] · [[Linh Quy Bát Pháp]] · [[Hà Đồ]] · [[Ngũ hành]]

""" + SRC)

w(U, 'Gieo quẻ và bấm độn', fm(['Dự đoán học', 'Lập quái', 'Hào động'],
                               ['kinh-dịch/ứng-dụng']) + """
# Gieo quẻ và bấm độn

Hào là vạch, quái do hào lập nên: **ba hào là đơn quái, sáu hào là trùng quái**. [[Bát quái]] là tám hiện tượng kỳ lạ, quái dị, biến hóa ra thiên hình vạn trạng của tự nhiên.

## 1. Phép gieo đồng tiền để lập quái
Người xưa cầm nghiêng **ba đồng tiền**, giơ hơi cao và thả xuống một cái đĩa:

| Kết quả | Ghi | Ý nghĩa |
|---|---|---|
| **1 đồng sấp** | một vạch liền | vạch dương |
| **2 đồng sấp** | một vạch đứt | vạch âm |
| **3 đồng sấp** | một vạch liền + dấu **O** | vạch dương **động** → sẽ biến thành âm |
| **3 đồng ngửa** | một vạch đứt + dấu **X** | vạch âm **động** → sẽ biến thành dương |

- **Ba lần gieo đầu** → vạch từ dưới lên được **nội quái**.
- Sau đó nghĩ về ước muốn của mình một cách thành kính rồi **gieo ba lần nữa** → được **ngoại quái**.
- Khi đọc: đọc tên **ngoại quái trước, nội quái sau**, rồi tên quẻ kép.

### Ví dụ
| Lần gieo | Kết quả | Vạch |
|---|---|---|
| 6 | 1 sấp | dương |
| 5 | 3 sấp | dương **O** (động) |
| 4 | 1 sấp | dương |
| 3 | 3 ngửa | âm **X** (động) |
| 2 | 2 sấp | âm |
| 1 | 1 sấp | dương |

Ngoại quái [[Càn]], nội quái [[Chấn]] → quẻ hiện tại là **[[25 Thiên Lôi Vô Vọng]]**. Do có 2 hào biến nên **quẻ tương lai là [[30 Bát Thuần Ly]]** — chủ về ngay chính thì tốt, nên thận trọng và tìm cho mình chỗ đứng chính đáng.

## 2. Phép bấm độn trên bàn tay
Dùng khi cần kíp và không có phương tiện, **nhưng kém ứng nghiệm hơn phép gieo tiền**.

Đặt [[Hậu Thiên Bát Quái]] lên lòng bàn tay trái, rồi:

### Tìm nội quái và ngoại quái
Ví dụ **ngày 16 tháng 7 âm lịch, giờ Dậu**:
1. Lấy vị trí quẻ [[Khôn]] ở số 7 (tương ứng tháng 7), ngày đầu của tháng là 1.
2. Đếm 1 từ quẻ Khôn tới số 16 → được quẻ [[Ly]] làm **nội quái**.
3. Từ quẻ Ly đếm giờ khởi là Tý rồi lần lượt tới giờ Dậu → được quẻ [[Khôn]] làm **ngoại quái**.
4. Vậy được quẻ kép **[[36 Địa Hỏa Minh Di]]**.

### Tìm hào động
Cộng số thứ tự của nội quái và ngoại quái, **trừ dần cho 6**; số lẻ còn lại là số thứ tự của hào động.
- Nếu trừ 6 mà hết thì hào động là **6**.
- Nếu tổng nhỏ hơn 6 thì lấy ngay số đó làm hào động.

Ở ví dụ trên: [[Ly]] = 3, [[Khôn]] = 8 → 8 + 3 = 11; 11 − 6 = **5**. Hào động là hào 5.

- **Quẻ chính**: [[36 Địa Hỏa Minh Di]] — thời hiện tại khó khăn, phải che bớt ánh sáng của mình, kiên nhẫn chờ thời, chỉ hoạt động văn tài viết lách, chớ nên hoạt động chính trị. Triệu: *"qua hà chiết kiều"*. **Quẻ xấu.**
- **Quẻ biến**: [[63 Thủy Hỏa Ký Tế]] — việc đã xong. Triệu: *"kim bảng đề danh"*. **Quẻ tốt.**

## Nguyên tắc quan trọng
> Phương pháp suy đoán dựa trên quái **chỉ có tác dụng tham khảo về xu thế** và nói về những điểm chung nhất, luôn căn dặn con người ta **giữ lấy chính đạo, trung thực, dũng cảm và biết nắm bắt thời cơ**. Tuyệt nhiên **không mang màu sắc mê tín, dị đoan**.
>
> Suy đoán về Dịch **không nên cụ thể vào một việc nào đó**. Nếu có ai suy đoán theo thần thánh mê tín thì có lẽ họ đã làm biến đổi tinh thần của Dịch, và như vậy **không còn là tinh thần của Dịch nữa**.

## Liên quan
[[Triệu]] · [[Hậu Thiên Bát Quái]] · [[Lục thập tứ quái]] · [[Quẻ]]

""" + SRC)

w(U, 'Lục bộ mạch trên cổ tay', fm(['Bộ vị mạch', 'Thốn quan xích'],
                                   ['kinh-dịch/ứng-dụng', 'y-học-cổ-truyền']) + """
# Lục bộ mạch trên cổ tay

Người xưa đã phát hiện mối liên hệ giữa **trạng thái bệnh của tạng phủ** với **trạng thái mạch ở cổ tay**. Có nhiều cách lý giải tại sao các bộ vị lại được xếp đặt như vậy.

## Bảng bộ vị
| Bộ | Tay trái | Tay phải |
|---|---|---|
| **Thốn** | Tâm – Tiểu Trường | Phế – Đại Trường |
| **Quan** | Can – Đởm | Tỳ – Vị |
| **Xích** | Thận âm – Bàng Quang | Thận dương – Mệnh môn hỏa |

## Cách lý giải thứ nhất — theo tam tiêu
Nếu giơ tay theo quy tắc Đông y:
- **Bộ thốn** trên cùng thuộc **thượng tiêu**: Tâm – Phế
- **Bộ quan** thuộc **trung tiêu**: Tỳ – Vị
- **Bộ xích** thuộc **hạ tiêu**: Can – Thận

> Cách lý giải này còn **một điều chưa rõ: can thuộc trung tiêu hay hạ tiêu?**

## Cách lý giải thứ hai — diễn dịch từ tiên đề âm dương
Lấy **tiên đề [[Âm dương]] và [[Ngũ hành]]** để diễn dịch bộ vị mạch trên cổ tay: từ tiên đề âm dương ta có thể **suy ra** vị trí các bộ vị mạch, thay vì phải chấp nhận sự xếp đặt một cách máy móc.

Đây chính là tinh thần mà [[Hà Đồ]] đem lại cho ngũ hành: giải thích được **tại sao** lại quy nạp sự vật vào ngũ hành như vậy.

## Liên quan
[[Kinh Dịch với Y lý]] · [[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]] · [[Ngũ hành]] · [[Âm dương]]

""" + SRC)

w(U, 'Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông',
  fm(['Huyền Tẫn Phát Vi', 'Mệnh môn hỏa', 'Thủy Hỏa', 'Tâm Thận'],
     ['kinh-dịch/ứng-dụng', 'y-học-cổ-truyền']) + """
# Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông

**Hải Thượng Lãn Ông Lê Hữu Trác** là người rất sâu sắc trong y lý; sự vận dụng Kinh Dịch vào y học của ông đã trở nên nhuần nhuyễn. Một trong những chương quan trọng nhất là chương học thuyết thủy hỏa mà ông gọi là **Huyền Tẫn Phát Vi** — *nói rõ bí mật của âm dương, thủy hỏa*.

## 1. Thái cực trong nhân thể
**Hai quả thận trong người họp lại thành một hình [[Thái cực|thái cực]]**: quả trái là âm thủy, quả phải là dương thủy, **mệnh môn nằm ở giữa hai quả thận**. Bên trái mệnh môn có một vòng tròn nhỏ và đen — đó là **huyệt chân thủy**; bên phải có một vòng tròn nhỏ và trắng — đó là **huyệt tướng hỏa**.

Đây chính là vận dụng **quẻ [[Khảm]]**:
- **Hai hào âm** hai bên = hai quả thận
- **Hào dương ở giữa** = thận dương, tức **mệnh môn hỏa**

Ở người: giữa **đốt sống thắt lưng 2 và 3** là huyệt Mệnh môn, đo ra hai bên 1,5 tấc là hai huyệt Thận du.

> **Dương số nhỏ nhất là 1 nên thận dương có một; âm số nhỏ nhất là 2 nên có hai quả thận.** Âm là hữu hình nên thận nhìn thấy; dương là vô hình nên mệnh môn hỏa không nhìn thấy, chỉ thấy gián tiếp qua sức nóng của cơ thể (37°C).

### Ghi chú khảo cứu
Trong *Nội Kinh* không có tên mệnh môn. **Mệnh môn xuất xứ từ Nạn 36 sách Nạn Kinh của Biển Thước** — theo Hải Thượng Lãn Ông. Nhưng trong sách *Nạn Kinh* xuất bản năm 2000 của chương trình quốc gia về Y học cổ truyền, mệnh môn lại ở **Nạn 29**, và cho rằng trong hai quả thận thì một quả là thận âm còn một quả là mệnh môn. Tác giả sách nguồn nêu ý kiến cá nhân: **vẫn tin vào Lãn Ông nhiều hơn**.

**Chử Tề Hiên**: *"Con người sinh ra, bắt đầu thụ thai ở mạch nhâm (nhâm chủ bào cung), duy có mệnh môn là có đầy đủ trước rồi sau mới thành ngũ tạng."* Điều này được chứng minh ở [[Hà Đồ]]: *thiên nhất sinh thủy, địa lục thành chi* — số 1 là số của thủy, thủy do ngũ hành vận động mà tạo nên tạng thận; thủy nằm phương bắc, nơi ở của thiên can **nhâm** và **quý**, vậy nó có tên **thiên quý** — nước của trời cho.

## 2. Chữa bệnh phải chữa vào can thận
**Rồng (mệnh môn hỏa) lặn ở đáy bể (thận cung)** — vì thận là khảm thủy, nơi ở của nó là biển.

| Loại hỏa | Vị trí | Tên gọi |
|---|---|---|
| **Quân hỏa** (có một) | Tâm, quẻ [[Ly]] phương nam | quân hỏa |
| **Tướng hỏa của thận** | Khảm thủy | **long hỏa** — lúc lặn hỏa còn non gọi là *thiếu hỏa*; khi rồng bay lên trời thì hỏa đi lên, gọi là *long hỏa, tráng hỏa* |
| **Tướng hỏa của can** | Can ở vị trí quẻ [[Chấn]] | **lôi hỏa** — tướng hỏa **dữ dội nhất** trong cơ thể |

**Khi rồng bay lên làm mưa thì kéo theo lôi hỏa là sấm chớp, vì vậy *long lôi tướng hỏa* hay đi cùng nhau.**

Theo [[Hà Đồ]], vị trí của can mộc là **giáp ất**, tâm hỏa là **bính đinh**, tỳ thổ là **mậu kỷ**, phế kim là **canh tân**, thận thủy là **nhâm quý**. **Can với thận liền nhau mà thận thủy sinh can mộc; ất quý lại cùng nguồn, long lôi hỏa hay phối hợp** — thì cớ gì khi chữa bệnh mà không chữa cả hai mà chỉ chữa vào một tạng?

## 3. Thủy hỏa ký tế
| Tạng | Quẻ | Cấu tạo | Ý nghĩa |
|---|---|---|---|
| **Tâm** | [[Ly]] | một hào âm giữa hai hào dương | Như mặt trời trên cao, là quân hỏa. **Hào âm là chân âm, là máu trong cơ thể** |
| **Thận** | [[Khảm]] | một hào dương giữa hai hào âm | **Hào dương là tướng hỏa** như hỏa trong lòng đất — mệnh môn hỏa |

**Vòng tuần hoàn sự sống:**
- Hỏa của mệnh môn chưng đốt thủy làm **thủy bốc lên bổ sung cho chân âm của tâm**.
- Lửa trên tâm cộng với khí trời **bổ sung hỏa cho mệnh môn**.
- Thận vận dụng lên trên, tâm truyền đạt xuống dưới. Hỏa của mệnh môn được bổ sung từ tâm hỏa; thủy của tâm được thận cung cấp.

> **Đó chính là năng lượng để duy trì sự sống. Nếu mệnh môn tắt thì đời người chỉ như một đống tro tàn mà thôi.**

| Trạng thái | Quẻ | Tên chứng |
|---|---|---|
| Mối quan hệ thủy hỏa **tốt** | [[63 Thủy Hỏa Ký Tế]] | **tâm thận tương giao** |
| **Thủy suy hỏa bốc** sinh bệnh | [[64 Hỏa Thủy Vị Tế]] | **tâm thận bất giao** |

## 4. Bài thuốc
| Bài | Thành phần | Ý nghĩa số |
|---|---|---|
| **Lục vị** (bổ âm) | 6 vị thuốc | **Số 6 là số của hành Thủy** trong [[Hà Đồ]] — bồi bổ chân âm mong giữ được hỏa |
| **Thận khí hoàn** (Bát vị quế phụ, bổ dương) | Lục vị + **phụ tử** + **nhục quế** | |

- **Phụ tử**: thuốc lưu thông kinh mạch, **tính chạy mà không giữ lại**; nóng, đi 12 kinh để dẫn hỏa quy nguyên.
- **Nhục quế**: giỏi nạp khí dẫn hỏa quy nguyên, **tính giữ mà không thích chạy**; thích hợp với thận dương hư mà hư hỏa thượng phù.
- **Lục vị** thuần âm, bồi bổ thận để **khống chế quế phụ**, khơi thông đường rồi mới dẫn xuống thận.

Nhục quế và phụ tử ở bài này là **quân dược** có tác dụng bổ thận; ở bài khác chỉ có tác dụng tuyên thông mà thôi.

> **Câu hỏi để ngỏ trong sách:** Hải Thượng nói Trọng Cảnh còn dùng bài Lục vị để chế ngự quế phụ mà làm bền chặt thận dương. Vậy thì **bài Lục vị là do ai tạo ra — Trương Trọng Cảnh hay Tiền Ất?**

## Liên quan
[[Kinh Dịch với Y lý]] · [[Khảm]] · [[Ly]] · [[Hà Đồ]] · [[63 Thủy Hỏa Ký Tế]] · [[64 Hỏa Thủy Vị Tế]] · [[Lục bộ mạch trên cổ tay]]

""" + SRC)

print('OK gen7')
