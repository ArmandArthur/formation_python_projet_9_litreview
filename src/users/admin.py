from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Créer une table transitoire car relation ManyToMany sur elle même.
class CustomUsersInline(admin.TabularInline):
    """
        Sinon bug admin
    """
    model = CustomUser.subscribes.through
    fk_name = 'from_customuser'
    
class CustomUserAdmin(UserAdmin):
    """ 
        Définition des forms + champs à afficher
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1', 'password2', 'is_staff', 'is_active', 'groups')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    inlines = (CustomUsersInline,)
    exclude = ('subscribes',)

admin.site.register(CustomUser, CustomUserAdmin)



