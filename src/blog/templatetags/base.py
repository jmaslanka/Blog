from django import template
from django.db.models import Count

from taggit.models import Tag

from articles.models import (
    Article,
    Category,
)


register = template.Library()


@register.simple_tag
def get_popular_tags(limit=7):
    return Tag.objects \
        .annotate(articles_count=Count('taggit_taggeditem_items')) \
        .order_by('-articles_count')[:limit]


@register.simple_tag
def get_popular_posts(limit=3):
    return Article.published \
        .only('title', 'slug', 'image') \
        .order_by('-views_count')[:limit]


@register.simple_tag
def get_categories(limit=5):
    return Category.objects \
        .annotate(articles_count=Count('articles')) \
        .order_by('-articles_count')[:limit]


@register.filter
def pagination_range(obj, current=1, limit=6):
    left = limit // 2 + 1
    right = limit // 2
    total = len(obj)

    if limit % 2 == 0:
        right -= 1

    if current < left:
        return obj[:limit]
    if current > total - right:
        return obj[total - limit:]

    return obj[current - left:current + right]
