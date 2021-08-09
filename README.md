## zipfile39

- Backport of zipfile Python 3.9 (especially caae717) to older Python including **Python 2.7.**
- Uses backports.lzma for ZIP_LZMA (method 14) Python2 handler.
- Introduces ZIP_DEFLATED64 (method 9), ZIP_ZSTANDARD(method 93), ZIP_XZ (method 95) and ZIP_PPMD (method 98) handlers.
    - ZIP_ZSTANDARD Python2 uses zstandard 0.14.1 (the last compatible version).
    - Due to bindings availability, DEFLATED64 is Python3 only.
- If isal is installed:
    - crc32 and inflation are accelerated automatically.
    - compresslevel -1, -2 and -3 are available, which correspond to isal compression level 1, 2 and 3.

- Installation requisites:
    - pathlib2 (Python2 only)
    - contextlib2 (Python2 only)
- Optional requisites:
    - backports.lzma (Python2 only)
    - zstandard
    - isal
        - Python2 need https://github.com/cielavenir/python-isal-py2/releases/tag/v0.11.0-py2
    - pyppmd
        - experimental; need zipfile39_compatible branch for now
        - Python2 need https://github.com/cielavenir/pyppmd/releases/tag/v0.15.2.3 (or `setup.py bdist_wheel` locally)
        - Python3 can do `python3 -m pip install git+https://github.com/cielavenir/pyppmd@zipfile39_compatible2`
- Optional requisites (only available for Python3):
    - zipfile_deflate64
