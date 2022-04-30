from django.urls import path

from . import views

urlpatterns = [
    path('ticket/add/', views.TicketCreateView.as_view(), name='add_ticket'),
    path('review_with_ticket/add/', views.ReviewWithTicket.as_view(), name='add_review_with_ticket'),
    path('review_with_ticket/update/<int:pk>', views.ReviewWithTicket.as_view(), name='update_review_with_ticket'),
    path('ticket/update/<int:pk>', views.TicketUpdateView.as_view(), name='update_ticket'),
    path('ticket/delete/<int:pk>', views.TicketDeleteView.as_view(), name='delete_ticket'),
    path('review/delete/<int:pk>', views.ReviewDeleteView.as_view(), name='delete_review')

    # path('ticket/detail/<int:pk>', views.TicketDetailView.as_view(), name='detail_ticket'),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]