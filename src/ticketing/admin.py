from django.contrib import admin
from .models import Ticket
from .models import Review


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'user', 'thumbnail_preview', 'created_at', 'updated_at',]
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Image Preview'
    thumbnail_preview.allow_tags = True

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_review', 'description_review', 'user', 'ticket', 'created_at', 'updated_at',] 


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)