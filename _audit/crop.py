"""Cắt trang PDF ra ảnh để đọc trực tiếp.

    python crop.py <book> <trang_pdf> [số_lát]

book: chudich | tamchu | nhantuong | tuvi
Mặc định cắt 2 lát (trên/dưới), chồng mép 4% để không mất dòng giáp ranh.
Ảnh ghi ra D:\\claude\\_audit\\crops\\<book>_p<NNNN>_<i>.png
"""
import fitz, os, sys

SRC = r"D:\claude\claude-source\nguồn thô"
OUT = r"D:\claude\_audit\crops"
PREFIX = {"chudich": "Chu d", "tamchu": "kinhdich-",
          "nhantuong": "TÌM HIỂU", "tuvi": "TỬ VI"}

book, page = sys.argv[1], int(sys.argv[2])
slices = int(sys.argv[3]) if len(sys.argv) > 3 else 2

pdf = next(f for f in os.listdir(SRC) if f.startswith(PREFIX[book]))
doc = fitz.open(os.path.join(SRC, pdf))
p = doc[page - 1]
r = p.rect
os.makedirs(OUT, exist_ok=True)

for i in range(slices):
    top = max(0.0, i / slices - 0.02)
    bot = min(1.0, (i + 1) / slices + 0.02)
    clip = fitz.Rect(0, r.height * top, r.width, r.height * bot)
    path = os.path.join(OUT, f"{book}_p{page:04d}_{i+1}.png")
    p.get_pixmap(dpi=300, colorspace=fitz.csGRAY, clip=clip).save(path)
    print(path)
