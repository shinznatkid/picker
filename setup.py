# -*- coding: utf-8 -*-
# from distutils.core import setup
import os
import sys
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

version = '1.0.1'

setup(
    name='django-picker',
    version=version,
    author=u'ShinZ Natkid',
    author_email='shinznatkid@gmail.com',
    packages=find_packages(),
    url='http://github.com/shinznatkid/picker',
    license='BSD',
    include_package_data=True,
    install_requires=[
    ],
    description='Put javascript, css framework into your project.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
    ]
)
