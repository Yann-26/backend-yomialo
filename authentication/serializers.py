from .models import User, Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import re
from django.contrib.auth.models import Group




# API DE CONNEXION
class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Récupérer l'utilisateur actuel
        user = self.user
        
        # Vérifier si l'utilisateur appartient au groupe 'Patients'
        patient_group = Group.objects.get(name='Patients')
        if patient_group in user.groups.all():
            data.update({'username': user.username})
        else:
            raise serializers.ValidationError("Vous n'êtes pas autorisé à vous connecter.")
        
        return data


# API DE CREATION DE COMPTE
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        # Vérifier si l'utilisateur appartient au groupe 'Patients'
        patient_group = Group.objects.get(name='Patients')
        
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        # Assigner l'utilisateur au groupe 'Patients'
        user.groups.add(patient_group)
        
        # Créer un profil associé
        Profile.objects.create(
            user=user,
            prenom=validated_data['first_name'],
            nom=validated_data['last_name'],
            email=validated_data['email'],
            number='',  # Ajoutez la logique pour récupérer le numéro si nécessaire
            bio='',
            poste='',
            sexe='',
            
        )

        return user



    
   
## PASSWORD 
class ResetPasswordViaEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')

        # Vérifier si l'email existe dans la base de données
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("L'utilisateur avec cet email n'existe pas")

        return attrs
    

# numero serializer
class ResetPasswordViaSMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15) 

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        if not User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("Ce numéro de téléphone n'existe pas")
        
    def validate_phone_number(self, value):
        #  numéro de téléphone contient uniquement des chiffres
        if not re.match(r'^\d+$', value):
            raise serializers.ValidationError("Le numéro de téléphone ne doit contenir que des chiffres.")
        #  format international avec un certain nombre de chiffres :
        if not re.match(r'^\+\d{1,3}\d{5,15}$', value):
            raise serializers.ValidationError("Format de numéro de téléphone incorrect.")

        return value


#otp serializer
class OTPVerificationSerializer(serializers.Serializer):
    verification_code = serializers.CharField(max_length=6, min_length=6, required=True)
    
    def validate(self, value):
        #  numéro de téléphone contient uniquement des chiffres
        if not re.match(r'^\d+$', value):
            raise serializers.ValidationError("Le code ne doit contenir que des chiffres.")


class ResetPassWordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        # Vérifier si les deux mots de passe correspondent
        if password != password2:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas")

        return attrs

    def save(self, user):
        password = self.validated_data['password']

        # Chiffrer le mot de passe et le sauvegarder
        user.set_password(password)
        user.save()
