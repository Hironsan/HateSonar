#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys

from setuptools import find_packages, setup

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
    'numpy>=1.19.0', 'pandas>=1.1.0', 'scikit-learn>=0.24.0', 'scipy>=1.5.0', 'joblib>=1.0.0'
]

setup(
    name=NAME,
    version='0.0.8',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=required,
    include_package_data=True,
    license=LICENSE,
    python_requires='>=3.9',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
