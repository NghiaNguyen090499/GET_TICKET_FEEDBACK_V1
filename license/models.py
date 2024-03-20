
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# models.py
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

class License(models.Model):
    key = models.CharField(max_length=255, unique=True)
    expiration_date = models.DateField()
    max_users = models.PositiveIntegerField()
    used_users = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)  # Trạng thái của license
    notification_sent = models.BooleanField(default=False)
    def is_valid(self):
        return self.is_active and self.expiration_date > timezone.now().date()

@receiver(pre_save, sender=License)
def update_license_status(sender, instance, **kwargs):
    if instance.expiration_date < timezone.now().date() or instance.used_users > instance.max_users:
        instance.is_active = False
        instance.notification_sent = True
