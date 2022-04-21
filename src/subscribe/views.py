from django.views.generic.edit import FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SubscribeForm
from django.urls import reverse, reverse_lazy
from users.models import CustomUser
from django.http import HttpResponseRedirect


class SubscribeCreateView(LoginRequiredMixin, FormView):
    form_class = SubscribeForm
    template_name = "subscribe/subscribe_manage.html"
    
    # Permet de passer les valeurs aux formulaires
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['owner'] = CustomUser.objects.get(id=self.request.user.id)
        return context
    
    def get_success_url(self):
        return reverse('manage_subscribe')
    
    # session
    def form_valid(self, form):
        
        if form.is_valid():
            owner = self.request.user
            owner.subscribes.add(form.cleaned_data['subscribe'])
            owner.save()
        return super().form_valid(form)
 
class SubscribeDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'subscribe/subscribe_confirm_delete.html'
    success_url = reverse_lazy('manage_subscribe')

    def form_valid(self, form):
        owner = self.request.user
        subscribe_id = self.kwargs.get("pk")
        subscribe = CustomUser.objects.filter(id=subscribe_id).first()
        owner.subscribes.remove(subscribe)
        owner.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)