# Generated by Django 5.1.2 on 2024-11-07 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_travel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='travel',
            new_name='hotel',
        ),
    ]