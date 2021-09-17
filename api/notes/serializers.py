from rest_framework import serializers
from core.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {
            'classroom': {
                'required': False
            }
        }
