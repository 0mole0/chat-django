# Generated by Django 2.2.3 on 2019-07-06 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('invated', models.ManyToManyField(related_name='invated_user', to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'Комната чата',
                'verbose_name_plural': 'Комнаты чата',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправления')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_room.Room', verbose_name='Комнта чата')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Сообщение чата',
                'verbose_name_plural': 'Сообщения чата',
            },
        ),
    ]