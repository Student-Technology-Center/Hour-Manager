'''Sub URLS from the hour manager'''
from django.conf.urls import url

from hour_manager.views import index, AddHour, claim_page

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^addhour/', AddHour, name='AddHour'),
    url(r'^claimpage/(?P<pk>\d+)/$', claim_page, name='claim_page')
]