from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.http import JsonResponse
from chat.models import *
# Create your views here.

def home(request):
    return render(request , 'api/home.html')


def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)

    context = {
        'username' : username,
        'room' : room,
        'room_details' : room_details
    }

    return render(request , 'api/room.html',context)

def checkview(request):

    room = request.POST['room_name']
    username = request.POST['username']
    passw = request.POST['passw']


    if Room.objects.filter(name = room).exists() :

        room_obj = Room.objects.get(name = room)
        if room_obj.password == passw:

            return redirect(room+'/?username='+username)
        else:
            context = {
                'message' : 'Wrong Password'
            }
            return render(request, 'api/home.html',context)



    else:
        new_room = Room.objects.create(name = room,password = passw)
        new_room.save()

        return redirect(room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value = message,user = username,room = room_id)
    new_message.save()

    return HttpResponse("SENT")


def getMessages(request,room):
    room_details = Room.objects.get(name = room)

    message = Message.objects.filter(room = room_details.id )
    return JsonResponse({"messages" : list(message.values())})