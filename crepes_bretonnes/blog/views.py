from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from datetime import datetime
from .models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def show_article(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/show.html', {'article': article})


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def somme(request, nombre1, nombre2):
    total = nombre1 + nombre2

    return render(request, 'blog/somme.html', locals())
