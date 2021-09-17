from django.db import models
from rest_framework import generics, permissions
from classrooms.models import Classroom
from .serializers import ClassroomSerializer
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
