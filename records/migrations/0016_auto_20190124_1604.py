# Generated by Django 2.1.3 on 2019-01-24 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0015_auto_20190122_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 16, 4, 13, 444482), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]