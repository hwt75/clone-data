"""Tìm cụm từ trong OCR, bỏ qua khác biệt dấu phụ và ngắt dòng.

    python find.py <book> "cụm từ" ["cụm từ 2" ...]
    book: chudich | tuvi | nhantuong | tamchu
"""
import re, sys, os, unicodedata

OCR = r"D:\claude\_audit\ocr"


def sd(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


book = sys.argv[1]
path = os.path.join(OCR, f"{book}_full.txt")
raw = open(path, encoding="utf-8").read()
lines = raw.split("\n")

# haystack chuẩn hoá + bản đồ vị-trí-ký-tự → chỉ-số-dòng
buf, lineno = [], []
for i, ln in enumerate(lines):
    t = re.sub(r"[^a-z0-9]+", " ", sd(ln).lower()).strip()
    if t:
        buf.append(t)
        lineno.extend([i] * (len(t) + 1))
hay = " ".join(buf) + " "
lineno.append(len(lines) - 1)

# mốc trang
page_at = {}
for i, ln in enumerate(lines):
    m = re.match(r"=== trang PDF (\d+) ===", ln)
    if m:
        page_at[i] = int(m.group(1))
pages = sorted(page_at)


def page_of(i):
    p = None
    for k in pages:
        if k <= i:
            p = page_at[k]
        else:
            break
    return p


for q in sys.argv[2:]:
    n = " " + re.sub(r"[^a-z0-9]+", " ", sd(q).lower()).strip() + " "
    hits, start = [], 0
    while True:
        j = hay.find(n.strip(), start)
        if j < 0:
            break
        hits.append(j)
        start = j + 1
        if len(hits) >= 8:
            break
    print(f"\n##### {q!r} — {len(hits)} kết quả" + (" (>=8, cắt bớt)" if len(hits) >= 8 else ""))
    if not hits:
        print("   KHÔNG CÓ trong OCR")
    for j in hits:
        i = lineno[min(j, len(lineno) - 1)]
        print(f"   [tr.PDF {page_of(i)} | dòng {i+1}] "
              + " ⏎ ".join(x.strip() for x in lines[max(0, i - 1):i + 2] if x.strip())[:260])
