from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
from django.core.asgi import get_asgi_application


application = ProtocolTypeRouter({
  "http": get_asgi_application(),  # Handles HTTP requests
  "websocket" : AuthMiddlewareStack(
    URLRouter(
      chat.routing.websocket_urlpatterns
    )
  ),
})