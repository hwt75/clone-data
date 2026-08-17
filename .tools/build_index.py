# -*- coding: utf-8 -*-
"""Sinh wiki/_Index.md — chỉ mục một dòng mỗi note để tra cứu nhanh.

Chạy:  PYTHONUTF8=1 python .tools/build_index.py
Chạy lại mỗi khi thêm/sửa note. Không sửa tay _Index.md.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
OUT = os.path.join(WIKI, "_Index.md")

# Thư mục không đưa vào chỉ mục (text OCR thô, ảnh, script)
SKIP_DIRS = {"ocr-raw", "_ocr", ".obsidian", ".tools"}
# Độ dài tối đa của phần tóm tắt mỗi note
SUMMARY_LEN = 130
# Mục H2 có ở hầu hết note, không mang thông tin phân biệt -> không liệt kê
BORING_HEADINGS = {"Liên quan", "Xem thêm", "Nguồn"}
# Thứ tự trình bày các nhóm; nhóm không liệt kê ở đây xếp cuối theo alphabet
GROUP_ORDER = [
    "",  # note nằm ngay trong wiki/
    "Khái niệm",
    "Bát quái",
    "64 quẻ",
    "Hà Lạc",
    "Hà Lạc/Lời đoán",
    "Lục Hào",
    "Ứng dụng",
    "Tử Vi Đẩu Số",
    "Tử Vi Đẩu Số/Khái niệm",
    "Tử Vi Đẩu Số/Sao",
    "Tử Vi Đẩu Số/Lá số",
    "Tử Vi Đẩu Số/Luận đoán",
    "Tử Vi Đẩu Số/Cách cục",
    "Tử Vi Đẩu Số/Nhân vật Phong Thần",
    "Nhân Tướng Học",
    "Nhân Tướng Học/Khái niệm",
    "Nhân Tướng Học/Bộ vị",
    "Nhân Tướng Học/Lưu niên",
    "Nguồn",
]

# Mô tả từng nhóm — dùng cho mục lục đầu tệp, để khi câu hỏi còn mơ hồ thì
# đọc ~25 dòng đầu là đủ biết nên grep từ khóa nào, khỏi đọc cả chỉ mục.
GROUP_DESC = {
    "": "Ba bản đồ nội dung tổng quan",
    "Khái niệm": "âm dương, ngũ hành, hào, quẻ, Hà Đồ, Lạc Thư, Thập Dực, đồ thuyết",
    "Bát quái": "tám quẻ đơn: Càn Đoài Ly Chấn Tốn Khảm Cấn Khôn",
    "64 quẻ": "mỗi quẻ: thoán từ, giảng, 6 hào từ, triệu",
    "Hà Lạc": "lập cấu trúc Hà Lạc, tiểu vận, mệnh hợp cách",
    "Hà Lạc/Lời đoán": "lời đoán theo từng quẻ đời người",
    "Lục Hào": "nạp giáp, lục thân, dụng thần, ứng kỳ — bói theo Chu Dịch dự đoán học",
    "Ứng dụng": "y lý, gieo quẻ, bấm độn, Mai Hoa Dịch Số, Linh Quy Bát Pháp",
    "Tử Vi Đẩu Số": "bản đồ nội dung Tử Vi",
    "Tử Vi Đẩu Số/Khái niệm": "can chi, ngũ hành, lịch sử Trần Đoàn, năm huyền thuật",
    "Tử Vi Đẩu Số/Sao": "14 chính tinh, phụ tinh, tứ hóa, miếu hãm, độ sáng",
    "Tử Vi Đẩu Số/Lá số": "an sao, 12 cung, lưu niên",
    "Tử Vi Đẩu Số/Luận đoán": "cách cục, phương pháp đoán, 144 mẫu lá số",
    "Tử Vi Đẩu Số/Nhân vật Phong Thần": "nhân vật Phong Thần ứng với các sao",
    "Nhân Tướng Học": "bản đồ nội dung Nhân Tướng",
    "Nhân Tướng Học/Khái niệm": "ngũ hình, tam đình, thần khí, tướng xương, tam quan tứ ải",
    "Nhân Tướng Học/Bộ vị": "mắt, mũi, miệng, tai, trán, lông mày, gò má, nhân trung…",
    "Nhân Tướng Học/Lưu niên": "xem tướng mặt theo tuổi",
    "Nguồn": "6 sách gốc, mục lục từng cuốn, tình trạng số hóa",
}


def parse_frontmatter(text):
    """Trả về (dict thô của frontmatter, phần thân còn lại)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end]
    body = text[end + 4 :]
    data, key = {}, None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t", "-")) and key:
            item = line.strip().lstrip("-").strip().strip('"').strip("'")
            if item:
                data.setdefault(key, []).append(item)
        elif ":" in line:
            key, val = line.split(":", 1)
            key, val = key.strip(), val.strip().strip('"').strip("'")
            data[key] = [val] if val else []
    return data, body


