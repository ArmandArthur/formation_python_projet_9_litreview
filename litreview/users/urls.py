from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='account_signup'),
    path('login/', auth_views.LoginView.as_view(), name='account_login'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
