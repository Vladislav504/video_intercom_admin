from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/image/", consumers.WebImageConsumer.as_asgi()),
    re_path(r"ws/text/", consumers.WebTextConsumer.as_asgi()),
]
