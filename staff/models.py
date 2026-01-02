from django.db import models


class Staff(models.Model):
    ROLE_CHOICES = [
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
        ('RECEPTIONIST', 'Receptionist'),
    ]
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    specialization = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    is_on_duty = models.BooleanField(default=False)
    availability_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_role_display()})"

# Create your models here.
