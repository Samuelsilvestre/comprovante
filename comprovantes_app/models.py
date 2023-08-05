from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Comprovante(Base):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    detalhes = models.TextField()
    comprovante = models.FileField(upload_to = 'comprovantes/')

