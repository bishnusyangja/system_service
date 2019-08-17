import os
from pathlib import Path

build_dir = Path(__file__).resolve().parents[1]/'static'/'docs'/'build'

os.chdir(Path(__file__).resolve().parent)
os.system('make BUILDDIR="{}" html'.format(str(build_dir)))
