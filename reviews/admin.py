from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Review

@admin.register(Review)
class ReviewAdmin(TranslationAdmin):
    list_display = ("name", "position", "created_at")
    search_fields = ("name", "position", "text")
    ordering = ("-created_at",)