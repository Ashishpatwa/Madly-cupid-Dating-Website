from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from . models import UserProfile,Notifiy,Relationship,Friend
from chat.models import Message
from django.http import Http404
from datetime import date
from django.urls import reverse


def update(request):
    if request.user.username == "": 
        return redirect('loginpage')
    elif request.method == "POST":
        username = request.user.username
        print("hii",username)
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = request.POST["age"]
        gender = request.POST.get("gender")
        gender_value = {"Male": "M", "Female" : "F"}
        status = request.POST["status"]
        pic = request.FILES.get("profile_pic")
        City = request.POST["City"]
        lives = request.POST["lives"]
        Interested = request.POST["Interested"]
        Relationships= request.POST["Relationships"]
        Looking= request.POST["Looking"]
        Height= request.POST["Height"]
        Education= request.POST["Education"]
        Favourite_music= request.POST["Favourite_music"]
        Favourite_movie= request.POST["Favourite_movie"]
        Favoutite_Books= request.POST["Favoutite_Books"]
        obj = User.objects.get(username = username)
        obj.first_name = firstname
        obj.last_name = lastname
        obj.save()
        profile = UserProfile.objects.get(user=obj)
        profile.City =City
        profile.Lives = lives
        profile.Interested = Interested
        profile.Relationship = Relationships
        profile.Looking = Looking
        profile.Height = Height
        profile.Education = Education
        profile.Favoutite_music =Favourite_music
        profile.Favoutite_movie = Favourite_movie
        profile.Favoutite_Books = Favoutite_Books
        profile.age=age
        profile.gender = gender_value[gender]
        profile.status = status
        profile.profilepic = pic
        profile.save()
        return redirect('profile_pic')
 
    return render(request, "HOME/update.html",{"room_names":"broadcast"})




def profile(request):
    if request.user.username == "": 
        return redirect('loginpage') 
    try:
        user_obj = User.objects.get(username = request.user.username)
        profile_obj = UserProfile.objects.get(user = user_obj)
        print(profile_obj,"---")

        senderUser = User.objects.get(username = request.user.username)
        senderProfile = UserProfile.objects.get(user = senderUser)
        senderFrnd = Friend.objects.get(user_id = senderProfile)

        friendList = [friend for friend in senderFrnd.friend_list.all()]
        return render(request, "HOME/profile.html",{"friendList": friendList,"profile_obj":profile_obj, "room_names":"broadcast"})
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")

def viewprofile(request, **kwargs):
    if request.user.username == "": 
        return redirect('loginpage')
    try:
        user_obj = User.objects.get(username = kwargs.get('user'))
        profile_obj = UserProfile.objects.get(user_id = user_obj)
        print("---------------------",profile_obj.profilepic.url, "0", profile_obj)
        usernames = [request.user.username, kwargs.get('user')]
        usernames.sort()  
        room_name = ''.join(usernames)

        senderUser = User.objects.get(username = request.user.username)
        senderProfile = UserProfile.objects.get(user = senderUser)
        senderFrnd = Friend.objects.get(user_id = senderProfile)

        friendList = [friend for friend in senderFrnd.friend_list.all()]

        return render(request, "HOME/profile.html",{"friendList": friendList,"profile_obj":profile_obj, 'room_names':"broadcast", 'room_name':room_name})
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")
    
def sendRequest(request, **kwargs):
    if request.user.username == "": 
        return redirect('loginpage')
        
    try:
        
        receiver = User.objects.get(username = kwargs.get('user'))
        sender = User.objects.get(username = request.user.username)
        receiverUser = UserProfile.objects.get(user = receiver)
        senderUser = UserProfile.objects.get(user = sender)

        senderFriend = Friend.objects.get(user_id= senderUser)
        receiverFriend = Friend.objects.get(user_id = receiverUser)
        request_type = "send"
        print("uuu",senderUser, receiverUser, request_type)
        notificationCreate = Relationship(sender=senderFriend, receiver=receiverFriend, status=request_type)
        notificationCreate.save()
        
    except Exception as e:
        print(f"Error creating notification: {e}")
        return JsonResponse({'success': False, 'error': str(e)})
        
    
    return JsonResponse({'success': True})


def sendLike(request, **kwargs):
    if request.user.username == "": 
        return redirect('loginpage')
        
    try:
        receiver = User.objects.get(username = kwargs.get('user'))
        sender = User.objects.get(username = request.user.username)
        receiverUser = UserProfile.objects.get(user = receiver)
        senderUser = UserProfile.objects.get(user = sender)

        senderFriend = Friend.objects.get(user_id= senderUser)
        receiverFriend = Friend.objects.get(user_id = receiverUser)
        request_type = "like"
        print(senderUser, receiverUser, request_type)
        notificationCreate = Relationship(sender=senderFriend, receiver=receiverFriend, status=request_type)
        notificationCreate.save()
    except Exception as e:
        print(f"Error creating notification: {e}")
        return JsonResponse({'success': False, 'error': str(e)})
        
    
    return JsonResponse({'success': True})

def visitor(request, **kwargs):
    if request.user.username == "": 
        return redirect('loginpage')
        
    try:
        receiver = User.objects.get(username = kwargs.get('user'))
        sender = User.objects.get(username = request.user.username)
        receiverUser = UserProfile.objects.get(user = receiver)
        senderUser = UserProfile.objects.get(user = sender)

        senderFriend = Friend.objects.get(user_id= senderUser)
        receiverFriend = Friend.objects.get(user_id = receiverUser)
        request_type = "visitor"
        print("-----------5555555555555555555555")
        print(senderUser, receiverUser, request_type)
        notificationCreate = Relationship(sender=senderFriend, receiver=receiverFriend, status=request_type)
        notificationCreate.save()
    except Exception as e:
        print(f"Error creating notification: {e}")
        return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': True})


