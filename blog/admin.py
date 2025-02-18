from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Article, MetaData

@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published_at',)

@admin.register(MetaData)
class MetaDataAdmin(TranslationAdmin):
    list_display = ('meta_description', 'meta_keywords')

    def has_add_permission(self, request):
      if MetaData.objects.exists():
          return False
      return True 