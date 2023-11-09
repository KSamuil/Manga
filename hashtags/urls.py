from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.ContentView.as_view()),
    path('content/<int:id>/', views.ContentDetailView.as_view()),
]