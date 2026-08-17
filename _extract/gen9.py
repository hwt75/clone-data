# -*- coding: utf-8 -*-
import os, re
from hex_lib import NAMES, SYM, fname, short

W = r'D:\claude\claude-source\wiki'

rows = []
for n in range(1, 65):
    p = os.path.join(W, '64 quẻ', fname(n) + '.md')
    txt = open(p, encoding='utf-8').read()
    dg = re.search(r'^đánh-giá: (.+)$', txt, re.M).group(1)
    name, ngoai, noi = NAMES[n]
    rows.append((n, name, ngoai, noi, dg))


def table(sub):
    out = ['| # | Quẻ | Trên | Dưới | Đánh giá |', '|---:|---|---|---|---|']
    for n, name, ng, no, dg in sub:
        out.append('| %s | [[%s\\|%s]] | %s %s | %s %s | %s |'
                   % (chr(0x4DC0 + n - 1) + ' ' + str(n), fname(n), name,
                      SYM[ng], ng, SYM[no], no, dg))
    return '\n'.join(out)


index = """---
aliases:
  - "Kinh Dịch MOC"
  - "Bản đồ nội dung"
tags:
  - moc
  - kinh-dịch
---

# 📖 Kinh Dịch — Bản đồ nội dung

Wiki hệ thống hóa từ [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] (NXB Y học, 2006).
Tình trạng số hóa các tệp gốc: [[Trạng thái số hóa nguồn thô]].

---

## 🌱 Bắt đầu từ đâu
1. [[Kinh Dịch]] — Dịch là gì, học Dịch để làm gì
2. [[Ba nghĩa của chữ Dịch]] — Bất Dịch, Giao Dịch, Biến Dịch
3. [[Thái cực]] → [[Lưỡng nghi]] → [[Tứ tượng]] → [[Bát quái]] → [[Lục thập tứ quái]]
4. [[Hào]] và [[Ngôi hào — trung, chính, ứng, thời]] — bộ ngữ pháp để đọc mọi quẻ
5. [[Triệu]] — cách đọc lời chiêm mà không rơi vào mê tín

---

## 🧭 Khái niệm nền tảng

### Tổng quan và lịch sử
[[Kinh Dịch]] · [[Ba nghĩa của chữ Dịch]] · [[Nguồn gốc và năm tác giả Kinh Dịch]] · [[Ba loại Dịch]] · [[Thập Dực]] · [[Bố cục Kinh Dịch]] · [[Quan điểm Nho gia về Kinh Dịch]] · [[Kinh Dịch trong văn minh phương Đông]]

### Vũ trụ luận
[[Thái cực]] · [[Lưỡng nghi]] · [[Tứ tượng]] · [[Âm dương]] · [[Ngũ hành]]

### Ngữ pháp của quẻ
[[Hào]] · [[Quẻ]] · [[Ngôi hào — trung, chính, ứng, thời]] · [[Lục thập tứ quái]] · [[Triệu]]

### Đồ hình
[[Hà Đồ]] · [[Lạc Thư]] · [[Cửu Trù Hồng Phạm]] · [[Tiên Thiên Bát Quái]] · [[Hậu Thiên Bát Quái]] · [[Thuyết Lục Tử]]

---

## ☯ Bát quái — tám quẻ đơn

| Số | Quẻ | Tượng | Tính | Gia đình | Ngũ hành | Cơ thể |
|---|---|---|---|---|---|---|
| 1 | ☰ [[Càn]] | trời, con rồng | mãnh liệt, cương quyết | cha | dương Kim | đầu |
| 2 | ☱ [[Đoài]] | đầm, sông, suối | vui vẻ, hòa duyệt | thiếu nữ | âm Kim | mồm miệng |
| 3 | ☲ [[Ly]] | lửa, mặt trời | sáng, rỗng | trung nữ | Hỏa | tim, mắt |
| 4 | ☳ [[Chấn]] | sấm | động | trưởng nam | dương Mộc | thân động ở dưới |
| 5 | ☴ [[Tốn]] | gió, gỗ, cây cỏ | vào, nhún nhường | trưởng nữ | âm Mộc | hai đùi |
| 6 | ☵ [[Khảm]] | nước, mây, mưa | hiểm, dày đặc | trung nam | Thủy | thận, hai tai |
| 7 | ☶ [[Cấn]] | núi, đồi | đậu lại, dừng lại | thiếu nam | dương Thổ | hai tay |
| 8 | ☷ [[Khôn]] | đất, con trâu | thuận, hòa, hiền lành | mẹ | âm Thổ | bụng, tỳ vị |

---

## ䷀ 64 quẻ

### [[Chu Dịch Thượng Kinh]] — quẻ 1–30 (thiên lý)

%s

### [[Chu Dịch Hạ Kinh]] — quẻ 31–64 (nhân sự)

%s

---

## 🩺 Ứng dụng

[[Kinh Dịch với Y lý]] — *bất tri Dịch, bất khả tri Y*
[[Gieo quẻ và bấm độn]] — phép gieo ba đồng tiền, phép độn trên bàn tay, tìm hào động
[[Lục bộ mạch trên cổ tay]] — thốn, quan, xích
[[Học thuyết Thủy Hỏa của Hải Thượng Lãn Ông]] — mệnh môn hỏa, tâm thận tương giao, Lục vị và Bát vị
[[Linh Quy Bát Pháp]] — tính giờ mở huyệt trong châm cứu

---

## 📚 Nguồn

[[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] · [[Trạng thái số hóa nguồn thô]]

---

## 🔖 Quy ước trong wiki này

- Mỗi quẻ có frontmatter `số`, `ngoại-quái`, `nội-quái`, `đánh-giá` → dùng được với Dataview.
- Tag phân tầng: `#kinh-dịch/khái-niệm`, `#kinh-dịch/bát-quái`, `#kinh-dịch/quẻ`, `#kinh-dịch/đồ-hình`, `#kinh-dịch/ứng-dụng`, `#kinh-dịch/lịch-sử`, `#y-học-cổ-truyền`, `#nguồn`.
- Tên tệp quẻ có số thứ tự để giữ đúng thứ tự Văn Vương; alias cho phép viết `[[Thủy Lôi Truân]]` là link được.
- Trích dẫn nguyên văn từ sách để trong `>` hoặc *in nghiêng*; phần diễn giải là văn xuôi thường.

> [!note] Về tính chất của tri thức này
> Sách nguồn nhấn mạnh nhiều lần rằng **Kinh Dịch tuyệt nhiên không mê tín**; phần [[Triệu|triệu / lời chiêm]] chỉ mang tính tham khảo về xu thế. Các nội dung y học ở đây là **ghi chép hệ thống hóa lý luận y học cổ truyền**, không phải hướng dẫn chẩn đoán hay điều trị.
""" % (table(rows[:30]), table(rows[30:]))

open(os.path.join(W, 'Kinh Dịch — Bản đồ nội dung.md'), 'w', encoding='utf-8').write(index)
print('OK index')
