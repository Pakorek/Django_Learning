from django.urls import path
from django.views.generic import TemplateView, ListView
from . import views, models


urlpatterns = [
    path('', views.ListArticles.as_view(), name='blog_index'),
    path('categorie/<int:id>', views.ListArticlesByCategory.as_view(), name="show_by_category"),
    path('faq/', TemplateView.as_view(template_name='blog/faq.html')),
    path('article/new', views.add_article, name="add_article"),
    path('article/edit/<int:id>', views.edit_article, name="edit_article"),
    path('article/<int:id>-<slug:slug>', views.show_article, name='show_article'),
    path('contact/', views.contact, name='contact'),
    path('date', views.date_actuelle, name='date'),
    # path('somme/<int:nombre1>/<int:nombre2>/', views.somme, name='somme')
]
