from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework import status

from apps.users import models, serializers
from apps.users.permissions import UsersPermissions

# Create your views here.
class UserAPIViewSet(GenericViewSet, 
                    mixins.ListModelMixin, 
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(
        detail=True, permission_classes=[IsAuthenticated, UsersPermissions], methods=['put', 'patch']
    )
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = serializers.ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = serializer.data.get('old_password')
        new_password = serializer.data.get('new_password')
        if not user.check_password(old_password):
            return Response(
                {'old_password' : 'Старый пароль неверный'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.set_password(new_password)
        user.save()
        return Response(
            {'OK' : 'Пароль изменен успешно'},
            status=status.HTTP_200_OK
        )

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return serializers.UserDetailSerializer
        if self.action in ('create', ):
            return serializers.UserRegisterSerializer
        if self.action in ('update', 'partial_update'):
            return serializers.UserUpdateSerializer
        if self.action in ('change_password', ):
            return serializers.ChangePasswordSerializer
        return serializers.UserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

class PremiumAPIViewSet(GenericViewSet, 
                        mixins.ListModelMixin, 
                        mixins.CreateModelMixin, 
                        mixins.RetrieveModelMixin, 
                        mixins.DestroyModelMixin):
    queryset = models.Premium.objects.all()
    serializer_class = serializers.PremiumSerializer
    permission_classes = (IsAuthenticated, UsersPermissions)

class UserContactAPIViewSet(GenericViewSet,
                            mixins.CreateModelMixin, 
                            mixins.DestroyModelMixin):
    queryset = models.UserContact.objects.all()
    serializer_class = serializers.UserContactSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)

class WorkExperienceAPIViewSet(GenericViewSet, 
                               mixins.CreateModelMixin, 
                               mixins.UpdateModelMixin, 
                               mixins.DestroyModelMixin):
    queryset = models.WorkExperience.objects.all()
    serializer_class = serializers.WorkExperienceSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class EducationAPIViewSet(GenericViewSet, 
                          mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, 
                          mixins.DestroyModelMixin):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class SkillsAPIViewSet(GenericViewSet, 
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, 
                       mixins.DestroyModelMixin):
    queryset = models.Skills.objects.all()
    serializer_class = serializers.SkillsSerializer
  
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)