from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.vacancies.models import Vacancy, VacancyFavorite
from apps.vacancies.serializers import VacancySerializer, VacancyFavoriteSerializer
from apps.vacancies.permissions import VacancyPermissions

# Create your views here.
class VacancyAPIViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin,
                        CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), VacancyPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class VacancyFavoriteAPIViewSet(GenericViewSet, CreateModelMixin, 
                                UpdateModelMixin, DestroyModelMixin):
    queryset = VacancyFavorite.objects.all()
    serializer_class = VacancyFavoriteSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            return (IsAuthenticated(), VacancyPermissions())
        return (AllowAny(), )

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)