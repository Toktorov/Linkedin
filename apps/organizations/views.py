from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.organizations.models import Organization, OrganizationPost, OrganizationPostComment, OrganizationPostLike
from apps.organizations.serializers import OrganizationSerializer, OrganizationDetailSerializer, OrganizationPostSerializer, OrganizationPostCommentSerializer, OrganizationPostLikeSerializer
from apps.organizations.permissions import OrganizationPermissions

# Create your views here.
class OrganizationAPIViewSet(GenericViewSet, ListModelMixin, CreateModelMixin,
                        UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return OrganizationDetailSerializer
        return OrganizationSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), OrganizationPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class PostAPIViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, 
                    UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = OrganizationPost.objects.all()
    serializer_class = OrganizationPostSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), OrganizationPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class CommentAPIViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, 
                        UpdateModelMixin, DestroyModelMixin):
    queryset = OrganizationPostComment.objects.all()
    serializer_class = OrganizationPostCommentSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), OrganizationPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class LikeAPIViewSet(GenericViewSet, ListModelMixin,
                        CreateModelMixin, DestroyModelMixin):
    queryset = OrganizationPostLike.objects.all()
    serializer_class = OrganizationPostLikeSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), OrganizationPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)