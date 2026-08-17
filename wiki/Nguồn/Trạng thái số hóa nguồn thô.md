---
aliases:
  - "Nguồn thô"
  - "Trạng thái PDF"
tags:
  - nguồn
  - meta
---


# Trạng thái số hóa nguồn thô

Ghi nhận tình trạng kỹ thuật của sáu PDF trong thư mục `nguồn thô/`, tính đến **13-8-2026**.

| # | Tệp | Số trang | Lớp văn bản | Đã đưa vào wiki |
|---|---|---|---|---|
| 1 | **Chu dịch.pdf** — *Thiệu Vĩ Hoa*, ***Chu Dịch với Dự Đoán Học***, người dịch Mạnh Hà, NXB Văn Hóa, Hà Nội 1995 (496tr in, 23 trang đầu số La Mã) | 522 | ✅ **Đã OCR xong 522/522 trang** bằng Tesseract 5.4 (`_audit/ocr/chudich_full.txt`) | ⏳ **Khoảng 70%** — đã có chương 5 (mục II, III, VI) → 23. **Thiếu chương 1–4** và chương 5 mục I, IV, V (tr. 13–147). Xem [[Chu Dịch với Dự Đoán Học — Thiệu Vĩ Hoa\|note nguồn + mục lục đầy đủ 23 chương]] |
| 2 | **Kinh Dịch Diễn Giảng** — *Ths.BS Kiều Xuân Dũng*, NXB Y học 2006 | 118 | ✅ **Có lớp text đầy đủ** (~263.000 ký tự) | ✅ **Toàn bộ** |
| 3 | **kinhdich-Sách tam-chu-ha-lac-va-quy-dao-doi-nguoi** — *Xuân Cang*, ***Tám chữ Hà Lạc và quỹ đạo đời người***, NXB Văn hóa Thông tin (604tr in) | 608 | ✅ **Đã OCR xong 608/608 trang** bằng Tesseract 5.4 (`_audit/ocr/tamchu_full.txt`) | ⏳ **Khoảng 5%** — mới có Bài Ba, Bốn, Năm (tr. 28–59). **Thiếu Bài Một–Hai, toàn bộ Phần hai (lời đoán 64 quẻ, tr. 75–420) và Phần ba (11 chân dung nhà văn, tr. 421–578)**. Xem [[Tám chữ Hà Lạc và quỹ đạo đời người — Xuân Cang\|note nguồn + mục lục đầy đủ]] |
| 4 | **Kinh Dịch Trọn Bộ (Ngô Tất Tố).pdf** — NXB Văn học, 2004, 938 trang | 938 | ✅ **Có lớp text đầy đủ** | ✅ **Toàn bộ** — 384 hào từ của 64 quẻ, Phép bói cỏ thi, Tượng và Chiêm, Lý-Tượng-Số, Đồ thuyết của Chu Hy. Xem [[Kinh Dịch Trọn Bộ — Ngô Tất Tố]] |
| 5 | **TỬ VI ĐẨU SỐ (CỔ ĐỒ THƯ - dịch NGUYỄN MẠNH LINH).pdf** | 608 | ✅ **Đã OCR xong toàn bộ 608 trang** bằng Tesseract 5.4 (`nguồn thô/_ocr/tuvi_ocr_raw.md`) | ⏳ **Khung thì đủ, ruột thì chưa.** Có note cho **cả 8 chương + 7 phụ lục**, nhưng hai chỗ mới là *mô tả cấu trúc* chứ chưa có nội dung: **chương 8** (mới 1/144 mẫu — [[144 mẫu lá số]]) và **phụ lục 5–7 *Toàn Thư*** (mới có khẩu quyết 12 cung, mô tả 4 sao, [[Nữ Mệnh Cốt Tủy Phú]] — xem [[Nguồn tri thức Tử Vi — thứ tự ưu tiên]]). Xem [[Tử Vi Đẩu Số — Bản đồ nội dung]] |
| 6 | **TÌM HIỂU NHÂN TƯỚNG HỌC THEO KINH DỊCH (THIỆU VĨ HOA - biên dịch CỔ ĐỒ THƯ).pdf** | 362 | ✅ **Đã OCR xong toàn bộ 362 trang** bằng Tesseract 5.4 (`nguồn thô/_ocr/nhantuong_ocr_raw.md`) | ✅ **Toàn bộ** — 17 chương. Xem [[Nhân Tướng Học — Bản đồ nội dung]] |

