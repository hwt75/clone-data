import sys, os, runpy

# Tên tệp PDF trong `nguồn thô/` lưu ở dạng Unicode NFD, nên chuỗi literal NFC
# không khớp — phải dò bằng listdir thay vì ghép đường dẫn cứng.
HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _ocr -> nguồn thô -> vault
SRC = os.path.join(VAULT, 'nguồn thô')
PDF = os.path.join(SRC, next(f for f in os.listdir(SRC) if f.startswith('kinhdich-S')))
OUT = os.path.join(HERE, 'tamchu_ocr_raw.md')
start = sys.argv[1] if len(sys.argv) > 1 else '0'

# v3 = Tesseract 5 + vie (đang dùng) · v2 = VietOCR · ocr_book.py = EasyOCR (bản đầu)
ENGINE = os.path.join(HERE, 'ocr_book_v3.py')
sys.argv = [ENGINE, PDF, OUT, start]
runpy.run_path(ENGINE, run_name='__main__')
