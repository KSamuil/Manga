from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('post_link/', views.postView, name='posts'),
]