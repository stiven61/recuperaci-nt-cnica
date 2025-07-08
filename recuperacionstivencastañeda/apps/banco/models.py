from django.db import models

# Create your models here.
class Banco(models.Model):
    cuenta = models.TextField("cuenta")
    codigo = models.IntegerField("codigo")