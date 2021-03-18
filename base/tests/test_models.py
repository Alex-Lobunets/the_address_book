from django.test import TestCase
from base.models import Person

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(
            name_and_lastname='Test Person4',
            url='https://github.com/',
            phone_number='123456789',
            picture='https://www.google.com/photos',
        )

    def test_name_and_lastname_label(self):
        person=Person.objects.get(id=1)
        field_label = person._meta.get_field('name_and_lastname').verbose_name
        self.assertEquals(field_label,'Name and lastname')
    
    def test_name_and_lastname_max_length(self):
        person=Person.objects.get(id=1)
        max_length = person._meta.get_field('name_and_lastname').max_length
        self.assertEquals(max_length,250)

    def test_phone_number_max_length(self):
        person=Person.objects.get(id=1)
        max_length = person._meta.get_field('phone_number').max_length
        self.assertEquals(max_length,20)
    
    
    def test_object_name_is_name_and_lastname(self):
        person=Person.objects.get(id=1)
        expected_object_name = person.name_and_lastname
        self.assertEquals(expected_object_name,str(person))

