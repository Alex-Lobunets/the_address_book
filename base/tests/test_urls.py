from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import PersonList, PersonCreate, PersonUpdate, PersonDelete


class TestUrls(SimpleTestCase):

    def test_persons_url_resolves(self):
        url = reverse('persons')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PersonList)
    
    def test_persons_create_resolves(self):
        url = reverse('person-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PersonCreate)

    def test_person_update_resolves(self):
        url = reverse('person-update', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PersonUpdate)

    def test_person_delete_resolves(self):
        url = reverse('person-delete', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PersonDelete)
    




