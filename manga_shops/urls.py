from django.urls import path
from . import views

urlpatterns = [
    path('manga_list/', views.MangaListView.as_view(), name='mangaList'),
    path('manga_detail/<int:id>/', views.MangaDetailView.as_view(), name='detail'),
    path('manga_detail/<int:id>/delete/',
         views.DeletMangaView.as_view(), name='delete'),
    path('manga_detail/<int:id>/update/',
         views.UpdateMangaView.as_view(), name='update'),
    path('/create_manga/', views.CreateMangaView.as_view(), name='createManga'),
    path('search/', views.Search.as_view(), name='search'),
]

