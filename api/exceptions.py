from rest_framework.exceptions import APIException
from rest_framework import status


class PermissionDenied(APIException):
    status_code = 401
    default_detail = 'Permission denied'
