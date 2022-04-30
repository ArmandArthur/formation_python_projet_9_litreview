from django import forms

from .models import Ticket, Review

class TicketForm(forms.ModelForm):

    class Meta(object):
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):

    class Meta(object):
        model = Review
        fields = ['title_review', 'description_review']