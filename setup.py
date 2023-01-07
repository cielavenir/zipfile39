from setuptools import setup

versionContext = {}
with open('zipfile39/version.py') as f:
    exec(f.read(), versionContext)

import sys
install_requires = [
    'pathlib2; python_version < "3"',
    'contextlib2; python_version < "3"',
]
extras_require = {
    'all': [
        'backports.lzma; python_version < "3"',
        'backports.tempfile; python_version < "3"',
        'funcsigs; python_version < "3"',
        'isal',
        'slz',
        'zipfile_deflate64>=0.2.0',
        'codecs7z',
        'dclimplode',
        'zstandard',
        'pyppmd>=0.17.0',
    ],
}

setup(
    name='zipfile39',
    description='Backport of zipfile Python 3.9 to Python 2.7 with some enhancements',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    version=versionContext['__version__'],
    url='https://github.com/cielavenir/zipfile39',
    license='PSF',
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    packages=['zipfile39'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
