from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging


logger = logging.getLogger(__name__)

def send_mail_after_registration(email, token):
    subject = 'Votre compte doit être vérifié'
    message = f"Please confirm your email by clicking on the link below"
    email_template_name = "emailConfirmation.html"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    try:
        # Render the HTML email content
        html_message = render_to_string(email_template_name, {'message': message, 'token': token})
        # Send email via Django's send_mail
        send_mail(subject, strip_tags(html_message), email_from, recipient_list, html_message=html_message)
        logger.debug(f"Email sent to {email} with token {token}")
    
    except Exception as e:
        logger.error(f"Error sending email to {email}: {e}")
