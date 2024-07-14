from django.contrib import admin
from .models import User, Profile

# Définir le ModelAdmin pour le modèle User
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name']  # Définir les champs de recherche

# Enregistrer le modèle User avec le ModelAdmin personnalisé
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
