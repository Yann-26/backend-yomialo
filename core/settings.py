import os
from decouple import config
from unipath import Path
from datetime import timedelta


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=True, cast=bool)
DEBUG = True

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1'), '*']
AUTH_USER_MODEL = "authentication.User"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True    
EMAIL_PORT = 587
EMAIL_HOST_USER ='etudiant.2604@gmail.com'
EMAIL_HOST_PASSWORD = 'yhbejtayaeaowdld'
FROM_EMAIL = 'yannassiri26@gmail.com' 

# Application definition

DEFAULTS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'apps',  # Enable the inner home (home)
    'ChatBot',
    'pharmacies.apps.PharmaciesConfig',
    'authentication.apps.AuthenticationConfig',
    'coursier.apps.CoursierConfig',
    'payement.apps.PayementConfig',
   
]

DJANGO_APPS_PACKAGES = [
    'rest_framework',
    'django_twilio',
    'corsheaders',
    'rest_framework.authtoken',
    'oauth2_provider',
    'rest_framework_simplejwt.token_blacklist',

    # socials auth
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

INSTALLED_APPS = DEFAULTS_APPS + DJANGO_APPS_PACKAGES + CUSTOM_APPS 

CORS_ALLOWED_ORIGINS = [
    "http://192.168.210.68",
    "http://127.0.0.1",
    'http://localhost',
]

CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # """"
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'allauth.account.middleware.AccountMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context.processors.backends',

            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)


#############################################################
#############################################################
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '767553232932-37lfc23b1or6r5uqpmgtnhac1ksjlvto.apps.googleusercontent.com',
            'secret': '<your-client-secret>',
            'key': 'AIzaSyAYsc2LnspyxvQooM3T0nki1DGWAPDX9cA'
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# AUTHENTICATION_BACKENDS = [

#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
#     'allauth.account.auth_backends.facebook.FacebookOAuth2',
# ]

# # facebook auth
# SOCIAL_AUTH_FACEBOOK_KEY ="741837434774452"
# SOCIAL_AUTH_FACEBOOK_SECRET ="032a0dabccb1a5f594606ad2d57bfca8"
# SOCIAL_AUTH_FACEBOOK_SCOPE = [
#     'email',
#     'public_profile',
# ]

SIMPLE_JWT = {
     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
     'ROTATE_REFRESH_TOKENS': True,
     'BLACKLIST_AFTER_ROTATION': True
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='etudiant.2604@gmail.com'
EMAIL_HOST_PASSWORD = 'yhbejtayaeaowdld'
FROM_EMAIL = 'yannassiri26@gmail.com' 

TWILIO_ACCOUNT_SID = 'AC98cd311d901af556606072dc8cc4129c'
TWILIO_AUTH_TOKEN = 'd2c914a69a357afea577261919c883b6'
TWILIO_PHONE_NUMBER = '+16562284991'
DJANGO_TWILIO_BLACKLIST_CHECK = True

# DJANGO_BASE_FRONTEND_URL= 'http://192.168.1.5:8000'
# GOOGLE_OAUTH2_CLIENT_ID= "767553232932-37lfc23b1or6r5uqpmgtnhac1ksjlvto.apps.googleusercontent.com"
# GOOGLE_OAUTH2_CLIENT_SECRET=VOTRE_SECRET_CLIENT_GOOGLE
