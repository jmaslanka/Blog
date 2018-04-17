from django.db.models import F
from django.utils.translation import gettext as _
from django.views.generic import (
    ListView,
    DetailView,
)

from .mixins import ArticleQuerysetMixin
from .models import Article


class ArticleListView(ArticleQuerysetMixin, ListView):
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 5


class ArticleDetailView(ArticleQuerysetMixin, DetailView):
    template_name = 'articles/details.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        Article.objects.filter(
            id=self.object.id
        ).update(views_count=F('views_count') + 1)

        return response


class TagArticleListView(ArticleListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_title'] = (
            _('Articles with tag: %(tag)s') % {
                'tag': self.kwargs['slug'].replace('-', ' ')
            }
        )
        return context

    def get_queryset(self):
        return super().get_queryset().filter(
            tags__slug=self.kwargs['slug'],
        )


class CategoryArticlesView(ListView):
    pass
