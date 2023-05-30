from django.contrib import admin
from .models import UserProfile,Friend,Relationship,Notifiy
# Register your models here.

# admin.site.register(Uprofile)
admin.site.register(UserProfile)
admin.site.register(Friend)
admin.site.register(Relationship)
admin.site.register(Notifiy)
