from .models import Article


class ArticleQuerysetMixin:
    queryset = Article.published.all()

    def get_queryset(self):
        return super().get_queryset() \
            .select_related('author', 'category') \
            .prefetch_related('tags')
