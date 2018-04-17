from django.conf.urls import url

from .views import (
    ArticleListView,
    ArticleDetailView,
    TagArticleListView,
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
    url(
        r'^tag/(?P<slug>[\w-]+)',
        TagArticleListView.as_view(),
        name='by_tag'
    )
]
