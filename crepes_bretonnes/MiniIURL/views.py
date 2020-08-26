from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import MiniURL
from .forms import URLGenForm


# def generate_url(request):
#     form = URLGenForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('url_list')
#
#     return render(request, 'MiniURL/new_url.html', {'form': form})

class URLCreate(CreateView):
    model = MiniURL
    template_name = 'MiniURL/new_url.html'
    form_class = URLGenForm
    success_url = reverse_lazy('url_list')


class URLUpdate(UpdateView):
    model = MiniURL
    template_name = 'MiniURL/new_url.html'
    form_class = URLGenForm
    success_url = reverse_lazy('url_list')

    def get_object(self, queryset=None):
        mini_url = self.kwargs.get('mini_url', None)
        return get_object_or_404(MiniURL, mini_url=mini_url)

    # def form_valid(self, form):
    #     self.object = form.save()
    #     # send mess to user
    #     messages.success(self.request, "Votre profil a été mis à jour avec succès")
    #     return HttpResponseRedirect(self.get_success_url())


class URLDelete(DeleteView):
    model = MiniURL
    template_name = 'MiniURL/delete.html'
    context_object_name = "mini_url"
    success_url = reverse_lazy('url_list')

    def get_object(self, queryset=None):
        mini_url = self.kwargs.get('mini_url', None)
        return get_object_or_404(MiniURL, mini_url=mini_url)


def redirection(request, mini_url):
    """ Redirection vers l'URL enregistrée """

    mini = get_object_or_404(MiniURL, mini_url=mini_url)
    mini.nb_access += 1
    mini.save()

    return redirect(mini.url, permanent=True)
