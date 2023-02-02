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