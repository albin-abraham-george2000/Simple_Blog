from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
                    UserProfileView,
                    UserRegistrationView,
                    UserLoginView,
                    ForgotPasswordView,
                    ResetPasswordView
                    )

app_name = 'auth_users'

urlpatterns = [
    path('login/',UserLoginView.as_view(), name= 'login'),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(), name='logout'),
   
   path('reset-password/',ResetPasswordView.as_view(), name='reset-password'),
    path('forgot-password/',ForgotPasswordView.as_view(),name = 'forgot-password'),
    path('user-profile/',UserProfileView.as_view(),name = 'user_profile' ),
    
    
    
    
    
    # API MODULE
    
    # path('api/auth/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    
    # # User login endpoint
    # path('api/auth/login/', UserLoginAPIView.as_view(), name='user-login'),
    
    # # Token refresh endpoint
    
    # path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    # # Add token blacklist endpoint for logout
    # path('api/auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]