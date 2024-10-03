from django.urls import path
from api.views import( 
                      BlogListCreateAPIView,
                      BlogDetailAPIView, 
                      UserRegistrationAPIView, 
                      UserLoginAPIView, 
                      UserProfileAPIView
                      )

from rest_framework_simplejwt.views import (
                            TokenObtainPairView,
                            TokenRefreshView,
                        )
app_name = 'API_Interface'
urlpatterns = [
    path('api/blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('api/blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),    
    path('api/auth/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('api/auth/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/auth/profile/', UserProfileAPIView.as_view(), name='user-profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    
]