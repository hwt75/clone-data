"""Tìm cặp danh từ riêng trong vault chỉ khác nhau 1 ký tự — dấu hiệu lỗi gõ/OCR.
Ưu tiên cặp lệch nhiều về tần suất (một dạng dùng 20 lần, dạng kia 1 lần)."""
import re, os, unicodedata, collections, itertools

WIKI = r"D:\claude\claude-source\wiki"
tok_re = re.compile(r"[^\W\d_]+", re.UNICODE)
SEP = re.compile(r"[|,;:·/()\[\]{}«»\"'…—–-]|\.\s|\.$")

STOP = set("""kinh dich chu nguon xem theo khi neu nhung va cua cho voi trong ngoai tren duoi
mot hai ba bon nam sau bay tam chin muoi moi cac nhung nay do o la co khong duoc
chuong bai muc phan bang hinh tr trang de da dang dau tuc nguoi cung con van cai su
viec loai phai nen the vi boi tu tuy rieng chi that rat kha hoi hop nhom cot dong
hang lop buoc cuoi giua an cach lam dat dua dap doan doc dinh ung uc it am ong di""".split())


def sd(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


freq = collections.Counter()
where = collections.defaultdict(set)

for root, dirs, files in os.walk(WIKI):
    if "ocr-raw" in root:
        continue
    for fn in files:
        if not fn.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(root, fn), WIKI).replace("\\", "/")
        for i, line in enumerate(open(os.path.join(root, fn), encoding="utf-8"), 1):
            for seg in SEP.split(re.sub(r"\[\[.*?\|", "", line)):
                caps = []
                for m in tok_re.finditer(seg):
                    w = m.group()
                    if not w[0].isupper() or len(w) == 1:
                        caps = []
                        continue
                    caps.append(w)
                    if len(caps) >= 2:
                        g = " ".join(caps[-2:])
                        if all(sd(x).lower() not in STOP for x in caps[-2:]):
                            freq[g] += 1
                            where[g].add(f"{rel}:{i}")


def dist1(a, b):
    """True nếu a,b khác nhau đúng 1 phép sửa ký tự."""
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    if len(a) > len(b):
        a, b = b, a
    for i in range(len(b)):
        if b[:i] + b[i + 1:] == a:
            return True
    return False


keys = sorted(freq)
buckets = collections.defaultdict(list)
for k in keys:
    buckets[len(k)].append(k)

pairs = []
for L in buckets:
    for a, b in itertools.combinations(buckets[L], 2):
        if dist1(a, b):
            pairs.append((a, b))
    for a in buckets[L]:
        for b in buckets.get(L + 1, []):
            if dist1(a, b):
                pairs.append((a, b))

pairs.sort(key=lambda p: -abs(freq[p[0]] - freq[p[1]]))
print(f"{len(pairs)} cặp lệch 1 ký tự\n")
for a, b in pairs:
    fa, fb = freq[a], freq[b]
    rare, common = (a, b) if fa < fb else (b, a)
    print(f"{common!r} ×{freq[common]}   vs   {rare!r} ×{freq[rare]}")
    for loc in sorted(where[rare])[:3]:
        print(f"      {loc}")
