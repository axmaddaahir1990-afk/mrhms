from django.db import models
from patients.models import Patient
from appointments.models import Appointment


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    lab_results = models.TextField(blank=True)
    doctor_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient.name} ({self.created_at:%Y-%m-%d})"

# Create your models here.
