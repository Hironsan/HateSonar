#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys

from setuptools import find_packages, setup

# from m2r import convert

# Package meta-data.
NAME = 'hatesonar'
DESCRIPTION = 'Hate Speech Detection Library for Python'
URL = 'https://github.com/Hironsan/HateSonar'
EMAIL = 'hiroki.nakayama.py@gmail.com'
AUTHOR = 'Hironsan'
LICENSE = 'MIT'

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

required = [
    'numpy>=1.14.0', 'pandas>=0.22.0', 'scikit-learn>=0.19.1', 'scipy>=1.0.0'
]

setup(
    name=NAME,
    version='0.0.4',
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=required,
    include_package_data=True,
    license=LICENSE,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)