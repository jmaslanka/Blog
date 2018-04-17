from .models import Article


class ArticleQuerysetMixin:
    queryset = Article.published.all()

    def get_queryset(self):
        queryset = super().get_queryset() \
            .select_related('author', 'category') \
            .prefetch_related('tags') \
            .order_by('-created')

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(title__icontains=q)

        return queryset
