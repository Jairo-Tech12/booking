from django.db import models

# Create your models here.
class fligth(models.Model):
    DESTINATION_CHOICES = [
        ('Dubai', 'Dubai'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('South Africa', 'South Africa'),
        ('Diani', 'Diani'),
        ('Germany', 'Germany'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES)  # Dropdown choices
    date = models.DateField()
    
            
def __str__(self):
    return f"{self.name} - {self.destination}"



