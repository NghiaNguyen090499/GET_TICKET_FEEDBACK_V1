# Generated by Django 4.2.10 on 2024-03-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_khachhang_trang_thai'),
    ]

    operations = [
        migrations.AddField(
            model_name='danhsachcho',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='danhsachcho',
            name='ticket_number',
            field=models.IntegerField(null=True),
        ),
    ]
