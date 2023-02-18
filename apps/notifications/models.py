from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_notifications"
    )
    message = models.CharField(
        max_length=255,
        verbose_name="Уведомление"
    )
    is_read = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} {self.created}"
    
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"