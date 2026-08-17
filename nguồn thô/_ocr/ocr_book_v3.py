r"""OCR tiếng Việt cho PDF scan — Tesseract 5 + vie (tessdata_best).

    python ocr_book_v3.py <pdf> <out.md> [start_page]

## Vì sao chọn Tesseract

Đo trên trang PDF 171 của "Chu dịch" (trang in 148), so với bản gõ tay:

    EasyOCR dpi300  (bản đầu)          CER 20,4%   WER 37,7%   22,0 s/trang
    VietOCR + tự cắt dòng              CER  0,9%   WER  3,8%   14,3 s/trang
    Tesseract 5.4 vie dpi300 psm6      CER  1,1%   WER  4,5%    1,6 s/trang  ← chọn

VietOCR chính xác hơn một chút nhưng **chậm gấp 9 lần**, và có hai nhược điểm
nặng hơn con số:

1. Nó là bộ nhận dạng *một dòng*. Gặp bảng biểu — nơi một dòng chứa nhiều ô —
   nó **bịa ra tiếng Việt trôi chảy** trông y như thật. Ví dụ hàng đầu bảng Mã
   số Can ra thành "Chính Trình (Chính Trận Thị Trị Trị Trung Thị...". Sai kiểu
   này rất khó phát hiện khi đọc lại.
2. Nó trả về từng dòng rời, mất ranh giới đoạn văn.

Tesseract giữ được **bố cục**: dòng trống giữa các đoạn, và dấu `|` ngăn ô của
bảng. Chỗ nào đọc hỏng thì hỏng lộ liễu chứ không giả làm câu văn hợp lý.

## Hai cạm bẫy của máy này

- **Tesseract không mở được đường dẫn có dấu tiếng Việt.** `--tessdata-dir` trỏ
  vào `wiki/Nguồn/...` sẽ báo "Error opening data file ... Ngu?n ...". Vì vậy
  `vie.traineddata` để ở `D:\claude\.tessdata` (thuần ASCII).
- Tên PDF trong `nguồn thô/` ở dạng Unicode NFD — xem run_*.py.

## Vẫn còn hạn chế

Số liệu trong bảng vẫn sai (thiếu ô, lẫn chữ số). **Với bảng biểu và sơ đồ,
vẫn phải render trang ra PNG rồi đọc ảnh trực tiếp** — xem CLAUDE.md.
"""
import os
import subprocess
import sys
import time

import fitz

DPI = 300
PSM = '6'          # coi cả trang là một khối văn bản — giữ được bố cục bảng
LANG = 'vie'
TESS = os.environ.get('TESSERACT_EXE', r'C:\Program Files\Tesseract-OCR\tesseract.exe')
# vie.traineddata lấy từ github.com/tesseract-ocr/tessdata_best (chính xác hơn tessdata thường).
# BẮT BUỘC là đường dẫn thuần ASCII — xem ghi chú ở đầu tệp.
TDIR = os.environ.get('TESSDATA_DIR', r'D:\claude\.tessdata')


def ocr_page(png_bytes):
    cmd = [TESS, 'stdin', 'stdout', '-l', LANG, '--psm', PSM,
           '-c', 'preserve_interword_spaces=1']
    if os.path.isdir(TDIR):
        cmd += ['--tessdata-dir', TDIR]
    r = subprocess.run(cmd, input=png_bytes, capture_output=True)
    if r.returncode != 0:
        return f'[OCR ERROR: {r.stderr.decode("utf-8", "replace")[:200]}]'
    return r.stdout.decode('utf-8', 'replace').strip()


def main():
    pdf_path, out_path = sys.argv[1], sys.argv[2]
    start_page = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    if not os.path.isfile(TESS):
        sys.exit(f'Khong thay tesseract.exe tai {TESS}')
    if not os.path.isdir(TDIR):
        sys.exit(f'Khong thay thu muc tessdata tai {TDIR}')

    # Thất bại sớm: nếu thiếu vie.traineddata thì dừng ngay, đừng chạy 500 trang rác.
    probe = subprocess.run([TESS, '--list-langs', '--tessdata-dir', TDIR],
                           capture_output=True, text=True)
    if 'vie' not in probe.stdout:
        sys.exit(f'Khong nap duoc goi tieng Viet tu {TDIR}: {probe.stderr[:200]}')

    doc = fitz.open(pdf_path)
    n = len(doc)
    mode = 'a' if start_page > 0 else 'w'
    with open(out_path, mode, encoding='utf-8') as f:
        for i in range(start_page, n):
            t0 = time.time()
            png = doc[i].get_pixmap(dpi=DPI, colorspace=fitz.csGRAY).tobytes('png')
            text = ocr_page(png)
            f.write(f'\n\n<!-- page {i+1}/{n} -->\n\n{text}\n')
            f.flush()
            print(f'page {i+1}/{n} done in {time.time()-t0:.1f}s', flush=True)

    print('ALL DONE', pdf_path)


if __name__ == '__main__':
    main()
