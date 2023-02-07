from django.db import models

from apps.users.models import User

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_notifications"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} {self.created}"
    
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"