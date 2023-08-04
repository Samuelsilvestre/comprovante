from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import FormRegisterUser
class CreateUser(CreateView):
    template_name = 'usuario/register/form.html'
    form_class = FormRegisterUser
    success_url = reverse_lazy('login')
