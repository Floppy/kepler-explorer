from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView#, TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    # Preview page changes
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='index'),
    url(r'^$', RedirectView.as_view(url='/systems/'), name='index'),
    url(r'', include('celestial.urls')),
)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
