from django.urls import path
from . import views
app_name = 'qrcode'
urlpatterns = [
    path('login', views.login, name = 'login'),
    path('file', views.upload_file, name='upload'),
    path('data_qr', views.quet_3_nguoi, name='quet-3-nguoi'),
    path('file_1', views.run_word_macro, name='upload_1'),
    # path('scan', views.scan_QR, name='test'),
  



    
]
