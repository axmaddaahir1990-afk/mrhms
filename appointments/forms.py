from django import forms
from .models import Appointment
from staff.models import Staff


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["patient", "doctor", "scheduled_for", "status", "notes"]
        widgets = {
            "scheduled_for": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Staff.objects.filter(role='DOCTOR')

