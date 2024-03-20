# license_manager.py
from datetime import date
from django.utils import timezone
from .models import License

class LicenseManager:
    _instance = None
    license_key = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LicenseManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.load_license_info()
        return cls._instance

    def load_license_info(self):
        if self.license_key:
            try:
                license = License.objects.get(key=self.license_key)
                if license.is_valid():
                    self.license_info = license
                else:
                    self.license_info = None
            except License.DoesNotExist:
                self.license_info = None
        else:
            self.license_info = None

    def is_valid_license(self):
        return self.license_info is not None

    def get_license_info(self):
        return self.license_info

    def set_license_key(self, license_key):
        self.license_key = license_key
        self.load_license_info()
