from broadcast_notification.models import Broadcast
def notifications(request):
    allnotifications = Broadcast.objects.all()
    return {'notifications': allnotifications}