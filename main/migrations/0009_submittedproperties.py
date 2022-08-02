# Generated by Django 4.0.4 on 2022-06-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_herosectionproperty_delete_propertystatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmittedProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('neighbour', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('budget', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('property_type', models.CharField(max_length=255)),
                ('land_status', models.CharField(max_length=255)),
                ('pool', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
            ],
        ),
    ]