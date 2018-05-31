from django.conf.urls import url

from hour_manager.api.api import Hour

urlpatterns = [
    url(r'^hour/(?P<pk>[0-9])*/?$', Hour.as_view(), name='hour')
]