from django.urls import path
from app.consumers import MySynconsumer

websocket_urlpatterns = [
    path('ws/sc/', MySynconsumer.as_asgi()),
    path('ws/sc/<str:grpname>/', MySynconsumer.as_asgi()),
]