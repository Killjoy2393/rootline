from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Project,  MetaData

@admin.register(Project)
class ProjectAdmin(TranslationAdmin): 
    list_display = ('title', 'short_description')
    search_fields = ('title', 'short_description')
    filter_horizontal = ('services',) 


@admin.register(MetaData)
class MetaDataAdmin(TranslationAdmin):
    list_display = ('meta_description', 'meta_keywords')

    def has_add_permission(self, request):
      if MetaData.objects.exists():
          return False
      return True 
