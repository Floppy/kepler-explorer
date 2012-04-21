from django.conf.urls.defaults import *

from .views import SystemList, SystemDetail, PlanetList, PlanetDetail


urlpatterns = patterns('',
    url(r'^systems/$', SystemList.as_view(), name='system-list'),
    url(r'^systems/(?P<pk>[^/]+)/$', SystemDetail.as_view(), name='system-detail'),
    url(r'^planets/$', PlanetList.as_view(), name='planet-list'),
    url(r'^planets/(?P<pk>[^/]+)/$', PlanetDetail.as_view(), name='planet-detail'),
)

