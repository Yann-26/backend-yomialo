import hmac
import hashlib
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hmac
import hashlib
from django.shortcuts import render
import json
import requests
from .models import Payment
from django.http import JsonResponse




def generate_hmac_token(data, secret_key):
    return hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()


@csrf_exempt
def cinetpay_notify(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        # Récupérer les données de la requête
        cpm_site_id = data.get('cpm_site_id')
        cpm_trans_id = data.get('cpm_trans_id')
        cpm_trans_date = data.get('cpm_trans_date')
        cpm_amount = data.get('cpm_amount')
        cpm_currency = data.get('cpm_currency')
        signature = data.get('signature')
        payment_method = data.get('payment_method')
        cel_phone_num = data.get('cel_phone_num')
        cpm_phone_prefixe = data.get('cpm_phone_prefixe')
        cpm_language = data.get('cpm_language')
        cpm_version = data.get('cpm_version')
        cpm_payment_config = data.get('cpm_payment_config')
        cpm_page_action = data.get('cpm_page_action')
        cpm_custom = data.get('cpm_custom')
        cpm_designation = data.get('cpm_designation')
        cpm_error_message = data.get('cpm_error_message')
        
        # Vérifier l'intégrité des données avec le token HMAC
        x_token = request.headers.get('x-token')
        hmac_secret = 'votre_cle_secrete_obtenue_de_cinetpay'
        data_to_sign = f"{cpm_site_id}{cpm_trans_id}{cpm_amount}{cpm_currency}{payment_method}{cpm_trans_date}"
        generated_token = hmac.new(hmac_secret.encode(), data_to_sign.encode(), hashlib.sha256).hexdigest()
        
        if x_token != generated_token:
            return JsonResponse({'error': 'Invalid token'}, status=400)
        
        # Vérifier dans la base de données
        payment = Payment.objects.filter(transaction_id=cpm_trans_id, site_id=cpm_site_id).first()
        
        if payment:
            if payment.status == 'SUCCESS':
                return JsonResponse({'message': 'Payment already successful'}, status=200)
            else:
                # Appeler l'API de vérification de transaction de CinetPay
                api_url = "https://api.cinetpay.com/v1/?method=checkPayStatus"
                api_key = "votre_api_key"
                
                response = requests.post(api_url, json={
                    'apikey': api_key,
                    'site_id': cpm_site_id,
                    'transaction_id': cpm_trans_id,
                })
                
                response_data = response.json()
                
                if response_data.get('transaction', {}).get('status') == 'ACCEPTED':
                    payment.status = 'SUCCESS'
                    payment.save()
                    return JsonResponse({'message': 'Payment successful'}, status=200)
                else:
                    payment.status = 'FAILED'
                    payment.save()
                    return JsonResponse({'message': 'Payment failed'}, status=400)
        else:
            return JsonResponse({'error': 'Payment not found'}, status=404)
        
    return JsonResponse({'error': 'Invalid request method'}, status=400)



def payment_return(request):
    token = request.GET.get('token')
    transaction_id = request.GET.get('transaction_id')
    
    # Vérifier le statut du paiement dans votre base de données
    payment = Payment.objects.filter(transaction_id=transaction_id).first()
    
    if payment and payment.status == 'SUCCESS':
        message = "Votre paiement a été traité avec succès."
    else:
        message = "Votre paiement a échoué ou n'a pas encore été traité."
    
    # Retourner la réponse JSON
    return JsonResponse({'message': message})

