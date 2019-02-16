from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets
from rest.serializers import PersonSerializer
from .models import Person


# API get detail, update, delete
class PersonDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'


# API get list and create
class PersonListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
