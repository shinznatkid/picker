Picker - Django Assets Manager
======

[![Downloads](https://img.shields.io/travis/shinznatkid/picker.svg)](https://travis-ci.org/shinznatkid/picker/)
[![Downloads](https://img.shields.io/pypi/dm/django-picker.svg)](https://pypi.python.org/pypi/django-picker/)
[![Downloads](https://img.shields.io/pypi/v/django-picker.svg)](https://pypi.python.org/pypi/django-picker/)
[![Downloads](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/django-picker/)

Choose your javascript, css framework into your project.

Installation
------------
1. Python package

        pip install django-picker

2. Add 'picker' to INSTALLED_APPS:

        'picker',

Setting
------------
1. Define PICKER_INSTALLED_APPS in settings.py

        PICKER_INSTALLED_APPS = (
            'jquery',
        )

Use in templates
------------
1. Define following tag in templates

        {% load pickertags %}
2. Define following tag inside body in templates

        {% load pickertags %}
        <html>
            <head>
                {% load_css %}
            </head>
            <body>
                {% load_js %}
            </body>
        </html>
        

Usable list
------------
- jquery *3.6.0*
- bootstrap *5.1.1*
- bootstrap3 *3.2.2*
- bootstrap4 *4.3.1*
- bootstrap5 *5.1.1*
- popper *1.15.1*
- bootstrap-theme *3.2.2*
- bootstrap-cosmo *3.2.2*
- bootstrap4-darkly *4.3.1*
- less *2.3.1*
- ember *1.5.1*
- angularjs *1.3.11*
- vuejs *2.6.10*
- vuejs-dev *2.6.10*
- vue-router *3.0.7*
- fontawesome *5.9.0*
