from django.db import models

# Create your models here.
class Heroes(models.Model):
    idHero = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField()
    password = models.CharField(max_length=100)

class Ligne(models.Model):
    idLigne = models.CharField(max_length=100)
    compagnie = models.CharField(max_length=100)
    
