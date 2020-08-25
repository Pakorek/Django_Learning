from django.shortcuts import render
from django.views.generic import ListView
from .models import MiniURL

class ListURL(ListView):
    model = MiniURL
    template_name = 'MiniURL/index.html'
    context_object_name = 'URLs'

