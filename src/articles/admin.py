from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'publication_date',
        'is_public',
        'tags_list',
    )
    list_editable = (
        'is_public',
    )
    list_filter = (
        'is_public',
        'author',
    )
    readonly_fields = (
        'created',
        'modified',
    )
    raw_id_fields = (
        'author',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = (
        'title',
        'author__name',
        'author__email',
        'tags__name',
    )
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'author',
                'is_public',
                'publication_date',
            )
        }),
        ('Content', {
            'fields': (
                'image',
                'description',
                'content',
                'tags',
            )
        }),
        ('Other', {
            'fields': (
                'created',
                'modified',
            )
        })
    )

    def get_queryset(self, request):
        return super().get_queryset(request) \
            .select_related('author') \
            .prefetch_related('tags')

    def tags_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all()[:3])


admin.site.register(Article, ArticleAdmin)
