# Kết quả rà soát wiki đối chiếu OCR Tesseract mới

Nguồn đối chiếu: `D:\claude\_audit\ocr\{chudich,tamchu,nhantuong,tuvi}_full.txt`
(Tesseract 5.4 vie, ~1% sai ký tự) + ảnh trang gốc `D:\claude\_audit\pages_*/pNNNN.png`.

---

## Agent: Nhân Tướng — Lưu niên (Lưu niên pháp, Bát thương nhị khố)
**Không tìm thấy lỗi.** Cả hai note khớp chính xác với OCR mới (bảng Cửu chấp lưu niên, 10 Đại vận Bát thương nhị khố, các mốc tuổi đặc thù 31/15/22/25/35/41/51/61/71 đều khớp tr.316-351).

---

## Agent: Tử Vi — Chương 1–2 (5 note Khái niệm)

> Kết quả này bị mất khi phiên trước kết thúc; khôi phục lại từ transcript agent
> `a041dbeb2b3754803` ngày 13-8-2026, và đã **kiểm chứng lại bằng ảnh trang gốc** ở phiên này.

**Tìm được 2 sai lệch.**

### 1. Số cung trời và số sao trong thuật chiêm tinh — sai số liệu ✅ đã xác nhận bằng ảnh

File: `Tử Vi Đẩu Số/Khái niệm/Tử Vi Đẩu Số — thiên hạ đệ nhất thần số.md`, mục
"Nội hàm văn hóa", gạch đầu dòng **Thuật chiêm tinh** (dòng 34).

| | Nội dung |
|---|---|
| Wiki đang ghi | "chia bầu trời thành **12 cung**, dựa vào phân bố/tổ hợp/độ sáng của **1.110 ngôi sao**" |
| Sách in (tr. PDF 65) | "phân chia bầu trời thành **hai mươi cung**, và căn cứ vào sự phân bố, tổ hợp cùng độ sáng của tổng cộng **111 ngôi sao**" |

Đã render lại tr.65 ở 320 dpi và đọc trực tiếp: khung "Thuật chiêm tinh" in rõ
"hai mươi cung" và "111 ngôi sao". "1.110" gần như chắc chắn là tàn dư EasyOCR
đọc nhầm "111".

### 2. Thiên can tương xung — wiki khác sách, nhưng **sách mới là bên sai**

File: `Tử Vi Đẩu Số/Khái niệm/Thiên Can và Địa Chi.md`, dòng 31.

| | Nội dung |
|---|---|
| Wiki đang ghi | "Thiên can tương xung: **Giáp-Canh**, Ất-Tân, Bính-Nhâm, Đinh-Quý" |
| Sách in (tr. PDF 90 và 92, in hai lần giống nhau) | "**Thân** và Giáp tương xung; Ất và Tân…" |

Thân là **địa chi**, không phải thiên can; ba cặp còn lại đều cách nhau 6 vị trí
trong Thập Can, nên cặp đúng phải là Giáp-Canh. Đây là **lỗi in trong chính cuốn
sách**, không phải lỗi wiki.
→ **Đề xuất: giữ nguyên "Giáp-Canh", thêm chú thích ghi rõ sách gốc in "Thân và Giáp".**
Không sửa wiki thành "Thân-Giáp".

---

## Cảnh báo về độ tin cậy của nguồn Tử Vi (phát hiện thêm ở phiên này)

Trang PDF 65 còn in: lý luận can chi "xác lập nên vị trí của toàn bộ **hai mươi cung**
trong lá số". Lá số Tử Vi chỉ có **12 cung** — đã đối chiếu ảnh gốc, sách in đúng là
"hai mươi cung". Vậy bản dịch này **lặp lại lỗi "hai mươi" ở nhiều chỗ**.

Hệ quả cho phần rà soát còn lại: khi wiki lệch với OCR ở một con số, **không mặc định
wiki sai**. Phải hỏi thêm: con số đó có nhất quán với hệ thống Tử Vi không. Wiki ghi
"12 cung" ở dòng 33 là **đúng** dù sách in khác.

---

## Vòng rà bằng máy (phiên 13-8 tối)

Thay vì đọc tay từng note, dùng hai script quét toàn vault. Cả hai để ở scratchpad
phiên này (`scan.py`, `dup.py`, `find.py`).

**Khoanh vùng trước**: chỉ 59/165 note dẫn nguồn từ 4 cuốn **sách scan**. 104 note còn lại
dẫn *Kinh Dịch Diễn Giảng — Kiều Xuân Dũng* (PDF có sẵn text layer) → **không có rủi ro OCR**,
loại khỏi phạm vi.

