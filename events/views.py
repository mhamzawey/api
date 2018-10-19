from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer


class EventList(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id','title','description','category','start_date','end_date','link','created_at','updated_at')
