# -*- coding: utf-8 -*-
# from distutils.core import setup
import os
import sys
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

version = '0.1.5'

setup(
    name='django-picker',
    version=version,
    author=u'ShinZ Natkid',
    author_email='shinznatkid@gmail.com',
    packages=find_packages(),
    url='http://github.com/shinznatkid/picker',
    license='BSD',
    include_package_data=True,
    description='Put javascript, css framework into your project.',
    long_description=open('README.md').read(),
    zip_safe=False,
    install_requires=[
        "django>=1.3.1",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
    ]
)
