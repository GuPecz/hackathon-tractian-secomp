from django.db import models

class FichaTecnica(models.Model):
    installation_adequate = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='media/', null=True, blank=True)
    img2 = models.ImageField(upload_to='media/', null=True, blank=True)
    img3 = models.ImageField(upload_to='media/', null=True, blank=True)