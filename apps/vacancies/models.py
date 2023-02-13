from django.db import models

from apps.users.models import User
from apps.organizations.models import Organization

# Create your models here.
class Vacancy(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_vacancies"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название ваканции"
    )
    description = models.TextField(
        verbose_name="Описание ваканции"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} - {self.title}"

    class Meta:
        verbose_name = "Ваканция от пользователя"
        verbose_name_plural = "Ваканции от пользователей"

class VacancyFavorite(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="vacancy_users"
    )
    vacancy = models.ForeignKey(
        Vacancy, 
        on_delete=models.CASCADE,
        related_name="users_vacancies"
    )

    def __str__(self):
        return f"{self.user} {self.vacancy}"

    class Meta:
        verbose_name = "Избранная ваканция от пользователя"
        verbose_name_plural = "Избранные ваканции от пользователей"

class OrganizationVacancy(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="organization_vacancy",
        verbose_name="Организация"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="organization_user_vacancy",
        null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название ваканции"
    )
    description = models.TextField(
        verbose_name="Описание ваканции"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} - {self.title}"

    class Meta:
        verbose_name = "Ваканция от организации"
        verbose_name_plural = "Ваканции от организации"

class OrganizationVacancyFavorite(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="organization_vacancy_favorite",
        verbose_name="Организация"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="vacancy_users_favorite"
    )
    vacancy = models.ForeignKey(
        Vacancy, 
        on_delete=models.CASCADE,
        related_name="organizations_vacancies"
    )

    def __str__(self):
        return f"{self.user} {self.vacancy}"

    class Meta:
        verbose_name = "Избранная ваканция от организации"
        verbose_name_plural = "Избранные ваканции от организации"