| Script | Cách làm | Kết quả |
|---|---|---|
| `scan.py` | Trích cụm 2–3 từ viết hoa + số ≥3 chữ số trong note, đối chiếu với OCR của **đúng cuốn sách note đó dẫn** (so khớp bỏ dấu, bỏ ngắt dòng) | 119 tên riêng + 2 số không khớp, trên 25 note |
| `dup.py` | Tìm cặp danh từ riêng trong vault lệch nhau **đúng 1 ký tự**, ưu tiên cặp lệch mạnh về tần suất | 71 cặp |

Hai mẹo cần nhớ nếu chạy lại:
- **Dải regex `[À-Ỹ]` chứa cả chữ thường tiếng Việt** — không dùng nó để bắt chữ hoa.
  Phải tách từ rồi `w[0].isupper()`. Bản đầu vì lỗi này sinh 1.747 kết quả rác.
- **Phải cắt dòng tại dấu phân cách** (`| , ; · ( )`) trước khi ghép cụm, nếu không mỗi hàng
  bảng sẽ đẻ ra n-gram ghép chéo ô.
- **grep thẳng vào OCR gần như vô dụng**: `grep "Thừa Tương"` ra 0 kết quả dù sách có đầy —
  Tesseract đọc thành "Thừa tương". Luôn tra bằng `find.py` (bỏ dấu).

---

## Lỗi ĐÃ SỬA trong wiki

| Note | Trước | Sau | Căn cứ |
|---|---|---|---|
| `Tử Vi/Khái niệm/Tử Vi Đẩu Số — thiên hạ đệ nhất thần số.md:34` | 12 cung · **1.110** ngôi sao | hai mươi cung · **111** ngôi sao | ảnh tr.65 @320dpi |
| `Nhân Tướng/Bộ vị/Địa Các và Tai Cốt.md:38` | "Hộ **Ấu**" | "Hộ **Đấu**" | sách tr.307, 313; và note *Bát thương nhị khố* trong chính vault ghi "Hộ Đấu" |
| `Nhân Tướng/Bộ vị/Trán.md:29` | "**Tiên** Sơn khởi cốt" | "**Tiền** Sơn khởi cốt" | ảnh tr.128 — sách in "Tiền sơn hoặc Hậu sơn"; vault dùng "Tiền Sơn" ×10, "Hậu Sơn" ×9 |
| `Lục Hào/Phản ngâm, phục ngâm…md:37` | "(ví dụ **Khôn→Tốn**)" | "(theo đúng bốn cặp ở bảng trên)" | Sách tr.310 chỉ có 4 cặp: càn↔tốn, khảm↔ly, chấn↔đoài, khôn↔**cấn**. Khôn→Tốn không tồn tại, lại mâu thuẫn với bảng ở dòng 24–27 của chính note |

## Chỗ SÁCH GỐC IN SAI — wiki đúng, đã thêm chú thích cảnh báo

| Note | Sách in | Wiki giữ | Lý do |
|---|---|---|---|
| `Thiên Can và Địa Chi.md` | "**Thân** và Giáp tương xung" (tr.90, 92) | Giáp-Canh | Thân là địa chi; ba cặp kia đều cách 6 vị trí trong Thập Can |
| `Lục cát, Lục sát, Tứ Hóa…md` | khẩu quyết tr.185: "Tân: Cự, Dương, **Vũ**, Xương" | Tân Hóa Khoa = **Văn Khúc** | Chính khẩu quyết ấy dùng "Khúc" cho Văn Khúc ở can Kỷ |

## Đã kiểm, KHÔNG phải lỗi

- **"cả bầy hào dương"** — `Hà Lạc/Lời đoán/09 Phong Thiên Tiểu Súc — Hà Lạc.md:84`. Ảnh 600 dpi
  thấy rõ dấu huyền: sách in **"bầy"**, không phải "bảy". Nghĩa cũng khớp — quẻ Tiểu Súc chỉ có
  **5 hào dương**, nên "bảy hào dương" là vô nghĩa. Wiki đang đúng, không sửa.
- **Bảng Tứ Hóa đầy đủ 10 can × 4 hóa = 40 ô: khớp 39/40** với khẩu quyết tr.185
  (ảnh gốc), ô lệch duy nhất là can Tân nói trên.
- `259.200 người mới có hai người vận mệnh giống nhau` — **đúng**, ảnh tr.49 (chữ viết tay,
  OCR đọc thành "2592.9200"). Chỉ lệch nhỏ: sách in "**Châu** thiên vận mệnh", wiki ghi
  "chu thiên" — không sửa, cùng một chữ 周.
- "Tửu Trì" (Thừa Tương, 61 tuổi): sách in "Tửu **chì**" (ảnh tr.342) — lỗi in của sách,
  酒池 đọc là *tửu trì*. Wiki đúng.
