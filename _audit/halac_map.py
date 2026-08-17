"""Dò tiêu đề 64 quẻ trong Phần hai 'Tám chữ Hà Lạc' và lập bản đồ quẻ → trang PDF."""
import re

LINES = open(r"D:\claude\_audit\ocr\tamchu_full.txt", encoding="utf-8").read().split("\n")

head_re = re.compile(r"^\s*(\d{1,2})\s*[-–—.]\s*(.{4,45}?)\s*$")

page, hits = 0, []
for ln in LINES:
    m = re.match(r"=== trang PDF (\d+) ===", ln)
    if m:
        page = int(m.group(1))
        continue
    if not (70 < page < 425):
        continue
    m = head_re.match(ln)
    if not m:
        continue
    n, title = int(m.group(1)), m.group(2)
    letters = [c for c in title if c.isalpha()]
    if not (1 <= n <= 64) or len(letters) < 4:
        continue
    # tiêu đề in HOA: đại đa số chữ cái là chữ hoa
    if sum(c.isupper() for c in letters) / len(letters) < 0.8:
        continue
    hits.append((n, page, title))

print(f"{len(hits)} dòng ứng viên\n")
seen = {}
for n, p, t in hits:
    seen.setdefault(n, (p, t))
for n in range(1, 65):
    if n in seen:
        p, t = seen[n]
        print(f"{n:>3}  tr.PDF {p:>3}   {t}")
    else:
        print(f"{n:>3}  --- KHÔNG DÒ ĐƯỢC ---")
