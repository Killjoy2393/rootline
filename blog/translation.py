from modeltranslation.translator import register, TranslationOptions
from .models import Article, MetaData

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(MetaData)
class MetaDataTranslationOptions(TranslationOptions):
    fields = ('meta_description', 'meta_keywords')
