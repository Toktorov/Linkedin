from rest_framework.routers import DefaultRouter

from apps.chats.views import ChatAPIViewSet


router = DefaultRouter()
router.register(prefix='chat', viewset=ChatAPIViewSet)

urlpatterns = router.urls