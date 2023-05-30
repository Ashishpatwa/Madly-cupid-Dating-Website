from django.urls import path
from . import views


urlpatterns=[
    path('',views.profile, name="profile_pic"),
    path('<user>',views.viewprofile, name="viewprofile_pic"),
    path('sendrequest/<str:user>', views.sendRequest, name="createRequest"),
    path('sendlike/<str:user>', views.sendLike, name="createLike"),
    path('noti/', views.noti, name="noti"),
    path('termcondition/',views.termcondition, name="term"),
    path('privacy/', views.privacy, name="privacy"),
    path('like/', views.like, name="like"),
    path('sendvisitor/<str:user>',views.visitor, name="visitor"),
    path('visitor/',views.showVisitor, name="showVisitor"),
    path('sendmessage/<str:user>',views.sendmessage, name="sendMessage"),
    path('chatting/<str:room_name>', views.chatting, name="chatting"),
    path('friends/', views.friends, name="friends"),
    path('update/', views.update, name="update"),


]