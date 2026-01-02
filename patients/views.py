from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm


@login_required
def patient_list(request):
    patients = Patient.objects.order_by('-created_at')
    return render(request, 'patients/list.html', {'patients': patients})


@login_required
def patient_create(request):
    form = PatientForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        patient = form.save()
        messages.success(request, 'Patient created successfully • Bukaanka waa la abuuray')
        return redirect('patient_detail', pk=patient.pk)
    return render(request, 'patients/form.html', {'form': form, 'title': 'Add Patient • Ku dar Bukaan'})


@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Patient updated • Bukaanka waa la cusbooneysiiyay')
        return redirect('patient_detail', pk=patient.pk)
    return render(request, 'patients/form.html', {'form': form, 'title': 'Edit Patient • Tafatir Bukaan'})


@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/detail.html', {'patient': patient})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.warning(request, 'Patient deleted • Bukaanka waa la tirtiray')
        return redirect('patient_list')
    return render(request, 'patients/delete_confirm.html', {'patient': patient})

