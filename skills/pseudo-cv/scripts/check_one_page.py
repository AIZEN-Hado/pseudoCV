#!/usr/bin/env python3
"""Compile a resume .tex file and check that it fills exactly one page.

Usage:  python3 check_one_page.py resume.tex [--keep-pdf]

The first line is always a status:
  OK                     1 page and well filled (FILL between 94% and 100%)
  UNDERFILLED            1 page but noticeable empty space at the bottom (FILL < 94%)
  OVERFLOW               more than 1 page
  NO_LATEX               no pdflatex / xelatex / tectonic found
  COMPILE_ERROR          compile failed; the first LaTeX errors follow
  LEFTOVER_PLACEHOLDERS  template <<PLACEHOLDERS>> still present (listed)
The second line, when compiled, is:  PAGES=<n> FILL=<pct>%
FILL = how far down the usable area of page 1 the last line of text reaches.
Exit code: 0 for OK, 1 otherwise.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MARGIN_PT = 18.0          # template uses 0.25in margins = 18pt
TARGET_MIN_FILL = 94.0    # below this the page looks empty


def find_engine():
    for name in ("pdflatex", "xelatex", "tectonic"):
        path = shutil.which(name)
        if path:
            return name, path
    return None, None


def measure(pdf: Path):
    """Return (pages, fill_percent or None)."""
    if not shutil.which("pdftotext"):
        pages = None
        if shutil.which("pdfinfo"):
            out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
            m = re.search(r"^Pages:\s+(\d+)", out, re.M)
            pages = int(m.group(1)) if m else None
        if pages is None:
            pages = max(1, len(re.findall(rb"/Type\s*/Page(?!s)", pdf.read_bytes())))
        return pages, None
    html = subprocess.run(["pdftotext", "-bbox", str(pdf), "-"],
                          capture_output=True, text=True).stdout
    page_tags = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">', html)
    pages = len(page_tags)
    first = html.split("</page>")[0]
    ys = [float(y) for y in re.findall(r'<word [^>]*yMax="([\d.]+)"', first)]
    if not page_tags or not ys:
        return pages, None
    height = float(page_tags[0][1])
    usable = height - 2 * MARGIN_PT
    fill = (max(ys) - MARGIN_PT) / usable * 100
    return pages, round(min(fill, 100.0), 1)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    tex = Path(sys.argv[1]).resolve()
    keep_pdf = "--keep-pdf" in sys.argv
    if not tex.is_file():
        print(f"COMPILE_ERROR\nFile not found: {tex}")
        return 1

    leftovers = sorted(set(re.findall(r"<<[^<>]+>>", tex.read_text(encoding="utf-8"))))
    if leftovers:
        print("LEFTOVER_PLACEHOLDERS")
        print("\n".join(f"  {item}" for item in leftovers))
        return 1

    name, engine = find_engine()
    if not engine:
        print("NO_LATEX\nInstall TeX Live (pdflatex + tex-gyre) or tectonic, or compile in Overleaf.")
        return 1

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        if name == "tectonic":
            cmd = [engine, "--outdir", str(tmpdir), str(tex)]
        else:
            cmd = [engine, "-interaction=nonstopmode", "-halt-on-error",
                   f"-output-directory={tmpdir}", str(tex)]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=tex.parent, timeout=180)
        pdf = tmpdir / (tex.stem + ".pdf")
        if proc.returncode != 0 or not pdf.exists():
            print("COMPILE_ERROR")
            log = proc.stdout + proc.stderr
            errors = [ln for ln in log.splitlines() if ln.startswith("!") or "Error" in ln]
            print("\n".join(errors[:10]) or log[-1500:])
            return 1

        pages, fill = measure(pdf)
        fill_txt = f"{fill}%" if fill is not None else "unknown"
        if pages > 1:
            status, hint = "OVERFLOW", "Cut the least JD-relevant bullet or shorten long bullets, then re-run."
        elif fill is not None and fill < TARGET_MIN_FILL:
            status, hint = "UNDERFILLED", ("Page looks empty at the bottom. Expand in order: summary -> one more "
                                           "bullet or detail per project -> extra skills row / real achievement. "
                                           "Re-run after each change.")
        else:
            status, hint = "OK", ""
        print(status)
        print(f"PAGES={pages} FILL={fill_txt}")
        if hint:
            print(hint)
        if keep_pdf:
            out = tex.with_suffix(".pdf")
            shutil.copy(pdf, out)
            print(f"PDF saved: {out}")
        return 0 if status == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
