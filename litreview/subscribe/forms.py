from django import forms
from users.models import CustomUser

class SubscribeForm(forms.Form):
    user_subscribe = forms.ModelChoiceField(queryset=CustomUser.objects.all(), initial=0) 
    