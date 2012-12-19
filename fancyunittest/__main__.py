import sys

from .main import main


if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "python -m unittest"

main(module=None)