## Wiki hiện nay được rút từ nguồn số 2 và số 4
Xem [[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] và [[Kinh Dịch Trọn Bộ — Ngô Tất Tố]]. Hai nguồn này khớp nhau về kinh văn (nguồn 2 trích thoán từ từ nguồn 4), nên được dựng chung trong `wiki/64 quẻ/`.

## Ghi chú kỹ thuật
- Trích xuất bằng **PyMuPDF**. Lưu ý: `pdftotext -layout` **làm mất dấu tiếng Việt** trên các tệp có lớp text (font nhúng thiếu ToUnicode CMap cho dấu phụ) — *"Kinh Dịch"* ra thành *"Kinh Dch"*. PyMuPDF cho ra Unicode đúng.
- Tên tệp có dấu tiếng Việt khiến các công cụ MinGW (`pdftotext`, `pdfinfo`) không mở được; phải sao chép sang tên ASCII trước.
- Máy này không có quyền admin nên **không cài được Tesseract qua Chocolatey** (`UnauthorizedAccessException` ghi vào `C:\ProgramData\chocolatey`). Vòng đầu vì thế dùng **EasyOCR** (thuần Python). Sau đó cài được Tesseract 5.4 theo đường khác (`C:\Program Files\Tesseract-OCR`) và **OCR lại toàn bộ** — xem bảng đo bên dưới. EasyOCR nay chỉ còn là di sản.

## Nguồn 5 và 6
- **Nguồn 5** ([[Tử Vi Đẩu Số — Nguyễn Mạnh Linh]]): **có note cho cả 8 chương + 7 phụ lục** — mệnh lý học nền tảng, 23 bước lập lá số, đặc tính 32 sao Giáp + 31 sao Ất + 26 sao Bính, phương pháp luận đoán, cách cục, 144 mẫu lá số, *Tử Vi Đẩu Số Toàn Thư*.
  > [!warning] Hai chỗ mới có vỏ, chưa có ruột — phát hiện 17-8-2026 khi luận một lá số thật
  > - **Chương 8 — 144 mẫu lá số.** Note cũ chỉ mô tả *cấu trúc* chương; **nội dung 144 mẫu chưa chép chữ nào**. Nay được 1/144 ([[Mẫu lá số — Tử Vi tại Dần]]). Lý do bị bỏ sót: sơ đồ 12 cung là **bảng in**, OCR ra rác nên các mẻ trước bỏ qua mà không ghi lại là đã bỏ qua.
  > - **Phụ lục 5–7 — Toàn Thư (tr. 476–608, gần 1/4 độ dày sách).** Mới khai thác khẩu quyết 12 cung, mô tả 4 sao và trọn [[Nữ Mệnh Cốt Tủy Phú]]. Bản đồ chỗ nào bù được gì: [[Nguồn tri thức Tử Vi — thứ tự ưu tiên]].
  >
  > **Bài học chung: "đã có note cho chương X" ≠ "đã số hóa chương X".** Chỗ nào chỉ có note mô tả cấu trúc thì phải ghi rõ ngay tại bảng này, nếu không lần sau lại tưởng đã xong.
- **Nguồn 6** ([[Tìm Hiểu Nhân Tướng Học — Thiệu Vĩ Hoa]]): **xong toàn bộ 17 chương** — từ tướng xương đầu mặt, Tam Đình, Ngũ Hình, 12 cung, 13 bộ vị, 11 chương bộ vị chi tiết, đến phép lưu niên xem tướng theo tuổi.

> [!note] Hai chỗ sách tự mâu thuẫn (đã ghi rõ trong note tương ứng)
> - **Văn Xương / Văn Khúc** (Tử Vi, ch.4 bước 9): khẩu quyết chữ Hán và phần diễn giải tiếng Việt nói ngược chiều đếm của nhau.
> - **Tương sinh hữu tình / vô tình** (Tử Vi, ch.6 vs. phụ lục 2): hai chỗ định nghĩa trái ngược nhau.
> - **Hóa Khoa can Tân** (Tử Vi, ch.4 bước 12): khẩu quyết in "Vũ", bảng tra in "Văn Khúc".

## Nguồn 1 và 3 — OCR xong, wiki còn dở

**Đã OCR xong toàn bộ 1.130 trang** bằng Tesseract 5.4 (13-8-2026, `_audit/ocr_run2.py`). Từ đây trở đi
phần việc còn lại **không phải là OCR mà là viết note**:

| Nguồn | Trang đã đưa vào wiki | Còn thiếu |
|---|---|---|
| **1. Chu Dịch với Dự Đoán Học** | tr. 148–496 (13 note) | chương 1–4 + chương 5 mục I, IV, V — tr. 13–147. Riêng **Thần sát** (ch.4 mục VII) và **Ví dụ cổ / ví dụ ngày nay** (ch.5 mục IV–V) chưa có ở đâu trong vault |
| **3. Tám chữ Hà Lạc** | tr. 28–59 (3 note) + Phần hai: dẫn nhập tr. 76–77 và **quẻ 1–21** (tr. 77–176) | **~428/604 trang**. Nặng nhất vẫn là Phần hai — còn **quẻ 22–64** (tr. 176–420) |

> [!warning] Bản scan nguồn 3 **thiếu trang in 100**
> PDF tr.99 in số "99", PDF tr.100 in số "101" — đã đối chiếu ảnh cả hai, nội dung đứt mạch thật.
> Hệ quả: [[05 Thủy Thiên Nhu — Hà Lạc]] thiếu hào 4 và một phần hào 3, hào 5. Muốn bù phải tìm bản in khác.
> Từ tr. PDF 100 trở đi, **trang in = trang PDF + 1**.

### Đã rà hết chuyện thiếu trang của cả bốn bản scan (13-8-2026)

So số in ở chân trang với số trang PDF trên toàn bộ 2.100 trang, chỗ nào nghi ngờ thì render
ảnh xác nhận (`_audit/page_gaps.py`, `_audit/footer.py`; chi tiết trong `_audit/findings.md`).
**Toàn bộ bốn cuốn chỉ thiếu ba trang in:**

| Bản scan | Trang in thiếu | Ảnh hưởng |
|---|---|---|
| Chu Dịch với Dự Đoán Học | *(không thiếu trang nào)* | — |
| Tám chữ Hà Lạc | **100** | ❗ [[05 Thủy Thiên Nhu — Hà Lạc]], như cảnh báo trên |
| Tìm Hiểu Nhân Tướng Học | **354** | không — là một trang **mục lục cuối sách**, wiki chỉ trích tới tr.351 |
| Tử Vi Đẩu Số | **112** | không — trang **tranh minh họa** trong mục *Sao Thiên Phủ*; truyện Khương Hoàng hậu ở tr.111 đã trọn vẹn |

Riêng vùng **tr. 20–141 của Tám chữ Hà Lạc** (phần lời đoán quẻ đang dựng dở) đã được đóng
khung chặt: tr.100 là chỗ mất **duy nhất**, nên khi viết tiếp quẻ 10–64 không có lỗ nào chờ sẵn.

> [!caution] Số trang nhảy một bậc chưa chắc là mất trang — có thể là **chụp lặp**
> Hai lần bị hố: PDF 448 của *Tám chữ Hà Lạc* và PDF 14 của *Tử Vi* đều là **bản chụp lại
> trang liền trước**, làm các trang sau lệch một bậc y như mất trang. Trang in 448 và 12
> thực ra vẫn còn. Khi nghi ngờ, phải render **ba trang liên tiếp** (trước–giữa–sau) rồi so
> cả số in lẫn nguyên văn: trùng nguyên văn là chụp lặp.

> Lưu ý khi ước lượng độ thiếu của nguồn 1: phần lớn nội dung chương 1–2 (tiên/hậu thiên bát quái,
> Hà Đồ, Lạc Thư, ngôi hào, tượng quẻ) **đã có trong vault từ nguồn 2 và 4**. Thứ thực sự vắng mặt là
> phần Thiệu Vĩ Hoa nói riêng: thần sát, và các ví dụ dự đoán.

Đã hoàn tất bước khảo sát: xác định được tác giả, nhà xuất bản, **mục lục đầy đủ** và **quy đổi số trang PDF ↔ trang in** của cả hai — xem [[Chu Dịch với Dự Đoán Học — Thiệu Vĩ Hoa]] và [[Tám chữ Hà Lạc và quỹ đạo đời người — Xuân Cang]].

Khi có nội dung thì **đối chiếu với các ghi chép hiện có**:
- **Nguồn 1** mở rộng đáng kể [[Gieo quẻ và bấm độn]] bằng 18 chương lục hào nạp giáp; nhưng lưu ý nó **cho phép đoán cụ thể từng việc**, trái với lời căn dặn của Kiều Xuân Dũng — giữ nguyên chỗ khác biệt, đừng hòa trộn.
- **Nguồn 3** nối [[Thiên Can và Địa Chi]] với 64 quẻ qua số [[Hà Đồ]] – [[Lạc Thư]], và có 11 ca chân dung nhà văn có thật để kiểm chứng.

> [!success] Đã đổi công cụ OCR (13-8-2026) — văn xuôi giờ trích dẫn được
> Bản EasyOCR ban đầu sai tới **20% ký tự / 38% số từ**, chỉ đủ dò vị trí. Sau khi đo thử ba công cụ trên cùng một trang, đã chuyển sang **Tesseract 5.4 + gói `vie` của tessdata_best**:
>
> | Công cụ | CER | WER | Giây/trang |
> |---|---|---|---|
> | EasyOCR dpi300 | 20,4% | 37,7% | 22,0 |
> | VietOCR + tự cắt dòng | 0,9% | 3,8% | 14,3 |
> | **Tesseract 5.4 vie psm6** | **1,1%** | **4,5%** | **1,6** |
>
> VietOCR nhỉnh hơn về con số nhưng chậm gấp 9 lần, mất ranh giới đoạn văn, và — nguy hiểm nhất — gặp bảng biểu thì **bịa ra tiếng Việt trôi chảy trông y như thật**. Tesseract giữ bố cục đoạn và cột, hỏng thì hỏng lộ liễu.
>
> **Vẫn còn nguyên một hạn chế**: số liệu trong **bảng biểu và sơ đồ** không đáng tin ở cả ba công cụ. Với bảng, vẫn phải **render trang ra ảnh rồi đọc trực tiếp**.
>
> **Cập nhật 13-8-2026 tối**: đã OCR lại bằng Tesseract **cả bốn** cuốn scan, kể cả nguồn 5 và 6, đặt tại
> `D:\claude\_audit\ocr\*_full.txt` kèm ảnh từng trang ở `_audit\pages_*`. Nhờ đó rà soát lại được phần
> wiki đã viết từ bản EasyOCR — kết quả trong `_audit\findings.md`.
>
> Bản OCR trong vault nay cũng là Tesseract cả bốn cuốn: `nguồn thô/_ocr/*_ocr_raw.md` (thư mục này
> **đã dời khỏi `wiki/Nguồn/ocr-raw/`** để không nhiễu tìm kiếm tri thức). Bản EasyOCR cũ được giữ lại
> dưới tên `*_ocr_raw_easyocr.md` — **file có đuôi `_easyocr` thì đừng trích**, chỉ dùng định vị trang.

## Liên quan
[[Kinh Dịch Diễn Giảng — Kiều Xuân Dũng]] · [[Kinh Dịch Trọn Bộ — Ngô Tất Tố]] · [[Kinh Dịch]]
