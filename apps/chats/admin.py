from django.contrib import admin

from apps.chats.models import Chat, ChatMessage

# Register your models here.
admin.site.register(Chat)
admin.site.register(ChatMessage)