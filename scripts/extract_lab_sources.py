"""Extract scanned lab handouts with Ghostscript and Japanese Tesseract."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "source-text"

def extract(pdf, last=None):
    target = OUT / pdf.stem
    target.mkdir(parents=True, exist_ok=True)
    command = [
        "gs", "-q", "-dSAFER", "-dBATCH", "-dNOPAUSE",
        "-sDEVICE=pnggray", "-r180",
    ]
    if last is not None:
        command.append(f"-dLastPage={last}")
    subprocess.run(command + [
        f"-sOutputFile={target}/page-%03d.png", str(pdf),
    ], check=True)
    parts = []
    pages = sorted(target.glob("page-*.png"))
    for page in pages:
        result = subprocess.run([
            "tesseract", str(page), "stdout", "-l", "jpn+eng", "--psm", "3",
        ], check=True, capture_output=True, text=True,
            env={**os.environ, "OMP_THREAD_LIMIT": "1"})
        parts.append(f"\n\n===== {pdf.name} / {page.stem} =====\n\n{result.stdout}")
    (OUT / f"{pdf.stem}.txt").write_text("".join(parts), encoding="utf-8")
    print(f"{pdf.stem}: {len(pages)} pages", flush=True)

if __name__ == "__main__":
    sources = sorted(ROOT.glob("IE3_exp*/*.pdf"))
    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(extract, sources))
