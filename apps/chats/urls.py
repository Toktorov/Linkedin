from rest_framework.routers import DefaultRouter

from apps.chats.views import ChatAPIViewSet, ChatMessageAPIViewSet


router = DefaultRouter()
router.register(prefix='chat', viewset=ChatAPIViewSet)
router.register(prefix='message', viewset=ChatMessageAPIViewSet)

urlpatterns = router.urls