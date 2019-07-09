from rest_framework import serializers
from django.contrib.auth.models import User
from chat_room.models import Room, Chat

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'USERNAME_FIELD', 'REQUIRED_FIELDS')

class RoomSerializers(serializers.ModelSerializer):
    creater = UserSerializers()
    invated = UserSerializers(many=True)
    class Meta:
        model = Room
        fields = ('id','creater', 'invated', 'date','roomname')
    
class ChatSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Chat
        fields = ('user', 'text', 'date')

class ChatPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('text', 'room')