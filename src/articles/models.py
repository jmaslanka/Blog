from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID
from taggit.managers import TaggableManager
from taggit.models import ItemBase, TagBase


class Category(models.Model):
    name = models.CharField(
        _('name'),
        max_length=32,
        unique=True,
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    @cached_property
    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return reverse('article:by_category', kwargs={'slug': self.slug})


class ArticleTag(TagBase):

    class Meta:
        verbose_name = _('Article tag')
        verbose_name_plural = _('Article tags')


class TaggedArticle(ItemBase):
    tag = models.ForeignKey(
        ArticleTag,
        related_name='tag_items',
    )
    content_object = models.ForeignKey(
        'Article',
        related_name='tag_items',
    )

    @classmethod
    def tags_for(cls, model, instance=None, **extra_filters):
        kwargs = extra_filters or {}
        if instance is not None:
            kwargs.update({
                '%s__content_object' % cls.tag_relname(): instance
            })
            return cls.tag_model().objects.filter(**kwargs)
        kwargs.update({
            '%s__content_object__isnull' % cls.tag_relname(): False
        })

        return cls.tag_model().objects.filter(**kwargs).distinct()


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_public=True,
        )


class Article(models.Model):
    title = models.CharField(
        _('title'),
        max_length=224,
    )
    slug = models.SlugField(
        _('slug'),
        max_length=255,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('author'),
        related_name='articles',
    )
    is_public = models.BooleanField(
        _('is public'),
        default=False,
    )
    publication_date = models.DateTimeField(
        _('publication date'),
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_('category'),
        related_name='articles',
    )

    image = StdImageField(
        upload_to=UploadToUUID(path='articles'),
        variations={
            'cover': (742, 422),
        },
        blank=True,
    )
    description = models.TextField(
        _('description'),
        max_length=255,
    )
    content = RichTextUploadingField()

    views_count = models.PositiveSmallIntegerField(
        _('views count'),
        default=0,
        editable=True,
    )
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        _('modified'),
        auto_now=True,
    )

    objects = models.Manager()
    tags = TaggableManager(through=TaggedArticle)
    published = PublishedArticleManager()

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:details', kwargs={'slug': self.slug})
