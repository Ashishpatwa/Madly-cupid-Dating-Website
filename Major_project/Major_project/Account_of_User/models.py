from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    gender_option = (
        ("M","Male"),
        ("F", "Female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=True)
    gender = models.CharField(max_length=1, choices=gender_option, blank=True, null=True)
    profilepic = models.ImageField(upload_to= "images",  default="images/default.jpg")    
    status = models.TextField( blank=True, null=True)
    City = models.CharField(max_length=30,  blank=True, null=True)
    Lives = models.CharField(max_length=10, blank=True, null=True)
    Interested  = models.CharField(max_length=20,  blank=True, null=True)
    Relationship = models.CharField(max_length=20,  blank=True, null=True)
    Looking = models.CharField(max_length=10,  blank=True, null=True)
    Height = models.IntegerField( blank=True, null=True)
    Education = models.CharField(max_length=20,  blank=True, null=True)
    Favoutite_music = models.CharField(max_length=30,  blank=True, null=True)
    Favoutite_movie = models.CharField(max_length=30, blank=True, null=True)
    Favoutite_Books = models.CharField(max_length=30, blank=True, null=True)
    Favoutite_TV_shows = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Friend(models.Model):
    user_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    friend_list = models.ManyToManyField(UserProfile, related_name="friend_list", blank=True)
    send_friend_request = models.ManyToManyField(UserProfile, related_name="send_friend_request", blank=True)
    like = models.PositiveIntegerField(default=0)
    visitor = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.user_id.user.username

class Relationship(models.Model):
    STATUS_CHOICES=(
        ("send","send"),
        ("accepted","accepted"),
        ('like', 'like'),
        ('visitor', 'visitor')
    )
    sender = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.sender.user_id.user.username
    
class Notifiy(models.Model):
    STATUS_CHOICES=(
        ("visited","visited"),
        ("like","like"),
        ("frndrequest","frndrequest"),
    )
    sender = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name="notisender")
    receiver = models.ForeignKey(Friend, on_delete=models.CASCADE, related_name="notireceiver")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.user_id.user.username

    


