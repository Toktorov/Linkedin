from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Chat(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="chat_from_user",
        verbose_name="Чат от пользователя"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="chat_to_user",
        verbose_name="Чат к пользователю"
    )
    
    def __str__(self):
        return f"From {self.from_user}, to {self.to_user}"

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
        unique_together=(('from_user', 'to_user',),)

class ChatMessage(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE,
        related_name="chat_messages",
        verbose_name="Чат"
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="message_sender",
        verbose_name="Отправитель сообщения",
        null = True
    )
    message = models.CharField(
        max_length=300,
        verbose_name="Сообщение"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создан"
    )

    def __str__(self):
        return f"{self.chat.id}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"