from django.contrib import admin

from .models import (
    Article,
    Category,
)


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'publication_date',
        'is_public',
        'views_count',
        'category',
    )
    list_editable = (
        'is_public',
    )
    list_filter = (
        'is_public',
    )
    readonly_fields = (
        'views_count',
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
        'slug',
        'author__first_name',
        'author__email',
        'category__name',
        'tags__name',
    )
    save_on_top = True
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'category',
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
        ('Informations', {
            'fields': (
                'views_count',
                'created',
                'modified',
            )
        })
    )

    def get_queryset(self, request):
        return super().get_queryset(request) \
            .select_related('author', 'category') \
            .prefetch_related('tags')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
