# Generated by Django 4.2.10 on 2024-03-18 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_capnhatdulieu_tong_alter_capnhatdulieu_thong_bao'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanhSachCho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('khach_hang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='danh_sach_cho', to='customer.khachhang')),
            ],
        ),
    ]