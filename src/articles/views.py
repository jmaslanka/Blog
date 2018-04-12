from django.views.generic import (
    ListView,
    DetailView,
)


from .mixins import ArticleQuerysetMixin


class ArticleListView(ArticleQuerysetMixin, ListView):
    template_name = 'articles/list.html'
    paginate_by = 5


class ArticleDetailView(ArticleQuerysetMixin, DetailView):
    template_name = 'articles/list.html'  # For now
