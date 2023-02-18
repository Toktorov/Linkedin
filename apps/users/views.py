from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
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

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return serializers.UserDetailSerializer
        if self.action in ('create', ):
            return serializers.UserRegisterSerializer
        if self.action in ('update', 'partial_update'):
            return serializers.UserUpdateSerializer
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

class ChangePasswordAPIView(UpdateAPIView):
    model = models.User
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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