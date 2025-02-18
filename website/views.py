from django.shortcuts import render
from services.models import Service 
from projects.models import Project
from reviews.models import Review
from blog.models import Article
from .models import HeroSection, InfoBlock, ServicesBlock, ProjectsBlock, ReviewsBlock, ArticlesBlock, MetaData
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactFormModelForm
from django.utils.translation import gettext_lazy as _


def handle_contact_form_submission(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Ваше повідомлення успішно відправлено! Незабаром ми з вами зв'яжемось"))  # Успешное сообщение
        else:
            messages.error(request, _("Помилка при відправці форми. Перевірте введені дані."))  # Ошибка валидации

        # Рендерим ту же страницу без редиректа
        

    return redirect(request.META.get('HTTP_REFERER', '/')) 



def home(request):
    hero_section = HeroSection.objects.last()
    info_block = InfoBlock.objects.last()
    services_block = ServicesBlock.objects.last()
    projects_block = ProjectsBlock.objects.last()
    reviews_block = ReviewsBlock.objects.last()
    articles_block = ArticlesBlock.objects.last()

    form = ContactFormModelForm()
    
    meta = MetaData.objects.last() 

    services = Service.objects.all()[:3]
    articles = Article.objects.all()[:3]
    projects = Project.objects.all()[:7]
    reviews =  Review.objects.all()


    payload = {
        'hero_section': hero_section,
        'info_block': info_block,
        'services_block': services_block,
        'projects_block': projects_block,
        'reviews_block': reviews_block,
        'articles_block': articles_block,
        'services':  services,
        'projects':  projects,
        'reviews': reviews,
        'articles': articles,
        'form': form,
        'meta': meta
    }


    return render(request, 'website/Home.html', payload)
