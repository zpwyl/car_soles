# Generated by Django 2.1.3 on 2018-12-27 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20181226_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryManagement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.IntegerField()),
                ('car_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.CarInfo')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Distributor')),
            ],
        ),
    ]
