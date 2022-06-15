from django.db import models

class Raza(models.Model):
    nombre = models.TextField(blank=True)
    description = models.TextField(blank=True)
    armas = models.TextField()
    planeta = models.TextField()
    papel = models.TextField()
    rango = models.TextField()
    habilidad = models.TextField()
    tamano = models.TextField()
# Create your models here.
