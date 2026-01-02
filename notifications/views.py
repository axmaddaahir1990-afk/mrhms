from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Notification


@login_required
def notification_list(request):
    notifications = Notification.objects.order_by('-created_at')[:100]
    return render(request, 'notifications/list.html', {'notifications': notifications})

