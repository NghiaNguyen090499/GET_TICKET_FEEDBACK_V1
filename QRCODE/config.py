# my_app/config.py

from django.utils.translation import gettext_lazy as _

def jet_side_menu_items():
    return [
        {'label': _('Danh mục chính'), 'items': [
        {'name': 'customer.service','label': _('Quầy')},
        {'name': 'customer.thongke', 'label': _('Thống kê')},
        {'name': 'customer.manage', 'label': _('Quản lý lấy số')},
        {'name': 'customer.khachhang', 'label': _('Thống kê đánh giá')},
        
    ]},
    {'label': _('Quản trị người dùng'), 'items': [
        {'name': 'auth.user'},
        {'name': 'auth.group'},
    ]},
    # Thêm hoặc loại bỏ các nhóm và mục menu tùy chỉnh theo yêu cầu của bạn
]