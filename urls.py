'''Sub URLS from the hour manager'''
from django.conf.urls import url

from hour_manager.views import index, AddHour

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^addhour/', AddHour, name='AddHour'),
]