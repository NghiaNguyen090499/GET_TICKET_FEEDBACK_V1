# Generated by Django 4.1.5 on 2023-06-24 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QRcodes', '0009_rename_ngay_sinh_donchungnhanhonnhan_thanh_tien_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donchungnhanhonnhan',
            old_name='ho_va_ten_nu',
            new_name='ho_va_ten',
        ),
        migrations.RenameField(
            model_name='donchungnhanhonnhan',
            old_name='so_cccd_nu',
            new_name='so_cccd',
        ),
    ]