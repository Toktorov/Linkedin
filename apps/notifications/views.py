from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer
from apps.notifications.permissions import NotificationPermissions

# Create your views here.
class NotificationAPIViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, NotificationPermissions)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)