from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import About

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')

    def has_add_permission(self, request):
      if About.objects.exists():
          return False
      return True

    