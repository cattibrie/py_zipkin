#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup
import os

__version__ = '0.12.0'

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

setup(
    name='py_zipkin',
    version=__version__,
    provides=["py_zipkin"],
    author='Yelp, Inc.',
    author_email='opensource+py-zipkin@yelp.com',
    license='Copyright Yelp 2018',
    url="https://github.com/Yelp/py_zipkin",
    description='Library for using Zipkin in Python.',
    long_description='\n\n'.join((read('README.md'), read('CHANGELOG.rst'))),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=('tests*', 'testing*', 'tools*')),
    package_data={'': ['*.thrift']},
    install_requires=[
        'six',
        'thriftpy',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
