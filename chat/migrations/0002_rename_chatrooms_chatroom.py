# Generated by Django 3.2 on 2021-05-02 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatRooms',
            new_name='ChatRoom',
        ),
    ]
