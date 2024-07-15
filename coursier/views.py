from rest_framework.permissions import AllowAny
from rest_framework import generics
from authentication.models import User
from .serializers import RegisterCoursierSerializer, CoursierLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterCoursierView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterCoursierSerializer
        

class LoginCoursierView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CoursierLoginSerializer    
