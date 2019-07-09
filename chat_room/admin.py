from django.contrib import admin
from chat_room.models import Room, Chat

class RoomAdmin(admin.ModelAdmin):
    list_display = ('creater', 'invated_user', 'date', 'roomname')

    def invated_user(self, obj):
        return "\n".join([user.username for user in obj.invated.all()])



class ChadAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'text', 'date')


admin.site.register(Chat, ChadAdmin)
admin.site.register(Room, RoomAdmin)
