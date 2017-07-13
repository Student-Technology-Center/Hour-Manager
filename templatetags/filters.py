'''
Here we can define custom filters for template usage
'''

from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime, date

register = template.Library()

@register.filter(name='time_format')
@stringfilter
def time_format(value):
    time = value.split(':')
    tod = ""

    if int(time[0]) >= 12:
        tod = "P.M."
    else:
        tod = "A.M."

    return "{}:{} {}".format(time[0][1] if time[0][0] == '0' else time[0], time[1], tod)