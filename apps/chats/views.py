from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.chats import models, serializers, permissions

# Create your views here.

class ChatAPIViewSet(viewsets.GenericViewSet, 
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.CreateModelMixin, 
                    mixins.DestroyModelMixin):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def get_permissions(self):
        if self.action in ('list', 'update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), permissions.ChatPermissions())
        return (permissions.AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)

class ChatMessageAPIViewSet(viewsets.GenericViewSet, 
                            mixins.ListModelMixin, 
                            mixins.UpdateModelMixin,  
                            mixins.RetrieveModelMixin, 
                            mixins.CreateModelMixin, 
                            mixins.DestroyModelMixin):
    queryset = models.ChatMessage.objects.all()
    serializer_class = serializers.ChatMessageSerializer
    permission_classes = (IsAuthenticated, )