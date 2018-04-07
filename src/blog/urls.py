from django.contrib import admin
from django.conf import settings
from django.conf.urls import (
    url,
    include,
)


urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
