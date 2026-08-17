"""OCR lại khối 'Hà Lạc giải đoán' (64 quẻ) của sách Xuân Cang bằng VietOCR.

Vì sao không dùng bản Tesseract chung: phông chữ cuốn này (serif + nhiều chữ
nghiêng) bị Tesseract đọc hỏng nhãn mục — "MKHC" ra "MK]IC", "Hào 1" ra "lào I",
"Toán Hà Lạc giải" ra "Toán là Lạc giải". VietOCR đọc đúng các nhãn ấy, mà nhãn
chính là thứ bộ trích cần để cắt mục. Đổi lại chậm hơn (~14 giây/trang).

    python run_tamchu_vietocr.py [start_pdf_page]
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
PDF = os.path.join(SRC, next(f for f in os.listdir(SRC) if f.startswith('kinhdich-S')))
OUT = os.path.join(HERE, 'tamchu_halac_vietocr.md')

FIRST, LAST = 78, 420          # trang PDF: trang in 77..419


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
    start = int(sys.argv[1]) if len(sys.argv) > 1 else FIRST
    from vietocr.tool.config import Cfg
    from vietocr.tool.predictor import Predictor
    cfg = Cfg.load_config_from_name('vgg_transformer')
    cfg['device'] = 'cpu'
    cfg['cnn']['pretrained'] = False
    voc = Predictor(cfg)

    doc = fitz.open(PDF)
    mode = 'a' if start > FIRST else 'w'
    with open(OUT, mode, encoding='utf-8') as f:
        for i in range(start, LAST + 1):
            t0 = time.time()
            pix = doc[i - 1].get_pixmap(dpi=300, colorspace=fitz.csGRAY)
            img = Image.frombytes('L', (pix.width, pix.height), pix.samples)
            text = '\n'.join(voc.predict(l.convert('RGB')) for l in cut_lines(img))
            f.write(f'\n\n<!-- page {i}/608 -->\n\n{text}\n')
            f.flush()
            print(f'page {i}/{LAST} done in {time.time()-t0:.1f}s', flush=True)
    print('ALL DONE')


if __name__ == '__main__':
    main()
