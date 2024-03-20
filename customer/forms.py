from django import forms
from .widgets import CustomStatusWidget
from .models import Service, Employee, Manage, KhachHang, Choice

class KhachHangForm(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = '__all__'
        widgets = {
            'status': CustomStatusWidget(),
        }
