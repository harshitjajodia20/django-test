# Generated by Django 3.2.4 on 2021-06-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikename', models.CharField(max_length=100)),
                ('ownername', models.CharField(max_length=100)),
                ('bike_price', models.CharField(max_length=100)),
            ],
        ),
    ]
