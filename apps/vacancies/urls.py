from rest_framework.routers import DefaultRouter

from apps.vacancies.views import VacancyAPIViewSet, VacancyFavoriteAPIViewSet, OrganizationVacancyAPIViewSet, OrganizationVacancyFavoriteAPIViewSet

router = DefaultRouter()
router.register(prefix='vacancy', viewset=VacancyAPIViewSet)
router.register(prefix='vacancy_favorite', viewset=VacancyFavoriteAPIViewSet)
router.register(prefix='organization_vacancy', viewset=OrganizationVacancyAPIViewSet)
router.register(prefix='organization_vacancy_favorite', viewset=OrganizationVacancyFavoriteAPIViewSet)

urlpatterns = router.urls