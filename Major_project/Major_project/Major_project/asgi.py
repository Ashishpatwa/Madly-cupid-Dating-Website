"""
ASGI config for Major_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from broadcast_notification.routing import websocket_urlpatterns
# from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Major_project.settings')
django.setup()

from channels.auth import AuthMiddleware, AuthMiddlewareStack

from chat.routing import websocket_urlpatterns as chat_websocket
from broadcast_notification.routing import websocket_urlpatterns as broad_websocket

# ws_patterns = [
#     path('ws/test/',BroadcastNotification)
# ]

# application = ProtocolTypeRouter(
#     "websocket": URLRouter(ws_patterns)
# )
websocket_urlpatterns= chat_websocket + broad_websocket

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
    #
    })

# django_asgi_app = get_asgi_application()
# from channels.security.websocket import AllowedHostsOriginValidator

# import Account_of_User.routing

# application = ProtocolTypeRouter(
#     {
#         "http": django_asgi_app,
#         "websocket": AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(Account_of_User.routing.websocket_urlpatterns))
#         ),
#     }
# )


