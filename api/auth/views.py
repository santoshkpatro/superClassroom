from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserCreateSerializer, UserProfileSerializer, UserLoginSerializer


@api_view(['POST'])
def register_view(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = AccessToken.for_user(user)
        return Response({'details': 'user created', 'access_token': str(token)}, status=status.HTTP_201_CREATED)
    else:
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    email = request.data['email']
    password = request.data['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise APIException('user not found', 404)
    else:
        raise APIException('email id or password entered in invalid', 401)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return user
