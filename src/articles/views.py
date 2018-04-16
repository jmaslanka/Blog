from django.db.models import F
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
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        response = self.render_to_response(context)

        Article.objects.filter(
            id=self.object.id
        ).update(views_count=F('views_count') + 1)

        return response
