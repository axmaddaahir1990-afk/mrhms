from django.db import models
from patients.models import Patient


class Room(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, default='General')

    def __str__(self):
        return f"{self.name} ({self.type})"


class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
    number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    assigned_patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Bed {self.number} - {self.room.name}"

# Create your models here.
