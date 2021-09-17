from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.tokens import AccessToken


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'profile_url', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        # return super().create(validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'profile_url']
        read_only_fields = ['email']


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'profile_url', 'token']

    def get_token(self, obj):
        return str(AccessToken.for_user(obj))
