from django.urls import path
from django.views.generic import TemplateView, ListView
from . import views, models

urlpatterns = [
    path('', ListView.as_view(model=models.MiniURL,
                              template_name='MiniURL/index.html',
                              context_object_name='URLs'), name="url_list"),
    path('generate/', views.generate_url, name="generate_url"),
    path('<slug:mini_url>/', views.redirection, name="redirection"),
]
