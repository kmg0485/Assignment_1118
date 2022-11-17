from django import template
from django.db import connection
from django.core.wsgi import get_wsgi_application
import sys


register = template.Library()

@register.simple_tag
def get_database_info():
    return connection.settings_dict['ENGINE']

@register.simple_tag(takes_context=True)
def get_request_info(context):
    return context['request'].headers['Host']

@register.simple_tag
def get_wsgi_info():
    return f"python {' '.join(sys.argv)}"