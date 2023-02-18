from rest_framework.routers import DefaultRouter

from apps.vacancies.views import VacancyAPIViewSet, VacancyFavoriteAPIViewSet


router = DefaultRouter()
router.register(prefix='vacancy', viewset=VacancyAPIViewSet)
router.register(prefix='vacancy_favorite', viewset=VacancyFavoriteAPIViewSet)

urlpatterns = router.urls