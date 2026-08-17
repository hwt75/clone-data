# -*- coding: utf-8 -*-
import os
W = r'D:\claude\claude-source\wiki'
SRC = 'Nguồn: [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]]'

# name, sym, so, ten_khac, tuong, tinh, giadinh, cothe, hanh, tt_phuong, ht_phuong,
# lacthu_so, huyet, kinh, mach, cautao, banve
T = [
 ("Càn", "☰", 1, "thiên", "trời, con rồng", "mãnh liệt, cương quyết",
  "cha", "cái đầu", "dương Kim (vì tính Càn cương kiện)", "Nam", "Tây Bắc", 6,
  "Công tôn (IV-4)", "Tỳ", "Xung",
  "Càn tam liên — ba vạch liền",
  "Ba vạch dương liên tiếp là **dương đến tột cùng**, tính nó mãnh liệt, cương quyết đến tuyệt đối."),
 ("Đoài", "☱", 2, "trạch", "đầm lầy, sông, suối", "vui vẻ, hòa duyệt",
  "thiếu nữ", "mồm miệng, lúc nào cũng ướt", "âm Kim (vì tính Đoài mềm mại)", "Đông Nam", "Tây", 7,
  "Hậu khê (VI-3)", "Tiểu trường", "Đốc",
  "Đoài thượng khuyết — khuyết ở vạch trên",
  "Chỉ cần thay một vạch dương của quẻ [[Càn]] thành vạch âm ở **hào trên cùng**, quẻ Đoài đã trở nên mềm mại, tính tình vui vẻ."),
 ("Ly", "☲", 3, "hỏa", "lửa, mặt trời", "sáng, rỗng",
  "trung nữ", "quả tim và mắt", "Hỏa", "Đông", "Nam", 9,
  "Liệt khuyết (I-7)", "Phế", "Nhâm",
  "Ly trung hư — rỗng ở giữa",
  "**Bẻ gãy vạch giữa** quẻ [[Càn]] là quẻ Ly. Ly là sáng sủa, là trống rỗng; Ly là lửa có sức đốt mãnh liệt mà còn kém quẻ Càn."),
 ("Chấn", "☳", 4, "lôi", "sấm", "động",
  "trưởng nam", "thân người động ở dưới; gắn với lôi hỏa của can mộc", "dương Mộc (cây cứng rắn như đinh, lim)", "Đông Bắc", "Đông", 3,
  "Ngoại quan (X-5)", "Tam tiêu", "Dương duy",
  "Chấn ngưỡng vu — như cái chậu ngửa",
  "Một hào dương **dưới** hai hào âm thì dương không chịu, dương đi lên và phát ra tiếng nổ — nên gọi là sấm, và tính của Chấn là động."),
 ("Tốn", "☴", 5, "phong", "gió, gỗ, cây cỏ thảo mộc", "vào, nhún nhường",
  "trưởng nữ", "hai đùi", "âm Mộc (hoa, lá, cỏ mềm mại)", "Tây Nam", "Đông Nam", 4,
  "Túc lâm khấp (XI-41)", "Đởm", "Đới",
  "Tốn hạ đoạn — đứt ở vạch dưới",
  "Hai hào dương **trên** một hào âm; âm không đủ để hấp dẫn dương nên bay đi mà tạo thành gió. Là gió nên hay nhún nhường, là gió nên hay vào mọi chỗ."),
 ("Khảm", "☵", 6, "thủy", "nước, mây, mưa", "hiểm, dày đặc",
  "trung nam", "thận; hai lỗ tai", "Thủy", "Tây", "Bắc", 1,
  "Thân mạch (VII-62)", "Bàng quang", "Dương kiểu",
  "Khảm trung mãn — đầy ở giữa",
  "Là quẻ [[Khôn]] thêm một hào dương ở giữa. Tính Khảm mềm thấm xuống, cũng thuần nhưng kém Khôn. **Nhờ hào dương ở giữa mà nước còn tính ấm áp.**"),
 ("Cấn", "☶", 7, "sơn", "núi, đồi", "đậu lại, dừng lại, đỗ lại",
  "thiếu nam", "hai tay ở phía trước", "dương Thổ (vì đá cứng hơn đất)", "Tây Bắc", "Đông Bắc", 8,
  "Nội quan (IX-6)", "Tâm bào", "Âm duy",
  "Cấn phúc uyển — như cái bát úp",
  "Một hào dương **trên** hai hào âm; âm hấp dẫn dương làm hào dương ở lại, dừng lại, đỗ lại, đậu lại. Cấn chính là quẻ [[Khôn]] lấy một hào dương của [[Càn]] mà thành: hai âm tĩnh kéo một dương động mà dừng lại."),
 ("Khôn", "☷", 8, "địa", "đất, con trâu", "thuận, hòa, hiền lành",
  "mẹ", "bụng và Tỳ Vị", "âm Thổ (vì Khôn thuận hòa)", "Bắc", "Tây Nam", 2,
  "Chiếu hải (VIII-6)", "Thận", "Âm kiểu",
  "Khôn lục đoạn — sáu đoạn đứt",
  "Ba vạch thuần âm là **âm tới cùng tột**, tính quẻ Khôn là nhu nhuận, mềm mại."),
]

