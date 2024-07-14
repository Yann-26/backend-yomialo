from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

from django.db import models



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    profile_photo = models.ImageField(upload_to='profile_photo/')
    bio = models.TextField()
    poste = models.CharField(max_length=100)
    SEX_CHOICES = (
        ('F','Femme'),
        ('H', 'Homme'), 
    )
    sexe = models.CharField(choices=SEX_CHOICES, max_length=1)

    def __str__(self):
        return self.nom


class VerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verification_code')
    code = models.CharField(max_length=6)
