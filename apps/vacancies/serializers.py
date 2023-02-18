from rest_framework import serializers

from apps.vacancies.models import Vacancy, VacancyFavorite


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'user', 'title', 'description', 'created')

class VacancyFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyFavorite
        fields = ('id', 'user', 'vacancy')