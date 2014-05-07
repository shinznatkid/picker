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

	output_html = ''

	for config_item in picker_settings.CONFIG:
		file_path = static('picker/%s' % picker_settings.PICKER_REPO[config_item]['main'])
		scripts = '<script src="%s"></script>' % file_path
		output_html += format_html(scripts)
	return output_html
