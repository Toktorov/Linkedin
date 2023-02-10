from django.db import models

from apps.users.models import User

# Create your models here.
class Organization(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="users_Organizations"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True, null=True
    )
    logo = models.ImageField(
        upload_to="organization_logo/",
        verbose_name="Логотип"
    )
    banner = models.ImageField(
        upload_to="organization_banner/",
        verbose_name="Баннер",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

class OrganizationPost(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name="Организация"
    )
    title = models.TextField(
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to="organization_image/",
        verbose_name="Фотография поста"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title 

class OrganizationPostLike(models.Model):
    post = models.ForeignKey(
        OrganizationPost,
        on_delete=models.CASCADE,
        related_name="organization_post_likes",
        verbose_name="Пост"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organization_posts_user",
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.post} - {self.user}"

    class Meta:
        verbose_name = "Пост организации"
        verbose_name_plural = "Посты организации"

class OrganizationPostComment(models.Model):
    post = models.ForeignKey(
        OrganizationPost,
        on_delete=models.CASCADE,
        related_name="organization_post_comments",
        verbose_name="Пост"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organization_posts_comment_user",
        verbose_name="Пользователь"
    )
    comment = models.CharField(
        max_length=300,
        verbose_name="Текст"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.post} - {self.user}"

    class Meta:
        verbose_name = "Комментарий организации"
        verbose_name_plural = "Комментарии организации"