from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), 
    path("", include("apps.home.urls")),           
    path("", include("coursier.urls")),
    path("", include("payement.urls")),
    # path("", include("apps.gestion_users.urls")),
    path("", include("pharmacies.urls")),
]
