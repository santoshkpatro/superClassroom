from rest_framework import serializers
from core.models import Assignment, Submission


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        extra_kwargs = {
            'classroom': {
                'required': False
            }
        }


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
