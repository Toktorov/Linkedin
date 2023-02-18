from rest_framework import serializers

from apps.chats.models import Chat, ChatMessage


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat 
        fields = "__all__"

    def validate(self, attrs):
        if attrs['from_user'] == attrs['to_user']:
            raise serializers.ValidationError({"error": "Нельзя писать самому себе"})
        if Chat.objects.filter(from_user = attrs['from_user'], to_user = attrs['to_user']).exists() or Chat.objects.filter(to_user = attrs['from_user'], from_user = attrs['to_user']).exists():
            raise serializers.ValidationError({"exits" : "Такой чат уже существует"})
        return 

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"

class ChatMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"