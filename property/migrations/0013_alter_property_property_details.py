# Generated by Django 4.0.4 on 2022-05-26 12:02

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_property_property_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_details',
            field=tinymce.models.HTMLField(),
        ),
    ]
