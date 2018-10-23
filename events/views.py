from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_filters import FilterSet
from events.models import Event
from events.serializers import EventSerializer
from rest_framework import filters



class EventFilter(FilterSet):
    class Meta:
        model = Event
        fields = {
            'title':['exact', 'in', 'startswith','contains'],
            'description':['exact', 'in', 'startswith','contains'],
            'category':['exact', 'in', 'startswith','contains'],
            'start_date':['exact','lte','gte','lt','gt','in'],
            'end_date':['exact','lte','gte','lt','gt','in'],
            'link':['exact','in','contains'],
            'created_at':['exact','lte','gte','lt','gt','in'],
            'updated_at':['exact','lte','gte','lt','gt','in']
        }


class EventList(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description','category')

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class EventListFilters(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter
