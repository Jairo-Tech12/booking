# Generated by Django 5.1.2 on 2024-11-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0003_delete_fligth'),
    ]

    operations = [
        migrations.CreateModel(
            name='fligth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('destination', models.CharField(choices=[('Dubai', 'Dubai'), ('Canada', 'Canada'), ('Australia', 'Australia'), ('South Africa', 'South Africa'), ('Diani', 'Diani'), ('Germany', 'Germany')], max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]