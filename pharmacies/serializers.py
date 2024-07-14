from rest_framework import serializers
from .models import Assurance, Pharmacie


class AssuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assurance
        fields = ['nom', 'entreprise', 'numero', 'patient']


class PharmacieSerializer(serializers.ModelSerializer):
    assurances = AssuranceSerializer(read_only=True)
    image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Pharmacie
        fields = ['nom', 'adresse', 'numero', 'localisation', 'horaire_ouverture', 'horaire_fermeture', 'latitude', 'longitude', 'contact', 'pharmacien', 'image', 'est_de_garde', 'etoiles', 'assurances']
