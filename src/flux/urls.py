from django.urls import path
from . import views


urlpatterns = [
    path('home', views.FluxListView.as_view(), name='list_flux'),
    path('answer_ticket/<int:pk>', views.ReviewCreateView.as_view(), name='answer_ticket'),
]
