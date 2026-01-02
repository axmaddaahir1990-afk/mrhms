from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from patients.models import Patient
from staff.models import Staff
from appointments.models import Appointment
from rooms.models import Bed


@login_required
def dashboard(request):
    metrics = {
        "total_patients": Patient.objects.count(),
        "doctors_on_duty": Staff.objects.filter(role='DOCTOR', is_on_duty=True).count(),
        "appointments_today": Appointment.objects.filter(scheduled_for__date=timezone.now().date()).count(),
        "available_beds": Bed.objects.filter(is_available=True).count(),
    }
    return render(request, 'dashboard/index.html', {"metrics": metrics})