- "Thiểu dương / Thiểu Âm", "Tiên thương", "Quan Phủ" (nhóm Bác Sĩ), "phạm Tuế Quân",
  "Thập Thần", "Thoa Xuyến Kim", khẩu quyết Lộc Tồn, "Thiên Khôi = Thiên Ất Quý Nhân /
  Thiên Việt = Ngọc Đường Quý Nhân" — **đều khớp sách**, là dương tính giả của script.
- **Ngũ Nhạc**: wiki ghi Nam Nhạc = Hằng Sơn *và* Bắc Nhạc = Hằng Sơn, Trung Nhạc = Tùng Sơn.
  Sách in **y hệt** (tr.44). Đúng ra Nam Nhạc là Hành Sơn 衡山, Trung Nhạc là Tung Sơn 嵩山 —
  nhưng đây là lỗi của sách, wiki chép trung thành. **Chưa đụng vào.**

## Cảnh báo về độ tin cậy của nguồn Tử Vi

Trang PDF 65 còn in: lý luận can chi "xác lập nên vị trí của toàn bộ **hai mươi cung**
trong lá số". Lá số Tử Vi chỉ có **12 cung** — đã đối chiếu ảnh gốc, sách in đúng là
"hai mươi cung". Vậy bản dịch này **lặp lại lỗi "hai mươi" ở nhiều chỗ**.

Hệ quả: khi wiki lệch với OCR ở một con số, **không mặc định wiki sai**. Wiki ghi
"12 cung" ở dòng 33 là **đúng** dù sách in khác. Trong 7 sai lệch tìm được ở phiên này,
**4 là lỗi của sách chứ không phải của wiki**.

---

## Bản scan Tám chữ Hà Lạc **thiếu trang in 100** ✅ đã xác nhận bằng ảnh

Phát hiện khi dựng lời đoán quẻ 5. **PDF tr.99 in số "99", PDF tr.100 in số "101"** — hai
trang PDF liền nhau nhưng số in nhảy một bậc. Đã đọc ảnh cả hai trang: nội dung đứt mạch
(tr.99 kết ở MKHC hào 3; tr.100 mở đầu bằng một khối *Vận năm* mang giọng cát tường,
không thể thuộc hào 3 vốn xấu — nó là Vận năm của hào 5).

**Mất theo trang ấy**: Vận năm của hào 3, **toàn bộ hào 4**, và Lời Kinh + Toán Hà Lạc giải
+ MHC + MKHC của hào 5 — quẻ [[05 Thủy Thiên Nhu — Hà Lạc]]. Note đã đánh dấu ❌ đúng
chỗ thiếu thay vì lấp bằng suy đoán.

Cách dò: `_audit/missing_pages.py <book>` — so số trang in ở chân trang với số trang PDF.

> **Cảnh báo về script này**: nó rất nhiễu. Heuristic "số đứng một mình cuối trang = số trang in"
> hay vớ phải số lẻ trong bảng biểu, nên phần lớn dòng báo là dương tính giả. **Chỉ tin những
> ca "MẤT 1 trang" mà hai trang PDF hai bên liền nhau và đọc số sạch**, rồi vẫn phải mở ảnh xác nhận.

### ✅ Đã đóng sổ chuyện thiếu trang cho CẢ BỐN cuốn scan

Công cụ mới, thay hẳn `missing_pages.py`:

- `_audit/footer.py <book> <trang…>` — cắt dải 11% ở **đầu và chân** mỗi trang, xếp chồng
  vào **một** ảnh, đọc số in của nhiều trang chỉ bằng một lần Read.
- `_audit/page_gaps.py [book…]` — dò tự động, lọc hai tầng (trung vị trượt + đối chứng
  hàng xóm). Xem docstring để biết vì sao **không** được dùng luật "d không bao giờ giảm".

#### ⚠️ Cạm bẫy đã làm tôi kết luận sai hai lần

**Số trang nhảy một bậc KHÔNG có nghĩa là mất trang — có thể là trang bị chụp LẶP.**
Bản scan lặp trang X thì trang PDF kế tiếp lại in X, đẩy các trang sau lệch đi một bậc,
tạo ra tín hiệu y hệt mất trang khi chỉ nhìn hai trang ở ranh giới.

Đã dính đúng kiểu này 2/5 lần, cả hai đều do **chỉ render hai trang bị báo, không render
trang liền TRƯỚC**:

