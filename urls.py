'''Sub URLS from the hour manager'''
from django.conf.urls import url, include

from hour_manager.views import index, AddHour, claim_page, history, comments

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^addhour/(?P<pk>\d+)?/?$', AddHour, name='AddHour'),
    url(r'^claimpage/(?P<pk>\d+)/$', claim_page, name='claim_page'),
    url(r'^history/', history, name="history"),
    url(r'^comments/', comments, name="comments"),
    url(r'^api/', include('hour_manager.api_urls'))
]
