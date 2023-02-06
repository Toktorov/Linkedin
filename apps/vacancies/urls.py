from django.urls import path 
from rest_framework.routers import DefaultRouter

from apps.vacancies.views import VacancyAPIViewSet

router = DefaultRouter()
router.register(prefix='vacancy', viewset=VacancyAPIViewSet)

urlpatterns = router.urls