# Generated by Django 3.1.5 on 2021-01-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0044_auto_20210126_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourpackage',
            name='destination_name',
        ),
        migrations.AddField(
            model_name='tourpackage',
            name='destination',
            field=models.ManyToManyField(to='travel_agency_app.Destination'),
        ),
    ]
