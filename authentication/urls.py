from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from .apiViews import *
from .socialAuthViews import *
from django.contrib.auth import views as auth_view
from rest_framework_simplejwt.views import TokenRefreshView

   

urlpatterns = [
    path('login/', user_login.as_view(), name='token_obtain_pair'),
    # path('check-login/', check_user_login, name='check_user_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    path('facebook-auth/', facebook_auth, name='facebook_auth'),
    # PASSWORD
    # path('password/reset/', RequestPasswordReset.as_view(), name='request-password-reset'),
    # path('password/verify/', VerifyResetCode.as_view(), name='verify-reset-code'),
    # path('password/reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name='password-token-check'),
    # path('password/reset/new/', SetNewPasswordAPIView.as_view(), name='set-new-password'),
    path('', login_view, name="login"),
    path('register-user/', register_user, name="register"),
    
]
