from django.conf.urls import url

from .views import (
    ArticleListView,
    ArticleDetailView,
)


urlpatterns = [
    url(
        r'^$',
        ArticleListView.as_view(),
        name='list'
    ),
    url(
        r'^article/(?P<slug>[\w-]+)',
        ArticleDetailView.as_view(),
        name='details'
    ),
]
