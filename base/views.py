from django.db.models import Q
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PersonForm
from .models import Person


class PersonList(ListView):
    
    model = Person
    context_object_name = 'persons'

    def get(self,request):
        persons = Person.objects.all()
    
        query = self.request.GET.get('q')
        if query:
            persons = Person.objects.filter(
            Q(name__icontains=query) | Q(lastname__icontains=query)
            )
        else:
            persons = Person.objects.all()
        return render(request, 'base/person_list.html', {'persons': persons, 'query': query})
    

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

