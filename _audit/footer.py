"""Cắt dải chân trang (và đầu trang) của nhiều trang PDF, xếp chồng vào MỘT ảnh
để đọc số trang in bằng một lần Read.

    python footer.py <book> <trang1> <trang2> ...

Ghi ra D:\\claude\\_audit\\crops\\<book>_footers.png
Dùng để xác nhận các ca nghi mất trang do missing_pages.py báo.
"""
import fitz, os, sys

SRC = r"D:\claude\claude-source\nguồn thô"
OUT = r"D:\claude\_audit\crops"
PREFIX = {"chudich": "Chu d", "tamchu": "kinhdich-",
          "nhantuong": "TÌM HIỂU", "tuvi": "TỬ VI"}
BAND = 0.11          # 11% chiều cao ở mỗi mép

book = sys.argv[1]
pages = [int(a) for a in sys.argv[2:]]

pdf = next(f for f in os.listdir(SRC) if f.startswith(PREFIX[book]))
doc = fitz.open(os.path.join(SRC, pdf))
os.makedirs(OUT, exist_ok=True)

strips = []
for pno in pages:
    p = doc[pno - 1]
    r = p.rect
    for tag, clip in (("dau", fitz.Rect(0, 0, r.width, r.height * BAND)),
                      ("chan", fitz.Rect(0, r.height * (1 - BAND), r.width, r.height))):
        pix = p.get_pixmap(dpi=400, colorspace=fitz.csGRAY, clip=clip)
        strips.append((f"{book} PDF {pno} [{tag}]", pix))

# xếp chồng: tự dựng pixmap trắng rồi dán từng dải
gap = 30
W = max(pix.width for _, pix in strips)
H = sum(pix.height for _, pix in strips) + gap * len(strips)
canvas = fitz.Pixmap(fitz.csGRAY, fitz.IRect(0, 0, W, H), False)
canvas.clear_with(255)

y = 0
for label, pix in strips:
    pix.set_origin(0, y)
    canvas.copy(pix, pix.irect)
    y += pix.height + gap
    print(f"y={y - pix.height - gap:6d}  {label}")

path = os.path.join(OUT, f"{book}_footers.png")
canvas.save(path)
print("->", path, f"({W}x{H})")
