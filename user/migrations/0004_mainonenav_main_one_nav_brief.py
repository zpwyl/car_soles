# Generated by Django 2.1.3 on 2018-12-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_cartypebaseinfo_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainonenav',
            name='main_one_nav_brief',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
