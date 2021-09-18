from rest_framework import generics, permissions
from rest_framework.exceptions import APIException
from core.models import Note
from api.mixins import ClassroomEnrolledLookupMixin
from api.exceptions import PermissionDenied
from .serializers import NoteSerializer


class NoteCreate(ClassroomEnrolledLookupMixin, generics.CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        classroom = self.get_classroom()
        if not self.request.user.has_permission(classroom, 'teacher'):
            raise PermissionDenied
        serializer.save(classroom=classroom)


class NoteList(ClassroomEnrolledLookupMixin, generics.ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        classroom = self.get_classroom()
        queryset = super().get_queryset()
        return queryset.filter(classroom=classroom)


class NoteDetail(ClassroomEnrolledLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        classroom = self.get_classroom()
        if not self.request.user.has_permission(classroom, 'teacher'):
            raise PermissionDenied
        note = super().get_object()
        if note.classroom != classroom:
            raise PermissionDenied
        return note
