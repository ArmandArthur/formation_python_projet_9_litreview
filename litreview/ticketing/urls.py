from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.TicketCreateView.as_view(), name='add_ticket'),
    path('detail/<int:pk>', views.TicketDetailView.as_view(), name='detail_ticket'),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]