from modeltranslation.translator import register, TranslationOptions
from .models import HeroSection, InfoBlock, ServicesBlock, ProjectsBlock, ReviewsBlock, ArticlesBlock, MetaData

@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'button_text')


@register(InfoBlock)
class InfoBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'caption', 'span', 'button_text')


@register(ServicesBlock)
class ServicesBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'link_text')


@register(ProjectsBlock)
class ProjectsBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'link_text',)


@register(ReviewsBlock)
class ReviewsBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'caption',)


@register(ArticlesBlock)
class ReviewsBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'link_text',)


@register(MetaData)
class MetaDataTranslationOptions(TranslationOptions):
    fields = ('meta_description', 'meta_keywords')