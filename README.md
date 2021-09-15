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

### Requisites

- Installation requisites:
    - [pathlib2](https://pypi.org/project/pathlib2/) (Python2 only)
    - [contextlib2](https://pypi.org/project/contextlib2/) (Python2 only)
- Optional requisites:
    - [backports.lzma](https://pypi.org/project/backports.lzma/) (Python2 only)
    - [dclimplode](https://pypi.org/project/dclimplode/)
    - [zstandard](https://pypi.org/project/zstandard/)
    - [isal](https://pypi.org/project/isal/)
        - Python2 need `python -m pip install git+https://github.com/cielavenir/python-isal-py2@0.11.0-py2`
            - (now this branch support macOS as well)
        - Also see https://github.com/cielavenir/python-isal-py2/releases/tag/v0.11.1-py2
    - [slz](https://pypi.org/project/slz/)
    - [pyppmd](https://pypi.org/project/pyppmd/)
        - Python2 need `python -m pip install git+https://github.com/cielavenir/pyppmd-py2@py2`
        - Also see https://github.com/cielavenir/pyppmd-py2/releases/tag/v0.16.1.1
    - [zipfile_deflate64](https://pypi.org/project/zipfile_deflate64/)
        - Due to buffering problem, both Python2 and Python3 should use `python -m pip install git+https://github.com/cielavenir/zipfile-deflate64@py2`
        - Also see https://github.com/cielavenir/zipfile-deflate64/releases/tag/v0.1.6.1
            - For Python3, discussion is ongoing at https://github.com/brianhelba/zipfile-deflate64/pull/18
        - But also note that resumable infback9 implementation (to address buffering problem) is experimental~
