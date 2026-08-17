"""Dò trang in bị thiếu trong bản scan: so số trang in đọc được ở chân trang
với số trang PDF. Chỗ nào hai trang PDF liền nhau mà số in nhảy > 1 là mất trang."""
import re, sys

book = sys.argv[1] if len(sys.argv) > 1 else "tamchu"
lines = open(rf"D:\claude\_audit\ocr\{book}_full.txt", encoding="utf-8").read().split("\n")

pdf, seen = 0, {}
for l in lines:
    m = re.match(r"=== trang PDF (\d+) ===", l)
    if m:
        pdf = int(m.group(1))
        continue
    s = l.strip()
    if re.fullmatch(r"\d{1,3}", s):
        seen[pdf] = int(s)          # số cuối cùng đứng một mình = số trang in

ks = sorted(seen)
print(f"[{book}] đọc được số trang in ở {len(ks)}/{max(ks) if ks else 0} trang PDF\n")
gaps = []
for a, b in zip(ks, ks[1:]):
    if b - a != 1:
        continue                     # bỏ qua chỗ không đọc được số
    d = seen[b] - seen[a]
    if d != 1:
        gaps.append((a, seen[a], b, seen[b], d))

if not gaps:
    print("Không thấy chỗ nào mất trang.")
for a, va, b, vb, d in gaps:
    if d > 1:
        print(f"MẤT {d-1} trang in: PDF {a} (in {va})  →  PDF {b} (in {vb})"
              f"   ⇒ thiếu trang in {va+1}..{vb-1}")
    else:
        print(f"LỆCH ngược: PDF {a} (in {va}) → PDF {b} (in {vb})")
