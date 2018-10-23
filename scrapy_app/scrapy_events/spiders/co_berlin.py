import scrapy
import string
import datetime

from django.db import IntegrityError

from events.models import Event
from events.serializers import EventSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


import logging
logger = logging.getLogger(__name__)

class CoBerlin(scrapy.Spider):
    name = "co_berlin"
    BASE_URL = "https://www.co-berlin.org"

    def start_requests(self):
        urls = [
            self.BASE_URL+"/en/calendar",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def clean_text(self,text):
        printable = set(string.printable)
        return ''.join(filter(lambda x: x in printable, text))

    def parse(self, response):
        for event in response.css(".seite-c-single"):
            title = event.css(".article-title::text").extract_first()
            category = event.css(".article-category::text").extract_first()
            desc = event.css(".article-text::text").extract_first()
            href = self.BASE_URL + event.css(".seite-c-single ::attr(href)").extract_first()
            try:
                start = [x.strip() for x in event.css(".date-display-start ::attr(content)").extract_first().split('T')][0]
                start = datetime.datetime.strptime(start, '%Y-%m-%d').strftime('%Y-%m-%d')# %I:%m:%s.%f')
                end = [x.strip() for x in event.css(".date-display-end ::attr(content)").extract_first().split('T')][0]
                end = datetime.datetime.strptime(end, '%Y-%m-%d').strftime('%Y-%m-%d')# %I:%m:%s.%f')#2018-10-21 12:04:26.255181 2018-12-02 12:12:1543708800.000000
            except:
                start = [x.strip() for x in event.css(".date-display-single ::attr(content)").extract_first().split('T')][0]
                start = datetime.datetime.strptime(start, '%Y-%m-%d').strftime('%Y-%m-%d')# %I:%m:%s.%f')
                end = start

            event_object = Event(title=title, start_date=start,
                                 end_date=end,category=category,
                                 link=href,description=desc,
                                 web_source="Co-Berlin")

            serializer = EventSerializer(event_object)
            content = JSONRenderer().render(serializer.data)
            stream = io.BytesIO(content)
            data = JSONParser().parse(stream)
            serializer = EventSerializer(data=data)
            #print(serializer)
            #print(serializer.is_valid())
            serializer.is_valid()
            try:
                serializer.save()
            except IntegrityError as e:
                logger.error(e.__str__())



