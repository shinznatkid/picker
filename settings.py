from __future__ import absolute_import, unicode_literals

import warnings

from django.conf import settings
from django.utils import six
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
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'repo.json')) as handle:
        PICKER_REPO = json.load(handle)
except IOError:
    PICKER_REPO = {}

for CONFIG_ITEM in CONFIG:
	if CONFIG_ITEM not in PICKER_REPO:
		CONFIG.remove(CONFIG_ITEM)
