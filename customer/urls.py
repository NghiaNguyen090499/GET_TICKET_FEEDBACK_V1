from django.urls import path
from customer.views import *
from QRcodes.views import *
from django.contrib.auth.decorators import login_required

app_name = 'customer'
urlpatterns = [
    path('dang_nhap',dang_nhap, name='dang-nhap'),
    path('',trang_chu_2, name='trang-chu'),
    path('danh_gia/<int:pk>/<int:ticket_number>/',danh_gia, name='danh_gia'),
    path('lay_so/<int:pk>/',get_ticket, name='lay-so'),
    path('gui_khach_hang/<int:pk>/<int:ticket_number>/',gui_khach_hang, name='gui-khach-hang'),
    path('bang_khach_hang',bang_khach_hang, name='bang-khach-hang'),
    path('chon_dich_vu',chon_dich_vu, name='chon-dich-vu'),
    path('nhan_vien/<int:assigned_service_id>/',nhan_vien, name='nhan-vien'),
    path('employee/<int:employee_id>/get_status/',toggle_employee_status, name='get_employee_status'),
    path('tong_hop',tong_hop, name='tong-hop'),
    path('text_to_speech',text_to_speech, name='text_to_speech'),
    path('test',test, name='some_function'),
    path('dem',dem,name='dem'),
    path('feedback-chart/', feedback_chart_data, name='feedback_chart_data'),
    path('move-to-waiting-list/<int:khachhang_id>/', move_to_waiting_list, name='move_to_waiting_list'),
   
]
    