from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from django.contrib.auth.models import Group
        try:
            for role in ["Admin", "Doctor", "Nurse", "Receptionist"]:
                Group.objects.get_or_create(name=role)
        except Exception:
            # During migrations or initial setup, DB may not be ready.
            pass
