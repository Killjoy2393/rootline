from django.contrib import admin
from modeltranslation.admin import TranslationAdmin 
from .models import HeroSection, InfoBlock, ServicesBlock, ProjectsBlock, ReviewsBlock, ContactForm, ArticlesBlock, MetaData


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ("name", "email", "phone", "message", "created_at")

    def has_add_permission(self, request):
        """Запрещаем добавление записей вручную"""
        return False


@admin.register(HeroSection)
class HeroSectionAdmin(TranslationAdmin):
    list_display = ("title", "created_at", "updated_at")

    def has_add_permission(self, request):
        if HeroSection.objects.exists():
            return False
        return True
    

@admin.register(InfoBlock)
class InfoBlockAdmin(TranslationAdmin):
    list_display = ("title", "button_text", "created_at", "updated_at")
    search_fields = ("title",)   


    def has_add_permission(self, request):
        if InfoBlock.objects.exists():
            return False
        return True 


@admin.register(ServicesBlock)
class ServicesBlockAdmin(TranslationAdmin):
    list_display = ('title',)


    def has_add_permission(self, request):
      if ServicesBlock.objects.exists():
          return False
      return True 
    

@admin.register(ProjectsBlock)
class ProjectsBlockAdmin(TranslationAdmin):
    list_display = ('title',)


    def has_add_permission(self, request):
      if ProjectsBlock.objects.exists():
          return False
      return True 
    

@admin.register(ReviewsBlock)
class ReviewsBlockAdmin(TranslationAdmin):
    list_display = ('title', 'caption',)


    def has_add_permission(self, request):
      if ReviewsBlock.objects.exists():
          return False
      return True 
    

@admin.register(ArticlesBlock)
class ArticlesBlockAdmin(TranslationAdmin):
    list_display = ('title',)


    def has_add_permission(self, request):
      if ArticlesBlock.objects.exists():
          return False
      return True 
    

@admin.register(MetaData)
class MetaDataAdmin(TranslationAdmin):
    list_display = ('meta_description', 'meta_keywords')


    def has_add_permission(self, request):
      if MetaData.objects.exists():
          return False
      return True 
