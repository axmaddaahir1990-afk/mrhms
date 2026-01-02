from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Medicine
from notifications.models import Notification


@login_required
def medicine_list(request):
    medicines = Medicine.objects.order_by('name')
    low_stock = [m for m in medicines if m.is_low_stock()]
    if low_stock:
        Notification.objects.get_or_create(
            title="Low-stock medicines",
            message=f"{len(low_stock)} items are low in stock.",
            level="warning"
        )
    return render(request, 'pharmacy/list.html', {'medicines': medicines})

