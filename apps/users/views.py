from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.models import User, UserContact, WorkExperience, Education, Skills
from apps.users.serializers import (UserSerializer, UserDetailSerializer, UserRegisterSerializer, 
                                    UserContactSerializer, UserUpdateSerializer, WorkExperienceSerializer, 
                                    EducationSerializer, SkillsSerializer)
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
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)

class WorkExperienceAPIViewSet(GenericViewSet, CreateModelMixin, 
                                UpdateModelMixin, DestroyModelMixin):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class EducationAPIViewSet(GenericViewSet, CreateModelMixin,
                            UpdateModelMixin, DestroyModelMixin):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class SkillsAPIViewSet(GenericViewSet, CreateModelMixin,
                        UpdateModelMixin, DestroyModelMixin):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
  
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)