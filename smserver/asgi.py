import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from ws.classrooms.consumers import ClassroomChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smserver.settings.local')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chats/classrooms/<uuid:classroom_id>/', ClassroomChatConsumer.as_asgi())
        ])
    )
})
