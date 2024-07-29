from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class registerForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                'class': 'vTextField',
                'maxlength': '150',
                'autocapitalize': 'none',
                'autocomplete': 'username',
                'autofocus': True,
            })
            self.fields['password1'].widget.attrs.update({
                'type': 'password',
                'autocomplete': 'new-password',
            })
            self.fields['password2'].widget.attrs.update({
                'type': 'password',
                'autocomplete': 'new-password',
            })
