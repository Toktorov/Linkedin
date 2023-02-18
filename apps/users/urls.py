from django.urls import path 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users import views

router = DefaultRouter()
router.register(prefix='user', viewset=views.UserAPIViewSet)
router.register(prefix='contact', viewset=views.UserContactAPIViewSet)
router.register(prefix='experience', viewset=views.WorkExperienceAPIViewSet)
router.register(prefix='education', viewset=views.EducationAPIViewSet)
router.register(prefix='skills', viewset=views.SkillsAPIViewSet)
router.register(prefix='premium', viewset=views.PremiumAPIViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]

urlpatterns += router.urls