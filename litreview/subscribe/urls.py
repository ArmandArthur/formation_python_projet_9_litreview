from django.urls import path

from . import views

urlpatterns = [
    path('abo/manage/', views.SubscribeCreateView.as_view(), name='manage_subscribe')
]