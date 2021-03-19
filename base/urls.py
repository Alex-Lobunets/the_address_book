from django.urls import path
from .views import PersonList, PersonCreate, PersonUpdate, PersonDelete


urlpatterns = [
    path('', PersonList.as_view(), name='persons'),
    path('person-create/', PersonCreate.as_view(), name='person-create'),
    path('person-update/<int:pk>/', PersonUpdate.as_view(), name='person-update'),
    path('person-delete/<int:pk>/', PersonDelete.as_view(), name='person-delete'),
    
]

