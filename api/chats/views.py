from rest_framework import generics
from api.mixins import ClassroomEnrolledLookupMixin
from chats.models import Chat
from chats.serializers import ChatSerializer


class ChatList(ClassroomEnrolledLookupMixin, generics.ListAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def get_queryset(self):
        chats = super().get_queryset()
        classroom = self.get_classroom()
        return chats.filter(classroom=classroom)
