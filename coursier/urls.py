
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register_coursier/', RegisterView.as_view(), name='register_coursier'),
   
]
