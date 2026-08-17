# -*- coding: utf-8 -*-
import os
W = r'D:\claude\claude-source\wiki'
SRC = 'Nguồn: [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]]'

NAMES = {
 1: ("Bát Thuần Càn", "Càn", "Càn"), 2: ("Bát Thuần Khôn", "Khôn", "Khôn"),
 3: ("Thủy Lôi Truân", "Khảm", "Chấn"), 4: ("Sơn Thủy Mông", "Cấn", "Khảm"),
 5: ("Thủy Thiên Nhu", "Khảm", "Càn"), 6: ("Thiên Thủy Tụng", "Càn", "Khảm"),
 7: ("Địa Thủy Sư", "Khôn", "Khảm"), 8: ("Thủy Địa Tỷ", "Khảm", "Khôn"),
 9: ("Phong Thiên Tiểu Súc", "Tốn", "Càn"), 10: ("Thiên Trạch Lý", "Càn", "Đoài"),
 11: ("Địa Thiên Thái", "Khôn", "Càn"), 12: ("Thiên Địa Bĩ", "Càn", "Khôn"),
 13: ("Thiên Hỏa Đồng Nhân", "Càn", "Ly"), 14: ("Hỏa Thiên Đại Hữu", "Ly", "Càn"),
 15: ("Địa Sơn Khiêm", "Khôn", "Cấn"), 16: ("Lôi Địa Dự", "Chấn", "Khôn"),
 17: ("Trạch Lôi Tùy", "Đoài", "Chấn"), 18: ("Sơn Phong Cổ", "Cấn", "Tốn"),
 19: ("Địa Trạch Lâm", "Khôn", "Đoài"), 20: ("Phong Địa Quán", "Tốn", "Khôn"),
 21: ("Hỏa Lôi Phệ Hạp", "Ly", "Chấn"), 22: ("Sơn Hỏa Bí", "Cấn", "Ly"),
 23: ("Sơn Địa Bác", "Cấn", "Khôn"), 24: ("Địa Lôi Phục", "Khôn", "Chấn"),
 25: ("Thiên Lôi Vô Vọng", "Càn", "Chấn"), 26: ("Sơn Thiên Đại Súc", "Cấn", "Càn"),
 27: ("Sơn Lôi Di", "Cấn", "Chấn"), 28: ("Trạch Phong Đại Quá", "Đoài", "Tốn"),
 29: ("Tập Khảm", "Khảm", "Khảm"), 30: ("Bát Thuần Ly", "Ly", "Ly"),
 31: ("Trạch Sơn Hàm", "Đoài", "Cấn"), 32: ("Lôi Phong Hằng", "Chấn", "Tốn"),
 33: ("Thiên Sơn Độn", "Càn", "Cấn"), 34: ("Lôi Thiên Đại Tráng", "Chấn", "Càn"),
 35: ("Hỏa Địa Tấn", "Ly", "Khôn"), 36: ("Địa Hỏa Minh Di", "Khôn", "Ly"),
 37: ("Phong Hỏa Gia Nhân", "Tốn", "Ly"), 38: ("Hỏa Trạch Khuê", "Ly", "Đoài"),
 39: ("Thủy Sơn Kiển", "Khảm", "Cấn"), 40: ("Lôi Thủy Giải", "Chấn", "Khảm"),
 41: ("Sơn Trạch Tổn", "Cấn", "Đoài"), 42: ("Phong Lôi Ích", "Tốn", "Chấn"),
 43: ("Trạch Thiên Quải", "Đoài", "Càn"), 44: ("Thiên Phong Cấu", "Càn", "Tốn"),
 45: ("Trạch Địa Tụy", "Đoài", "Khôn"), 46: ("Địa Phong Thăng", "Khôn", "Tốn"),
 47: ("Trạch Thủy Khốn", "Đoài", "Khảm"), 48: ("Thủy Phong Tỉnh", "Khảm", "Tốn"),
 49: ("Trạch Hỏa Cách", "Đoài", "Ly"), 50: ("Hỏa Phong Đỉnh", "Ly", "Tốn"),
 51: ("Bát Thuần Chấn", "Chấn", "Chấn"), 52: ("Bát Thuần Cấn", "Cấn", "Cấn"),
 53: ("Phong Sơn Tiệm", "Tốn", "Cấn"), 54: ("Lôi Trạch Quy Muội", "Chấn", "Đoài"),
 55: ("Lôi Hỏa Phong", "Chấn", "Ly"), 56: ("Hỏa Sơn Lữ", "Ly", "Cấn"),
 57: ("Bát Thuần Tốn", "Tốn", "Tốn"), 58: ("Bát Thuần Đoài", "Đoài", "Đoài"),
 59: ("Phong Thủy Hoán", "Tốn", "Khảm"), 60: ("Thủy Trạch Tiết", "Khảm", "Đoài"),
 61: ("Phong Trạch Trung Phu", "Tốn", "Đoài"), 62: ("Lôi Sơn Tiểu Quá", "Chấn", "Cấn"),
 63: ("Thủy Hỏa Ký Tế", "Khảm", "Ly"), 64: ("Hỏa Thủy Vị Tế", "Ly", "Khảm"),
}

