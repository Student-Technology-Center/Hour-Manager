from . import api_views as view
from django.conf.urls import url

urlpatterns = [
    url(r'claim/', view.claim),
    url(r'delete/(?P<pk>\d+)/?$', view.delete),
]