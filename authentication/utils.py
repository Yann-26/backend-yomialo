from django.core.mail import send_mail
import random
import string
from twilio.rest import Client
from django.conf import settings
from  django.contrib import messages


def generate_random_code(length=6):
    """Generate a random code of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class Util:
    @staticmethod
    def send_email(data):
        email_body = data['email_body']
        to_email = data['to_email']
        email_subject = data['email_subject']
        
        send_mail(
            email_subject,
            email_body,
            'yannassiri26@gmail.com',  
            [to_email],
            fail_silently=False,
        )
    @staticmethod
    def send_sms_verification_code(verification_code, phone_number):
        # Initialisation du client Twilio avec les informations d'authentification
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Envoi du SMS
        message = client.messages.create(
            body=f"Your verification code is: {verification_code}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )

        # Gestion de la réponse
        if message.sid:
            messages.succes("SMS sent successfully!")
        else:
            messages.succes("Failed to send SMS.")


def get_error_message(exception):
    """
    Renvoie un message d'erreur approprié pour une exception donnée.
    
    Args:
        exception: L'exception pour laquelle un message d'erreur doit être généré.
        
    Returns:
        str: Le message d'erreur approprié pour l'exception.
    """
    # Ajoutez des conditions pour gérer différents types d'exceptions et renvoyer des messages d'erreur appropriés
    if isinstance(exception, ValueError):
        return "Valeur incorrecte : " + str(exception)
    elif isinstance(exception, ValidationError):
        return "Erreur de validation : " + str(exception)
    elif isinstance(exception, PermissionError):
        return "Erreur de permission : " + str(exception)
    elif isinstance(exception, User.DoesNotExist):
        return "Utilisateur non trouvé : " + str(exception)
    else:
        return "Une erreur s'est produite : " + str(exception)



    