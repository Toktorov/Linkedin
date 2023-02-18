from rest_framework import serializers

from apps.chats.models import Chat, ChatMessage


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat 
        fields = ('id', 'from_user', 'to_user')

    def validate(self, attrs):
        if attrs['from_user'] == attrs['to_user']:
            raise serializers.ValidationError({"error": "Нельзя писать самому себе"})
        return attrs

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"

class ChatDetailSerializer(serializers.ModelSerializer):
    chat_messages = ChatMessageSerializer(read_only=True, many=True)
    
    class Meta:
        model = Chat 
        fields = ('id', 'from_user', 'to_user', 'chat_messages')

class ChatMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"