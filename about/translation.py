from modeltranslation.translator import register, TranslationOptions
from .models import About

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'meta_description', 'meta_keywords')
