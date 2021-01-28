# Generated by Django 3.1.5 on 2021-01-24 23:38

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0014_auto_20210124_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('destination_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TourPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=6, max_digits=10)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('Availability', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None)),
                ('tour_package', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='travel_agency_app.tourpackage')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TourCapacity',
            fields=[
                ('capacity', models.IntegerField()),
                ('tour_package', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='travel_agency_app.tourpackage')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('destination', models.ManyToManyField(blank=True, to='travel_agency_app.Destination')),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='tour_package',
            field=models.ManyToManyField(to='travel_agency_app.TourPackage'),
        ),
        migrations.CreateModel(
            name='DangerLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('danger_score', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('destination', models.ManyToManyField(blank=True, to='travel_agency_app.Destination')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='destination',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travel_agency_app.destination'),
        ),
    ]