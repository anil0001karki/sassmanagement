# Generated by Django 2.1.3 on 2019-01-16 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20190115_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 11, 31, 56, 921516)),
        ),
    ]
