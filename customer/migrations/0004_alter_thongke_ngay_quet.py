# Generated by Django 3.2.2 on 2024-01-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_khachhang_trang_thai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thongke',
            name='ngay_quet',
            field=models.DateTimeField(null=True),
        ),
    ]