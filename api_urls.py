from django.conf.urls import url

import hour_manager.api

urlpatterns = [
    url(r'^hour/(?P<pk>\d+)/$', hour_manager.api.hour, name='hour_json'),
    url(r'^allhours/$', hour_manager.api.all_hours, name="allhours")
]