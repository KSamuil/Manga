from django.urls import path
from . import views

urlpatterns = [
    path('manga_list_parser/', views.ParserMangaListView.as_view()),
    path('start_parsing/', views.ParserFormView.as_view()),
]