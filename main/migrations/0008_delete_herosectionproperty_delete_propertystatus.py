# Generated by Django 4.0.4 on 2022-05-26 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_herosectionproperty_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeroSectionProperty',
        ),
        migrations.DeleteModel(
            name='PropertyStatus',
        ),
    ]
