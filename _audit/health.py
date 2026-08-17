"""Kiểm tra sức khỏe vault: wikilink gãy, frontmatter thiếu, note mồ côi,
trùng tên, tệp lạc ngoài wiki, thư mục rỗng."""
import re, os, collections

ROOT = r"D:\claude\claude-source"
WIKI = os.path.join(ROOT, "wiki")

notes = {}          # tên tệp (không .md) -> đường dẫn tương đối
aliases = {}        # bí danh -> tên tệp
no_fm, no_h1 = [], []
# Trong bảng Obsidian dấu ống được escape thành "\|" — phải cắt cả dấu "\" cuối.
link_re = re.compile(r"\[\[([^\]|#]+?)\\?(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")

for root, dirs, files in os.walk(WIKI):
    if "ocr-raw" in root:
        dirs[:] = []
        continue
    for fn in files:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(root, fn)
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        stem = fn[:-3]
        notes.setdefault(stem, []).append(rel)
        text = open(path, encoding="utf-8").read()
        if not text.startswith("---\n"):
            no_fm.append(rel)
        else:
            fm = text.split("---\n", 2)[1]
            if "aliases" not in fm or "tags" not in fm:
                no_fm.append(rel + "  (thiếu aliases/tags)")
            for a in re.findall(r'^\s*-\s*"?([^"\n]+?)"?\s*$', fm, re.M):
                aliases[a.strip()] = stem
        if not re.search(r"^# ", text, re.M):
            no_h1.append(rel)

known = set(notes) | set(aliases)
broken = collections.defaultdict(list)
linked_to = set()

for root, dirs, files in os.walk(WIKI):
    if "ocr-raw" in root:
        dirs[:] = []
        continue
    for fn in files:
        if not fn.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(root, fn), ROOT).replace("\\", "/")
        for i, line in enumerate(open(os.path.join(root, fn), encoding="utf-8"), 1):
            for t in link_re.findall(line):
                t = t.strip()
                if t in known:
                    linked_to.add(aliases.get(t, t))
                else:
                    broken[t].append(f"{rel}:{i}")

print("=" * 70)
print(f"{sum(len(v) for v in notes.values())} note  ·  {len(known)} tên gọi (kể cả bí danh)")
print("=" * 70)

print(f"\n■ WIKILINK GÃY: {len(broken)} đích, {sum(len(v) for v in broken.values())} lần dùng")
for t, locs in sorted(broken.items(), key=lambda x: -len(x[1])):
    print(f"   [[{t}]]  ×{len(locs)}   vd: {locs[0]}")

print(f"\n■ THIẾU FRONTMATTER (không lọt vào _Index): {len(no_fm)}")
for r in no_fm:
    print(f"   {r}")

print(f"\n■ THIẾU H1: {len(no_h1)}")
for r in no_h1:
    print(f"   {r}")

dups = {k: v for k, v in notes.items() if len(v) > 1}
print(f"\n■ TRÙNG TÊN NOTE: {len(dups)}")
for k, v in dups.items():
    print(f"   {k}: {v}")

orphans = sorted(set(notes) - linked_to)
print(f"\n■ MỒ CÔI (không note nào trỏ tới): {len(orphans)}")
for o in orphans:
    print(f"   {notes[o][0]}")

print("\n■ TỆP .md NẰM NGOÀI wiki/ (trong claude-source):")
for fn in os.listdir(ROOT):
    if fn.endswith(".md"):
        print(f"   {fn}")

print("\n■ THƯ MỤC RỖNG trong wiki/:")
for root, dirs, files in os.walk(WIKI):
    if "ocr-raw" in root:
        dirs[:] = []
        continue
    if not dirs and not files:
        print(f"   {os.path.relpath(root, ROOT)}")
