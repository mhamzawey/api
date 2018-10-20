from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
import rest_framework_filters as filters

from events.models import Event
from events.serializers import EventSerializer


class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'title':['exact', 'in', 'startswith','contains'],
            'description':['exact', 'in', 'startswith','contains'],
            'category':['exact', 'in', 'startswith','contains'],
            'start_date':['exact','lte','gte','lt','gt','in'],
            'end_date':['exact','lte','gte','lt','gt','in'],
        }

class EventList(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter