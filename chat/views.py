from django.shortcuts import render
from . models import ChatRoom


def index(request):
	all_rooms = ChatRoom.objects.all()
	return render(request, 'chat/index.html', {'all_rooms': all_rooms})


def room(request, room_name):
	return render(request, 'chat/chatroom.html', {'room_name': room_name})
