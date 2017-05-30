'''Sub URLS from the hour manager'''
from django.conf.urls import url

from hour_manager.views import index, AddHour, claim_page, history

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^addhour/', AddHour, name='AddHour'),
    url(r'^claimpage/(?P<pk>\d+)/$', claim_page, name='claim_page'),
    url(r'^history/', history, name="history")
]