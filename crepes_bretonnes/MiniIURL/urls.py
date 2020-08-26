from django.urls import path
from django.views.generic import TemplateView, ListView
from . import views, models

urlpatterns = [
    path('', ListView.as_view(model=models.MiniURL,
                              template_name='MiniURL/index.html',
                              context_object_name='URLs'), name="url_list"),
    path('generate/', views.URLCreate.as_view(), name="generate_url"),
    path('update/<slug:mini_url>', views.URLUpdate.as_view(), name="update_url"),
    path('delete/<slug:mini_url>', views.URLDelete.as_view(), name="delete_url"),
    path('<slug:mini_url>/', views.redirection, name="redirection"),
]
