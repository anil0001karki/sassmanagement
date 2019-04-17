# Generated by Django 2.1.3 on 2019-03-18 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0023_auto_20190318_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_students',
            name='Proimage',
            field=models.ImageField(blank=True, null='True', upload_to='media/'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 22, 12, 17, 868317), help_text='Please specify english date: <em>YYYY-MM-DD</em>.'),
        ),
    ]