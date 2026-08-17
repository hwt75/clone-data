import sys
import time
import numpy as np
import fitz
import easyocr

pdf_path, out_path, start_page = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 0

reader = easyocr.Reader(['vi'], gpu=False)
doc = fitz.open(pdf_path)
n = len(doc)

mode = 'a' if start_page > 0 else 'w'
with open(out_path, mode, encoding='utf-8') as f:
    for i in range(start_page, n):
        t0 = time.time()
        pix = doc[i].get_pixmap(dpi=300)
        arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        try:
            blocks = reader.readtext(arr, detail=0, paragraph=True)
        except Exception as e:
            blocks = [f'[OCR ERROR: {e!r}]']
        text = '\n'.join(blocks)
        f.write(f'\n\n<!-- page {i+1}/{n} -->\n\n{text}\n')
        f.flush()
        print(f'page {i+1}/{n} done in {time.time()-t0:.1f}s', flush=True)

print('ALL DONE', pdf_path)
