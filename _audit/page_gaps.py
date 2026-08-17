"""Dò trang in bị thiếu trong bản scan — bản thay thế cho missing_pages.py.

    python page_gaps.py <book> [<book> ...]

Vì sao cần bản mới: missing_pages.py chỉ so hai trang PDF **kề nhau** và chỉ khi cả hai
đều đọc ra số in, nên (a) bỏ lọt chỗ mất nằm trong vùng OCR không đọc được số, và
(b) đẻ ra dương tính giả mỗi khi OCR đọc hụt một chữ số.

Cách làm ở đây dựa trên độ lệch d = (số trang in) - (số trang PDF). Trong một mạch trang
liên tục d là **hằng số**; d **tăng** đúng bằng số trang in bị mất, và d **giảm** khi bản
PDF có trang không đánh số (tranh chèn, trang ngăn phần) hoặc sách đánh số lại từ đầu.

Lọc OCR đọc sai bằng **đối chứng hàng xóm**: chỉ tin mốc nào có d trùng với d của trang PDF
liền kề. Một mốc lẻ loi mang d dị thường gần như luôn là OCR đọc hụt chữ số.

> Đừng thay bằng luật toàn cục "d không bao giờ giảm". Đã thử: `tamchu` có chỗ đánh số lại
> nên d tụt, luật ấy vứt nhầm 149 mốc và **giấu mất trang in 448** vốn đã xác nhận bằng ảnh.

Lợi thế then chốt: hai mốc tin cậy **đóng khung** cả khoảng trống giữa chúng — nếu
bước PDF bằng bước số in thì bên trong chắc chắn không mất trang nào, khỏi phải render ảnh.
"""
import re, sys


def read_marks(book):
    """{trang PDF: số in đọc được ở chân trang}"""
    path = rf"D:\claude\_audit\ocr\{book}_full.txt"
    pdf, seen = 0, {}
    for l in open(path, encoding="utf-8"):
        m = re.match(r"=== trang PDF (\d+) ===", l)
        if m:
            pdf = int(m.group(1))
            continue
        s = l.strip()
        if re.fullmatch(r"\d{1,3}", s):
            seen[pdf] = int(s)      # số cuối cùng đứng một mình = số trang in
    return seen


def corroborated(marks):
    """Lọc hai tầng rồi trả về danh sách mốc tin cậy.

    Tầng 1 — trung vị trượt: d phải nằm sát trung vị của 21 mốc quanh nó. Tầng này bắt
    những số **không phải số trang** mà OCR vớ được ở cuối trang (số trong bảng biểu, số
    thứ tự trong danh sách). Không có nó, `chudich` báo "mất 500 trang" chỉ vì hai trang
    liền nhau kết thúc bằng 861 và 862.

    Tầng 2 — đối chứng hàng xóm: d phải trùng với d của trang PDF liền kề.
    """
    d = {p: v - p for p, v in marks.items()}
    ks = sorted(marks)
    keep = []
    for i, p in enumerate(ks):
        win = sorted(d[k] for k in ks[max(0, i - 10): i + 11])
        if abs(d[p] - win[len(win) // 2]) <= 2:
            keep.append(p)
    return [p for p in keep
            if d.get(p - 1) == d[p] or d.get(p + 1) == d[p]]


for book in sys.argv[1:] or ["chudich", "tamchu", "nhantuong", "tuvi"]:
    marks = read_marks(book)
    good = corroborated(marks)
    print(f"\n=== {book} === {len(marks)} mốc đọc được, "
          f"loại {len(marks) - len(good)} mốc không có hàng xóm đối chứng, "
          f"còn {len(good)} mốc tin cậy")

    lost = 0
    for a, b in zip(good, good[1:]):
        gap = (marks[b] - marks[a]) - (b - a)
        if gap > 0:
            lost += gap
            khung = "" if b - a == 1 else (
                f"  (giữa còn {b-a-1} trang PDF không đọc được số — chưa khoanh hẹp được)")
            print(f"  MẤT {gap} trang in: PDF {a} (in {marks[a]}) → PDF {b} (in {marks[b]}){khung}")
        elif gap < 0:
            print(f"  [đánh số lại / trang không đánh số] PDF {a} (in {marks[a]})"
                  f" → PDF {b} (in {marks[b]})")
    print(f"  → tổng cộng thiếu {lost} trang in" if lost else "  Không mất trang nào.")
