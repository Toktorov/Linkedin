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

    def __str__(self):
        return self.username 

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"