from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Article
from .forms import ContactForm, ArticleForm


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def add_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        # titre = form.cleaned_data['titre']
        # auteur = form.cleaned_data['auteur']
        # slug = form.cleaned_data['slug']
        # contenu = form.cleaned_data['contenu']
        # categorie = form.cleaned_data['categorie']

        # data = {
        #     'titre': titre,
        #     'slug': slug,
        #     'auteur': auteur,
        #     'contenu': contenu,
        #     'categorie': categorie
        # }

        form.save()

    return render(request, 'blog/add_article.html', {'form': form})


def edit_article(request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()

    return render(request, 'blog/edit_article.html', {'form': form, 'id': id})


def show_article(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/show.html', {'article': article})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        _from = form.cleaned_data['_from']
        copy = form.cleaned_data['copy']

        # send email here
        send = True

    return render(request, 'blog/contact.html', locals())


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def somme(request, nombre1, nombre2):
    total = nombre1 + nombre2

    return render(request, 'blog/somme.html', locals())
