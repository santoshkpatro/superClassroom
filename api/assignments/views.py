import uuid
from django.db import models
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from core.models import Assignment, Submission
from api.mixins import ClassroomEnrolledLookupMixin
from api.exceptions import PermissionDenied
from .serializers import AssignmentSerializer, SubmissionSerializer
from django.conf import settings
from django.http import Http404


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


def handle_local_upload(f, host=None):
    url = settings.MEDIA_ROOT
    filename = uuid.uuid4().hex
    extension = f.content_type.split('/')[1]
    resource_url = f'{url}/submissions/{filename}.{extension}'
    with open(resource_url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    path = f'{host}{settings.MEDIA_URL}{resource_url.split(settings.MEDIA_URL)[1]}'
    return path


class AssignmentSubmission(ClassroomEnrolledLookupMixin, APIView):
    parser_classes = [FileUploadParser]

    def get_object(self, pk):
        try:
            assignment = Assignment.objects.get(id=pk)
            return assignment
        except Assignment.DoesNotExist:
            raise Http404

    def put(self, request, pk, filename, format=None):
        host = request.get_host()
        file_obj = request.data['file']
        classroom = self.get_classroom()
        assignment = self.get_object(pk)
        resource_url = handle_local_upload(file_obj, host)
        submission = Submission.objects.create(student=request.user,
                                               resource_url=resource_url, assignment=assignment)
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data, status=201)
