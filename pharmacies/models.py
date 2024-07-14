# Dans models.py de votre application pharmacy

from django.db import models

class Assurance(models.Model):
    nom = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Pharmacie(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    ouverture = models.CharField(max_length=10)
    fermeture = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact = models.CharField(max_length=20)
    pharmacien = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='pharmacy_images/', blank=True, null=True)
    assurance = models.ForeignKey(Assurance, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
