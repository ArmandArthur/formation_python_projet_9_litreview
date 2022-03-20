from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2038, blank=True)
    user: User = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.user.username}"

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('ticket_detail', kwargs={'pk': self.pk})