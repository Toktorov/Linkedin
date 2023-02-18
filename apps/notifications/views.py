from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.notifications import models, serializers, permissions

# Create your views here.
class NotificationAPIViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer
    permission_classes = (IsAuthenticated, permissions.NotificationPermissions)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)