| Ranh giới | Tôi kết luận (sai) | Sự thật khi render thêm trang trước |
|---|---|---|
| tamchu PDF 448→449 (447→449) | mất trang in 448 | **PDF 448 chụp lặp PDF 446** (nguyên văn giống hệt, cùng in 447). Trang in 448 vẫn còn ở **PDF 447** |
| tuvi PDF 14→15 (11→13) | mất trang in 12 | **PDF 14 chụp lặp PDF 12** (cùng in 11). Trang in 12 vẫn còn ở **PDF 13** |

→ **Quy tắc**: gặp ranh giới nghi mất trang, luôn render **ít nhất 3 trang liên tiếp**
(trước–giữa–sau) rồi so cả *số in* lẫn *nguyên văn*. Trùng nguyên văn = chụp lặp, không phải mất.

#### Kết quả cuối — toàn bộ 4 cuốn chỉ thiếu 3 trang in

| Sách | Trang in thiếu | Nội dung mất | Ảnh hưởng wiki |
|---|---|---|---|
| chudich | *(không có)* | — | — |
| tamchu | **100** | Vận năm hào 3, cả hào 4, phần đầu hào 5 quẻ 5 | ❗ đã đánh dấu ❌ trong [[05 Thủy Thiên Nhu — Hà Lạc]] |
| nhantuong | **354** | một trang **mục lục cuối sách** (ảnh: toàn dòng "PHÂN TÍCH TƯỚNG LÝ CUNG…") | không — wiki chỉ trích tới tr.351 |
| tuvi | **112** | trang tranh minh họa trong mục *Sao Thiên Phủ* | không — xem dưới |

Các ca đã loại (dương tính giả của `missing_pages.py`): tamchu 304→305 (OCR đọc nhầm 305
thành "304"; nội dung liền mạch hào 5 → hào 6 quẻ Cấu), nhantuong 100→101 (đọc nhầm 99 thành
"98"; chữ bắc cầu đúng: `…hoặc "bạc` + `phúc"…`), cùng hai ca chụp lặp ở bảng trên.

**Vì sao tr.112 của tuvi không mất gì**: mục lục (ảnh PDF 20) cho thấy *Sao Thiên Phủ* bắt
đầu tr.111 và *Sao Thiên Đồng* bắt đầu tr.113 → tr.112 **nằm trong mục Thiên Phủ**, không
phải một sao riêng. Truyện Khương Hoàng hậu ở tr.111 đã trọn vẹn (đủ *móc mắt*, *đốt hai
tay*, và đoạn phong thần) nên hàng Thiên Phủ trong [[Hệ thống nhân vật Phong Thần]] không
thiếu gì.

> Nhân tiện: **mục lục sách Tử Vi bỏ sót mục *Sao Tử Vi - Bá Ấp Khảo*** (in ở tr.116, mục lục
> nhảy thẳng từ Thiên Đồng 113 sang Thái Dương 118). Lỗi của sách; wiki có đủ hàng này.

#### Mẹo: đóng khung bằng số học, khỏi render ảnh

Vùng OCR không đọc được số trang vẫn có thể giấu trang mất. Không cần render từng trang:
lấy hai mốc tin cậy hai đầu khoảng trống, nếu **bước PDF = bước số in** thì khoảng giữa
**không thể** mất trang nào.

Áp dụng cho toàn vùng sách Hà Lạc mà wiki đang dựa vào (tr. 20–141): 9 trang không đọc được
số (PDF 80–83, 86, 87, 93, 110, 130) đều được đóng khung an toàn → **tr.100 là trang mất duy
nhất trong tr. 20–141**, tức phần dựng quẻ 10–20 sắp tới không có lỗ nào chờ sẵn.

> Chỗ mù còn lại của `page_gaps.py`: trang đánh số **lẻ loi** (đầu sách, không trang kề nào
> đọc được số) bị tầng đối chứng loại mất. Vì thế nó không tự báo ca tuvi PDF 14 — ca đó tìm
> ra nhờ `missing_pages.py`. Hai script bù nhau; chạy cả hai khi cần chắc.

## Phần chưa rà

Script chỉ bắt được **danh từ riêng và số hiếm**. Chưa kiểm được bằng máy:

- Số viết bằng chữ trong sách ("mười bốn", "ba mươi mốt") so với chữ số trong wiki.
- Câu văn diễn giải, quan hệ nhân quả, mô tả tướng — phải đọc đối chiếu tay.
- Bảng số liệu chụp ảnh (mức độ sáng của sao theo cung, 144 mẫu lá số) — OCR không đọc nổi,
  phải render ảnh từng trang.

Note chưa có ai đọc kỹ tay: Tử Vi *Luận đoán* (4), *Lá số* (4), Nhân Tướng *Bộ vị* (14),
*Khái niệm* (5), Hà Lạc (3), Lục Hào (11), Ứng dụng (2).
