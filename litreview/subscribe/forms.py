from django import forms
from users.models import CustomUser

class SubscribeForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['subscribe'].queryset = CustomUser.objects.exclude(followers__in=CustomUser.objects.filter(id=self.user.id))
        
    subscribe = forms.ModelChoiceField(queryset=None) 
    
