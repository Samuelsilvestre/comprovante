from django.urls import path

from .views import *

urlpatterns = [
    path('', ComprovanteCreateView.as_view(), name = 'form_comprovante'),
    path('comprovante/list/', ComprovanteListView.as_view(), name = 'comprovante_list')
]