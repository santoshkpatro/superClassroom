from classrooms.models import Classroom
from rest_framework.exceptions import APIException


class ClassroomEnrolledLookupMixin:
    def get_classroom(self):
        if 'classroom_id' not in self.request.query_params:
            raise APIException('classroom id missing')
        classroom_id = self.request.query_params['classroom_id']
        try:
            classroom = Classroom.objects.get(id=classroom_id)
            if classroom not in self.request.user.classrooms.all():
                raise APIException('permission denies', 403)
        except Classroom.DoesNotExist:
            raise APIException('classroom does not exists', 404)
        return classroom
