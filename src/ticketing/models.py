from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2038, blank=True)
    user: User = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)

    image = models.ImageField(upload_to='ticketing/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('list_posts')
    
class Review(models.Model):
    title_review = models.CharField(max_length=128)
    description_review = models.TextField(max_length=2038, blank=True)
    choices_note = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    note = models.CharField(max_length=10, choices=choices_note, default="1")
    ticket: Ticket = models.OneToOneField(to=Ticket,
                                   on_delete=models.CASCADE, related_name = 'reviews_rel')
    user: User = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title_review}"