from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_index'),
    path('article/new', views.add_article, name="add_article"),
    path('article/edit/<int:id>', views.edit_article, name="edit_article"),
    path('article/<int:id>-<slug:slug>', views.show_article, name='show_article'),
    path('contact/', views.contact, name='contact'),
    path('date', views.date_actuelle, name='date'),
    path('somme/<int:nombre1>/<int:nombre2>/', views.somme, name='somme')
]
