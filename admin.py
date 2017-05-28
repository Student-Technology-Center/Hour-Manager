'''Registers our models'''
from django.contrib import admin
from .models import HourModel, hour_history

admin.site.register(HourModel)
admin.site.register(hour_history)



