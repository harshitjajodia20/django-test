# Generated by Django 3.2.4 on 2021-06-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bikerepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikename', models.CharField(max_length=100)),
                ('ownername', models.CharField(max_length=50)),
                ('startdate', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bikeshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikename', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('bike_price', models.IntegerField()),
            ],
        ),
    ]
