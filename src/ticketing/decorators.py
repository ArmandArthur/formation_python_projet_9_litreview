from functools import wraps
from django.http import HttpResponseRedirect
from .models import Ticket, Review

def is_owner_review(function):
    """
        Est autorisé à accéder à la review? Sinon redirect login
    """
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if 'pk' in kwargs:
            review = Review.objects.filter(id=kwargs['pk']).first()
            if request.user == review.user :
                return function(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/users/login')
        else:
            return function(request, *args, **kwargs)

    return wrap

def is_owner_ticket(function):
    """
        Est autorisé à accéder au ticket? Sinon redirect login
    """
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if 'pk' in kwargs:
            ticket = Ticket.objects.filter(id=kwargs['pk']).first()
            if request.user == ticket.user :
                return function(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/users/login')
        else:
            return function(request, *args, **kwargs)
    return wrap
