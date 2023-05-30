from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile,Friend,Notifiy,Relationship
@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        Friend.objects.create(user_id = profile)

@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_= instance.sender
    receiver_= instance.receiver
    if instance.status == "accepted":
        sender_.friend_list.add(receiver_.user_id)
        sender_.send_friend_request.remove(receiver_.user_id)
        Notifiy.objects.get(sender=instance.receiver, receiver=instance.sender, status="frndrequest").delete()
        receiver_.friend_list.add(sender_.user_id)
        sender_.save()
        receiver_.save()
    elif instance.status == "send":
        notificationObject = Notifiy.objects.filter(sender=instance.sender, receiver=instance.receiver, status="frndrequest")
        if not notificationObject:
            receiver_.send_friend_request.add(sender_.user_id)
            Notifiy.objects.create(sender=instance.sender, receiver=instance.receiver, status="frndrequest")
            receiver_.save()
        else:
            Notifiy.objects.get(sender=instance.sender, receiver=instance.receiver, status="frndrequest").delete()
    elif instance.status == 'like':
        notificationObject = Notifiy.objects.filter(sender = instance.sender, receiver= instance.receiver, status="like") 
        if not notificationObject:
            receiver_.like += 1
            Notifiy.objects.create(sender=instance.sender, receiver=instance.receiver, status="like")
            receiver_.save()
        else:
            Notifiy.objects.get(sender=instance.sender, receiver=instance.receiver, status="like").delete()

    elif instance.status == 'visitor':
        receiver_.visitor += 1
        Notifiy.objects.create(sender=instance.sender, receiver=instance.receiver, status="visitor")
        receiver_.save()

