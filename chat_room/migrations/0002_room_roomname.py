# Generated by Django 2.2.3 on 2019-07-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomname',
            field=models.TextField(default='name', max_length=30, verbose_name='Название комнаты'),
            preserve_default=False,
        ),
    ]
