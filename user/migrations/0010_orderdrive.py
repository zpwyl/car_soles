# Generated by Django 2.1.3 on 2018-12-23 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20181221_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDrive',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=10)),
                ('car_name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=2)),
                ('telephone', models.CharField(max_length=11)),
                ('province', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=10)),
                ('dealer', models.CharField(max_length=30)),
                ('confirm', models.CharField(max_length=1)),
                ('order_time', models.DateTimeField()),
                ('confirm_time', models.DateTimeField(blank=True, null=True)),
                ('staff_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
