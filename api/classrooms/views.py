from django.db.models import Q
from rest_framework import generics, permissions
from classrooms.models import Classroom
from core.models import Room
from .serializers import ClassroomSerializer, RoomSerializer
from .permissions import IsAdminOrReadOnly


class ClassroomCreate(generics.CreateAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ClassroomList(generics.ListAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin:
            return super().get_queryset()
        return self.request.user.classrooms.all()


class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]


class ClassroomRoomList(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        classrooms = self.request.user.classrooms.all()
        q = None
        for classroom in classrooms:
            if q is None:
                q = classroom.rooms.all()
            else:
                q = q.union(classroom.rooms.all())
        return q.order_by('schedule_on').reverse()