def sendmessage(request, **kwargs):
    if request.user.username == "": 
        return redirect('loginpage')
    
    try:
        senderUser = User.objects.get(username = request.user.username)
        senderProfile = UserProfile.objects.get(user = senderUser)
        senderFrnd = Friend.objects.get(user_id = senderProfile)

        receiverUser = User.objects.get(username = kwargs.get('user'))
        receiverProfile = UserProfile.objects.get(user = receiverUser)
        receiverFrnd = Friend.objects.get(user_id = receiverProfile)

        friendList = [friend.user for friend in receiverFrnd.friend_list.all()]
        
        print(friendList)
        print(senderFrnd.user_id)
     
        if senderFrnd.user_id.user in friendList:
            usernames = [request.user.username, kwargs.get('user')]
            usernames.sort()  
            room_name = ''.join(usernames)

            messages = Message.objects.filter(room=room_name)

            receiver = User.objects.get(username = kwargs.get('user'))
            username = UserProfile.objects.get(user = receiver)
            return render(request, 'HOME/room.html', {'room_name': room_name, 'receiverpic': username, 'receivername': receiver, 'messages': messages, 'sendername':kwargs.get('user'), "username": request.user.username, "room_names":"broadcast"})
            # return render(request, "HOME/404.html")

            # return redirect(f'{url}?username={request.user.username}&user={kwargs.get('user')}')
            # return redirect(f'{url}?username={request.user.username}&user={receiverProfile}')
            # return render(request, "HOME/noti.html")

        else:
            url = reverse('viewprofile_pic', args=[kwargs.get('user')])
            return redirect(f'{url}?showPopup=true')
        
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")
    



def noti(request):

    if request.user.username == "": 
        return redirect('loginpage')
    users = []
    try:
        receiverUser = User.objects.get(username = request.user.username)
        receiverProfile = UserProfile.objects.get(user = receiverUser)
        receiverFrnd = Friend.objects.get(user_id = receiverProfile)
        users = Notifiy.objects.filter(receiver = receiverFrnd)
        print(":::",receiverProfile,receiverFrnd)

        return render(request, "HOME/noti.html",{"users":users, "room_names":"broadcast", 'today': date.today()})
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")
    

def like(request):

    if request.user.username == "": 
        return redirect('loginpage')
    users = []
    try:
        receiverUser = User.objects.get(username = request.user.username)
        receiverProfile = UserProfile.objects.get(user = receiverUser)
        receiverFrnd = Friend.objects.get(user_id = receiverProfile)
        users = Notifiy.objects.filter(receiver = receiverFrnd, status= "like")
        print(":::",receiverProfile,receiverFrnd)

        return render(request, "HOME/like.html",{"users":users, "room_names":"broadcast", 'today': date.today()})
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")


def chatting(request, room_name):
    if request.user.username == "": 
        return redirect('loginpage')
    
    try:
        return render(request,'HOME/chatting.html', {'room_name': room_name, 'username': request.user.username, "room_names":"broadcast"})
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")
    
def showVisitor(request):
    if request.user.username == "": 
        return redirect('loginpage')
    users = []
    try:
        receiverUser = User.objects.get(username = request.user.username)
        receiverProfile = UserProfile.objects.get(user = receiverUser)
        receiverFrnd = Friend.objects.get(user_id = receiverProfile)
        visitors = Notifiy.objects.filter(receiver = receiverFrnd, status="visitor")
        print(":::",receiverProfile,receiverFrnd)
        visitor_dict = {}
        for visitor in visitors:
            if visitor.sender.user_id.user.username not in visitor_dict:
                visitor_dict[visitor.sender.user_id.user.username] = {
                    "count": 1,
                    "profilepic": visitor.sender.user_id.profilepic.url,
                    "age": visitor.sender.user_id.age,
                    "gender": visitor.sender.user_id.gender,
                }
            else:
                visitor_dict[visitor.sender.user_id.user.username]["count"] += 1
        unique_visitors = [
            {
                "username": username,
                "count": visitor_dict[username]["count"],
                "profilepic": visitor_dict[username]["profilepic"],
                "age": visitor_dict[username]["age"],
                "gender": visitor_dict[username]["gender"],
            }
            for username in visitor_dict
        ]
        unique_visitors.sort(key=lambda x: x["count"], reverse=True)
        

        return render(request, "HOME/visitor.html",{"unique_visitors": unique_visitors, "room_names":"broadcast"})
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")


def termcondition(request):
    if request.user.username == "": 
        return redirect('loginpage')
    return render(request, "HOME/term.html", {"room_names":"broadcast"})

def privacy(request):
    if request.user.username == "": 
        return redirect('loginpage')
    return render(request, "HOME/privacy.html", {"room_names":"broadcast"})

def friends(request):
    if request.user.username == "": 
        return redirect('loginpage')
    
    try:
        senderUser = User.objects.get(username = request.user.username)
        senderProfile = UserProfile.objects.get(user = senderUser)
        senderFrnd = Friend.objects.get(user_id = senderProfile)

        friendList = [friend for friend in senderFrnd.friend_list.all()]

        return render(request, "HOME/friends.html",{"friendList": friendList, "room_names":"broadcast"})
    except Exception as e:
        print(f"Error creating notification: {e}")
        return render(request, "HOME/404.html")
    




    
    











    


