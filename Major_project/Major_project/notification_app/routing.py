from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/notification/(?P<room_names>\w+)/$", consumers.NotificationConsumer.as_asgi()),
]