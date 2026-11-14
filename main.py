# The day's news, copied onto the page the judge opens.
import os
import shutil
from pathlib import Path

folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
folder.mkdir(parents=True, exist_ok=True)
shutil.copyfile(Path(__file__).resolve().parent / "entry.png", folder / "entry.png")
