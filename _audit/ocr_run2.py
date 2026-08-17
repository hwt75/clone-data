import fitz, subprocess, sys, os, time

TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = r"D:\claude\.tessdata"

SRC_DIR = r"D:\claude\claude-source\nguồn thô"

def find_pdf(prefix):
    for f in os.listdir(SRC_DIR):
        if f.startswith(prefix):
            return os.path.join(SRC_DIR, f)
    raise FileNotFoundError(prefix)

JOBS = [
    (find_pdf("Chu d"), r"D:\claude\_audit\pages_chudich", r"D:\claude\_audit\ocr\chudich_full.txt"),
    (find_pdf("kinhdich-S"), r"D:\claude\_audit\pages_tamchu", r"D:\claude\_audit\ocr\tamchu_full.txt"),
]

def ocr_page(png_path):
    out_base = png_path[:-4]
    subprocess.run([TESS, png_path, out_base, "-l", "vie", "--psm", "6",
                     "--tessdata-dir", TESSDATA],
                    check=True, capture_output=True)
    with open(out_base + ".txt", "r", encoding="utf-8") as f:
        return f.read()

def run_job(pdf_path, img_dir, out_txt):
    os.makedirs(img_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    n = doc.page_count
    print(f"[{os.path.basename(pdf_path)}] {n} pages", flush=True)
    t0 = time.time()
    with open(out_txt, "w", encoding="utf-8") as out:
        for i in range(n):
            page = doc[i]
            pix = page.get_pixmap(dpi=170, colorspace=fitz.csGRAY)
            png_path = os.path.join(img_dir, f"p{i+1:04d}.png")
            pix.save(png_path)
            text = ocr_page(png_path)
            out.write(f"\n=== trang PDF {i+1} ===\n")
            out.write(text)
            os.remove(png_path[:-4] + ".txt")
            if (i + 1) % 25 == 0:
                elapsed = time.time() - t0
                print(f"  {i+1}/{n} pages, {elapsed:.0f}s elapsed", flush=True)
    print(f"[{os.path.basename(pdf_path)}] DONE in {time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for pdf_path, img_dir, out_txt in JOBS:
        if which != "all" and which not in pdf_path:
            continue
        run_job(pdf_path, img_dir, out_txt)
