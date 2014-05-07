# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-picker',
    version='0.1.0',
    author=u'ShinZ Natkid',
    author_email='shinznatkid@gmail.com',
    packages=['picker'],
    url='http://github.com/shinznatkid/picker',
    license='BSD licence',
    description='Choose your javascript, css framework into your project.',
    long_description=open('README.md').read(),
    zip_safe=False,
    install_requires=[
        "Django >= 1.4.0",
    ],
)