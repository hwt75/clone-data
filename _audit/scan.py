"""Quét máy: tìm danh từ riêng Hán-Việt trong note wiki KHÔNG xuất hiện trong
bản OCR Tesseract mới của đúng cuốn sách mà note đó dẫn nguồn.

Không xuất hiện => nghi ngờ là tàn dư EasyOCR đọc sai tên riêng.
"""
import re, os, unicodedata, json, sys

WIKI = r"D:\claude\claude-source\wiki"
OCR = r"D:\claude\_audit\ocr"
HERE = os.path.dirname(os.path.abspath(__file__))

BOOKS = {
    "Chu Dịch với Dự Đoán Học": "chudich_full.txt",
    "Tử Vi Đẩu Số — Nguyễn Mạnh Linh": "tuvi_full.txt",
    "Tìm Hiểu Nhân Tướng Học": "nhantuong_full.txt",
    "Tám chữ Hà Lạc": "tamchu_full.txt",
}


def strip_diacritics(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def norm(s):
    s = strip_diacritics(s).lower()
    return " " + re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip() + " "


hay = {}
for book, fn in BOOKS.items():
    with open(os.path.join(OCR, fn), encoding="utf-8") as f:
        hay[book] = norm(f.read())
    print(f"[haystack] {book}: {len(hay[book]):,} ký tự", file=sys.stderr)

# Từ thường bị viết hoa ở đầu câu / đầu ô bảng — không phải danh từ riêng.
STOP = set("""
kinh dich chu nguon xem theo khi neu nhung va cua cho voi trong ngoai tren duoi
mot hai ba bon nam sau bay tam chin muoi moi cac nhung nay do o la co khong duoc
chuong bai muc phan bang hinh tr trang note wiki obsidian de da dang dau tuc
nguoi nguoi ta cung con van cai su viec loai dang phai nen the vi boi tu tuy
rieng chi that rat kha hoi hop nhom cot dong hang lop buoc dau cuoi giua
an cach lam dat dua dap doan doc dinh dong ung uc it am ong di do dc
""".split())

pat_num = re.compile(r"\b\d[\d.,]{2,}\b")
tok_re = re.compile(r"[^\W\d_]+", re.UNICODE)


# Ngăn ghép chéo ô bảng / mục liệt kê: cắt dòng tại mọi dấu phân cách.
SEP = re.compile(r"[|,;:·/()\[\]{}«»\"'…—–-]|\.\s|\.$")


def candidates(line):
    """Cụm 2–3 từ liên tiếp đều viết hoa, trong cùng một đoạn của dòng."""
    out = set()
    for seg in SEP.split(line):
        caps = []
        for m in tok_re.finditer(seg):
            w = m.group()
            if not w[0].isupper() or len(w) == 1:
                caps = []
                continue
            caps.append(w)
            for n in (2, 3):
                if len(caps) >= n:
                    grp = caps[-n:]
                    if all(strip_diacritics(x).lower() not in STOP for x in grp):
                        out.add(" ".join(grp))
    return out


results = []
for root, dirs, files in os.walk(WIKI):
    if "ocr-raw" in root:
        continue
    for fn in files:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(root, fn)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        m = re.search(r"^Nguồn: \[\[(.+?)\]\]", text, re.M)
        if not m:
            continue
        book = next((b for b in BOOKS if m.group(1).startswith(b)), None)
        if not book:
            continue
        H = hay[book]

        lines = text.split("\n")
        in_fm = lines and lines[0].strip() == "---"
        names, nums = {}, {}
        for i, line in enumerate(lines, 1):
            if in_fm:
                if i > 1 and line.strip() == "---":
                    in_fm = False
                continue
            if line.startswith("Nguồn:"):
                continue
            clean = re.sub(r"\[\[.*?\]\]", " ", line)
            for c in candidates(clean):
                if norm(c) not in H:
                    names.setdefault(c, i)
            for c in pat_num.findall(clean):
                if norm(c) not in H and norm(c.replace(".", "").replace(",", "")) not in H:
                    nums.setdefault(c, i)

        if names or nums:
            results.append({
                "file": os.path.relpath(path, WIKI).replace("\\", "/"),
                "book": book,
                "names": sorted(names.items(), key=lambda x: x[1]),
                "nums": sorted(nums.items(), key=lambda x: x[1]),
            })

results.sort(key=lambda r: -(len(r["names"]) + len(r["nums"])))
with open(os.path.join(HERE, "scan.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)

tot_n = sum(len(r["names"]) for r in results)
tot_d = sum(len(r["nums"]) for r in results)
print(f"\n{len(results)} note có dấu hiệu · {tot_n} tên riêng + {tot_d} số không khớp OCR\n")
for r in results:
    print(f"── {r['file']}")
    for c, ln in r["names"]:
        print(f"     tên :{ln:<4} {c}")
    for c, ln in r["nums"]:
        print(f"     SỐ  :{ln:<4} {c}")
