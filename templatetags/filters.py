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

    hour = time[0]
    minutes = time[1]

    int_hour = int(hour)

    if int_hour >= 12:
        tod = "PM"
        if int_hour > 12:
            hour = str(int_hour - 12)
    else:
        tod = "AM"

    return "{}:{} {}".format("12" if hour == "00" else
                             (hour[1] if hour[0] == '0' else hour),
                             minutes,
                             tod
                            )
