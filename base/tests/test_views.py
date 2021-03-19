from django.test import TestCase, Client
from base.models import Person
from django.urls import reverse


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_persons = 4
        for person_num in range(number_of_persons):
            Person.objects.create(name='Jango %s' % person_num)
    
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('persons'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('persons'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'base/person_list.html', 'base/main.html')

    def test_person_create_url_accessible_by_name(self):
        resp = self.client.get(reverse('person-create'))
        self.assertEqual(resp.status_code, 200)
    
    def test_person_delete_url_accessible_by_name(self):
        resp = self.client.get(reverse('person-delete', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)
    
    def test_person_update_url_accessible_by_name(self):
        resp = self.client.get(reverse('person-update', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)






