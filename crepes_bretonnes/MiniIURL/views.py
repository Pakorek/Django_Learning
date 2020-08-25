from django.shortcuts import render, redirect, get_object_or_404
from .models import MiniURL

from .forms import URLGenForm


def generate_url(request):
    form = URLGenForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_list')

    return render(request, 'MiniURL/new_url.html', {'form': form})


def redirection(request, mini_url):
    """ Redirection vers l'URL enregistrée """

    mini = get_object_or_404(MiniURL, mini_url=mini_url)
    mini.nb_access += 1
    mini.save()

    return redirect(mini.url, permanent=True)
