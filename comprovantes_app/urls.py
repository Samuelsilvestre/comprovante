from django.urls import path

from .views import *

urlpatterns = [
    path('', ComprovanteCreateView.as_view(), name = 'form_comprovante'),
    path('ok/', ok, name = 'ok')
]