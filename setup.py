#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
dk-template - debugging django templates.

Parse a django template and find all template variables that are used.
Output the template variables in a format that can be included in the
template to verify the values of all context variables.
"""
import sys

classifiers = """\
Development Status :: 3 - Alpha
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Topic :: Software Development :: Libraries
"""

import setuptools

version = '1.0.1'


setuptools.setup(
    name='dk-template',
    version=version,
    install_requires=[
        'django==1.7.11',
        'dk'
    ],
    author='Bjorn Pettersen',
    author_email='bp@datakortet.no',
    description=__doc__.strip(),
    classifiers=[line for line in classifiers.split('\n') if line],
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(exclude=['tests']),
    zip_safe=False,
)
