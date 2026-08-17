# OCR các bản scan — quy trình và cạm bẫy

Chỉ đọc tệp này khi **làm việc với OCR hoặc dựng note mới từ sách scan**.
Trả lời câu hỏi tri thức thì không cần — nội dung đã hệ thống hóa nằm trong `wiki/`.

## Text OCR thô: `nguồn thô/_ocr/`

Chứa text OCR chưa hiệu đính của các PDF bản scan. **Nằm ngoài `wiki/`** (dời khỏi
`wiki/Nguồn/ocr-raw/` ngày 13-8-2026) để không lọt vào phạm vi tìm kiếm tri thức.

- **Văn xuôi dùng được** (từ 13-8-2026, sau khi đổi sang Tesseract 5): sai khoảng 1% ký tự,
  chủ yếu lệch một dấu phụ. Được phép trích, nhưng **đối chiếu lại ảnh trang trước khi đưa vào wiki**.
- **Bảng biểu và sơ đồ thì không.** Số liệu trong bảng vẫn sai. Với bảng, **render trang PDF ra
  ảnh rồi đọc ảnh**:
  `fitz.open(pdf)[n].get_pixmap(dpi=170, colorspace=fitz.csGRAY).save("out.png")` rồi Read file PNG.
- Cả bốn `*_ocr_raw.md` (chudich, tamchu, nhantuong, tuvi) **đều là bản Tesseract 5**. Bản EasyOCR
  cũ sai ~20% ký tự nay mang đuôi `*_ocr_raw_easyocr.md` — **đừng trích từ file có đuôi `_easyocr`**.
- `permissions.deny` chặn Read trên `*_ocr_raw*.md` (tránh kéo 3 MB text lỗi vào ngữ cảnh). Cần xem
  một đoạn thì dùng `Select-String` qua PowerShell để lấy đúng dòng. Script `.py` và `.log` trong
  cùng thư mục **không** bị chặn.

Kiểm tra tiến độ: `Get-Content "nguồn thô\_ocr\chudich_ocr.log" -Tail 2`.

## Chạy OCR

```
python "nguồn thô\_ocr\run_chudich.py" [start_page]
```

Máy OCR là `ocr_book_v3.py` (Tesseract 5 + vie). Kết quả đo trên cùng một trang:

| Công cụ | CER | WER | Giây/trang |
|---|---|---|---|
| EasyOCR dpi300 (bản đầu) | 20,4% | 37,7% | 22,0 |
| VietOCR + tự cắt dòng (`ocr_book_v2.py`) | 0,9% | 3,8% | 14,3 |
| **Tesseract 5.4 vie psm6 (`ocr_book_v3.py`)** | **1,1%** | **4,5%** | **1,6** |

Chọn Tesseract vì nhanh gấp 9 lần với độ chính xác tương đương, giữ được bố cục đoạn văn, và
**hỏng thì hỏng lộ liễu**. VietOCR là bộ nhận dạng *một dòng* nên gặp bảng biểu nó **bịa ra tiếng
Việt trôi chảy trông y như thật** — sai kiểu đó rất khó phát hiện.

> **Cạm bẫy**: Tesseract **không mở được đường dẫn có dấu tiếng Việt**. Vì thế `vie.traineddata`
> để ở `D:\claude\.tessdata` chứ không nằm trong vault.

> **Cạm bẫy**: 6 script `run_*.py` tính đường dẫn vault bằng số bậc thư mục tương đối. Dời thư mục
> `_ocr` là phải sửa lại cả 6.

## Dựng note mới từ sách scan — quy trình ba bước

1. Lấy bản đồ chương/quẻ → trang PDF (ví dụ `_audit/halac_map.py`), nhớ **độ lệch số trang in
   với số trang PDF** khác nhau theo từng cuốn và từng vùng.
2. Cắt text OCR của khoảng trang đó để **nắm bố cục trước** — biết trang nào có gì thì đọc ảnh nhanh hơn.
3. **Chữ đưa vào wiki phải lấy từ ảnh trang**, không lấy từ text OCR. OCR sai đều tay ở đúng chỗ
   quan trọng nhất: khối tiêu đề, tên riêng, bảng số.

Chi tiết rà soát và các ngã cụt: `D:\claude\_audit\findings.md` và `.tools/nhat-ky.md`.
