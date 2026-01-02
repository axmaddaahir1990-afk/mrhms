from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm


@login_required
def appointment_list(request):
    appointments = Appointment.objects.order_by('-scheduled_for')
    return render(request, 'appointments/list.html', {'appointments': appointments})


@login_required
def appointment_create(request):
    form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Appointment created • Ballan waa la abuuray')
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Book Appointment • Qor Ballan'})


@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Appointment updated • Ballan waa la cusbooneysiiyay')
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Edit Appointment • Tafatir Ballan'})