def strip_md(s):
    """Bỏ cú pháp markdown, giữ chữ đọc được."""
    s = re.sub(r"!?\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", s)  # [[a|b]] -> b
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # [a](b) -> a
    s = re.sub(r"[*_`>#]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def summarize(body):
    """Câu mở đầu của note: đoạn văn xuôi đầu tiên sau H1."""
    for para in re.split(r"\n\s*\n", body):
        line = para.strip()
        if not line or line.startswith(("#", "|", ">", "-", "*", "![")):
            continue
        text = strip_md(line)
        if len(text) < 15:
            continue
        if len(text) > SUMMARY_LEN:
            cut = text[:SUMMARY_LEN]
            sp = cut.rfind(" ")
            text = (cut[:sp] if sp > SUMMARY_LEN * 0.6 else cut) + "…"
        return text
    return ""


def thoan_tu(body):
    """Với note quẻ: lấy nguyên văn thoán từ — đặc trưng hơn câu mở đầu."""
    m = re.search(r"^##\s*Thoán từ\s*$(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith(">"):
            text = strip_md(line)
            if text:
                return text
    return ""


def headings(body, limit=5):
    """Danh sách mục H2 — cho biết note trả lời được những gì."""
    hs = [strip_md(m) for m in re.findall(r"^##\s+(.+)$", body, re.M)]
    hs = [h for h in hs if h and h not in BORING_HEADINGS]
    # tiêu đề dài thường kèm chú thích trong ngoặc — cắt cho gọn
    hs = [h.split(" (")[0][:48].strip() for h in hs]
    if len(hs) > limit:
        hs = hs[:limit] + ["…"]
    return hs


def collect():
    notes = []
    for dirpath, dirnames, filenames in os.walk(WIKI):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            if not text.strip():
                continue  # note rỗng — bỏ qua
            fm, body = parse_frontmatter(text)
            name = fn[:-3]
            group = os.path.relpath(dirpath, WIKI).replace("\\", "/")
            group = "" if group == "." else group
            # alias chỉ giữ khi thật sự khác tên note (bỏ "Bát Thuần Càn" của "01 Bát Thuần Càn")
            aliases = [a for a in fm.get("aliases", []) if a and a not in name]
            # các trường frontmatter riêng (số, ngoại-quái, đánh-giá…) làm nhãn
            extra = []
            for k, v in fm.items():
                if k in ("aliases", "tags") or not v:
                    continue
                extra.append("%s %s" % (k, ", ".join(v)))
            # 64 quẻ đều cùng một khung mục, nên thay danh sách mục bằng
            # nguyên văn thoán từ — thứ thật sự phân biệt quẻ này với quẻ kia
            is_que = group == "64 quẻ"
            summary = (thoan_tu(body) if is_que else "") or summarize(body)
            notes.append(
                {
                    "name": name,
                    "group": group,
                    "aliases": aliases,
                    "extra": extra,
                    "summary": summary,
                    "headings": [] if is_que else headings(body),
                    "size": len(text),
                }
            )
    return notes


def render(notes):
    groups = {}
    for n in notes:
        groups.setdefault(n["group"], []).append(n)

    order = [g for g in GROUP_ORDER if g in groups]
    order += sorted(g for g in groups if g not in GROUP_ORDER)

    out = [
        "---",
        "tags:",
        "  - index",
        "---",
        "",
        "# 🔎 Chỉ mục toàn wiki",
        "",
        "> [!warning] Tệp sinh tự động — đừng sửa tay.",
        "> Chạy lại: `PYTHONUTF8=1 python .tools/build_index.py`",
        "",
        "Mỗi dòng: **tên note** · *bí danh* · `nhãn` — câu mở đầu ▸ các mục trong note.",
        "Tên note = tên tệp; đường dẫn đầy đủ là `wiki/<nhóm>/<tên note>.md`.",
        "",
        "Tổng: **%d note**. Cách dùng nhanh nhất là **grep thẳng vào tệp này**;" % len(notes),
        "chỉ khi chưa rõ nên tìm từ khóa nào mới đọc bảng nhóm ngay dưới đây.",
        "",
        "| Nhóm | Note | Nội dung |",
        "|---|---|---|",
    ]
    for g in order:
        out.append(
            "| `%s` | %d | %s |"
            % (
                "wiki/" + g + "/" if g else "wiki/",
                len(groups[g]),
                GROUP_DESC.get(g, ""),
            )
        )
    out.append("")
    group_note = {
        "64 quẻ": "Mỗi note cùng một khung mục: **Lý do tiếp nối · Thoán từ · "
        "Giảng · Hào từ (6 hào) · Triệu · Liên quan**. "
        "Phần in nghiêng dưới đây là **nguyên văn thoán từ**.",
    }
    for g in order:
        out.append("## %s" % ("wiki/" + g + "/" if g else "wiki/"))
        if g in group_note:
            out.append(group_note[g])
            out.append("")
        for n in sorted(groups[g], key=lambda x: x["name"]):
            parts = ["- **%s**" % n["name"]]
            if n["aliases"]:
                parts.append(" · *%s*" % ", ".join(n["aliases"]))
            if n["extra"]:
                parts.append(" · `%s`" % " · ".join(n["extra"]))
            if n["summary"]:
                parts.append(" — %s" % n["summary"])
            if n["headings"]:
                parts.append(" ▸ %s" % " · ".join(n["headings"]))
            out.append("".join(parts))
        out.append("")
    return "\n".join(out)


def main():
    notes = collect()
    text = render(notes)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("Da ghi %s" % OUT)
    print("  %d note, %.1f KB" % (len(notes), len(text.encode("utf-8")) / 1024))


if __name__ == "__main__":
    sys.exit(main())
