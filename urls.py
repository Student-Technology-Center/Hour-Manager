'''Sub URLS from the hour manager'''
from django.conf.urls import url, include

from hour_manager.views import index

urlpatterns = [
    url(r'^$', index, name='index')
]
