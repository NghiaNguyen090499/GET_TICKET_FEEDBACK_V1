# views.py
from django.http import HttpResponse
from .models import License
from django.shortcuts import render, redirect
from .license_manager import LicenseManager
from twilio.rest import Client
from django.conf import settings
from django.http import HttpResponse
def check_license(request):
    license_key = request.GET.get('license_key')
    print(license_key)
    try:
        license = License.objects.get(key=license_key)
        if license.is_valid():
            # Chứng nhận license hợp lệ, cho phép sử dụng chức năng
            return HttpResponse("License hợp lệ, cho phép sử dụng chức năng")
        else:
            # License hết hạn
            return HttpResponse("License has expired.")
    except License.DoesNotExist:
        # License không hợp lệ
        return HttpResponse("License không hợp lệ")
# views.py

license_manager = LicenseManager()

def renew_license(request):
    if request.method == 'GET':
        license_key = request.GET.get('license_key')
        print(license_key)
        if license_key:
            license_manager.set_license_key(license_key)
            return redirect('license:check_license')  # Chuyển hướng đến trang chính hoặc trang khác
        else:
            return render(request, 'license/renew_license.html')
    return render(request, 'license/renew_license.html')


def send_sms(request):
    account_sid = 'AC6b94d6beaa2dba9081c46b4936c22655'
    auth_token = '9f824825af04f09d1ce638dbed5ed480'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+16592745257',
    body ='Vui lòng đến nơi lấy',
    to='+84967047453'
    )

    print(message.sid)
    return HttpResponse('ok')