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
        .only('title', 'slug') \
        .order_by('-views_count')[:limit]


@register.simple_tag
def get_categories(limit=5):
    return Category.objects \
        .annotate(articles_count=Count('articles')) \
        .order_by('-articles_count')[:limit]
