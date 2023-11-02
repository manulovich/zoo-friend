from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('register-user/', CreateUser.as_view()),
    path('update-user-login-email/', UpdateUserLoginEmail.as_view()),
    path('set-contact/', SetContact.as_view()),
    path('create-profile/', CreateProfile.as_view()),
    path('update-profile/', UpdateProfile.as_view()),
    path('update-password/', UpdateUserPassword.as_view()),
    path('login/', LoginUser.as_view()),
    path('logout/', logout_view),

    # password-reset
    path('password-reset/', UserForgotPassword.as_view()),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view())
]