PURE = {"Càn": "01 Bát Thuần Càn", "Khôn": "02 Bát Thuần Khôn", "Khảm": "29 Tập Khảm",
        "Ly": "30 Bát Thuần Ly", "Chấn": "51 Bát Thuần Chấn", "Cấn": "52 Bát Thuần Cấn",
        "Tốn": "57 Bát Thuần Tốn", "Đoài": "58 Bát Thuần Đoài"}

AM_DUONG = {"Càn": "dương", "Khôn": "âm", "Tốn": "âm", "Ly": "âm", "Đoài": "âm",
            "Chấn": "dương", "Khảm": "dương", "Cấn": "dương"}

EXTRA = {
 "Khảm": """
## Ghi chú y học
Quẻ Khảm là chìa khóa của [[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]]: **hai hào âm là hai quả thận, hào dương ở giữa là thận dương — còn gọi là mệnh môn hỏa**. Dương số nhỏ nhất là 1 nên thận dương có một; âm số nhỏ nhất là 2 nên có hai quả thận. Âm hữu hình nên thận nhìn thấy; dương vô hình nên mệnh môn hỏa không nhìn thấy, chỉ thấy gián tiếp qua thân nhiệt.

Tướng hỏa của thận ở khảm thủy nên gọi là **long hỏa** — con rồng lặn dưới đáy bể.
""",
 "Chấn": """
## Ghi chú y học
Theo [[Hà Đồ]], phương đông là vị trí hành **Mộc**, cũng là vị trí của **can**. Can ứng với quẻ Chấn, và trong các tướng hỏa thì tướng hỏa của can dữ dội nhất — đó chính là **lôi hỏa**. Khi rồng bay lên làm mưa thì kéo theo lôi hỏa là sấm chớp, vì vậy **long lôi tướng hỏa** hay đi cùng nhau. Xem [[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]].
""",
 "Ly": """
## Ghi chú y học
Quẻ Ly trên cao thuộc hỏa phương nam chính là **quân hỏa**, là hỏa của **tâm**, để ứng với thận thủy ([[Khảm]]) ở phương bắc. Tạng tâm thuộc quẻ Ly: một hào âm giữa hai hào dương, **hào âm là chân âm, là máu trong cơ thể**. Xem [[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]].
""",
 "Đoài": """
## Ghi chú y học
Phương tây trong [[Hậu Thiên Bát Quái]] là nơi ở của **phế kim**.
""",
}


def note(t):
    (name, sym, so, ten_khac, tuong, tinh, giadinh, cothe, hanh,
     ttp, htp, lt, huyet, kinh, mach, cautao, banve) = t
    al = [name, 'quẻ ' + name, ten_khac.capitalize()]
    a = '\n'.join('  - "%s"' % x for x in al)
    body = """---
aliases:
%s
tags:
  - kinh-dịch/bát-quái
số: %d
---

# %s %s

> **%s** · tên khác là **%s** · quẻ số **%d** trong [[Bát quái]]

| Thuộc tính | |
|---|---|
| Ký hiệu | %s |
| Cấu tạo | %s |
| Tượng | %s |
| Tính | %s |
| Vai trong [[Thuyết Lục Tử]] | **%s** |
| Trong cơ thể | %s |
| Quẻ âm hay dương | **%s** |
| [[Ngũ hành]] | %s |
| Phương [[Tiên Thiên Bát Quái|tiên thiên]] | %s |
| Phương [[Hậu Thiên Bát Quái|hậu thiên]] | %s |
| Số [[Lạc Thư]] | %d |

## Bàn về tính quẻ
%s
%s
## Trong [[Linh Quy Bát Pháp]]
Ứng với số **%d**, huyệt khóa **%s**, thuộc kinh **%s**, thông với **mạch %s**.

## Quẻ kép thuần
[[%s]] — cả nội quái và ngoại quái đều là %s.

## Liên quan
[[Bát quái]] · [[Thuyết Lục Tử]] · [[Tiên Thiên Bát Quái]] · [[Hậu Thiên Bát Quái]] · [[Quẻ]]

%s
""" % (a, so, sym, name, tuong.split(',')[0].strip().capitalize(), ten_khac, so,
       sym, cautao, tuong, tinh, giadinh, cothe, AM_DUONG[name], hanh, ttp, htp, lt,
       banve, EXTRA.get(name, ''),
       lt, huyet, kinh, mach, PURE[name], name, SRC)
    open(os.path.join(W, 'Bát quái', name + '.md'), 'w', encoding='utf-8').write(body.lstrip())


for t in T:
    note(t)
print('OK gen6 —', len(T), 'quẻ đơn')
