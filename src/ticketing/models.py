from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2038, blank=True)
    user: User = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('detail_ticket', kwargs={'pk': self.pk})
    
class Review(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2038, blank=True)
    ticket: Ticket = models.ForeignKey(to=Ticket,
                                   on_delete=models.CASCADE)
    user: User = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"