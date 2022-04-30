from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket, Review
from multi_form_view import MultiModelFormView
from ticketing.forms import TicketForm, ReviewForm
from django.urls import reverse_lazy

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title','description', 'image']
    # permission_required = 'ticketing.add_ticket'
    
    # session
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ['title','description', 'image']
    
    # session
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket

    def get_success_url(self):
        return reverse_lazy('list_posts')

class ReviewWithTicket(MultiModelFormView):
    form_classes = {
        'ticket_form' : TicketForm,
        'review_form' : ReviewForm,
    }
    template_name = 'ticketing/review_with_ticket_form.html'

    # Update
    def get_objects(self):
        self.review_id = self.kwargs.get('pk', None)
        try:
            review = Review.objects.get(id=self.review_id)
        except Review.DoesNotExist:
            review = None
        return {
            'review_form': review,
            'ticket_form': review.ticket if review else None
        }

    def get_success_url(self):
        return reverse_lazy('list_posts')

    def forms_valid(self, forms):

        ticket = forms['ticket_form'].save(commit=False)
        print(ticket)
        ticket.user = self.request.user
        ticket.save()

        review = forms['review_form'].save(commit=False)
        review.ticket = ticket
        review.user = self.request.user
        review.save()
        return super(ReviewWithTicket, self).forms_valid(forms)

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review

    def get_success_url(self):
        return reverse_lazy('list_posts')