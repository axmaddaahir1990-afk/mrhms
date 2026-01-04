import os
import sys
import django
from django.utils import timezone

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mrhms.settings")
django.setup()

from patients.models import Patient
from staff.models import Staff
from rooms.models import Room, Bed
from appointments.models import Appointment
from pharmacy.models import Medicine
from billing.models import Invoice
from notifications.models import Notification


def run():
    p, _ = Patient.objects.get_or_create(
        name="John Doe", age=35, gender="M", phone="555-0001"
    )
    s, _ = Staff.objects.get_or_create(
        full_name="Dr. Amina Ali",
        role="DOCTOR",
        defaults={"specialization": "Cardiology", "is_on_duty": True},
    )
    r, _ = Room.objects.get_or_create(name="Ward A", type="General")
    Bed.objects.get_or_create(room=r, number="A1", is_available=True)

    if p and s:
        Appointment.objects.get_or_create(
            patient=p, doctor=s, scheduled_for=timezone.now()
        )

    Medicine.objects.get_or_create(name="Paracetamol", unit="tablet", stock=50)
    Invoice.objects.get_or_create(patient=p, amount="25.00", status="UNPAID")
    Notification.objects.get_or_create(
        title="Welcome",
        message="MRHMS has been set up successfully.",
        level="success",
    )
    print("Seed complete")


if __name__ == "__main__":
    run()
