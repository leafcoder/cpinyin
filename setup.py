#!/usr/bin/env python

import io
import posixpath
from setuptools import setup
from distutils.extension import Extension

BASE_DIR = posixpath.abspath(
    posixpath.join(posixpath.dirname(posixpath.dirname(__file__))))
README = io.open(
    posixpath.join(BASE_DIR, 'README.md'), encoding='UTF-8').read()

setup(
    name='cpinyin',
    ext_modules=[
        Extension(
            'cpinyin._cpinyin',
            sources=['src/cpinyin/_cpinyin.pyx'],
        )
    ],
    version='0.1.0',
    description="Rewrite lxneng's xpinyin by cython",
    long_description=README,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='pinyin xpinyin cpinyin',
    author="leafcoder",
    author_email="leafcoder@gmail.com",
    url="https://github.com/leafcoder/cpinyin",
    test_suite='cpinyin.tests',
    package_dir={
        '': 'src',
        'src': 'src/cpinyin'
    },
    install_requires=[
        'Cython==0.29.13',
        'xpinyin==0.5.6'
    ],
    packages=['cpinyin'],
    include_package_data=True,
    license="BSD"
)
