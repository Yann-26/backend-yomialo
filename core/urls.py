from django.contrib import admin
from django.urls import path, include , re_path 
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api-auth/', include('rest_framework.urls')),        # Django admin route
    path("", include("authentication.urls")), 
    path("", include("apps.home.urls")),           
    path("", include("coursier.urls")),
    path("", include("payement.urls")),
    # path("", include("apps.gestion_users.urls")),
    path("", include("pharmacies.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
]
