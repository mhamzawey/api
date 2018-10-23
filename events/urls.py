from django.conf.urls import url,include
from rest_framework import routers

from events.views import EventList, EventListFilters

eventsList = routers.DefaultRouter()
eventsList.register(r'', EventList, 'list')



urlpatterns = [
    url(r'^events/$', include(eventsList.urls)),
    url(r'^filter/events/$', EventListFilters.as_view()),
]
