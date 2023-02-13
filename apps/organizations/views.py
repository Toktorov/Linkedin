from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.organizations.models import Organization, OrganizationPost, OrganizationPostComment, OrganizationPostLike
from apps.organizations.serializers import OrganizationSerializer, OrganizationDetailSerializer, OrganizationPostSerializer, OrganizationPostCommentSerializer, OrganizationPostLikeSerializer
from apps.organizations.permissions import OrganizationPermissions

# Create your views here.
class OrganizationAPIViewSet(GenericViewSet, ListModelMixin,
                        CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):
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