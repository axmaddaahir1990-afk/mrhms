from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm


@login_required
def staff_list(request):
    staff = Staff.objects.order_by('full_name')
    return render(request, 'staff/list.html', {'staff': staff})


@login_required
def staff_create(request):
    form = StaffForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Staff added • Shaqaalaha waa la daray')
        return redirect('staff_list')
    return render(request, 'staff/form.html', {'form': form, 'title': 'Add Staff • Ku dar Shaqaale'})

