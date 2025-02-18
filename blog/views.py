from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article, MetaData

def article_list(request):
    articles = Article.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
    meta = MetaData.objects.first()
    return render(request, 'blog/article_list.html', {'articles': articles, 'meta': meta})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/article_detail.html', {'article': article})
