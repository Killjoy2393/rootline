from modeltranslation.translator import register, TranslationOptions
from .models import Project, MetaData


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description',)


@register(MetaData)
class MetaDataTranslationOptions(TranslationOptions):
    fields = ('meta_description', 'meta_description')