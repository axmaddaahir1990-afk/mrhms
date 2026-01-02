from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Invoice


@login_required
def invoice_list(request):
    invoices = Invoice.objects.order_by('-created_at')[:100]
    return render(request, 'billing/list.html', {'invoices': invoices})

