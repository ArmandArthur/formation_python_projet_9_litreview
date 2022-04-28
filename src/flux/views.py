
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from ticketing.models import Ticket, Review
from users.models import CustomUser
from itertools import chain
from django.db.models import CharField, Value
from django.urls import reverse_lazy
from django.db.models import Q

class FluxListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'flux/home.html'

    def get_context_data(self, **kwargs):
        context = super(FluxListView, self).get_context_data(**kwargs)
        tickets_followers = Ticket.objects.filter(user__followers=self.request.user.id).annotate(content_type=Value('TICKET', CharField()))
        tickets_owner = Ticket.objects.filter(user=self.request.user.id).annotate(content_type=Value('TICKET', CharField()))
        tickets =  chain(tickets_followers, tickets_owner)
        reviews_followers = Review.objects.filter(user__followers=self.request.user.id).annotate(content_type=Value('REVIEW', CharField()))
        reviews_owner = Review.objects.filter(user=self.request.user.id).annotate(content_type=Value('REVIEW', CharField()))
        reviews = chain(reviews_followers, reviews_owner)
        posts = sorted(
            chain(reviews, tickets), 
            key=lambda post: post.created_at, 
            reverse=True
        )
        owner = CustomUser.objects.get(id=self.request.user.id)
        context.update({
            'post_list': posts,
            'owner': owner,
        })
        return context

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    success_url = reverse_lazy('list_flux')
    fields = ['title','description','ticket']

    template_name = 'flux/review_form.html'

    def get_form(self, form_class=None):
        form = super().get_form( form_class)
        ticket_id = self.kwargs.get("pk")
        form.fields['ticket'].widget = forms.HiddenInput(attrs={'value':ticket_id})
        return form

    # session
    def form_valid(self, form):
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