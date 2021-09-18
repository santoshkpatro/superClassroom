from rest_framework import generics, permissions
from rest_framework.exceptions import APIException
from core.models import Assignment
from api.mixins import ClassroomEnrolledLookupMixin
from api.exceptions import PermissionDenied
from .serializers import AssignmentSerializer


class AssignmentCreate(ClassroomEnrolledLookupMixin, generics.CreateAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        classroom = self.get_classroom()
        if not self.request.user.has_permission(classroom, 'teacher'):
            raise PermissionDenied
        serializer.save(classroom=classroom)


class AssignmentList(ClassroomEnrolledLookupMixin, generics.ListAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        classroom = self.get_classroom()
        queryset = super().get_queryset()
        return queryset.filter(classroom=classroom)


class AssignmentDetail(ClassroomEnrolledLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        classroom = self.get_classroom()
        if not self.request.user.has_permission(classroom, 'teacher'):
            raise PermissionDenied
        assign = super().get_object()
        if assign.classroom != classroom:
            raise PermissionDenied
        return assign
