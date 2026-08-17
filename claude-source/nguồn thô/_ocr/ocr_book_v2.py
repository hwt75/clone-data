"""OCR tiếng Việt cho PDF scan — cắt dòng bằng phép chiếu ngang + VietOCR.

Thay cho ocr_book.py (EasyOCR). Đo trên trang 171 của "Chu dịch":

    EasyOCR dpi300  (cũ)   CER 20,4%   WER 37,7%   22 giây/trang
    VietOCR + cắt dòng     CER  0,9%   WER  3,8%   13 giây/trang

Vừa chính xác hơn ~20 lần vừa nhanh hơn, vì VietOCR là bộ nhận dạng *theo dòng*
được huấn luyện riêng cho tiếng Việt, còn khâu dò chữ của EasyOCR (vốn là chỗ
yếu) được thay bằng phép chiếu ngang — hợp với sách một cột, chữ đen nền trắng.

VẪN CÒN HẠN CHẾ: bảng biểu và sơ đồ. Một dòng bảng bị gộp thành một dòng dài
nên VietOCR bịa chữ. Với bảng, phải render trang ra PNG rồi đọc ảnh trực tiếp.

    python ocr_book_v2.py <pdf> <out.md> [start_page]
"""
import sys
import time

import fitz
import numpy as np
from PIL import Image, ImageOps

DPI = 300
MIN_LINE_H = 12      # bỏ vệt bẩn mỏng hơn 12 điểm ảnh
ROW_GAP = 3          # nối các dải cách nhau <= 3 dòng, kẻo vỡ dấu phụ
PAD = 6


def cut_lines(img):
    """Cắt ảnh trang thành danh sách ảnh từng dòng chữ."""
    a = np.array(ImageOps.autocontrast(img))
    ink = a < a.mean() - a.std() * 0.4
    rows = ink.sum(axis=1)
    idx = np.where(rows > max(2, rows.max() * 0.02))[0]
    if len(idx) == 0:
        return []

    bands, start, prev = [], idx[0], idx[0]
    for i in idx[1:]:
        if i - prev > ROW_GAP:
            bands.append((start, prev))
            start = i
        prev = i
    bands.append((start, prev))

    out = []
    for y1, y2 in bands:
        if y2 - y1 + 1 < MIN_LINE_H:
            continue
        ya, yb = max(0, y1 - PAD), min(img.height, y2 + PAD + 1)
        xs = np.where(ink[ya:yb].sum(axis=0) > 0)[0]
        if len(xs) == 0:
            continue
        out.append(img.crop((max(0, xs[0] - PAD), ya,
                             min(img.width, xs[-1] + PAD), yb)))
    return out


def main():
    pdf_path, out_path = sys.argv[1], sys.argv[2]
    start_page = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    from vietocr.tool.config import Cfg
    from vietocr.tool.predictor import Predictor
    cfg = Cfg.load_config_from_name('vgg_transformer')
    cfg['device'] = 'cpu'
    cfg['cnn']['pretrained'] = False
    voc = Predictor(cfg)

    doc = fitz.open(pdf_path)
    n = len(doc)
    mode = 'a' if start_page > 0 else 'w'
    with open(out_path, mode, encoding='utf-8') as f:
        for i in range(start_page, n):
            t0 = time.time()
            pix = doc[i].get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
            img = Image.frombytes('L', (pix.width, pix.height), pix.samples)
            try:
                text = '\n'.join(voc.predict(l.convert('RGB')) for l in cut_lines(img))
            except Exception as e:
                text = f'[OCR ERROR: {e!r}]'
            f.write(f'\n\n<!-- page {i+1}/{n} -->\n\n{text}\n')
            f.flush()
            print(f'page {i+1}/{n} done in {time.time()-t0:.1f}s', flush=True)

    print('ALL DONE', pdf_path)


if __name__ == '__main__':
    main()
