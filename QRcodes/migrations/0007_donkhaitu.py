# Generated by Django 4.1.5 on 2023-06-24 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QRcodes', '0006_rename_ngay_sinh_nam_donkethon_thanh_tien_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donkhaitu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ho_va_ten', models.TextField(max_length=100)),
                ('so_cccd', models.CharField(max_length=20)),
                ('ho_va_ten_nguoi_mat', models.TextField(max_length=100)),
                ('so_cccd_nguoi_mat', models.CharField(max_length=20)),
                ('ngay_lam_don', models.DateTimeField(default=django.utils.timezone.now)),
                ('thanh_tien', models.CharField(max_length=20)),
                ('ghi_chu', models.CharField(max_length=200)),
                ('file', models.FileField(max_length=254, upload_to='QRcodes/reports/khai_tu')),
            ],
        ),
    ]