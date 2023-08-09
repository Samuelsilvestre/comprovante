from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class FormRegisterUser(UserCreationForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password1']

    def clean_email(self):
        email = self.cleaned_data('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError('este email é invalido')

        else:
            return email    
