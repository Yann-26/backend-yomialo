from .models import Coursier
from authentication.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
import re
from .utils import send_mail_after_registration
from django.contrib.auth.models import Group



# API DE CONNEXION
class CoursierLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Récupérer l'utilisateur actuel
        user = self.user 
        # Vérifier si l'utilisateur appartient au groupe 'Patients'
        patient_group = Group.objects.get(name='Coursiers')
        if patient_group in user.groups.all():
            data.update({'username': user.username})
        else:
            raise serializers.ValidationError("Vous n'êtes pas autorisé à vous connecter.")
        
        return data



# API DE CREATION DE COMPTE
class RegisterCoursierSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    quarier = serializers.CharField(max_length=120, required=True)
    phone_number = serializers.CharField(max_length=20, required=True)
    address = serializers.CharField(max_length=255, required=True)
    recto_card_image = serializers.ImageField(required=True)
    verso_card_image = serializers.ImageField(required=True)
    selfie_image = serializers.ImageField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name',
                  'quarier', 'phone_number', 'address', 'recto_card_image', 'verso_card_image', 'selfie_image')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        # Créer l'utilisateur
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        # Ajouter l'utilisateur au groupe 'Coursiers'
        coursier_group = Group.objects.get(name='Coursiers')
        user.groups.add(coursier_group)

        # Créer le coursier associé
        coursier = Coursier.objects.create(
            user=user,
            quarier=validated_data['quarier'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            recto_card_image=validated_data['recto_card_image'],
            verso_card_image=validated_data['verso_card_image'],
            selfie_image=validated_data['selfie_image'],
        )
        # Envoyer l'e-mail de confirmation
        send_mail_after_registration(user.email, user.auth_token)
        coursier.save()

        return user



    
