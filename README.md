## zipfile39

- Backport of zipfile Python 3.9 (especially caae717) to older Python including **Python 2.7.**
- Uses backports.lzma for ZIP_LZMA (method 14) Python2 handler.
- Introducing ZIP_XZ (method 95) and ZIP_ZSTANDARD (method 93) handlers.
    - ZIP_ZSTANDARD Python2 uses zstandard 0.14.1 (the last compatible version).

- Installation requisites:
    - pathlib2 (Python2 only)
    - contextlib2 (Python2 only)
- Optional requisites:
    - backports.lzma (Python2 only)
    - zstandard
