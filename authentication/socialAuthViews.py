from rest_framework import serializers
from rest_framework.views import APIView
from django.conf import settings
from django.shortcuts import redirect
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .mixins import PublicApiMixin, ApiErrorsMixin
# from .services import google_get_access_token, google_get_user_info
# from .serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import User


# def generate_tokens_for_user(user):
#     """
#     Generate access and refresh tokens for the given user
#     """
#     serializer = TokenObtainPairSerializer()
#     token_data = serializer.get_token(user)
#     access_token = token_data.access_token
#     refresh_token = token_data
#     return access_token, refresh_token


# class GoogleLoginApi(PublicApiMixin, ApiErrorsMixin, APIView):
#     class InputSerializer(serializers.Serializer):
#         code = serializers.CharField(required=False)
#         error = serializers.CharField(required=False)

#     def get(self, request, *args, **kwargs):
#         input_serializer = self.InputSerializer(data=request.GET)
#         input_serializer.is_valid(raise_exception=True)

#         validated_data = input_serializer.validated_data

#         code = validated_data.get('code')
#         error = validated_data.get('error')

#         login_url = f'{settings.BASE_FRONTEND_URL}/login'
    
#         if error or not code:
#             params = urlencode({'error': error})
#             return redirect(f'{login_url}?{params}')

#         redirect_uri = f'{settings.BASE_FRONTEND_URL}/google/'
#         access_token = google_get_access_token(code=code, 
#                                                redirect_uri=redirect_uri)

#         user_data = google_get_user_info(access_token=access_token)

#         try:
#             user = User.objects.get(email=user_data['email'])
#             access_token, refresh_token = generate_tokens_for_user(user)
#             response_data = {
#                 'user': UserSerializer(user).data,
#                 'access_token': str(access_token),
#                 'refresh_token': str(refresh_token)
#             }
#             return Response(response_data)
#         except User.DoesNotExist:
#             username = user_data['email'].split('@')[0]
#             first_name = user_data.get('given_name', '')
#             last_name = user_data.get('family_name', '')

#             user = User.objects.create(
#                 username=username,
#                 email=user_data['email'],
#                 first_name=first_name,
#                 last_name=last_name,
#                 registration_method='google',
#                 phone_no=None,
#                 referral=None
#             )
         
#             access_token, refresh_token = generate_tokens_for_user(user)
#             response_data = {
#                 'user': UserSerializer(user).data,
#                 'access_token': str(access_token),
#                 'refresh_token': str(refresh_token)
#             }
#             return Response(response_data)
        

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def facebook_auth(request):
    if request.method == 'POST':
        # Récupérer les données de l'utilisateur depuis la requête POST
        email = request.data.get('email')
        username = request.data.get('username')
        first_name = request.data.get('first_name')

        # Créer un nouvel utilisateur ou mettre à jour un utilisateur existant dans la base de données Django
        user, created = User.objects.update_or_create(
            email=email,
            defaults={'username': username, 'first_name': first_name}
        )

        # Retourner une réponse avec les détails de l'utilisateur
        return Response({'message': 'User created/updated successfully'}, status=201 if created else 200)
    else:
        # Retourner une réponse indiquant une méthode non autorisée
        return Response({'message': 'Method not allowed'}, status=405)
