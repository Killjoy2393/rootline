from django.shortcuts import render
from .models import About

def about_page(request):
    about = About.objects.last()  # Получаем последнюю запись (если только одна запись о компании)
    return render(request, 'about/about_page.html', {'about': about})
