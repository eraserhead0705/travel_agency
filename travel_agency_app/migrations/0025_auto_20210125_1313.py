# Generated by Django 3.1.5 on 2021-01-25 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency_app', '0024_auto_20210125_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dangerlevel',
            name='destinations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='travel_agency_app.destination'),
        ),
        migrations.AlterField(
            model_name='destinationtype',
            name='destinations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='travel_agency_app.destination'),
        ),
    ]
