# Generated by Django 5.1.2 on 2024-11-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='destination',
            field=models.CharField(choices=[('Maasai mara', 'Maasai mara'), ('Serena', 'serena'), ('Naivasha', 'Naivasha'), ('Rift hills', 'Rift hills'), ('Diani', 'Diani')], max_length=100),
        ),
    ]
