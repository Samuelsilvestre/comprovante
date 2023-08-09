from django.contrib import admin
from .models import Comprovante

@admin.register(Comprovante)
class ComprovanteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'date']