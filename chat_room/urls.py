from django.urls import path, include
from chat_room.views import *

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('roomdelete/', DeleteRoom.as_view()),
    path('invatedroom/', InvitedRoom.as_view()),
    path('dialog/', Dialog.as_view()),
    path('user/', AddUserRoom.as_view())
]