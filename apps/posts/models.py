from django.db import models

from apps.users.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="users_post",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name= "Заголовок"
    )
    image = models.ImageField(
        upload_to="post_image/",
        verbose_name="Фотография поста",
        blank=True, null = True
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"