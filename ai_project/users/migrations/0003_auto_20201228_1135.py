# Generated by Django 3.1.1 on 2020-12-28 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201010_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessmen',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='fitnesswomen',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
