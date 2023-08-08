from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Comprovante

def ok(request):
    return HttpResponse(f'ola voce esta logado {request.user}')



class ComprovanteCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Comprovante
    fields = ['detalhes','comprovante']
    template_name = 'comprovantes_app/form.html'
    success_url = reverse_lazy('ok')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.is_valid()
        return super().form_valid(form)