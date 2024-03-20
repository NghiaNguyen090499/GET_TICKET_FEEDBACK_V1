from django.urls import path
from license.views import *
from django.contrib.auth.decorators import login_required

app_name = 'license'
urlpatterns = [
    path('license/',renew_license, name='renew_license'),
    path('check_license/',check_license, name='check_license'),
    path('check_license/',check_license, name='check_license'),
    path('send',send_sms, name='send_sms')
]
    