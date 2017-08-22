"""config URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='pages/index.html'), name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^api/', include('apps.reservation.urls', namespace='api')),
    url(r'^api/docs/', include_docs_urls(title='Reservations')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

