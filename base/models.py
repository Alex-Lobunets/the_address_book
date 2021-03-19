from django.db import models

class Person(models.Model):
    name = models.CharField('Name', max_length=70, null=True)
    lastname = models.CharField('Lastname', max_length=70, null=True)
    country = models.CharField('Country', max_length=70, blank=True, default='')
    city = models.CharField('City', max_length=70, blank=True, default='')
    street = models.CharField('Street', max_length=70, blank=True, default='')
    url = models.URLField('Url', blank=True, default='')
    phone_number = models.CharField('Phone number', max_length=20)
    picture = models.ImageField('Picture',  upload_to="images/", null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('name', 'lastname',)


    



 