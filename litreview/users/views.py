from django.urls import reverse
from django.views import generic

from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse('account_login')