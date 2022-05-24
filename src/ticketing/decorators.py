from functools import wraps
from django.http import HttpResponseRedirect
from .models import Ticket, Review

def is_owner(function):
    """
        Est autorisé à accéder au ticket/review? Sinon redirect login
    """
    @wraps(function)
    def wrap(request, *args, **kwargs):
        url = request.resolver_match.url_name
        if 'pk' in kwargs:
            if url == 'update_ticket' or url == 'delete_ticket':
                item = Ticket.objects.filter(id=kwargs['pk']).first()
            else:
                item = Review.objects.filter(id=kwargs['pk']).first()
            if request.user == item.user:
                return function(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/users/login')
        else:
            return function(request, *args, **kwargs)
    return wrap
