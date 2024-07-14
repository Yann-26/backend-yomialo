from django.urls import path, include
from .views import api_root
from rest_framework.routers import SimpleRouter
from .views import *

# Créer un routeur SimpleRouter
router = SimpleRouter()

# Enregistrer les viewsets avec les chemins d'URL personnalisés

router.register(r'assurances', AssuranceViewSet, basename='assurances')
router.register(r'pharmacies', PharmaciesViewSet, basename='pharmacies')


urlpatterns = [
    path('api-root1/', api_root, name='pharmacies-api-root'),
    path('', include(router.urls)),
]
