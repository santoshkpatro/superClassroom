from rest_framework import serializers
from core.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        extra_kwargs = {
            'classroom': {
                'required': False
            }
        }
