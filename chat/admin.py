from django.contrib import admin
from chat.models import ChatRoom
from . import models


@admin.register(ChatRoom)
class RoomAdmin(admin.ModelAdmin):
	list_display = ('room', 'description', 'created')
