from django.conf.urls import url

from hour_manager.api.api import hour

urlpatterns = [
    url(r'^hour/(?P<pk>[0-9])*/?$', hour, name='hour')
]