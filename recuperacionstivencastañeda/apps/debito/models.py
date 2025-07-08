from django.db import models

# Create your models here.
class Debito(models.Model):
    banco = models.TextField("banco")
    valor = models.IntegerField("valor")