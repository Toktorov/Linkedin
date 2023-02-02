from django.urls import path 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPIViewSet, UserContactAPIViewSet

router = DefaultRouter()
router.register(prefix='user', viewset=UserAPIViewSet)
router.register(prefix='contact', viewset=UserContactAPIViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]

urlpatterns += router.urls