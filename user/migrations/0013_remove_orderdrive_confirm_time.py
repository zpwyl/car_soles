# Generated by Django 2.1.3 on 2018-12-23 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20181223_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdrive',
            name='confirm_time',
        ),
    ]
