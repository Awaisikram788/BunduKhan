# Generated by Django 4.0.4 on 2022-06-20 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_submittedproperties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submittedproperties',
            name='postcode',
        ),
    ]
