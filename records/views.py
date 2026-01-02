from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import MedicalRecord


@login_required
def records_list(request):
    records = MedicalRecord.objects.order_by('-created_at')[:50]
    return render(request, 'records/list.html', {'records': records})

