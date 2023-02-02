from django.urls import path 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPIViewSet, UserContactAPIViewSet, WorkExperienceAPIViewSet, EducationAPIViewSet, SkillsAPIViewSet

router = DefaultRouter()
router.register(prefix='user', viewset=UserAPIViewSet)
router.register(prefix='contact', viewset=UserContactAPIViewSet)
router.register(prefix='experience', viewset=WorkExperienceAPIViewSet)
router.register(prefix='education', viewset=EducationAPIViewSet)
router.register(prefix='skills', viewset=SkillsAPIViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]

urlpatterns += router.urls