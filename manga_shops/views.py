from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic

class MangaListView(generic.ListView):
    template_name = 'manga/manga_list.html'
    queryset = models.Manga_shops.objects.all()
    def get_queryset(self):
        return models.Manga_shops.objects.all()
class MangaDetailView(generic.DetailView):
    template_name = 'manga/manga_list.html'
    def get_object(self, **kwargs):
        manga_id = self.kwargs.get('id')
        return get_object_or_404(models.Manga_shops, id=manga_id)
class CreateMangaView(generic.CreateView):
    template_name = 'manga/manga_list.html'
    form_class = forms.MangaForm
    queryset = models.Manga_shops.objects.all()
    success_url = '/manga_list/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateMangaView, self).form_valid(form=form)
class DeletMangaView(generic.DeleteView):
    template_name = 'manga/confirm_delete.html'
    success_url = '/manga_list/'
    def get_object(self, **kwargs):
        manga_id = self.kwargs.get('id')
        return get_object_or_404(models.Manga_shops, id=manga_id)
class UpdateMangaView(generic.UpdateView):
    template_name = 'manga/confirm_delete.html'
    form_class = forms.MangaForm
    success_url = '/manga_list/'
    def get_object(self, **kwargs):
        manga_id = self.kwargs.get('id')
        return get_object_or_404(models.Manga_shops, id=manga_id)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateMangaView, self).form_valid(form=form)
class Search(generic.ListView):
    template_name = 'manga/manga_list.html'
    context_object_name = 'manga'
    paginate_by = 5
    def get_queryset(self):
        return models.Manga_shops.objects.filter(title__icontains=self.request.GET.get('q'))
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
