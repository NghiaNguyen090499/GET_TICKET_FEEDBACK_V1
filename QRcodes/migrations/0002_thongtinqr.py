# Generated by Django 4.1.5 on 2023-03-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QRcodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThongtinQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_cccd', models.CharField(max_length=20)),
                ('so_cmnd_cu', models.CharField(max_length=20)),
                ('ho_va_ten', models.TextField(max_length=100)),
                ('ngay_sinh', models.CharField(max_length=20)),
                ('gioi_tinh', models.CharField(max_length=10)),
                ('dia_chi', models.TextField(max_length=2000)),
                ('ngay_cap', models.TextField(max_length=150)),
                ('ngay_quet', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]