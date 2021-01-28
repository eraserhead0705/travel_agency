# Generated by Django 3.1.5 on 2021-01-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0042_auto_20210126_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='tours_packages',
        ),
        migrations.AddField(
            model_name='tourpackage',
            name='destination',
            field=models.ManyToManyField(related_name='tour_packages', to='travel_agency_app.Destination'),
        ),
    ]
