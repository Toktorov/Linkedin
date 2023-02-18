from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

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
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class PostImages(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="post_images",
        verbose_name="Пост"
    )
    image = models.ImageField(
        upload_to="post_images/",
        verbose_name="Фотография"
    )
    
    def __str__(self):
        return f"{self.id}, {self.post}"

    class Meta:
        verbose_name = "Фотография к посту"
        verbose_name_plural = "Фотография к постам"

class PostLike(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="post_likes",
        verbose_name = "Пользователь"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="post_users",
        verbose_name = "Пост"
    )

    def __str__(self):
        return f"{self.post} - {self.user}"

    class Meta:
        verbose_name = "Лайки к посту"
        verbose_name_plural = "Лайки к постам"
        unique_together = ('user', 'post')

class PostComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="post_comment_user",
        verbose_name = "Пользователь"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="post_commnets",
        verbose_name = "Пост"
    )

    def __str__(self):
        return f"{self.post} - {self.user}"

    class Meta:
        verbose_name = "Комментарий к посту"
        verbose_name_plural = "Комментарии к постам"
        unique_together = ('user', 'post')

class PostFavorites(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name = "Пользователь"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="post_favotites",
        verbose_name = "Пост"
    )
    def __str__(self):
        return f"{self.post} - {self.user}"

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        unique_together = ('user', 'post')