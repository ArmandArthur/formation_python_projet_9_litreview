from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    """
        Form ticket
    """
    class Meta(object):
        """
            Meta ticket
        """
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    """
        Form Review
    """
    class Meta(object):
        """
            Meta Review
        """
        model = Review
        fields = ['title_review', 'description_review', 'note']
