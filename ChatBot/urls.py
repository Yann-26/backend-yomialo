from django.urls import path
from .views import *

urlpatterns = [
    path('save_conversation/', save_conversation, name='save_conversation'),
    path('get_conversations/', get_conversations, name='get_conversations'),
]
