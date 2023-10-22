from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from . import models, forms

def mangaListView(request):
    manga_value = models.Manga_shops,object.all()
    html_name = 'manga/manga_list.html'
    context = {
        'manga_key': manga_value,
    }
    return render(request, html_name, context)

def mangaDetailView(request, id):
    manga_id = get_object_or_404(models.Manga_shops, id=id)
    html_name ='manga/manga_detail.html'
    context = {
        'manga_id': manga_id
    }
    return render(request, html_name, context)

#CRUD - CREAT READ UPDATE DELETE

#Create
def createMangaView(request):
    method = request.method
    if method == "POST":
        form = forms.MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Манга успешно добавлена')
        else:
            form = forms.MangaForm()

        return render(request, 'manga/create_manga.html', {'form':form})

#delete
def deletMangaView(request, id):
    manga_id = get_object_or_404(models.Manga_shops, id=id)
    manga_id.delete()
    return HttpResponse('Манга успешно удалена')

#update
def updateMangaView(request, id):
    manga_id = get_object_or_404(models.Manga_shops, id=id)
    if request.method == 'POST':
        form = forms.MangaForm(instance=manga_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм изменен')

    else:
        form = forms.MangaForm(instance=manga_id)
    return render(request, 'manga/update_manga.html',
                  {
                      'form': form,
                      'manga_id': manga_id

                      }
                  )
