from django.contrib import admin

from apps.vacancies.models import Vacancy, VacancyFavorite

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(VacancyFavorite)