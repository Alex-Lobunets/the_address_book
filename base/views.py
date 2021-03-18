from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Person


class PersonList(ListView):
    model = Person
    context_object_name = 'persons'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Person.objects.filter(name_and_lastname__icontains=query)
        else:
            return Person.objects.all()

 
class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('persons')


class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('persons')


class PersonDelete(DeleteView):
    model = Person
    context_object_name = 'person'
    success_url = reverse_lazy('persons')


