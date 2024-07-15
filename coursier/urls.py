
from django.urls import path
from .views import RegisterCoursierView, LoginCoursierView




urlpatterns = [
    path('register_coursier/', RegisterCoursierView.as_view(), name='register-coursier'),
    path('login_coursier/', LoginCoursierView.as_view(), name='login-coursier'),
   
]
