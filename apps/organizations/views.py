from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.organizations.models import Organization, OrganizationPost, OrganizationPostComment, OrganizationPostLike
from apps.organizations.serializers import OrganizationSerializer, OrganizationPostSerializer, OrganizationPostCommentSerializer, OrganizationPostLikeSerializer

# Create your views here.
class OrganizationAPIViewSet(GenericViewSet, ListModelMixin,
                        CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer