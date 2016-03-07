from __future__ import unicode_literals

from django.utils.html import escapejs, format_html
from django.template.loader import get_template
from django.template.context import Context
from django.template import Library
from django.conf import settings
from picker import settings as picker_settings

register = Library()


@register.simple_tag
def load_js():
    if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
        from django.contrib.staticfiles.templatetags.staticfiles import static
    else:
        from django.templatetags.static import static

    js_html = ''
    for js in picker_settings.PICKER_JS:
        file_path = static('picker/%s' % js)
        scripts = '<script type="text/javascript" src="%s"></script>' % file_path
        js_html += scripts
    return format_html(js_html)


@register.simple_tag
def load_css():
    if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
        from django.contrib.staticfiles.templatetags.staticfiles import static
    else:
        from django.templatetags.static import static

    css_html = ''
    for css in picker_settings.PICKER_CSS:
        file_path = static('picker/%s' % css)
        scripts = '<link rel="stylesheet" type="text/css" href="%s">' % file_path
        css_html += scripts
    return format_html(css_html)
