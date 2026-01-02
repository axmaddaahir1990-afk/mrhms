from django.db import models
from django.utils import timezone
from patients.models import Patient
from staff.models import Staff


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='appointments', limit_choices_to={'role': 'DOCTOR'})
    scheduled_for = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.full_name} on {self.scheduled_for:%Y-%m-%d %H:%M}"

# Create your models here.
