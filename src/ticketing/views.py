from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from multi_form_view import MultiModelFormView
from django.utils.decorators import method_decorator
from ticketing.forms import TicketForm, ReviewForm
from .decorators import is_owner_review, is_owner_ticket
from .models import Ticket, Review


class TicketCreateView(LoginRequiredMixin, CreateView):
    """
        Ticket create view
    """
    model = Ticket
    fields = ['title','description', 'image']
    # permission_required = 'ticketing.add_ticket'
    
    # session
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class TicketUpdateView(LoginRequiredMixin, UpdateView):
    """
        Ticket update view + securisation
    """
    model = Ticket
    fields = ['title','description', 'image']
    def get_success_url(self):
        return reverse_lazy('list_posts')

    @method_decorator(is_owner_ticket)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # session
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class TicketDeleteView(LoginRequiredMixin, DeleteView):
    """
        Ticket delete view + securisation
    """
    model = Ticket

    @method_decorator(is_owner_ticket)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('list_posts')

class ReviewWithTicket(MultiModelFormView):
    """
        Review form + ticket form + securisation
    """
    form_classes = {
        'ticket_form' : TicketForm,
        'review_form' : ReviewForm,
    }
    template_name = 'ticketing/review_with_ticket_form.html'

    @method_decorator(is_owner_review)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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

class ReviewWithoutTicket(LoginRequiredMixin, UpdateView):
    """
        Review update + securisation
    """
    model = Review
    fields = ['title_review','description_review', 'note']

    @method_decorator(is_owner_review)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('list_posts')

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """
        Review delete + securisation
    """
    model = Review

    @method_decorator(is_owner_review)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('list_posts')
