from django.db import models

class Person(models.Model):
    name_and_lastname = models.CharField('Name and lastname', max_length=250, unique=True)
    country = models.CharField('Country', max_length=70, blank=True, default='')
    city = models.CharField('City', max_length=70, blank=True, default='')
    street = models.CharField('Street', max_length=70, blank=True, default='')
    url = models.URLField('Url', blank=True, default='')
    phone_number = models.CharField('Phone number', max_length=20)
    picture = models.URLField('Picture', blank=True, default='')
    
    
    def __str__(self):
        return self.name_and_lastname


 