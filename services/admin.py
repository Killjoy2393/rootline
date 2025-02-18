from django.contrib import admin
from modeltranslation.admin import TranslationAdmin 
from .models import Service, MetaData

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}  # Генерация slug из title


@admin.register(MetaData)
class MetaDataAdmin(TranslationAdmin):
    list_display = ('meta_description', 'meta_keywords')

    def has_add_permission(self, request):
      if MetaData.objects.exists():
          return False
      return True 

