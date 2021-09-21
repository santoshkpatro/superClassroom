import json
from django.core.serializers.json import DjangoJSONEncoder
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from classrooms.models import Classroom
from accounts.models import User
from .models import Chat
from .serializers import ChatSerializer


class ClassroomChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['classroom_id']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = text_data_json['user_id']
        classroom_id = text_data_json['classroom_id']

        user = User.objects.get(id=user_id)
        classroom = Classroom.objects.get(id=classroom_id)

        chat = Chat.objects.create(user=user, classroom=classroom, message=message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'chat': chat
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        chat = event['chat']
        serializer = ChatSerializer(chat)

        # Send message to WebSocket
        self.send(text_data=json.dumps(serializer.data, cls=DjangoJSONEncoder))
