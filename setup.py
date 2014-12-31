# -*- coding: utf-8 -*-
"""
    gyroscope
    ~~~~~~~~~

    Rotate file.

    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from setuptools import setup, find_packages

requires = []

app_name = 'gyroscope'

rst_path = os.path.join(os.path.dirname(__file__), 'README.rst')
description = ''
with open(rst_path) as f:
    description = f.read()

setup(
    name=app_name,
    version='0.2',
    author='Shinya Ohyanagi',
    author_email='sohyanagi@gmail.com',
    url='http://github.com/heavenshell/py-gyroscope',
    description='Rotate file.',
    long_description=description,
    license='BSD',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    package_dir={'': '.'},
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System'
    ],
    tests_require=[],
    test_suite='tests'
)
