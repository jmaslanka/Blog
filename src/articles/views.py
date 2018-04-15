from django.views.generic import (
    ListView,
    DetailView,
)


from .mixins import ArticleQuerysetMixin


class ArticleListView(ArticleQuerysetMixin, ListView):
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 5


class ArticleDetailView(ArticleQuerysetMixin, DetailView):
    template_name = 'articles/details.html'
    context_object_name = 'article'
