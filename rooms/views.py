from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room


@login_required
def rooms_list(request):
    rooms = Room.objects.all().prefetch_related('beds')
    return render(request, 'rooms/list.html', {'rooms': rooms})

