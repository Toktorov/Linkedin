from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

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