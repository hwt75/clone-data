import sys, os, runpy

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _ocr -> nguồn thô -> vault
SRC = os.path.join(VAULT, 'nguồn thô')
PDF = os.path.join(SRC, next(f for f in os.listdir(SRC) if f.startswith('TỬ VI')))
OUT = os.path.join(HERE, 'tuvi_ocr_raw.md')
start = sys.argv[1] if len(sys.argv) > 1 else '0'

ENGINE = os.path.join(HERE, 'ocr_book_v3.py')
sys.argv = [ENGINE, PDF, OUT, start]
runpy.run_path(ENGINE, run_name='__main__')
