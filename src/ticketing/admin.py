from django.contrib import admin
from .models import Ticket
from .models import Review


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'user', 'created_at', 'updated_at',] 

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'user', 'ticket', 'created_at', 'updated_at',] 


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)