[![PyPI](https://img.shields.io/pypi/v/zipfile39)](https://pypi.org/project/zipfile39/)

## zipfile39

- Backport of zipfile Python 3.9 (especially caae717) to older Python including **Python 2.7.**
    - This means Python 2.7 can use `zf.open(name, 'w')`.
- Uses backports.lzma for ZIP_LZMA (method 14) Python2 handler.
- Introduces ZIP_DEFLATED64 (method 9), ZIP_DCLIMPLODED (method 10), ZIP_ZSTANDARD(method 93), ZIP_XZ (method 95) and ZIP_PPMD (method 98) handlers.
    - ZIP_ZSTANDARD Python2 uses zstandard 0.14.1 (the last compatible version).
    - isal / pyppmd / zipfile_deflate64 Python2 use my own backport.
- If isal is installed:
    - crc32 and inflation are accelerated automatically.
    - ZIP_DEFLATED compresslevel -10, -11, -12 and -13 are available, which correspond to isal compression level 0, 1, 2 and 3.
- If slz is installed:
    - ZIP_DEFLATED compresslevel -21 is available.
- If codecs7z is installed:
    - ZIP_DEFLATED/ZIP_BZIP2 compresslevel 11 - 19 are available. Enjoy 7-zip's ultimate compression on Python.

### Requisites

- Installation requisites:
    - [pathlib2](https://pypi.org/project/pathlib2/) (Python2 only)
    - [contextlib2](https://pypi.org/project/contextlib2/) (Python2 only)
- Optional requisites:
    - [backports.lzma](https://pypi.org/project/backports.lzma/) (Python2 only)
    - [dclimplode](https://pypi.org/project/dclimplode/)
    - [zstandard](https://pypi.org/project/zstandard/) or [pyzstd](https://pypi.org/project/pyzstd/) (Py2 unavailable)
    - [isal](https://pypi.org/project/isal/)
        - Python2 need `python -m pip install git+https://github.com/cielavenir/python-isal-py2@0.11.0-py2`
            - (now this branch support macOS as well)
        - Also see https://github.com/cielavenir/python-isal-py2/releases/tag/v0.11.1-py2
    - [slz](https://pypi.org/project/slz/)
    - [codecs7z](https://pypi.org/project/codecs7z/)
    - [pyppmd](https://pypi.org/project/pyppmd/)
        - Python2 need `python -m pip install git+https://github.com/cielavenir/pyppmd-py2@py2`
        - Also see https://github.com/cielavenir/pyppmd-py2/releases/tag/v0.17.0.1
    - [zipfile_deflate64](https://pypi.org/project/zipfile_deflate64/)
        - Need 0.2.0 or later.
        - Python2 need `python -m pip install git+https://github.com/cielavenir/zipfile-deflate64@py2`
        - Also see https://github.com/cielavenir/zipfile-deflate64/releases/tag/v0.2.0.4
        - or [inflate64](https://pypi.org/project/inflate64/) (Py2 unavailable)
- Test requisites:
    - All optional requisites
    - [backports.tempfile](https://pypi.org/project/backports.tempfile/) (Python2 only)
    - [funcsigs](https://pypi.org/project/funcsigs/) (Python2 only)

### Wheels

Some dependencies need complex build procedures. For your sake those wheels are published in actions CI.

### Legal

- I'm not sure about the license term when pyppmd / codecs7z / inflate64 is loaded (I'm not lawyer though).
    - For pyppmd, note that PPMd code itself is public domain. See https://github.com/miurahr/pyppmd/issues/5#issuecomment-892280467 for detail.
