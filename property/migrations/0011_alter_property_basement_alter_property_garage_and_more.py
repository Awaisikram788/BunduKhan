# Generated by Django 4.0.4 on 2022-05-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_property_full_house_image_property_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='basement',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='garage',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='pool',
            field=models.IntegerField(default=False),
        ),
    ]