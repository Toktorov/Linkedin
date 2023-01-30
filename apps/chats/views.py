from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.chats.models import Chat, ChatMessage
from apps.chats.serializers import ChatSerializer, ChatMessageSerializer
from apps.chats.permissions import ChatPermissions
# Create your views here.

class ChatAPIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, 
                        CreateModelMixin, DestroyModelMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_permissions(self):
        if self.action in ('list', 'update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), ChatPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)

class ChatMessageAPIViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin,  
                            RetrieveModelMixin, CreateModelMixin, DestroyModelMixin):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    