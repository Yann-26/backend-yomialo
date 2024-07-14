from django.db import models
import uuid
from  authentication.models import User


def user_directory_path(instance, filename):
    # Construit le chemin pour l'upload
    # Ici, 'courier/id_cards/user_<id>/<filename>'
    return f'courier/user_{instance.user.id}/{filename}'

# Create your models here.
class Coursier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quarier = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    recto_card_image = models.ImageField(upload_to=user_directory_path)
    verso_card_image = models.ImageField(upload_to=user_directory_path)
    selfie_image = models.ImageField(upload_to=user_directory_path)
    is_verified = models.BooleanField(default=False)
    auth_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.user.username