from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='account_login'),
    path('signup/', SignUpView.as_view(), name='account_signup'),
    path('', auth_views.LoginView.as_view(), name='default'),
]
