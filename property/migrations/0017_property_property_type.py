# Generated by Django 4.0.4 on 2022-05-27 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='Property_Type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.property_type'),
        ),
    ]