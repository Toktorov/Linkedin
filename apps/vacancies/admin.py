from django.contrib import admin

from apps.vacancies.models import Vacancy, VacancyFavorite, OrganizationVacancy, OrganizationVacancyFavorite

# Register your models here.
admin.site.register(Vacancy)
admin.site.register(VacancyFavorite)
admin.site.register(OrganizationVacancy)
admin.site.register(OrganizationVacancyFavorite)