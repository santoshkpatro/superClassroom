from rest_framework import serializers
from classrooms.models import Classroom
from core.models import Room


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'name', 'description', 'created_at')


class RoomClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'name')


class RoomSerializer(serializers.ModelSerializer):
    classroom = RoomClassroomSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'title', 'classroom', 'schedule_on', 'room_url')
