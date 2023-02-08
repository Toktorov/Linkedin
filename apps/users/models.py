from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to="profile_image/",
        verbose_name="Фотография профиля"
    )
    is_premium = models.BooleanField(
        verbose_name="Премиум",
        default=False
    )
    premium_date = models.DateTimeField(
        blank = True, null = True
    )

    def __str__(self):
        return self.username 

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class UserContact(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="from_user_contact",
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="to_user_contact",
    )
    is_contact = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.from_user} - {self.to_user} - {self.is_contact}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        unique_together = (('from_user', 'to_user',),)

class TypeEmployment(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Тип занятости"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Тип занятости"
        verbose_name_plural = "Типы занятости"

class JobType(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Тип места работы"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Тип места работ"
        verbose_name_plural = "Типы места работы"

class WorkExperience(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="users_work_experience",
        verbose_name="Пользователь"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Например: менеджер по продажам"
    )
    type_of_employment = models.ForeignKey(
        TypeEmployment, 
        on_delete=models.SET_NULL,
        verbose_name="Тип занятости", 
        null = True
    )
    name_company = models.CharField(
        max_length=100,
        verbose_name="Название компании"
    )
    location = models.CharField(
        max_length=200,
        verbose_name="Местоположение",
        blank = True, null = True
    )
    job_type = models.ForeignKey(
        JobType, 
        on_delete=models.SET_NULL,
        verbose_name="Тип работы",
        blank = True, null = True,
    )
    date_start = models.DateField(
        verbose_name="Дата начала",
    )
    date_end = models.DateField(
        verbose_name="Дата окончания",
        blank = True, null = True
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return f"{self.user} - {self.name}"

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

class Education(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="users_education",
        verbose_name="Пользователь"
    )
    educational_institution = models.CharField(
        max_length=255,
        verbose_name="Учебное заведение"
    )
    degree = models.CharField(
        max_length=100,
        verbose_name="Степень",
        blank = True, null = True
    )
    specialization = models.CharField(
        max_length=100,
        verbose_name="Специализация",
        blank = True, null = True
    )
    date_start = models.DateField(
        verbose_name="Дата начала",
        blank = True, null = True
    )
    date_end = models.DateField(
        verbose_name="Год окончания (или ожидаемый)",
        blank = True, null = True
    )

    def __str__(self):
        return f"{self.title} - {self.educational_institution}"

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образовании"

class Skills(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_skill"
    )
    skill = models.CharField(
        max_length=100,
        verbose_name="Название навыка"
    )

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"