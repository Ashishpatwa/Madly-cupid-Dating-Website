from django.urls import path
from . import views

urlpatterns=[
    path('',views.landing_page, name="landing_page"),
    path('home',views.Home, name="Home"),
    #  path('test',views.test, name="test"),
    path('login',views.loginpage, name="loginpage"),
    path('logout',views.logoutpage, name="logoutpage"),
    path('register',views.registerpage, name="registerpage"),
    path('search/',views.search, name="search"),
  

]