from django.db.models import fields
from rest_framework import serializers
from .models import Chat
from accounts.models import User


class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'profile_url')


class ChatSerializer(serializers.ModelSerializer):
    user = UserMessageSerializer()

    class Meta:
        model = Chat
        fields = ('id', 'classroom', 'message', 'user', 'created_at')
