from django.db import models

class Raza(models.Model):
    nombre = models.TextField(blank=True)
    description = models.TextField(blank=True)

# Create your models here.
