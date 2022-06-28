from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name':"Let's learn Python!"},
#     {'id':2, 'name':'Front end developers'},
#     {'id':3, 'name':'Back end developers'},
# ]

def home(request):
    rooms = Room.objects.all()

    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)
    # return HttpResponse("Hello")

def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {'room':room}
    return render(request, 'base/room.html', context)
    # return HttpResponse("Room")
