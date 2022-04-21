from django import forms
from users.models import CustomUser

class SubscribeForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user = CustomUser.objects.filter(id=self.user.id).first()
        self.fields['subscribe'].queryset = CustomUser.objects.exclude(followers=user.id).exclude(id=self.user.id)
        
    subscribe = forms.ModelChoiceField(queryset=None) 
    
