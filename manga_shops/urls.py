from django.urls import path
from . import views

urlpatterns = [
    path('manga_list/', views.mangaListView, name='mangaList'),
    path('manga_detail/<int:id>/', views.mangaDetailView, name='detail'),
    path('manga_detail/<int:id>/delete/',
         views.deleteMangaView, name='delete'),
    path('manga_detail/<int:id>/update/',
         views.updateMangaView, name='update'),
    path('/create_manga/', views.createMangaView, name='createManga')
]

