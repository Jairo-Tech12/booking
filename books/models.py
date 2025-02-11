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


# class explore(models.model):
#     image=models.imagefield(upload_to="explore/", verbose_name="explore image")
#     title=models.charfield(max_length=100, verbose_name="title")
#     date=models.DateField(auto_now_add=True, verbose_name="Dtae")
     
#     def image_tag(self):
#         if self.image:
#         #   return mark_safe(<img src="{self.image.url}" width="150 heigth="100"), 
#                            return "No image"
#                            def_str_(self)
#                            return self.title
                             




