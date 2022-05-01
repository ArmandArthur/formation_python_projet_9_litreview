from django.urls import path

from . import views

urlpatterns = [
    path('home', views.PostsListView.as_view(), name='list_posts'),
   
]