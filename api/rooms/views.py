from rest_framework import generics, permissions
from rest_framework.exceptions import APIException
from core.models import Room
from api.mixins import ClassroomEnrolledLookupMixin
from .serializers import RoomSerializer


class RoomCreate(ClassroomEnrolledLookupMixin, generics.CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        classroom = self.get_classroom()
        if not self.request.user.has_permission(classroom, 'teacher'):
            raise APIException('Permission denied', 403)
        serializer.save(classroom=classroom)


class RoomList(ClassroomEnrolledLookupMixin, generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        classroom = self.get_classroom()
        queryset = super().get_queryset()
        return queryset.filter(classroom=classroom)


class RoomDetail(ClassroomEnrolledLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        classroom = self.get_classroom()
        if not self.request.user.has_permission(classroom, 'teacher'):
            raise APIException('Permission denied', 403)
        room = super().get_object()
        if room.classroom != classroom:
            raise APIException('Permission denied', 403)
        return room
