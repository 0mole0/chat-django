from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from chat_room.models import Room, Chat
from chat_room.serializers import RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializers
from django.db.models import Q

class Rooms(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        rooms = Room.objects.filter(Q(creater=request.user)|Q(invated=request.user))
        serializers = RoomSerializers(rooms, many=True)
        return Response({'data': serializers.data})
    def post(self, request):
        name = request.data.get('room')
        print('name')
        print(name)
        print(request.GET.get('room'))
        room=Room(roomname=name, creater=request.user)
        room.save()
        return Response(status=201)

class InvitedRoom(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request): 
        idRoom = request.GET.get('room')
        room = Room.objects.get(id=idRoom)
        serializers = RoomSerializers(room)
        return Response({'data': serializers.data})

class DeleteRoom(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        idRoom = request.GET.get('room')
        print(idRoom)
        rooms = Room.objects.get(id=idRoom)
        if rooms.creater == request.user:
            rooms.delete()
            return Response(status=201)

class Dialog(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        room = request.GET.get('room')
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({'data': serializer.data})
    def post(self, request):
        room = request.data.get('room')
        dialog = ChatPostSerializers(data = request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)

class AddUserRoom(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invated.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)

