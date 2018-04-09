from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
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
                'content',
                'tags',
            )
        }),
        (None, {
            'fields': (
                'created',
                'modified',
            )
        })
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            'tags',
        )

    def tags_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all()[:3])


admin.site.register(Article, ArticleAdmin)
