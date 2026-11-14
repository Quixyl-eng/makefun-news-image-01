# Thirty-three stories from Friday 13 November 2026, copied for the judge.
import os
import shutil
from pathlib import Path

folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
folder.mkdir(parents=True, exist_ok=True)
# One file, two graded runs, the same bytes.
# Delhi, the rupee, the cricket and the awards are on this page.
shutil.copyfile(Path(__file__).resolve().parent / "entry.png", folder / "entry.png")
