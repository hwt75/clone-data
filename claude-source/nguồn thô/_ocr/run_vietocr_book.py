"""OCR một cuốn bằng VietOCR, tạo BẢN ĐỐI CHỨNG cho bản Tesseract.

    python run_vietocr_book.py <tiền tố tên PDF> <tên file ra> [start_page]

Vì sao cần hai bản: hai máy sai ở những chỗ khác nhau. Ví dụ thật trong sách
Nhân tướng, tr.317: Tesseract đọc "Bến luân", VietOCR đọc đúng "Bổn luân"; ngược
lại có chỗ Tesseract đúng mà VietOCR sai. **Chỗ hai bản bất đồng chính là chỗ
cần mở ảnh trang ra xem** — xem so_sanh_ocr.py.
"""
import os
import sys
import time

import fitz
import numpy as np
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _ocr -> nguồn thô -> vault
SRC = os.path.join(VAULT, 'nguồn thô')


def cut_lines(img):
    a = np.array(ImageOps.autocontrast(img))
    ink = a < a.mean() - a.std() * 0.4
    rows = ink.sum(axis=1)
    idx = np.where(rows > max(2, rows.max() * 0.02))[0]
    if len(idx) == 0:
        return []
    bands, start, prev = [], idx[0], idx[0]
    for i in idx[1:]:
        if i - prev > 3:
            bands.append((start, prev))
            start = i
        prev = i
    bands.append((start, prev))
    out = []
    for y1, y2 in bands:
        if y2 - y1 + 1 < 12:
            continue
        ya, yb = max(0, y1 - 6), min(img.height, y2 + 7)
        xs = np.where(ink[ya:yb].sum(axis=0) > 0)[0]
        if len(xs):
            out.append(img.crop((max(0, xs[0] - 6), ya,
                                 min(img.width, xs[-1] + 6), yb)))
    return out


def main():
    prefix, outname = sys.argv[1], sys.argv[2]
    start = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    pdf = os.path.join(SRC, next(f for f in os.listdir(SRC) if f.startswith(prefix)))
    out = os.path.join(HERE, outname)

    from vietocr.tool.config import Cfg
    from vietocr.tool.predictor import Predictor
    cfg = Cfg.load_config_from_name('vgg_transformer')
    cfg['device'] = 'cpu'
    cfg['cnn']['pretrained'] = False
    voc = Predictor(cfg)

    doc = fitz.open(pdf)
    n = len(doc)
    with open(out, 'a' if start > 1 else 'w', encoding='utf-8') as f:
        for i in range(start, n + 1):
            t0 = time.time()
            pix = doc[i - 1].get_pixmap(dpi=300, colorspace=fitz.csGRAY)
            img = Image.frombytes('L', (pix.width, pix.height), pix.samples)
            text = '\n'.join(voc.predict(l.convert('RGB')) for l in cut_lines(img))
            f.write(f'\n\n<!-- page {i}/{n} -->\n\n{text}\n')
            f.flush()
            print(f'page {i}/{n} done in {time.time()-t0:.1f}s', flush=True)
    print('ALL DONE', pdf)


if __name__ == '__main__':
    main()
