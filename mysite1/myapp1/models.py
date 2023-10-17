from django.db import models
from django_fields import DefaultStaticImageField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    #picture = models.ImageField(null=True,blank=True)
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    email = models.EmailField(blank = True)
    
    date = models.DateField(default = '2023-10-03')

    def __str__(self):
        return self.name

