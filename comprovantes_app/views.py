from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Comprovante

class ComprovanteListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Comprovante
    fiels = '__all__'
    context_object_name = 'object'
    template_name = 'comprovantes_app/list.html'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)





class ComprovanteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Comprovante
    fields = ['detalhes','comprovante']
    template_name = 'comprovantes_app/form.html'
    success_url = reverse_lazy('comprovante_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.is_valid()
        return super().form_valid(form)