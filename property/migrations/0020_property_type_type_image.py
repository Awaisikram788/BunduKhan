# Generated by Django 4.0.4 on 2022-05-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_property_floor_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_type',
            name='type_image',
            field=models.FileField(null=True, upload_to='properties/'),
        ),
    ]
