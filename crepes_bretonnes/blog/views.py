from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from datetime import datetime
from .models import Article, Categorie
from .forms import ContactForm, ArticleForm


# def home(request):
#     articles = Article.objects.all()
#     return render(request, 'blog/index.html', {'articles': articles})


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


# def show_article(request, id, slug):
#     article = get_object_or_404(Article, id=id, slug=slug)
#     return render(request, 'blog/show.html', {'article': article})

class ShowArticle(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/show.html'

    def get_object(self, queryset=None):
        # get object with super-class
        article = super(ShowArticle, self).get_object()
        # imaginons un attribut Nb de vues
        article.nb_vues += 1
        article.save()
        # request can be manip with self.request

        return article


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


# def somme(request, nombre1, nombre2):
#     total = nombre1 + nombre2
#
#     return render(request, 'blog/somme.html', locals())

class ListArticles(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/index.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListArticles, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context


class ListArticlesByCategory(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/index.html"
    paginate_by = 3
    # not dynamic
    # queryset = Article.objects.filter(categorie_id=1)

    def get_queryset(self):
        # return Article.objects.filter(categorie_id=self.args[0])
        return Article.objects.filter(categorie_id=self.kwargs['id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListArticlesByCategory, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context


