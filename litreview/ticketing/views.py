from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title','description','user']
    login_url = '/login/'
    redirect_field_name = '/home'

class TicketDetailView(DetailView):
    model = Ticket
    fields = ['title','description','user']