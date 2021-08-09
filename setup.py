from setuptools import setup

import sys
if sys.version_info[0]>=3:
    install_requires = []
else:
    install_requires = ['pathlib2', 'contextlib2']

setup(
    name='zipfile39',
    description='Backport of zipfile Python 3.9 to Python 2.7 with some enhancements',
    long_description=open("README.md").read(),
    version='0.0.1.2',
    url='https://github.com/cielavenir/zipfile39',
    license='PSF',
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    py_modules=['zipfile39'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
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
