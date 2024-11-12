from django.db import models

#Create your models here.
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


class travel(models.Model):
    DESTINATION_CHOICES = [
        ('Maasai mara', 'Maasai mara'),
        ('Malindi', 'Malindi'),
        ('Tsavo', 'Tsavo'),
        ('Baringo', 'Baringo'),
        ('Diani', 'Diani'),
            ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    destination = models.CharField(max_length=100, choices=DESTINATION_CHOICES)  # Dropdown choices
    date = models.DateField()
    
            
def __str__(self):
    return f"{self.name} - {self.destination}"

class message(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.phone}"









