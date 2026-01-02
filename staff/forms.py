from django import forms
from .models import Staff


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["full_name", "role", "specialization", "phone", "is_on_duty", "availability_notes"]

