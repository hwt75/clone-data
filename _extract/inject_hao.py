# -*- coding: utf-8 -*-
"""Chèn hào từ (Ngô Tất Tố) vào 64 note quẻ trong wiki."""
import os, re, json
from hex_lib import NAMES, fname

W = r'D:\claude\claude-source\wiki'
D = json.load(open('hao_tu.json', encoding='utf-8'))

# cấu tạo quẻ đơn, đọc từ dưới lên: 1 = dương, 0 = âm
TRI = {'Càn': (1, 1, 1), 'Đoài': (1, 1, 0), 'Ly': (1, 0, 1), 'Chấn': (1, 0, 0),
       'Tốn': (0, 1, 1), 'Khảm': (0, 1, 0), 'Cấn': (0, 0, 1), 'Khôn': (0, 0, 0)}
THU = {1: 'Sơ', 2: 'Nhị', 3: 'Tam', 4: 'Tứ', 5: 'Ngũ', 6: 'Thượng'}

# Vá: quẻ 1 hào 4 — bản ebook trộn lẫn lời hào với đoạn Văn Ngôn ở sau
# ('…hà dị dã? Tử viết…'). Lấy đúng lời hào, khớp với Tượng truyện cùng trang.
PATCH = {(1, 4): ('Hoặc dược tại uyên, vô cữu', 'Hoặc nhảy ở vực, không lỗi')}


def hao_name(n, ngoi):
    """tên hào suy từ cấu tạo quẻ, không tin nhãn của bản số hoá"""
    _, ngoai, noi = NAMES[n]
    bits = TRI[noi] + TRI[ngoai]          # dưới lên trên
    duong = bits[ngoi - 1] == 1
    if ngoi == 1:
        return ('Sơ Cửu' if duong else 'Sơ Lục'), duong
    if ngoi == 6:
        return ('Thượng Cửu' if duong else 'Thượng Lục'), duong
    return ('%s %s' % ('Cửu' if duong else 'Lục', THU[ngoi])), duong


SEC = """## Hào từ

> Sáu hào đọc **từ dưới lên**; bảng dưới xếp từ hào trên cùng xuống để khớp với hình quẻ.
> Bản dịch của [[Kinh Dịch Trọn Bộ — Ngô Tất Tố]] cố ý giữ lối văn cổ — xem [[Từ cổ trong bản dịch Ngô Tất Tố]].

| | Ngôi | Hào | Lời hào (Hán–Việt) | Dịch nghĩa |
|---|---:|---|---|---|
%s
"""

sai_ten, done = [], 0
for n in range(1, 65):
    p = os.path.join(W, '64 quẻ', fname(n) + '.md')
    txt = open(p, encoding='utf-8').read()
    haos = D[str(n)]['haos']
    rows = []
    for ngoi in range(6, 0, -1):
        h = haos.get(str(ngoi))
        if not h:
            continue
        ten, duong = hao_name(n, ngoi)
        if h['ten'] and h['ten'] != ten:
            sai_ten.append((n, ngoi, h['ten'], ten))
        am, nghia = h['am'], h['nghia']
        if (n, ngoi) in PATCH:
            am, nghia = PATCH[(n, ngoi)]
        glyph = '⚊' if duong else '⚋'
        rows.append('| %s | %d | **%s** | %s | %s |' % (glyph, ngoi, ten, am, nghia))
    # Dụng Cửu / Dụng Lục (chỉ quẻ 1 và 2)
    if '7' in haos:
        h = haos['7']
        ten = 'Dụng Cửu' if n == 1 else 'Dụng Lục'
        rows.append('| | — | **%s** | %s | %s |' % (ten, h['am'], h['nghia']))
    sec = SEC % '\n'.join(rows)

    if '## Hào từ' in txt:                       # chạy lại thì thay thế
        txt = re.sub(r'## Hào từ\n.*?(?=\n## Triệu)', sec.rstrip() + '\n', txt, flags=re.S)
    else:
        txt = txt.replace('## Triệu', sec + '\n## Triệu', 1)
    open(p, 'w', encoding='utf-8').write(txt)
    done += 1

print('Đã chèn hào từ vào %d note quẻ' % done)
print('Nhãn tên hào trong ebook lệch với cấu tạo quẻ: %d' % len(sai_ten))
for r in sai_ten:
    print('   quẻ %-2d ngôi %d: ebook ghi %-12s -> đúng phải là %s' % r)
