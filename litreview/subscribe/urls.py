from django.urls import path

from . import views

urlpatterns = [
    path('abo/add/', views.SubscribeCreateView.as_view(), name='add_subscribe')
]