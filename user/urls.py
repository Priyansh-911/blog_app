from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name='user-registraion'),
    path("token/", TokenObtainPairView.as_view(), name='token'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token-refresh')
]