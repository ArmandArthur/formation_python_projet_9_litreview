from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Ticket, Review


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title','description', 'image']
    # permission_required = 'ticketing.add_ticket'
    
    # session
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
