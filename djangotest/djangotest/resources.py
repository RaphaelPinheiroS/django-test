from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import PersonSerializer
from .models import Person

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer