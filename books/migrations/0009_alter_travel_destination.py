# Generated by Django 5.1.2 on 2024-11-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_hotel_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='destination',
            field=models.CharField(max_length=100),
        ),
    ]
