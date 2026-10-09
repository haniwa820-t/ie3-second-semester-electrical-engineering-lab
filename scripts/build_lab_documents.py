#!/usr/bin/env python3
"""Compile all report/prelab documents; leave outputs in each lab's build/."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
LATEXMK = shutil.which("latexmk") or "/Library/TeX/texbin/latexmk"


def build(document):
    destination = document.parent / "build"
    destination.mkdir(exist_ok=True)
    result = subprocess.run(
        [LATEXMK, "-r", str(ROOT / ".latexmkrc"), "-g", "-lualatex",
         "-outdir=build", document.name],
        cwd=document.parent, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, text=True,
    )
    (destination / (document.stem + ".build.log")).write_text(result.stdout)
    pdf = destination / (document.stem + ".pdf")
    okay = result.returncode == 0 and pdf.is_file()
    print(("OK   " if okay else "FAIL ") + str(pdf.relative_to(ROOT)), flush=True)
    if not okay:
        print(result.stdout[-2500:], flush=True)
    return okay


if __name__ == "__main__":
    documents = sorted(ROOT.glob("IE3_exp*/*_report.tex"))
    documents += sorted(ROOT.glob("IE3_exp*/*_prelab.tex"))
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(build, documents))
    print(f"{sum(results)}/{len(results)} documents compiled.")
    sys.exit(0 if all(results) else 1)
