# Generated by Django 3.2 on 2021-05-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_chatrooms_chatroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='room',
            field=models.CharField(max_length=50),
        ),
    ]
