from rest_framework.routers import DefaultRouter

from apps.notifications.views import NotificationAPIViewSet


router = DefaultRouter()
router.register(prefix='notification', viewset=NotificationAPIViewSet)

urlpatterns = router.urls