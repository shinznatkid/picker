import os


TEST_PROJECT_ROOT = os.path.abspath(
    os.environ.get('TEST_PROJECT_ROOT', '/tmp/'),
)

STATIC_ROOT = os.path.join(TEST_PROJECT_ROOT, 'picker_static')

STATIC_URL = '/static/'

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap',
)

SECRET_KEY = 'hellopicker'

INSTALLED_APPS = (
    'picker',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
