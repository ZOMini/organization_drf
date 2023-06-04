from django.urls import path

from ws.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("websocket/", ChatConsumer.as_asgi()),
]
