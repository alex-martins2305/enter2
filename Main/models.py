from django.db import models
from django.contrib.auth.models import User

class Aposentados(models.Model):
    mci=models.CharField(max_length=20)
    beneficio=models.CharField(max_length=255)
    tipo_beneficio=models.CharField(max_length=255)
    idade=models.CharField(max_length=255)
    analfabeto=models.CharField(max_length=20)
    agencia=models.CharField(max_length=20, blank=True)
    conta=models.CharField(max_length=20,blank=True)
    dia_recebimento=models.CharField(max_length=10)
    limite_vigente=models.CharField(max_length=10)
    precisa_prova_vida=models.CharField(max_length=10)
    ultimo_atendimento=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.mci
    

