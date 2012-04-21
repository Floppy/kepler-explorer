from django.conf.urls.defaults import *

from .views import PlanetList, PlanetDetail, SystemDetail


urlpatterns = patterns('',
    url(r'^$', PlanetList.as_view(), name='planet-list'),
    url(r'^planet/(?P<pk>[^/]+)/$', PlanetDetail.as_view(), name='planet-detail'),
    url(r'^system/(?P<pk>[^/]+)/$', SystemDetail.as_view(), name='system-detail'),
)

