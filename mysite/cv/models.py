from django.db import models

# Create your models here.
class Cv(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    formation = models.CharField(max_length=600)
    langue = models.CharField(max_length=200)
    profil = models.CharField(max_length=600)
    experience = models.CharField(max_length=600)
    competence = models.CharField(max_length=600)

    def __str__(self):
        return self.nom
