# note: this test use additional archive integrity test using 7z #
# note: this test requires all additional dependencies (backports.lzma / zstandard / pyppmd / zipfile_deflate64) #

import os
import sys
import hashlib
import subprocess
import itertools
import pytest
try:
    from tempfile import TemporaryDirectory
except ImportError:
    from backports.tempfile import TemporaryDirectory
try:
    from inspect import signature
except ImportError:
    from funcsigs import signature

mydir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(mydir,'..'))
os.chdir(mydir)

import zipfile39 as zipfile
import dclimplode
#dclimplode.decompressobj = dclimplode.decompressobj_pklib

info7z  = subprocess.check_output(['7z', 'i'])
avail7z = {
    zipfile.ZIP_STORED:      True,                              # method 0
    zipfile.ZIP_DEFLATED:    b'    40108 Deflate'   in info7z,  # method 8
    zipfile.ZIP_DEFLATED64:  b'    40109 Deflate64' in info7z,  # method 9
    zipfile.ZIP_DCLIMPLODED: b'    4010A PKImplode' in info7z,  # method 10
    zipfile.ZIP_BZIP2:       b'    40202 BZip2'     in info7z,  # method 12
    zipfile.ZIP_LZMA:        b'    30101 LZMA'      in info7z,  # method 14
    zipfile.ZIP_ZSTANDARD:   b'  4F71101 ZSTD'      in info7z,  # method 93
    zipfile.ZIP_XZ:          b'       21 LZMA2'     in info7z,  # method 95
    zipfile.ZIP_PPMD:        b'    30401 PPMD'      in info7z,  # method 98
}

fnames = [
    'data/10000SalesRecords.csv',
    # 'data/7zz',
]

methods = [
    (zipfile.ZIP_STORED, 0),
    (zipfile.ZIP_DEFLATED, 6),
    (zipfile.ZIP_DEFLATED64, 6),
    (zipfile.ZIP_DCLIMPLODED, 3),
    (zipfile.ZIP_DCLIMPLODED, 13),
    (zipfile.ZIP_BZIP2, 9),
    (zipfile.ZIP_LZMA, 6),
    (zipfile.ZIP_ZSTANDARD, 3),
    (zipfile.ZIP_XZ, 6),
    (zipfile.ZIP_PPMD, 5),
]
if 'compresslevel' in signature(zipfile._get_compressor).parameters:
    methods.extend([
        (zipfile.ZIP_DEFLATED, 19),
        (zipfile.ZIP_DEFLATED, -10),
        (zipfile.ZIP_DEFLATED, -12),
        (zipfile.ZIP_DEFLATED, -21),
        (zipfile.ZIP_BZIP2, 19),
    ])

@pytest.mark.parametrize('fname,method,level',[
    tuple([fname]+list(method)) for fname, method in itertools.product(fnames, methods)
])
def test_zipfile_writeread(fname,method,level):
    st = os.stat(fname)
    with open(fname, 'rb') as f:
        body = f.read()
        sha256 = hashlib.sha256(body).hexdigest()
    
    with TemporaryDirectory() as tmpdir:
        kwargs = {'compression': method}
        if 'compresslevel' in signature(zipfile._get_compressor).parameters:
            kwargs['compresslevel'] = level
        with zipfile.ZipFile(os.path.join(tmpdir, 'test.zip'), 'w', **kwargs) as zip:
            zip.write(fname)
        if avail7z[method]:
            subprocess.check_call(['7z', 't', os.path.join(tmpdir, 'test.zip')], shell=False)
        with zipfile.ZipFile(os.path.join(tmpdir, 'test.zip'), 'r') as zip:
            info = zip.getinfo(fname)
            assert info.compress_type == method
            dec = zip.read(info)
            assert len(dec) == st.st_size
            assert hashlib.sha256(dec).hexdigest() == sha256

@pytest.mark.parametrize('fname,method,level',[
    tuple([fname]+list(method)) for fname, method in itertools.product(fnames, methods)
])
def test_zipfile_open(fname,method,level):
    chunksiz = 512
    st = os.stat(fname)
    cnt = (st.st_size+chunksiz-1)//chunksiz

    with open(fname, 'rb') as f:
        body = f.read()
        sha256 = hashlib.sha256(body).hexdigest()
    
    with TemporaryDirectory() as tmpdir:
        kwargs = {'compression': method}
        if 'compresslevel' in signature(zipfile._get_compressor).parameters:
            kwargs['compresslevel'] = level
        with zipfile.ZipFile(os.path.join(tmpdir, 'test.zip'), 'w', **kwargs) as zip:
            with zip.open(fname, 'w') as zf:
                for i in range(cnt):
                    zf.write(body[chunksiz*i:chunksiz*(i+1)])
        if avail7z[method]:
            subprocess.check_call(['7z', 't', os.path.join(tmpdir, 'test.zip')], shell=False)
        with zipfile.ZipFile(os.path.join(tmpdir, 'test.zip'), 'r') as zip:
            info = zip.getinfo(fname)
            assert info.compress_type == method
            decsiz = 0
            hashobj = hashlib.sha256()
            with zip.open(info, 'r') as zf:
                while True:
                    dec0 = zf.read(chunksiz)
                    decsiz += len(dec0)
                    hashobj.update(dec0)
                    if len(dec0) < chunksiz:
                        break
                    assert len(dec0) == chunksiz
            assert decsiz == st.st_size
            assert hashobj.hexdigest() == sha256

@pytest.mark.parametrize('fname,level',[
    e for e in itertools.product(fnames, [5])  # list(range(1,10)))
])
def test_zipfile_read_deflate64(fname,level):
    #if sys.version_info[0]<3:
    #    pytest.skip('py2 does not support deflate64')
    chunksiz = 512
    st = os.stat(fname)
    with open(fname, 'rb') as f:
        body = f.read()
        sha256 = hashlib.sha256(body).hexdigest()
    
    with TemporaryDirectory() as tmpdir:
        subprocess.check_call(['7z', 'a', '-tzip', '-mm=Deflate64', '-mx=%d'%level, os.path.join(tmpdir, 'test.zip'), fname], shell=False)
        with zipfile.ZipFile(os.path.join(tmpdir, 'test.zip'), 'r') as zip:
            info = zip.getinfo(fname)
            assert info.compress_type == 9
            decsiz = 0
            hashobj = hashlib.sha256()
            with zip.open(info, 'r') as zf:
                while True:
                    dec0 = zf.read(chunksiz)
                    decsiz += len(dec0)
                    hashobj.update(dec0)
                    if len(dec0) < chunksiz:
                        break
                    assert len(dec0) == chunksiz
            assert decsiz == st.st_size
            assert hashobj.hexdigest() == sha256
