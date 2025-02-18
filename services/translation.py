from modeltranslation.translator import register, TranslationOptions
from .models import Service, MetaData


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_title',)


@register(MetaData)
class MetaDataTranslationOptions(TranslationOptions):
    fields = ('meta_description', 'meta_keywords')