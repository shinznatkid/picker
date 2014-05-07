# -*- coding: utf-8 -*-
# from distutils.core import setup
from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='django-picker',
    version=version,
    author=u'ShinZ Natkid',
    author_email='shinznatkid@gmail.com',
    packages=find_packages(), #['picker'],
    url='http://github.com/shinznatkid/picker',
    license='BSD',
    include_package_data=True,
    description='Put javascript, css framework into your project.',
    long_description=open('README.md').read(),
    # package_data={
    #     'picker': ['static/*'],
    # },
    install_requires=[
        "django",
    ],
)