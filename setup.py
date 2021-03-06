#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from ast import parse
from os import path
try:
    from future_builtins import filter
except ImportError:
    pass

with open("requirements.txt") as f:
    requirements = f.read().split('\n')

with open(path.join('smoomapy', '__init__.py')) as f:
    __version__ = parse(next(filter(lambda line: line.startswith('__version__'),
                                     f))).body[0].value.s

with open("README.rst") as f:
    long_desc = f.read()

setup(
    name='smoomapy',
    version=__version__,
    author="Matthieu Viry",
    author_email="matthieu.viry@cnrs.fr",
    packages=find_packages(),
    description="Brings smoothed maps through python",
    long_description=long_desc,
    url='http://github.com/mthh/smoomapy',
    license="MIT",
    test_suite="tests",
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        ],
    )
