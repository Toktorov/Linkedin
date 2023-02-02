from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.models import User, UserContact
from apps.users.serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer, UserContactSerializer, UserUpdateSerializer
from apps.users.permissions import UsersPermissions

# Create your views here.
class UserAPIViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin,
                        CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        if self.action in ('create', ):
            return UserRegisterSerializer
        if self.action in ('update', 'partial_update'):
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

class UserContactAPIViewSet(GenericViewSet,
                            CreateModelMixin, DestroyModelMixin):
    queryset = UserContact.objects.all()
    serializer_class = UserContactSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)