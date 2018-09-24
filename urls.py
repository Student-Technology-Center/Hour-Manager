from django.conf.urls import url, include

import hour_manager.views as view

urlpatterns = [
    url(r'^$', view.index),
    url(r'post/', view.post),
    url(r'history/', view.history),
    url(r'api/', include('hour_manager.api.api_urls')),
]