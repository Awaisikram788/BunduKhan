# Generated by Django 4.0.4 on 2022-05-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_appoinment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
