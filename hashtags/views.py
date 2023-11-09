from . import models
from django.views.generic import ListView, DetailView


class ContentView(ListView):
    queryset = models.Content.objects.all()
    template_name = 'hashtags/content.html'

    def get_queryset(self):
        return models.Content.objects.all()


class ContentDetailView(DetailView):
    template_name = 'hashtags/content_detail.html'

    def get_object(self, **kwargs):
        content_id = self.kwargs.get('id')
        return get_object_or_404(models.Content, id=content_id)