SYM = {"Càn": "☰", "Đoài": "☱", "Ly": "☲", "Chấn": "☳",
       "Tốn": "☴", "Khảm": "☵", "Cấn": "☶", "Khôn": "☷"}


def fname(n):
    return "%02d %s" % (n, NAMES[n][0])


def link(n):
    return "[[%s]]" % fname(n)


def short(n):
    """tên rút gọn của quẻ (chữ cuối cùng / tên riêng)"""
    full = NAMES[n][0]
    if full.startswith("Bát Thuần"):
        return full.replace("Bát Thuần ", "")
    if full == "Tập Khảm":
        return "Khảm"
    parts = full.split()
    return " ".join(parts[2:]) if len(parts) > 2 else parts[-1]


def write(n, thoan, dich, noi_tiep, giang, trieu, trieu_nghia, chu_su, danh_gia, lienquan=""):
    name, ngoai, noi = NAMES[n]
    hexchar = chr(0x4DC0 + n - 1)
    kinh = "[[Chu Dịch Thượng Kinh]]" if n <= 30 else "[[Chu Dịch Hạ Kinh]]"
    prev = ("← %s" % link(n - 1)) if n > 1 else "← *(mở đầu)*"
    nxt = ("%s →" % link(n + 1)) if n < 64 else "*(quay lại đầu vòng: %s)* →" % link(1)
    aliases = [name]
    s = short(n)
    if s != name:
        aliases.append("quẻ " + s)
    a = "\n".join('  - "%s"' % x for x in aliases)

    body = """---
aliases:
%s
tags:
  - kinh-dịch/quẻ
số: %d
ngoại-quái: %s
nội-quái: %s
đánh-giá: %s
---

# %s %d. %s

> **Ngoại quái** %s [[%s]] (trên) — **Nội quái** %s [[%s]] (dưới) · thuộc %s
> %s &nbsp;&nbsp;|&nbsp;&nbsp; %s

## Lý do tiếp nối
%s

## Thoán từ
> %s

**Dịch nghĩa:** %s

## Giảng
%s

## Triệu
> **%s** — *%s*

**Chủ về sự:** %s

**Đánh giá:** %s

## Liên quan
%s[[Lục thập tứ quái]] · [[Ngôi hào — trung, chính, ứng, thời]] · [[Triệu]]

%s
""" % (a, n, ngoai, noi, danh_gia,
       hexchar, n, name,
       SYM[ngoai], ngoai, SYM[noi], noi, kinh,
       prev, nxt,
       noi_tiep.strip(), thoan.strip(), dich.strip(), giang.strip(),
       trieu, trieu_nghia, chu_su, danh_gia,
       (lienquan.strip() + " · ") if lienquan.strip() else "",
       SRC)
    open(os.path.join(W, '64 quẻ', fname(n) + '.md'), 'w', encoding='utf-8').write(body.lstrip())
