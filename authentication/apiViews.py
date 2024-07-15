from rest_framework import generics
from .models import User
from .serializers import *
from rest_framework.permissions import AllowAny
from django.contrib.auth import  logout, authenticate
from rest_framework import  status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator



class user_login(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    def post(self, request):
        logout(request)
        return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)

         











































# # RECUPERATION ET MODIFICATION DE MOT DE PASSE 
# class RequestPasswordReset(generics.GenericAPIView):
#     queryset = User.objects.all()

#     def post(self, request):
#         # Check if the request contains an email or a phone number
#         if 'email' in request.data:
#             serializer = ResetPasswordViaEmailSerializer(data=request.data)
#         elif 'phone_number' in request.data:
#             serializer = ResetPasswordViaSMSSerializer(data=request.data)
#         else:
#             return Response({'error': 'Numero ou Email manquant'}, status=status.HTTP_400_BAD_REQUEST)
#         # valider les donnees
#         serializer.is_valid(raise_exception=True)
#         # generation d'un code aleatoire a 6 chiffres
#         verification_code = generate_random_code()

#         if 'email' in request.data:
#             # envoi de l'email avec le code de verification
#             email = request.data['email']
#             subject = 'Password Reset Verification Code'
#             message = f'Your verification code is: {verification_code}'
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [email]
#             Util.send_email(subject, message, email_from, recipient_list)
#         elif 'phone_number' in request.data:
#             # Send SMS with verification code (you need to implement this part)
#             phone_number = request.data['phone_number']
#             Util.send_sms_verification_code(verification_code, phone_number) 

#         # Return success response
#         return Response({'success': 'Code de vérification  envoyé avec succes'}, status=status.HTTP_200_OK)


# # otp verification
# class VerifyResetCode(APIView):
#     def post(self, request):
#         serializer = VerifyResetCodeSerializer(data=request.data)
#         if serializer.is_valid():
#             verification_code = serializer.validated_data['verification_code']
#             user_email = serializer.validated_data['email']  # ou 'phone_number' selon le cas

#             # Récupérer l'utilisateur associé à l'email ou au numéro de téléphone
#             if 'email' in request.data:
#                 user = User.objects.get(email=user_email)
#             elif 'phone_number' in request.data:
#                 user = User.objects.get(phone_number=user_phone_number)
            
#             # Récupérer le code de vérification stocké pour cet utilisateur
#             try:
#                 verification_code_obj = VerificationCode.objects.get(user=user)
#                 stored_verification_code = verification_code_obj.code

#                 # Comparer le code entré avec le code stocké
#                 if verification_code == stored_verification_code:
#                     # Code de vérification correct
#                     return Response({'message': 'Code de vérification correct.'}, status=status.HTTP_200_OK)
#                 else:
#                     # Code de vérification incorrect
#                     return Response({'error': 'Code de vérification incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
#             except VerificationCode.DoesNotExist:
#                 return Response({'error': 'Aucun code de vérification trouvé pour cet utilisateur.'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class PasswordTokenCheckAPIView(generics.GenericAPIView):
#     def get(self, request, uidb64,token):
#         try:
#             id= smart_str(urlsafe_base64_decode(uidb64))
#             user= User.objects.get(id=id)
#             if not PasswordResetTokenGenerator().check_token(user,token):
#                 return Response({'error':'token is not valid, please check the new one'},status=status.HTTP_401_UNAUTHORIZED)
#             return Response({'sucess':True, 'message':'Credential Valid','uidb64':uidb64, 'token':token},status=status.HTTP_200_OK)

#         except DjangoUnicodeDecodeError as indentifier:
#             return Response({'error':'token is not valid, please check the new one'},status=status.HTTP_401_UNAUTHORIZED)



# class SetNewPasswordAPIView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class=ResetPassWordSerializer

#     def patch(self, request):
#         serializer=self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response({'sucess':True, 'message':'Mot de passe réinitialisé avec succès'},status=status.HTTP_200_OK)

