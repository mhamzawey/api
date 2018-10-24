from django.test import TestCase
from events.models import Event
from django.urls import reverse
from events.serializers import EventSerializer
from rest_framework import status
from events.views import EventListFilters
from rest_framework.test import APIRequestFactory




class getAllEventsTest(TestCase):
    """ Test module for GET all Events API """

    def setUp(self):
        Event.objects.create(title="test title", category="test category",
                             description="test description",
                             start_date="2018-11-10", end_date="2018-11-11",
                             link="https://www.co-berlin.org/en/junior-05-wunder-der-dunkelkammer",
                             web_source="test source")
        Event.objects.create(title="test2 title", category="test2 category",
                             description="test2 description",
                             start_date="2018-11-10", end_date="2018-11-11",
                             link="https://www.co-berlin.org/en/junior-05-wunder-der-dunkelkammer/test",
                             web_source="test2 source")


    def test_get_all_events(self):
        # get API response
        request = APIRequestFactory().get("/filter/events/")
        event_list = EventListFilters.as_view()
        # get data from db
        events = Event.objects.all()
        response = event_list(request)
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
