from django.shortcuts import render
from .models import Message
from django.contrib.auth.models import User
from Account_of_User.models import UserProfile

# Create your views here.
def index(request):
  return render(request, 'HOME/index.html')

def room(request, room_name):
  username = request.user.username
  messages = Message.objects.filter(room=room_name)
  # user = request.GET.get('user', 'Anonymous')
  return render(request, 'HOME/room.html', {'room_name': room_name, 'username': username, 'messages': messages})

def rooms(request, room_name):
  username = request.GET.get('username', 'Anonymous')

  return render(request, 'HOME/rooms.html', {'room_name': room_name, 'username': username})
