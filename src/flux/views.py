from itertools import chain
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import CharField, Value
from ticketing.models import Ticket, Review
from users.models import CustomUser


class FluxListView(LoginRequiredMixin, ListView):
    """
        FluxListView
    """
    model = Ticket
    template_name = 'flux/home.html'

    def get_context_data(self, **kwargs):
        """
            Passer les variables au template
        """
        context = super(FluxListView, self).get_context_data(**kwargs)
        tickets = Ticket.objects.filter(user__followers=self.request.user.id).annotate(content_type=Value('TICKET', CharField()))
        reviews = Review.objects.filter(user__followers=self.request.user.id).annotate(content_type=Value('REVIEW', CharField()))
        posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.created_at,
            reverse=True
        )

        context.update({
            'post_list': posts,
            'owner': CustomUser.objects.get(id=self.request.user.id)
        })
        return context

class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
        Répondre à un ticket
    """
    model = Review
    success_url = reverse_lazy('list_flux')
    fields = ['title_review', 'description_review', 'note', 'ticket']

    template_name = 'flux/review_form.html'

    def get_form(self, form_class=None):

        # Passer le ticket en form hidden
        form = super().get_form( form_class)
        ticket_id = self.kwargs.get("pk")
        form.fields['ticket'].widget = forms.HiddenInput(attrs={'value':ticket_id})
        return form

    def form_valid(self, form):

        # Session user + ticker hidden
        form.instance.ticket = form.cleaned_data['ticket']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Affiche le ticket de la review qui va être créer
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        ticket_id = self.kwargs.get("pk")
        ticket = Ticket.objects.filter(id=ticket_id).first()
        context.update({
            'ticket': ticket,
        })
        return context
