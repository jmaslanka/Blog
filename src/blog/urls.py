from django.contrib import admin
from django.contrib.staticfiles import views
from django.conf import settings
from django.conf.urls import (
    url,
    include,
)
from django.views.static import serve

import articles.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include(articles.urls, namespace='article')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
