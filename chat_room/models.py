from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    creater = models.ForeignKey(User, verbose_name = 'Создатель', on_delete=models.CASCADE)
    roomname = models.TextField('Название комнаты', max_length=30)
    invated =models.ManyToManyField(User, verbose_name = 'Участники', related_name='invated_user')
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комнаты чата'
    
class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name='Комнта чата', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    date = models.DateTimeField('Дата отправления', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чата'
