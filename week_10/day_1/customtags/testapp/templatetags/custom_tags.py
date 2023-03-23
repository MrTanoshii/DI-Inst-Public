from django import template

from datetime import datetime

register = template.Library()


@register.simple_tag
def my_tag():
    return "Hello World!"


@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)
