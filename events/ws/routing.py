from django.urls import re_path

from ws import consumers

websocket_urlpatterns = [
    re_path(r'msg/', consumers.ChatConsumer.as_asgi()),
]