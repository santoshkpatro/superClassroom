import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import classrooms.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smserver.settings.local')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            classrooms.routing.websocket_urlpatterns
        )
    )
})
