from django.db import models

#Create your models here.



class travel(models.Model):
    DESTINATION_CHOICES = [
        ('Tsavo', 'Tsavo'),
        ('Malindi', 'malindi'),
        ('Serengeti', 'Serengeti'),
        ('Baringo', 'Baringo'),
        ('Diani', 'Diani'),
            ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES) 
    date = models.DateField()
            
def __str__(self):
    return f"{self.name} - {self.destination}"


class hotel(models.Model):
    DESTINATION_CHOICES = [
        ('Maasai mara', 'Maasai mara'),
        ('Serena', 'serena'),
        ('Naivasha', 'Naivasha'),
        ('Rift hills', 'Rift hills'),
        ('Diani', 'Diani'),
            ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES)  # Dropdown choices
    date = models.DateField()
    
            
def __str__(self):
    return f"{self.name} - {self.destination}"



class fligth(models.Model):
    DESTINATION_CHOICES = [
        ('Maasai mara', 'Maasai mara'),
        ('Serena', 'serena'),
        ('Naivasha', 'Naivasha'),
        ('Rift hills', 'Rift hills'),
        ('Diani', 'Diani'),
            ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES)  # Dropdown choices
    date = models.DateField()
    
            
def __str__(self):
    return f"{self.name} - {self.destination}"




