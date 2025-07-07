from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.TextField("nombre")
    precio = models.IntegerField("precio")