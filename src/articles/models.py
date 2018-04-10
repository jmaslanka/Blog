from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID
from taggit.managers import TaggableManager


class PublishedArticleManager(models.Manager):
    def ger_queryset(self):
        return super().get_queryset().filter(
            is_public=True,
            publication_date__lte=timezone.now(),
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

    image = StdImageField(
        upload_to=UploadToUUID(path='articles'),
        variations={
            'cover': (720, 480),
        },
        blank=True,
    )
    description = models.TextField(
        _('description'),
        max_length=255,
    )
    content = RichTextUploadingField()

    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        _('modified'),
        auto_now=True,
    )

    tags = TaggableManager()
    published = PublishedArticleManager()

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        return self.description[:50]
