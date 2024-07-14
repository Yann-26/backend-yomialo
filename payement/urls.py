from django.urls import path
from .views import cinetpay_notify

urlpatterns = [
    path('notify/', cinetpay_notify, name='cinetpay_notify'),
    path('retour/', cinetpay_notify, name='cinetpay_retour'),
]


















