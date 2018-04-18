from django.conf.urls import url

from .views import (
    ArticleListView,
    ArticleDetailView,
    CategoryArticleListView,
    TagArticleListView,
    TagsCategoriesView,
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
    ),
    url(
        r'^category/(?P<slug>[\w-]+)',
        CategoryArticleListView.as_view(),
        name='by_category'
    ),
    url(
        r'^tags-categories/$',
        TagsCategoriesView.as_view(),
        name='tags_categories_list'
    ),
]
