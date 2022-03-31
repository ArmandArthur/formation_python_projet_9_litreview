from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import SubscribeForm
from django.urls import reverse
from users.models import CustomUser

class SubscribeCreateView(LoginRequiredMixin, FormView):
    form_class = SubscribeForm
    template_name = "subscribe/subscribe_manage.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['owner'] = CustomUser.objects.filter(id=self.request.user.id)
        return context
    
    def get_success_url(self):
        return reverse('add_subscribe')
    
    # session
    def form_valid(self, form):
        
        if form.is_valid():
            owner = self.request.user
            owner.subscribes.add(form.cleaned_data['user_subscribe'])
            owner.save()
        return super().form_valid(form)
    