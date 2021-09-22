from channels.auth import AuthMiddlewareStack
from rest_framework_simplejwt.tokens import AccessToken


class TokenAuthMiddleware(AuthMiddlewareStack):
    pass
