from django.conf.urls import url

import hour_manager.api

urlpatterns = [
    url(r'^hour/(?P<pk>\d+)/$', hour_manager.api.hour, name='hour_json')
]