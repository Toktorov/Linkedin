from rest_framework import serializers

from apps.vacancies.models import Vacancy, VacancyFavorite, OrganizationVacancy, OrganizationVacancyFavorite


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'user', 'title', 'description', 'created')

class VacancyFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyFavorite
        fields = ('id', 'user', 'vacancy')

class OrganizationVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationVacancy
        fields = ('id', 'organization', 'user', 'title', 'description', 'created')

class OrganizationVacancyFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationVacancyFavorite
        fields = ('id', 'organization', 'user', 'vacancy')