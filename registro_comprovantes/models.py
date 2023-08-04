from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Comprovante(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    detalhe = models.TextField()
    arquivo = models.FileField(upload_to = 'arquivo/')

    def __str_(self):
        return f'{self.usuario} registrou o comprovante as {self.date}'