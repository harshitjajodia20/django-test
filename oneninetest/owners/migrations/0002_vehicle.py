# Generated by Django 3.2.4 on 2021-06-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=100)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_company', models.CharField(max_length=100)),
                ('vehicle_purchase_date', models.DateField(blank=True)),
            ],
        ),
    ]
