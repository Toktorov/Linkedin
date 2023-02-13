from rest_framework.routers import DefaultRouter

from apps.organizations.views import OrganizationAPIViewSet


router = DefaultRouter()
router.register(prefix='organization', viewset=OrganizationAPIViewSet)

urlpatterns = router.urls