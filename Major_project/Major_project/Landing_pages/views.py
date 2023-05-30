from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Account_of_User.models import UserProfile, Friend
from channels.layers import get_channel_layer
from django.template import RequestContext
import json

def Home(request):
    if request.user.username == "": 
        return redirect('landing_page')
    users = UserProfile.objects.all()
    
    return render(request, "HOME/home.html",{"users":users,
        'room_name':"broadcast"
    })

# from asgiref.sync import async_to_sync
# def test(request):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "notification_broadcast",
#         {
#             'type': 'send_notification',
#             'message': json.dumps("Notification")
#         }
#     )
#     return HttpResponse("Done")

def landing_page(request):
    if request.user.username == "":
        return render(request, "Home/landing_page.html")
    return redirect('Home')

def loginpage(request):
    if request.user.username != "": 
        return render(request, "Home/home.html")
    if request.method == "POST":
        obj = authenticate(username = request.POST["username"], password=request.POST["password"])
        if obj is None:
            return render(request, "Home/login.html")
        else:
            login(request, obj)
            return redirect('Home')
    return render(request, "Home/login.html")

def logoutpage(request):
    if request.user.username != "":
        logout(request)
    return redirect("landing_page")

def registerpage(request):
    if request.user.username != "": 
        return render(request, "Home/home.html")
    elif request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        gmail = request.POST["gmail"]
        password = request.POST["password"]
        age = request.POST["age"]
        gender = request.POST.get("gender")
        print(gender)
        gender_value = {"Male": "M", "Female" : "F"}
        obj = User.objects.create_user(username = username, first_name=firstname, last_name=lastname, email=gmail,password=password)
        obj.save()
        profile = UserProfile.objects.get(user=obj)
        profile.age=age
        profile.gender = gender_value[gender]
        profile.save()


        login(request,obj)
        return redirect("Home")
    return render(request, "Home/registration.html")

def search(request):
    if request.method == "POST":
        search_input = request.POST["search_input"]
        users=[]
        user_objs = User.objects.filter(username__startswith = search_input)
        for user_obj in user_objs:
            try:
                users.append(UserProfile.objects.get(user_id = user_obj))
            except UserProfile.DoesNotExist:
                pass
        if len(users)>0:
            return render(request, "HOME/search.html" , {"users":users, 'room_name':"broadcast"}, )
        else:
            return render(request, "HOME/404.html")




