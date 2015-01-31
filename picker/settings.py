from __future__ import absolute_import, unicode_literals


from .exception import PickerException
from django.conf import settings
import json
import os

CONFIG_DEFAULTS = []

USER_CONFIG = getattr(settings, 'PICKER_INSTALLED_APPS', [])

CONFIG = CONFIG_DEFAULTS[:]
for USER_CONFIG_ITEM in USER_CONFIG:
    if USER_CONFIG_ITEM not in CONFIG:
        CONFIG.append(USER_CONFIG_ITEM)

PICKER_REPO = {}
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'repo.json')) as handle:
        PICKER_REPO = json.load(handle)
except IOError:
    PICKER_REPO = {}


PICKER_JS = []
PICKER_CSS = []
PICKER_ASSETS = []
PICKER_LOADED = []


def load_configure(config_item):
    global PICKER_REPO, PICKER_LOADED, PICKER_JS, PICKER_CSS, PICKER_ASSETS
    if config_item not in PICKER_LOADED:
        if config_item not in PICKER_REPO:
            raise PickerException('Repo "%s" not found (Please upgrade django-picker package and try again).' % config_item)

        PICKER_LOADED.append(config_item)
        if 'dependencies' in PICKER_REPO[config_item]:
            for dependency, version in PICKER_REPO[config_item]['dependencies'].items():
                if dependency not in PICKER_LOADED:
                    load_configure(dependency)

        if 'js' in PICKER_REPO[config_item]:
            PICKER_JS += PICKER_REPO[config_item]['js']
        if 'css' in PICKER_REPO[config_item]:
            PICKER_CSS += PICKER_REPO[config_item]['css']
        if 'assets' in PICKER_REPO[config_item]:
            PICKER_ASSETS += PICKER_REPO[config_item]['assets']

for CONFIG_ITEM in CONFIG:
    load_configure(CONFIG_ITEM)
