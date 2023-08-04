from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class FormRegisterUser(UserCreationForm):
    email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password1']
